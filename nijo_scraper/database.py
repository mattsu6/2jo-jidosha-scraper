import pymysql
from nijo_scraper.config import Config

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
      results = cursor.fetchall()
      for r in results:
        print(r)
    connection.close()
  return wrapper

class DBConnector:
  @create_connection
  def findBookList(self, user_id):
    return 'select * from book where user_id={user_id}'.format(user_id=user_id)

db_con = DBConnector()
db_con.findBookList(1)