from csa_file import CsaFile

# TODO 棋譜ファイル（CSA形式）を読む
csaFile = CsaFile.load('https://golan.sakura.ne.jp/denryusen/dr2_tsec/kifufiles/dr2tsec+buoy_james8nakahi_dr2b3-11-bottom_43_dlshogi_xylty-60-2F+dlshogi+xylty+20210718131042.csa')

# 残り時間（秒） ＝ 持ち時間（秒） - 消費時間（秒）
remaining = [0,
             csaFile.timeLimit[1] - csaFile.erapsed[1],
             csaFile.timeLimit[2] - csaFile.erapsed[2]]
print(f'Remaining [1]{remaining[1]} [2]{remaining[2]}')

# 手番
print(f'Phase {csaFile.phase}')

# TODO 時計の表示（カウントダウンなどを描画）
