import pymysql
from config import Config

def create_connection(query):
  """
  クエリを発行するためのデコレータ

  :param query: クエリストリング
  :return:
  """
  def wrapper(*args, **kargs):
    config = Config()
    connection = pymysql.connect(host= config.nijo_db_host,
                                 user= config.nijo_db_user,
                                 password= config.nijo_db_pass,
                                 db= config.nijo_db_name,
                                 charset='utf8',
                                 cursorclass=pymysql.cursors.DictCursor)
    with connection.cursor() as cursor:
      cursor.execute(query(*args, **kargs))
      rows = cursor.fetchall()
    connection.commit()
    connection.close()
    return rows
  return wrapper

class DBConnector:

  @create_connection
  def __execute(self, query):
    return query

  def find_book_list(self, user_id):
    """
    予約待ちのリストを取得.
    優先度の高い順に取得する.

    :param user_id: ユーザID
    :return: WaitBookのリスト
    """
    rows = self.__execute('select * from book where ' \
                           'user_id={user_id} and ' \
                           'status="WAIT"'.format(user_id=user_id))
    wait_books = []
    for row in rows:
      wait_books.append(WaitBook(
        date=row['book_date'],
        period=row['book_period'],
        priority=row['priority']
      ))
    return sorted(wait_books, key=lambda wait_book: wait_book.priority, reverse=True)

  def change_to_pause(self):
    self.__execute('update book set status="PAUSE"')

class WaitBook:
  """予約待ち状況を表現するクラス"""

  def __init__(self, date, period, priority):
    """
    コンストラクタ
    :param date: 予約したい日付. datetime.date
    :param period: 予約したい時限. byte
    :param priority: 優先度 (高いほど優先される). byte
    """
    self.date = date
    self.period = period
    self.priority = priority