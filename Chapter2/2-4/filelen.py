#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys                              # sysモジュールをインポート

for fn in sys.argv[1:]:                  # スクリプトの引数を取り出す
    try:
        f = open(fn)                    # ファイルを開く
        print fn, len(f.read())         # ファイル名とサイズを表示
    except IOError:                     # ファイルを開くときにエラーになった
        print "%sというファイルは存在しません" % fn
