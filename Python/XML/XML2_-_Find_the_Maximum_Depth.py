import xml.etree.ElementTree as ETree


maxdepth = 0
def depth(elem, level):
    global maxdepth

    level += 1
    if len(list(elem)):
        for child in elem:
            depth(child, level)
    else:
        if level > maxdepth:
            maxdepth = level


xml = """<feed xml:lang='en'>
  <title>HackerRank</title>
  <subtitle lang='en'>Programming challenges</subtitle>
  <link rel='alternate' type='text/html' href='http://hackerrank.com/'/>
  <updated>2013-12-25T12:00:00</updated>
  <entry>
  	<author gender='male'>Harsh</author>
    <question type='hard'>XML 1</question>
    <description type='text'>This is related to XML parsing</description>
  </entry>
</feed>"""

tree = ETree.ElementTree(ETree.fromstring(xml))
depth(tree.getroot(), -1)
print maxdepth
