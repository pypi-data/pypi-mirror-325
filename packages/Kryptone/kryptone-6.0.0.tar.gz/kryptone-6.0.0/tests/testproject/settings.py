# This is the main settings file for a
# Kryptone project. To read more about
# settings and discover additional settings
# that you can use please visit:
# https://github.com/Zadigo/kryptone/wiki/List-of-settings

import pathlib

# Absolute path to the local project
# This should be set to the root directory
# of your specific spider project
PROJECT_PATH = pathlib.Path(__file__).parent.absolute()


# Specifies the Selenium WebDriver to use for browser automation.
# Example values: 'Chrome', 'Firefox', 'Edge', etc.
WEBDRIVER = 'Edge'


# Name of the media folder, used for storing
# resources like downloads and screenshots.
# The resolved path will point to
# `PROJECT_PATH / MEDIA_FOLDER`
MEDIA_FOLDER = 'media'


# Specifies the default wait time (in seconds)
# for the browser before navigating to the next URL
WAIT_TIME = 25


# Specifies a range for the browser's waiting time
# before moving to the next URL. Example: [10, 30] would
# randomly choose a wait time between 10 and 30 seconds
WAIT_TIME_RANGE = []


# Name of the file used for caching URLs
# to visit and already visited URLs
CACHE_FILE_NAME = 'cache'


# Storage settings for saving and retrieving data during spider execution

# A dictionary mapping storage aliases to their respective
# backend classes

# Example:

# 'default': 'kryptone.storages.FileStorage',
# 'backends': ['kryptone.storages.RedisStorage', 'kryptone.storages.AirtableStorage']
STORAGES = {
    'default': 'kryptone.storages.FileStorage',
    'backends': [
        'kryptone.storages.RedisStorage'
    ]
}


# Frequency (in seconds) at which data
# is sent to registered webhooks
WEBHOOK_INTERVAL = 15

# Pagination size for data sent to webhooks.
# Data is only sent if the accumulated data size
# meets this threshold
WEBHOOK_PAGINATION = 100


# Email setting values used essentially
# for alerting users for failed events
# or sending captured data
EMAIL_HOST = 'smtp.gmail'

EMAIL_PORT = 587

EMAIL_HOST_USER = None

EMAIL_HOST_PASSWORD = None

EMAIL_USE_TLS = True

DEFAULT_FROM_EMAIL = None


# The default language used by the website.
# Useful for text analysis and determining the stop
# words for content processing
WEBSITE_LANGUAGE = 'fr'


# Allow Selenium to be launched in headless mode
HEADLESS = False


# Determines whether to load images
# when launching the browser
LOAD_IMAGES = True

# Determines whether to execute JavaScript
# when launching the browser
LOAD_JS = True


# IP address of the proxy server
# to use for web scraping. Example:
# '192.168.0.1:8080'
PROXY_IP_ADDRESS = None
