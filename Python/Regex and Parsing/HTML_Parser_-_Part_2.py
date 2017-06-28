from HTMLParser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        data = data.split('\n')
        if len(data) == 1:
            print '>>> Single-line Comment'
            print data[0]
        else:
            print '>>> Multi-line Comment'
            for line in data:
                print line

    def handle_data(self, data):
        data = data.split('\n')
        for line in data:
            if line:
                print ">>> Data"
                print line

parser = MyHTMLParser()

# html = """<!--[if IE 9]>IE9-specific content
# <![endif]-->
# <div> Welcome to HackerRank</div>
# <!--[if IE 9]>IE9-specific content<![endif]-->"""

html = []
for _ in range(int(raw_input())):
    html.append(raw_input())

parser.feed(''.join(html))
