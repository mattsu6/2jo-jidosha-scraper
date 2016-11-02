import configparser

class Config:
  """コンフィグファイルのロードと管理"""

  FILE_NAME = './configs/config.ini'

  def __init__(self):
    iniFile = configparser.ConfigParser()
    iniFile.read(Config.FILE_NAME)

    self.user = iniFile.get('settings', 'user')
    self.password = iniFile.get('settings', 'pass')
    self.mail = iniFile.get('settings', 'mail')