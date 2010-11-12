# -*- coding: utf-8 -*-

class Bookmark:

    def __init__(self, title, url):
        # インスタンス初期化用のメソッド
        self.title = title              # タイトルをアトリビュートに代入
        self.url = url                  # URLをアトリビュートに代入
    
    def print_outline(self):
        # クラスの概要を説明するメソッド
        print "[Bookmarkクラス]"
        print "ブックマークを管理するためのクラスです"

    def set_title(self, title):
        # タイトルを設定するメソッド
        self.title = title              # 引数をアトリビュートに代入する

    def get_title(self):
        # タイトルを取得するメソッド
        return self.title

    def set_url(self, url):
        # URLを設定するメソッド
        self.url = url

    def get_url(self):
        # URLを取得するメソッド
        return self.url

    def __str__(self):
        # インスタンスオブジェクトの概要を表示する
        return "Title : %s, URL : %s" % (self.title, self.url)
