from html.parser import HTMLParser
from urllib.request import urlopen
class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.flag = False # タイトルタグの場合のフラグ
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'span' and attrs.get('class') == 'status_name':
            self.tmp = ""
            self.flag = True
        if tag == 'a' and attrs.get('class') == 'timestamp':
            self.tmp+=attrs.get('data-timestamp')+'\t'
        if tag == 'div' and attrs.get('class') == 'tweet emj':
            self.flag = True
    def handle_endtag(self, tag):
        if self.flag == True:
            if tag == 'div':
                print(self.tmp)
                txt.write(self.tmp+"\n")
            if tag=='span':
                self.tmp+="\t"
        if tag == 'span' or tag == 'div':
            self.flag =False
    def handle_data(self, data): # 要素内用を扱うためのメソッド
        if self.flag:
            self.tmp+=data.replace('\n','')

class MonoHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.tmp="--"
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'a' and attrs.get('class') == 'timestamp' and 'twitter.com' in attrs.get('href') : #togetterのコメントをはじくためhrefも
            self.tmp = attrs.get('data-timestamp')

if __name__ == "__main__":
    site = 826473
    txt = open('foo.txt', 'w',encoding='utf-8')
    i = 1
    url = 'http://togetter.com/li/'+str(site)+'?page='
    f = urlopen(url+'1')
    monoparser = MonoHTMLParser()
    monoparser.feed(f.read().decode('utf-8'))
    monotime = monoparser.tmp #1ページ目の最後のタイムスタンプを取得
#    print(monotime)
    while True:
        f = urlopen(url+str(i))
        read = f.read().decode('utf-8')
        monoparser = MonoHTMLParser()
        monoparser.feed(read)
        ftime = monoparser.tmp #各ページの最後のタイムスタンプを取得
        print(ftime)
        if monotime == ftime and i>2: #同じタイムスタンプが出て来たらbreak
            break
        parser = MyHTMLParser()
        parser.feed(read)
        i += 1
        print(i)
    txt.close()
    print("end!")