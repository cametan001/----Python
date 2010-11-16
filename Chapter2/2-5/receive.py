# -*- coding: utf-8 -*-
import poplib

s = poplib.POP3("host.to.mailserver")
# 認証処理を実行
for cnt in range(1, 10):
    r = s.retr(cnt)                     # インデックスを指定してメールを読み込む
    mailread("\n".join(r[1]))           # 本文を改行で連結して関数に渡す
