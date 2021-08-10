import urllib.request as urlreq
import re
import datetime
from csa_file import CsaFile

# TODO 棋譜ファイル（CSA形式）を読む
csaFile = CsaFile.load('https://golan.sakura.ne.jp/denryusen/dr2_tsec/kifufiles/dr2tsec+buoy_james8nakahi_dr2b3-11-bottom_43_dlshogi_xylty-60-2F+dlshogi+xylty+20210718131042.csa')

# TODO タイマーのルール取得（持ち時間、秒読み、加算時間など）
# 持ち時間
print(f'TimeLimit [0]{csaFile.timeLimit[0]} [1]{csaFile.timeLimit[1]} [2]{csaFile.timeLimit[2]}')
# 加算時間
print(f'Increment {csaFile.increment}')

# TODO 開始時刻を取得
print(f'StartTime Y={csaFile.startTime.year} M={csaFile.startTime.month} D={csaFile.startTime.day} H={csaFile.startTime.hour} m={csaFile.startTime.minute} s={csaFile.startTime.second}')

# TODO 指し手の消費時間を全て読取り、累計
print(f'Erapsed [0]{csaFile.erapsed[0]} [1]{csaFile.erapsed[1]} [2]{csaFile.erapsed[2]}')

# TODO 手番の判定

# TODO 時計の表示（カウントダウンなどを描画）
