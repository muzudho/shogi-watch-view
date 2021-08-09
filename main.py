import urllib.request as urlreq

# TODO 棋譜ファイル（CSA形式）を読む
f = urlreq.urlopen('https://golan.sakura.ne.jp/denryusen/dr2_tsec/kifufiles/dr2tsec+buoy_james8nakahi_dr2b3-11-bottom_43_dlshogi_xylty-60-2F+dlshogi+xylty+20210718131042.csa')
csa = f.read().decode("utf8")
print(csa) # 開いたファイルの中身を表示する
f.close()

# TODO タイマーのルール取得（持ち時間、秒読み、加算時間など）

# TODO 開始時刻を取得

# TODO 指し手の消費時間を全て読取り、累計

# TODO 手番の判定

# TODO 時計の表示（カウントダウンなどを描画）
