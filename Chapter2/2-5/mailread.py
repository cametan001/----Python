# -*- coding: utf-8 -*-
from email.Header import Header, make_header, decode_header
import email

def mailread(src):
    """生メールから件名、本文、添付ファイル(画像)を取り出す
    """
    # Messageオブジェクトを作る
    m = email.message_from_string(src)
    # ヘッダをデコード
    subj = decode_header(m["Subject"])
    # ヘッダを表示
    try:
        print unicode(make_header(subj))
    except: pass;
    print "-" * 70
    # 全パートをスキャン
    for part in m.walk():
        type = part.get_content_maintype() # maintypeを得る
        if type and type.find("image") != -1:
            # 画像の添付が見つかったら、ファイルに保存
            filename = part.get_filename("notitle.img")
            f = open(filename, "wb")
            f.write(part.get_payload(decode = True))
            f.close()
        elif type and type.find("text") != -1:
            # テキストは表示
            enc ~ part.get_charsets()[0] or "us-ascii"
            print part.get_payload().decode(enc, "ignore")
            




















