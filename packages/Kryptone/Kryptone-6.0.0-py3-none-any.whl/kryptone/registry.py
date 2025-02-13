import datetime
import inspect
import os
import sys
from collections import OrderedDict
from functools import lru_cache
from importlib import import_module
from pathlib import Path

from kryptone import logger
from kryptone.conf import settings
from kryptone.exceptions import SpiderExistsError

SPIDERS_MODULE = 'spiders'

ENVIRONMENT_VARIABLE = 'KRYPTONE_SPIDER'


class SpiderConfig:
    """
    Class that represents a spider and 
    its overall different configurations
    """

    def __init__(self, name, spiders_module):
        self.name = name
        self.dotted_path = None
        self.registry = None
        self.spider_class = getattr(spiders_module, name, None)

        self.MODULE = spiders_module

        paths = list(getattr(self.MODULE, '__path__', []))
        if not paths:
            filename = getattr(self.MODULE, '__file__', None)
            if filename is not None:
                paths = [os.path.dirname(filename)]

        # if len(paths) > 1:
        #     raise ValueError("There are multiple modules "
        #     "trying to start spiders")

        if not paths:
            raise ValueError(
                "No spiders module within your project. "
                "Please create a 'spiders.py' module."
            )

        self.path = paths[0]
        self.is_ready = False

    def __repr__(self):
        return f"<{self.__class__.__name__} for {self.name}>"

    @classmethod
    def create(cls, name, module, dotted_path=None):
        instance = cls(name, module)
        instance.dotted_path = dotted_path
        return instance

    def get_spider_instance(self):
        if self.spider_class is None:
            raise ValueError(
                f"Could not start spider '{self.name}' in "
                f"project: {self.dotted_path} because the spider class "
                "was None"
            )
        return self.spider_class()

    def check_ready(self):
        """Marks the spider as configured and
        ready to be used"""
        if self.spider_class is not None and self.name is not None:
            self.is_ready = True

    def run(self, windows=1, **params):
        """Runs the spider by calling the spider class
        which in return calls "start" method on the
        spider via the __init__ method"""
        spider_instance = self.get_spider_instance()

        try:
            settings['ACTIVE_SPIDER'] = spider_instance

            # This will tell the driver to open
            # one more window in additin to the
            # one that is opened
            if windows >= 1:
                spider_instance.boost_start(windows=windows, **params)
            else:
                spider_instance.start(**params)
        except KeyboardInterrupt:
            spider_instance.after_fail()
            logger.info('Program stopped')
            sys.exit(0)
        except Exception as e:
            spider_instance.after_fail()
            logger.error(e)
            raise Exception(e)

    def resume(self, windows=1, **spider_params):
        """Interface function used to call `SpiderCrawler.resume`"""
        spider_instance = self.get_spider_instance()

        try:
            spider_instance.resume(windows=windows, **spider_params)
        except KeyboardInterrupt:
            spider_instance.after_fail()
            sys.exit(0)
        except Exception as e:
            spider_instance.after_fail()
            logger.error(e)
            raise Exception(e)

    # TODO: Add enrichment to spider process
    def enrich(self,  windows=1, **spider_params):
        """Runs the spider by calling the spider class
        which in return calls "start_from_json" method on the
        spider via the __init__ method"""
        spider_instance = self.get_spider_instance()

        try:
            settings['ACTIVE_SPIDER'] = spider_instance
            spider_instance.start_from_json(windows=windows, **spider_params)
        except KeyboardInterrupt:
            spider_instance.after_fail()
            sys.exit(0)
        except Exception as e:
            spider_instance.after_fail()
            logger.error(e)
            raise Exception(e)


class MasterRegistry:
    def __init__(self):
        self.is_ready = False
        self.spiders_ready = False
        self.spiders = OrderedDict()
        self.project_name = None
        self.absolute_path = None
        self.middlewares = []
        self.has_running_spiders = False

    @property
    def has_spiders(self):
        return len(self.spiders.keys()) > 0

    @lru_cache(maxsize=1)
    def get_spiders(self):
        return self.spiders.values()

    def has_spider(self, name):
        return name in self.spiders

    def check_spiders_ready(self):
        if not self.has_spiders:
            raise ValueError(
                "Spiders are not yet loaded or "
                "there are no registered ones in your project. "
                "Ensure that you spider classes inherit from 'SiteCrawler' "
                "if you are using for example a mixin like 'EcommerceCrawlerMixin'"
            )

    def pre_configure_project(self, dotted_path, settings):
        # If the user did not explicitly set the path
        # to a MEDIA_FOLDER, we will be doing it
        # autmatically here. FIXME: If no explicit path
        # is defined use project path?
        media_folder = getattr(settings, 'MEDIA_FOLDER')
        if media_folder is None or media_folder == 'media':
            media_path = settings.PROJECT_PATH.joinpath('media')
        else:
            media_path = Path(settings.MEDIA_FOLDER)

        if not media_path.exists():
            raise ValueError("'MEDIA_FOLDER' path does not exist")
        setattr(settings, 'MEDIA_FOLDER', media_path)

        # Set the webhook interval to a
        # timedelta element
        delta = datetime.timedelta(
            minutes=getattr(settings, 'WEBHOOK_INTERVAL', 15)
        )
        setattr(settings, 'WEBHOOK_INTERVAL', delta)

        self.is_ready = True

    def populate(self):
        dotted_path = os.environ.get(ENVIRONMENT_VARIABLE, None)

        if dotted_path is None:
            # The user is lauching the application outside
            # of a project (standalone), it's
            # his responsibility to provide a module where
            # the spiders are located. This is done in order
            # to not completly block the project from functionning
            raise ValueError(
                "The registry requires a project in order "
                "to be populated correctly. Create a project "
                "using 'startproject'"
            )

        try:
            project_module = import_module(dotted_path)
        except ImportError:
            raise ImportError(
                "Could not load the project's "
                f"related module: '{dotted_path}'"
            )

        from kryptone.base import BaseCrawler
        from kryptone.conf import settings

        self.absolute_path = Path(project_module.__path__[0])
        self.project_name = self.absolute_path.name

        try:
            spiders_module = import_module(f'{dotted_path}.{SPIDERS_MODULE}')
        except Exception as e:
            logger.critical(e)
            raise ExceptionGroup(
                f"An error occured when trying to load the project '{
                    self.project_name}'",
                [
                    Exception(e),
                    ImportError(
                        f"Failed to load the spiders "
                        "module for '{self.project_name}' project",
                    )
                ]
            )

        # Check that there are class objects that can be used
        # and are subclasses of the main Spider class object
        spiders = inspect.getmembers(
            spiders_module,
            predicate=inspect.isclass
        )

        valid_spiders = filter(
            lambda x: issubclass(x[1], (BaseCrawler)),
            spiders
        )
        valid_spider_names = list(map(lambda x: x[0], valid_spiders))

        invalid_names = ['SiteCrawler']
        for name in valid_spider_names:
            if name in invalid_names:
                continue

            instance = SpiderConfig.create(
                name,
                spiders_module,
                dotted_path=dotted_path
            )
            instance.registry = self
            self.spiders[name] = instance

        for config in self.spiders.values():
            config.check_ready()

        self.spiders_ready = True
        # registry_populated.send(self, registry=registry)

        # Cache the registry in the settings
        # file for performance reasons
        settings['REGISTRY'] = self

        self.pre_configure_project(dotted_path, settings)

    def get_spider(self, spider_name):
        self.check_spiders_ready()
        try:
            return self.spiders[spider_name]
        except KeyError:
            raise SpiderExistsError(spider_name, self.spiders)


registry = MasterRegistry()
