#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3
# 郵便番号のリスト
postno = [[u"東京都千代田区", "100-0000"],
          [u"東京都千代田区飯田橋", "102-0072"],
          [u"東京都千代田区一番町", "102-0082"],
          [u"東京都千代田区岩本町", "101-0032"]]
# コネクションオブジェクトを作る
con = sqlite3.connect(":memory")
cur = con.cursor()                      # カーソルを作る
# テーブルを作成
cur.execute("""CREATE TABLE postdb(
address text, postno text)""")
# データを登録
for item in postno:
    cur.execute("""INSERT INTO postdb(address, postno)
    VALUES(?, ?)""", item)

# データを選択、表示
cur.execute("SELECT * FROM postdb WHERE postno = ?",
            ("102-0072",))
data = cur.fetchone()
print data[1], data[0]
