from lxml import html
import datetime
import re

class BookStatus:
  """予約状況を表現するクラス. 二条予約サイトから取得した情報を表現"""

  def __init__(self, date, period, status):
    """
    コンストラクタ
    :param date: 日付. datetime.date
    :param period: 時限. int
    :param status:空き状態. Status
    """
    self.date = date
    self.period = period
    self.status = status

class Status:
  """予約状況を表現する列挙型"""
  FULL = 0
  AVAILABLE = 1
  RESERVED = 3

  @staticmethod
  def get_str(status):
    return 'status' + str(status)

def find_book_status(page, status=Status.AVAILABLE):
  """
  与えられたHTMLページの予約状況を確認して返す.
  :param page: HTMLドキュメント
  :param status: 確認したい予約状況の数字 Statusクラスを参照
  :return: 予約状況を示すBookStatusのset
  """
  tree = html.fromstring(page)

  bookStatusSet = set([])
  for col, tr in enumerate(tree.xpath('//tr[@class="date"]')):
    for row, td in enumerate(tr):
      if td.attrib['class'] != Status.get_str(status):
        continue
      date = convert_date(tr.find('./td[@class="view"]').text_content())
      bookStatusSet.add(BookStatus(date, row, 0))

  return bookStatusSet

def convert_date(dateStr, year = 2016):
  """
  10月10日 (木) のような文字列をdatetime.dateに変換する.
  とりあえず，2016年で変換する
  :param dateStr: 日付. ex'10月22日'
  :return: 日付. datetime.date
  """
  pattern = re.compile(r'\s*(\d+)\D+(\d+)')
  m = pattern.match(dateStr)
  month = int(m.group(1))
  day = int(m.group(2))

  return datetime.date(year, month, day)