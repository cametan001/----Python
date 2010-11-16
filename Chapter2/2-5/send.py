s = smtplib.SMTP("mail.webcore.core.jp")
outer = makemail("日本語を含むmailの件名",
                 "toaddr@mail.host",
                 "本文です",
                 "takigawa.jpg")
s.sendmail("sender@mailhost.com", "toaddr@mail.host",
           outer.as_string())
s.quit()
