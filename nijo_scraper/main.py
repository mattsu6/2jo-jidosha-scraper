import logging
import os
from config import Config
from nijo_http import NijoHttpHelper
from database import DBConnector
import mailer

def init_logger():
  logging.basicConfig(
      filename='{home}/log/nijo.log'.format(home=os.path.dirname(__file__)),
      level=logging.INFO,
      format='%(asctime)s - %(levelname)s - %(message)s')
  logging.getLogger("requests").setLevel(logging.WARNING)


if __name__ == '__main__':
  init_logger()
  logging.info('Start app...')
  config = Config()
  http = NijoHttpHelper(config.user, config.password)

  db = DBConnector()
  wait_books = db.find_book_list(1) #マジックナンバー.ユーザid. #todo:user_infoテーブルを参照するように変更
  for wait_book in wait_books:
    if http.request_register(wait_book.date, wait_book.period):
      logging.info('Success for book: {date}, {period}'.format(date=wait_book.date, period=wait_book.period))
      mailer.send_mail('Success for book: {date}, {period}'.format(date=wait_book.date, period=wait_book.period), config.mail)
    else:
      logging.info('Failed for book: {date}, {period}'.format(date=wait_book.date, period=wait_book.period))
logging.info('End app...')
      # response = http.request_no_wish()
  #
  # context = scraper.find_book_status(response, scraper.Status.AVAILABLE)
  #
  # if len(context) > 0:
  #   text = ":予約可能日:\n"
  #   for c in context:
  #     text += c.date.strftime('%m/%d') + ' ' + str(c.period) + '\n'
  #   mailer.send_mail(text, config.mail)
  #   logging.info('mail sended, content size is %s', len(context))
  # else:
  #   logging.info('nothing...')
