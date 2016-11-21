import configparser
import os
import logging
import traceback

class Config:
  """コンフィグファイルのロードと管理"""
  class __Config:
    FILE_NAME = '{home}/configs/config.ini'.format(home=os.path.dirname(__file__))
    def __init__(self):
      iniFile = configparser.ConfigParser()
      iniFile.read(self.FILE_NAME)

      self.user = iniFile.get('settings', 'user')
      self.password = iniFile.get('settings', 'pass')
      self.mail = iniFile.get('settings', 'mail')

      self.nijo_db_host = iniFile.get('database', 'nijo.db.host')
      self.nijo_db_name = iniFile.get('database', 'nijo.db.name')
      self.nijo_db_user = iniFile.get('database', 'nijo.db.user')
      self.nijo_db_pass = iniFile.get('database', 'nijo.db.pass')

      self.mailer_name = iniFile.get('mailer', 'mailer.name')
      self.mailer_pass = iniFile.get('mailer', 'mailer.pass')

  instance = None

  def __init__(self):
    try:
      if not Config.instance:
        Config.instance = Config.__Config()
        logging.info('Loaded Config')
    except:
      tb = traceback.format_exc()
      logging.error(tb)
      logging.error('{home}/configs/config.ini'.format(home=os.path.dirname(__file__)))

  def __getattr__(self, item):
    return getattr(self.instance, item)