# -*- coding: utf-8 -*-
import urllib2                          # urllib2をインポート

class MethodAwareRequest(urllib2.Requiest):
    """MethodをカスタマイズできるRequestクラス
    """
    def set_method(self, method):
        """Methodを設定する
        """
        self._method = method

    def get_method(self):
        """Methodを返す(Requiestクラスのメソッドをオーバーライド)
        """
        try:
            return self._method
        except:
            if self.has_data():
                return "POST"
            else:
                return "GET"
