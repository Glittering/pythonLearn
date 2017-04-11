#coding:utf-8

# 主函数

from imooc.baide_spider import html_download
from imooc.baide_spider import html_output
from imooc.baide_spider import html_parser
from imooc.baide_spider import url_manager

# 调度器
class SpiderMain(object):

    # 初始化
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.download=html_download.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.output = html_output.HtmlOutputer()

    # 调度
    #     添加新url
    #     判断有没有新url     没有就结束，输出
    #     取新url
    #     下载网页
    #     解析
    #     添加新url
    #     添加内容
    def craw(self,root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url=self.urls.get_new_url()
                print 'craw %d: %s'% (count, new_url)
                html_cont = self.download.download(new_url)
                new_urls, new_data = self.parser.parse(new_url,html_cont)
                self.urls.add_new_urls(new_urls)
                self.output.collect_data(new_data)
                if count == 1000:
                    break
                count += 1
            except:
                print 'craw failed.'
        self.output.output_html()

# 运行时候
if __name__ =='__main__':
    root_url = 'http://baike.baidu.com/view/21087.htm'
    obj_spider=SpiderMain()     #调度程序
    obj_spider.craw(root_url)