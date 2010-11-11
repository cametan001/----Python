#! /usr/bin/env python
# -*- coding: utf-8 -*-
from Tkinter import *                   # Tkinterのクラスなどをインポート
import time

class App(Frame):                       # アプリケーションのクラスを定義
    TIME = 60 * 3                       # タイマーの待ち時間
    def __init__(self, master = None):
        " 初期化用のメソッド "
        Frame.__init__(self, master)
        self.time = 0
        self.master.title("Tk Timer")   # フレームのタイトル
        self.timestr = StringVar()      # タイマーの時間表示
        self.timestr.set("03:00")
        l = Label(self, textvariable = self.timestr,
                  font = ('Helvetica', '48', 'bold'))
        b1 = Button(self, text = "Start", command = self.countdown)
        b2 = Button(self, text = "Quit", command = self.master.destroy)
        for obj, sideparam in ((l, TOP), (b1, LEFT), (b2, RIGHT)):
            obj.pack(side = sideparam)
        self.pack()

    def countdown(self):
        " タイマーの時間を減らしていくメソッド "
        if self.time == 0:               # 初めてタイマーが稼働
            self.time = time.time()      # 時間を初期化
        timeleft = max(self.TIME - (time.time() - self.time), 0)
        min, sec = (timeleft) / 60, timeleft % 60
        self.timestr.set("%02d:%02d" % (min, sec))
        self.after(1000, self.countdown) # 1秒後にメソッドを呼ぶ

if __name__ == "__main__":
    app = App()
    app.mainloop()




















