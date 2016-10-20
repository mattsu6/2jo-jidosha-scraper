# 二条自動車教習所・予約監視
二条自動車教習所が提供する技能教習予約用のwebアプリを監視し
技能の空きがあれば自動的にメール通知をしてくれるソフトウェアです．
https://www.e-license.jp/el/nijo/

# 使い方
```sh
(you@2jo-jidosha-scraper)
$ cp ./2jo-jidosha-scraper/config/config-sample.ini ~/2jo-jidosha-scraper/config/config.ini
$ vi ./2jo-jidosha-scraper/config/config.ini #自分用の情報に編集する
$ python ./2jo-jidosha-scraper/main.py
```
