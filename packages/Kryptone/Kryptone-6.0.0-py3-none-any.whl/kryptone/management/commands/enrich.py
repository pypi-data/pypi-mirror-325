
import kryptone
from kryptone.checks.core import checks_registry
from kryptone.management.base import ProjectCommand
from kryptone.registry import registry


class Command(ProjectCommand):
    requires_system_checks = True

    def add_arguments(self, parser):
        parser.add_argument(
            'name',
            help='Spider name to execute',
            type=str
        )
        parser.add_argument(
            '-l',
            '--language',
            help='Specify the website language',
            default='fr',
            type=str
        )
        parser.add_argument(
            '-w',
            '--windows',
            type=int,
            default=0,
            help='Number of windows to launch for a spider'
        )

    # TODO: Add enrichment to process
    def execute(self, namespace):
        kryptone.setup()
        checks_registry.run()

        if not registry.spiders_ready:
            raise ValueError((
                "The spiders for the current project "
                "were not properly configured"
            ))

        params = {'language': namespace.language}

        spider_config = registry.get_spider(namespace.name)
        if namespace.windows < 0 or namespace.windows > 5:
            raise ValueError('Number of windows should be between 2 and 5')

        spider_config.enrich(
            windows=namespace.windows,
            **params
        )
