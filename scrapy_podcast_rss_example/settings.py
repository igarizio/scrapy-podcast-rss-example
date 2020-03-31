"""Minimal project settings.
"""

BOT_NAME = 'scrapy_podcast_rss_example'

SPIDER_MODULES = ['scrapy_podcast_rss_example.spiders']
NEWSPIDER_MODULE = 'scrapy_podcast_rss_example.spiders'

SCHEDULER_DEBUG = 'True'
LOG_LEVEL = 'DEBUG'
# LOG_FILE = './log.txt'

OUTPUT_URI = './my-podcast-rss.xml'  # Saves the content to a local file.
# To use S3 locations, install the package with:
# pip install scrapy-podcast-rss[s3_storage]
# Then, configure your S3 credentials (with aws configure or any other alternative).
# OUTPUT_URI = 's3://my-bucket/my-podcast-rss.xml'  # Saves the content to an S3 bucket.

ITEM_PIPELINES = {
    'scrapy_podcast_rss.pipelines.PodcastPipeline': 300,
}
