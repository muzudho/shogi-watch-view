from csa_file import CsaFile

# TODO 棋譜ファイル（CSA形式）を読む
# https://golan.sakura.ne.jp/denryusen/dr2_tsec/dist/#/multi?lt=1200&ln=30
csaFile = CsaFile.load('https://golan.sakura.ne.jp/denryusen/dr2_tsec/kifufiles/dr2tsec+buoy_james8nakahi_dr2b3-11-bottom_43_dlshogi_xylty-60-2F+dlshogi+xylty+20210718131042.csa')

print(f'Remaining       [1]{csaFile.remainingTime[1]} [2]{csaFile.remainingTime[2]}')

# 手番
print(f'Phase {csaFile.phase}')

# TODO 時計の表示（カウントダウンなどを描画）
if csaFile.phase==1:
    # 先手番の時計を進める
    pass
elif csaFile.phase==2:
    # 後手番の時計を進める
    pass
else:
    pass
