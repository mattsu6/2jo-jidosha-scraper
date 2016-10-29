import requests

class NijoHttpHelper:
  """二条のアプリにログインしたりするHttpリクエスト関連のクラス"""

  def __init__(self):
    self.headers = {
      'content-type' : 'application/x-www-form-urlencoded',
    }

  def get_cookies(self, user, password):
    """
    技能予約アプリにログインしてクッキーを取得する
    :param user: ログインユーザ名
    :param password: ログインパスワード
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
              'server='.format(user=user, password=password)

    return requests.post(url, data=payload, headers=self.headers).cookies

  def request_no_wish(self, user, password):
    """
    教官指名無し時のHTTPレスポンスを取得する
    :param user: ログインユーザ名
    :param password: ログインパスワード
    :return: HTTPレスポンス
    """
    cookies = self.get_cookies(user, password)
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
    return requests.post(url, data=payload, cookies=cookies, headers=self.headers)

  @staticmethod
  def decode_for_jp(response):
    """
    日本語に対応したデコードを行う
    :param response: HTTPレスポンス
    :return: デコード後のHTTPレスポンス
    """
    return response.content.decode('cp932')