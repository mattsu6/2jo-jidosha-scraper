from lxml import html

def find_status0(page):
  return 'class="status0"' in page
def find_status1(page):
  tree = html.fromstring(page)
  print(tree.xpath('//'))
  return
def find_status2(page):
  return 'class="status2"' in page


def find_status3(page):
  tree = html.fromstring(page)

  for ():
  print(tree.xpath('//td[@class="status3"]/text()'))

  print(tree.xpath('//td[@class="status3"]/../td[1]/font/text()'))
  print(tree.xpath('//td[@class="status3"]/../td[1]/font/text()'))