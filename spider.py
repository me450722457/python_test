from urllib import request


class Spider():
    url = 'https://www.panda.tv/cate/lol'

    def __fetch_content(self):
        r = request.urlopen(Spider.url)
        htmls = r.read()
        str(htmls, encoding = 'utf-8')
        a= 1
        
    def go(self):
        self.__fetch_content()

spider = Spider()
spider.go()
