import nijo_scraper.scraper as scraper
import nijo_scraper.mailer as mailer
from nijo_scraper.config import Config
from nijo_scraper.nijo_http import NijoHttpHelper

if __name__ == '__main__':
  config = Config()
  http = NijoHttpHelper()
  response = http.decode_for_jp(http.request_no_wish(config.user, config.password))

  context = scraper.find_book_status(response, scraper.Status.AVAILABLE)

  if len(context) > 0:
    text = ":予約可能日:"
    for c in context:
      text += c.date.strftime('%m/%d') + ' ' + str(c.period) + '\n'
    mailer.send_mail(text, config.mail)
    print('mail sended')
  else:
    print('nothing...')
