# -*- coding: utf-8 -*-
from email.Header import Header
from email.MIMEMultipart import MIMEMultipart
from email.MIMEImage import MIMEImage
from email.MIMEText import MIMEText

fromaddr = "sender@mailhost.com"

def makemail(subjstr, toaddr, body, filename):
    """サブジェクトと本文を渡してMessageオブジェクトを作る
    filenameにファイル名やパスを渡し、画像ファイルを添付する
    """
    outer = MIMEMultipart()             # Messageオブジェクトを作る
    subjstr = subjstr.encode("iso-2022-jp") # 件名をエンコード
    subj = Header(subjstr, "iso-2022-jp")
    outer["Subject"] = subj             # ヘッダに設定
    outer["From"] = fromaddr            # 送信元をヘッダに
    outer["To"] = toaddr                # 送信先をヘッダに
    mainpart = MIMEText("", _charset = "iso-2022-jp")
    mainpart.set_payload(body.encode("iso-2022-jp"))
    outer.attach(mainpart)              # Messageオブジェクトに追加

    img = MIMEImage(open(filename).read())
    img.add_header('Content-Disposition', # ファイル名を設定
                   'attachment', filename = 'takigawa.jpg')
    outer.attach(img)                   # Messageオブジェクトに追加

    return outer




















