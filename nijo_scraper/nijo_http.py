import requests

class NijoHttpHelper:
  """二条のアプリにログインしたりするHttpリクエスト関連のクラス"""

  def __init__(self, user, password):
    self.headers = {
      'content-type' : 'application/x-www-form-urlencoded',
    }
    self.user = user
    self.password = password
    self.cookies = self.get_cookies()

  def get_cookies(self):
    """
    技能予約アプリにログインしてクッキーを取得する
    :return: 発行されたクッキー
    """
    url = 'https://www.e-license.jp/el25/pc/p01a.action'
    payload = 'b.studentId={user}&' \
              'b.password={password}&' \
              'method%3AdoLogin=%83%8D%83O%83C%83%93&' \
              'b.wordsStudentNo=%8B%B3%8FK%90%B6%94%D4%8D%86&' \
              'b.processCd=&' \
              'b.kamokuCd=&' \
              'b.schoolCd=MpUBkZwk%2BuA%2BbrGQYS%2B1OA%3D%3D&index=0&' \
              'server='.format(user=self.user, password=self.password)

    return requests.post(url, data=payload, headers=self.headers).cookies

  def request_no_wish(self):
    """
    教官指名無し時のHTTPレスポンスを取得する
    :return: HTTPレスポンス
    """
    url = 'https://www.e-license.jp/el25/pc/p03c.action'
    payload = 'b.schoolCd=MpUBkZwk%2BuA%2BbrGQYS%2B1OA%3D%3D&' \
              'b.processCd=V&' \
              'b.kamokuCd=0&' \
              'b.carModelCd=301&' \
              'b.instructorCd=0&' \
              'b.dateInformationType=&' \
              'b.lastScreenCd=P03A&' \
              'b.instructorTypeCd=0&' \
              'b.page=1&' \
              'b.groupCd=1&' \
              '%23instructor.cd=2'
    return self.decode_for_jp(requests.post(url, data=payload, cookies=self.cookies, headers=self.headers))

  def request_register(self, date, period):
    """
    指定日時・時限で予約する.
    :param date: 日時. datetime.date
    :param period: 時限. int
    :return: 予約に成功したらTrue
    """
    url = 'https://www.e-license.jp/el25/pc/p03a.action'
    payload = 'b.schoolCd=MpUBkZwk%2BuA%2BbrGQYS%2B1OA%3D%3D&' \
              'b.processCd=V&' \
              'b.kamokuCd=0&' \
              'b.lastScreenCd=&' \
              'b.instructorTypeCd=0&' \
              'b.dateInformationType={date}&' \
              'b.infoPeriodNumber={period}&' \
              'b.carModelCd=301&' \
              'b.instructorCd=0&' \
              'b.page=1&' \
              'b.groupCd=1&' \
              'b.changeInstructorFlg=1&' \
              'b.nominationInstructorCd=0&' \
              'upDate=1478173167645'.format(date=date.strftime('%Y%m%d'), period=period)
    response = self.decode_for_jp(requests.post(url, data=payload, cookies=self.cookies, headers=self.headers))
    if '予約はできません' in response:
      return False
    if '予約の空きがありません' in response:
      return False
    return True

  #def request_register_musen(self, date, period):

  def decode_for_jp(self, response):
    """
    日本語に対応したデコードを行う
    :param response: HTTPレスポンス
    :return: デコード後のHTTPレスポンス
    """
    return response.content.decode('cp932')
