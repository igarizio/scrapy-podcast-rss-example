# scrapy-podcast-rss-example

This is a minimal example for [scrapy-podcast-rss](https://github.com/igarizio/scrapy-podcast-rss).  
To try it, you need to install scrapy-podcast-rss:
```console
$ pip install scrapy-podcast-rss
```
You can [fork](https://github.com/igarizio/scrapy-podcast-rss/fork) or clone 
this repo and then execute the spider by doing:
```console
$ pip scrapy crawl minimal
```
Or by adding this to your script:
```python
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

process = CrawlerProcess(get_project_settings())
process.crawl('minimal')
process.start()
```