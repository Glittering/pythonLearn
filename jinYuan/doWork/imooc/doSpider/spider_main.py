#!/etc/bin/python
# coding:utf-8
from imooc.doSpider import html_output
from imooc.doSpider import html_parser
from imooc.doSpider import url_manager
from imooc.doSpider import html_download


class SpiderMain(object):
    def __init__(self):
        self.download = html_download.HtmlDownload()
        self.urls = url_manager.UrlManager()
        self.parser = html_parser.HtmlParser()
        self.output = html_output.HtmlOutput()

    def craw(self, root_url):
        count = 1
        self.urls.add_new_url()
        while self.urls.get_new_url():
            try:
                new_url = self.urls.get_new_url()
                print 'craw %d: %s' % (count, new_url)
                html_cont = self.download.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.output.collect_data(new_data)
                if (count == 1000):
                    break
                count += 1
            except:
                print 'craw faild'
        self.output.output_html()


if __name__ == '__main__':
    root_url = 'http://baike.baidu.com/view/21087.htm'
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
