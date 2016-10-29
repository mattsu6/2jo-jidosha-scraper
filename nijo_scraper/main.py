from nijo_scraper.config import Config
from nijo_scraper.nijo_http import NijoHttpHelper
import nijo_scraper.scraper as scraper

if __name__ == '__main__':
  config = Config()
  http = NijoHttpHelper()
  response = http.decode_for_jp(http.request_no_wish(config.user, config.password))

  scraper.find_status3(response)
