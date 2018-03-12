# -*- coding: utf-8 -*-

# Scrapy settings for autohome project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'autohome'

SPIDER_MODULES = ['autohome.spiders']
NEWSPIDER_MODULE = 'autohome.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'autohome (+http://www.yourdomain.com)'


DOWNLOADER_MIDDLEWARES = {
    # 'xiaozhu.user_agent_middleware.RandomUserAgentMiddleware': 400,
    'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': None,

}

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 5
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

DEFAULT_REQUEST_HEADERS = {
'Host': 'club.autohome.com.cn',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36',
'Accept': 'text/html,application/xhtml+xm…plication/xml;q=0.9,*/*;q=0.8',
'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
'Accept-Encoding': 'gzip, deflate, br',
'Cookie': 'fvlid=1517023661115FbFQ7MXW; sessionip=125.71.2.65; sessionid=D3DAA4C8-41D6-4C2C-BF0F-0C2E6945DEDC%7C%7C2018-01-27+11%3A27%3A42.442%7C%7C0; ref=www.baidu.com%7C0%7C0%7C0%7C2018-03-12+14%3A45%3A30.458%7C2018-03-12+14%3A45%3A13.797; area=510199; ahpau=1; ahpvno=4; sessionuid=D3DAA4C8-41D6-4C2C-BF0F-0C2E6945DEDC%7C%7C2018-01-27+11%3A27%3A42.442%7C%7C0; sessionvid=8517DF4C-4ED4-4617-A341-C63F5B74DEC0; pvidchain=103419,102410; autoac=871302CF94CF441ED9557A6AB4FA83BA; autotc=F49A8ADF1F6900F08C49FC2C4A702B34; ahrlid=1520837125680g3N9CS4w-1520837129537',
'Connection': 'keep-alive',
'Upgrade-Insecure-Requests': '1',
'Cache-Control': 'max-age=0',
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'autohome.middlewares.AutohomeSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'autohome.middlewares.AutohomeDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'autohome.pipelines.AutohomePipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
HTTPCACHE_IGNORE_HTTP_CODES = [403,404,302]
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
