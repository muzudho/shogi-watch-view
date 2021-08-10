import os
import time
from csa_file import CsaFile

while True:
    # 棋譜ファイル（CSA形式）を読みに行く
    # URLを直打ちしないといけない
    # https://golan.sakura.ne.jp/denryusen/dr2_tsec/dist/#/multi?lt=1200&ln=30
    csaFile = CsaFile.load('https://golan.sakura.ne.jp/denryusen/dr2_tsec/kifufiles/dr2tsec+buoy_james8nakahi_dr2b3-11-bottom_43_dlshogi_xylty-60-2F+dlshogi+xylty+20210718131042.csa')

    # Windows用のコマンド　コンソール消去
    os.system('cls')

    # 残り時間の算出
    hours = [0, csaFile.remainingTime[1]//60, csaFile.remainingTime[2]//60]
    # seconds = [0, csaFile.remainingTime[1]%60, csaFile.remainingTime[2]%60]

    # 時計表示
    # そんなに精度出ないから１分単位にする
    print(f'') 
    print(f'') 
    print(f'    ▲ {hours[1]:02}分    △ {hours[2]:02}分')
    print(f'') 
    print(f'') 

    time.sleep(15) # 15秒スリープ
