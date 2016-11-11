import configparser

class Config:
  """コンフィグファイルのロードと管理"""
  class __Config:
    FILE_NAME = './configs/config.ini'
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

  instance = None

  def __init__(self):
    if not Config.instance:
      Config.instance = Config.__Config()
  def __getattr__(self, item):
    return getattr(self.instance, item)