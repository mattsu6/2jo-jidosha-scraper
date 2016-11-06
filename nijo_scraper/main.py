import datetime
import logging

from nijo_scraper.config import Config
from nijo_scraper.nijo_http import NijoHttpHelper


def init_logger():
  logging.basicConfig(
      filename='log/nijo.log',
      level=logging.INFO,
      format='%(asctime)s - %(levelname)s - %(message)s')

if __name__ == '__main__':
  init_logger()
  logging.info('launch app...')
  config = Config()
  http = NijoHttpHelper(config.user, config.password)
  http.request_register(datetime.date(2016, 11, 7), 1)
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
