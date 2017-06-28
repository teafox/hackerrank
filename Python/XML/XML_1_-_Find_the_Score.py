import xml.etree.ElementTree as ETree


def get_attr_number(node):
    count = 0
    count += len(node.attrib)
    for child in node:
        count += len(child.attrib)
        if len(list(child)):
            count += get_attr_number(child)
    return count



s_xml = """<feed xml:lang='en'>
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


tree = ETree.ElementTree(ETree.fromstring(s_xml))
root = tree.getroot()
print get_attr_number(root)
