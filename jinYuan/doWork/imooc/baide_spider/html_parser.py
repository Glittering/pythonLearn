import urlparse

import BeautifulSoup
import re


class HtmlParser(object):
    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        else:
            soup = BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')
            new_urls = self._get_new_urls(page_url,soup)
            new_data = self._get_new_data(page_url,soup)
            return new_urls,new_data

    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        links = soup.find_all('a', herf=re.compile(r'/view/\d+\.htm'))
        for link in links:
            link = link['href']
            new_url= urlparse.urljoin(page_url, link)
            new_urls.add(new_url)
        return new_urls
    def _get_new_data(self, page_url, soup):
        res_data = {'res_url':page_url,}
        titile_node = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h1')
        res_data['title'] = titile_node.get_text()

        summary_node = soup.find('div',class_='lemma-summary')
        res_data['summary'] = summary_node.get_text()
