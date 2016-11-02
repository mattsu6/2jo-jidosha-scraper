# 二条自動車教習所・予約監視
二条自動車教習所が提供する技能教習予約用のwebアプリを監視し  
技能の空きがあれば自動的にメール通知をしてくれるソフトウェアです．  
https://www.e-license.jp/el/nijo/

# 動作環境
Python3

# 使い方
## for Mac
```sh
(you@2jo-jidosha-scraper)
$ cp ./nijo_scraper/config/config-sample.ini ./nijo_scraper/config/config.ini
$ vi ./nijo_scraper/config/config.ini #自分用の情報に編集する
$ xcode-select --install #Xcodeのコマンドラインツールが必要
$ pip3 install lxml
$ pip3 install requests
$ python3 ./nijo_scraper/main.py
```
