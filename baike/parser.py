import reimport urlparsefrom bs4 import BeautifulSoupclass HtmlParser(object):    def parse(self, page_url, html_content):        soup = BeautifulSoup(html_content, 'html.parser', from_encoding='utf-8')        return self.get_new_url(page_url, soup), self.get_new_data(page_url, soup)    def get_new_url(self, page_url, soup):        urls = set()        links = soup.find_all('a', href=re.compile(r"/view/\d+\.htm"))        for link in links:            print urlparse.urljoin(page_url, link['href'])            urls.add(urlparse.urljoin(page_url, link['href']))        return urls    def get_new_data(self, page_url, soup):        new_data = {'url': page_url}        title = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h1')        new_data['title'] = title.get_text()        content = soup.find('div', class_='lemma-summary')        new_data['content'] = content.get_text()        return new_data