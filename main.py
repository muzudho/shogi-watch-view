import urllib.request as urlreq
import re

# TODO 棋譜ファイル（CSA形式）を読む
f = urlreq.urlopen('https://golan.sakura.ne.jp/denryusen/dr2_tsec/kifufiles/dr2tsec+buoy_james8nakahi_dr2b3-11-bottom_43_dlshogi_xylty-60-2F+dlshogi+xylty+20210718131042.csa')
csa = f.read().decode("utf8")
# print(csa) # 開いたファイルの中身を表示する
f.close()

# 手番。1が先手、2が後手。配列の添え字に使う
phase = 0
# Example: +2726FU
patternPhase = re.compile(r"^([+-])\d{4}\w{2}$")

# 加算時間
increment = 0
# Example: 'Increment:2
patternIncrement = re.compile(r"^'Increment:(\d+)$")

# 消費時間
erapsed = [0,0,0]
# Example: T2
patternErapsed = re.compile(r"^T(\d+)$")

for line in csa.split('\n'):
    result = patternPhase.match(line)
    if result:
        print(f"Phase {result.group(1)}")
        sign = result.group(1)
        if sign=='+':
            phase = 1
        elif sign=='-':
            phase = 2
        else:
            phase = 0 # Error
        continue

    result = patternErapsed.match(line)
    if result:
        print(f"Erapsed {result.group(1)}")
        erapsed[phase] += int(result.group(1))
        continue

    result = patternIncrement.match(line)
    if result:
        print(f"Increment {result.group(1)}")
        increment = int(result.group(1))
        continue

    print(f"> {line}")

# TODO タイマーのルール取得（持ち時間、秒読み、加算時間など）
# 加算時間
# 'Increment:2

# TODO 開始時刻を取得

# TODO 指し手の消費時間を全て読取り、累計
print(f'Erapsed [0]{erapsed[0]} [1]{erapsed[1]} [2]{erapsed[2]}')

# TODO 手番の判定

# TODO 時計の表示（カウントダウンなどを描画）
