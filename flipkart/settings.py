# Scrapy settings for flipkart project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'flipkart'

SPIDER_MODULES = ['flipkart.spiders']
NEWSPIDER_MODULE = 'flipkart.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'flipkart (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False
ITEM_PIPELINES = {'flipkart.pipelines.MongoDBPipeline': 200}

mongodb_srv = "mongodb://localhost:27017/"
MONGODB_SERVER = "localhost"
MONGODB_PORT = 27017
MONGODB_DB = "flipkart"
MONGODB_COLLECTION = "mobile"

USER_AGENT = {
    ('Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0)'
     '(like Gecko)'),
    ('Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
     'AppleWebKit/537.36 (KHTML, like Gecko)'
     'Chrome/74.0.3729.157'
     'Safari/537.36'),
    ('Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9a1)'
     'Gecko/20070308'
     'Minefield/3.0a1'),
    ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8)'
     'AppleWebKit/537.36 (KHTML, like Gecko)'
     'Chrome/49.0.2623.112'
     'Safari/537.36'),
    ('Mozilla/5.0 (Linux; U; Android 4.2.2; de-de; IdeaTab S6000-H Build/JDQ39)'
     'AppleWebKit/534.30 (KHTML, like Gecko)'
     'Version/4.0'
     'Safari/534.30'),
    ('Mozilla/5.0 (X11; CrOS x86_64 11895.118.0)'
     'AppleWebKit/537.36 (KHTML, like Gecko)'
     'Chrome/74.0.3729.159'
     'Safari/537.36'),
    ('Mozilla/5.0 (X11; OpenBSD i386)'
     'AppleWebKit/537.36 (KHTML, like Gecko)'
     'Chrome/36.0.1985.125'
     'Safari/537.36'),
    ('Mozilla/5.0 (X11; Linux x86_64) '
     'AppleWebKit/537.36 (KHTML, like Gecko) '
     'Chrome/57.0.2987.110 '
     'Safari/537.36'),  # chrome
    ('Mozilla/5.0 (X11; Linux x86_64) '
     'AppleWebKit/537.36 (KHTML, like Gecko) '
     'Chrome/61.0.3163.79 '
     'Safari/537.36'),  # chrome
    ('Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:55.0) '
     'Gecko/20100101 '
     'Firefox/55.0')  # firefox
}

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'flipkart.middlewares.FlipkartSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'flipkart.middlewares.FlipkartDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    'flipkart.pipelines.FlipkartPipeline': 300,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
AUTOTHROTTLE_ENABLED = True
# The initial download delay
AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
AUTOTHROTTLE_DEBUG = True

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
