from HTMLParser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print tag
        for a, value in attrs:
            print ' '.join(['->', a, '>', value])

parser = MyHTMLParser()

# html = """<head>
# <title>HTML</title>
# </head>
# <object type="application/x-flash"
#   data="your-file.swf"
#   width="0" height="0">
#   <!-- <param name="movie" value="your-file.swf" /> -->
#   <param name="quality" value="high"/>
# </object>"""

html = []
for _ in range(int(raw_input())):
    html.append(raw_input())

parser.feed('\n'.join(html))
