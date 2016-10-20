from nijo_scraper.config import Config
from nijo_scraper.nijo_http import NijoHttpHelper
import nijo_scraper.scraper as scraper

if __name__ == '__main__':
  config = Config()
  http = NijoHttpHelper()
  response = http.load_no_wish(config.user, config.password)

  print(scraper.find_status0(http.decode(response)))
