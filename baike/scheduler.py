from baike.outputer import HtmlOutputer
from baike.parser import HtmlParser
from baike.spider_baike import HtmlSpider
from baike.urlmanager import UrlManager

crawl_count = 100


class Scheduler(object):
    def __init__(self):
        self._url = UrlManager()
        self._spider = HtmlSpider()
        self._parser = HtmlParser()
        self._outputer = HtmlOutputer()

    def start(self):
        count = 0

        while self._url.hasNext():
            new_url = self._url.getNext()
            print 'new url: ' + new_url

            html_content = self._spider.crawl(new_url)
            new_urls, new_data = self._parser.parse(new_url, html_content)

            if new_urls is not None:
                self._url.add_new_urls(new_urls)

            self._outputer.save(new_data)

            count += 1

            if count == crawl_count:
                break

        self._outputer.output()


if __name__ == '__main__':
    obj_spider = Scheduler()
    obj_spider.start()




