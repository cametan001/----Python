#! /usr/bin/env python
# -*- coding: utf-8 -*-

from BaseHTTPServer import *
from SimpleHTTPServer import *
from threading import Thread

class ThreadedHTTPServer(Thread):
    def __init__(self, port = 8080, **kwargs):
        """Thread対応サーバオブジェクトの初期化
        """
        self.httpd = HTTPServer(("", port),
                                SimpleHTTPRequestHandler)
        self.httpd_running = False
        Thread.__init__(self)

    def run(self):
        """スレッドのコードを実行
        """
        self.httpd_running = True
        while self.httpd_running:
            self.httpd.handle_request()
        del self.httpd

    def stop(self):
        """スレッドの実行を停止するためフラグを建てる
        """
        self.httpd_running = False

    
