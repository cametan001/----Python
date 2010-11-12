# -*- coding: utf-8 -*-
from bookmark import Bookmark

class Blogmark(Bookmark):

    def __init__(self, title, url, rss):
        # インスタンス初期化用のメソッド
        self.rss = rss                  # RSSのURLをアトリビュートに代入
        Bookmark.__init__(self, title, url)
