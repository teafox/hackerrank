from HTMLParser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print "Start :", tag
        if attrs:
            for at, value in attrs:
                print ' '.join(['->', at, '>', str(value)])

    def handle_endtag(self, tag):
        print "End   :", tag

    def handle_startendtag(self, tag, attrs):
        print "Empty :", tag
        if attrs:
            for at, value in attrs:
                print ' '.join(['->', at, '>', str(value)])

    def handle_comment(self, data):
        pass

parser = MyHTMLParser()
html = []
for _ in range(int(raw_input())):
    html.append(raw_input())
parser.feed(''.join(html))
