import os
import time
from csa_file import CsaFile

intervalSeconds = 15 # 更新間隔15秒
heartBeatSeconds = 0
while True:
    # 棋譜ファイル（CSA形式）を読みに行く
    # URLを直打ちしないといけない
    # 電竜戦
    # https://golan.sakura.ne.jp/denryusen/dr2_tsec/dist/#/multi?lt=1200&ln=30
    # csaFile = CsaFile.load('denryu-sen', 'https://golan.sakura.ne.jp/denryusen/dr2_tsec/kifufiles/dr2tsec+buoy_james8nakahi_dr2b3-11-bottom_43_dlshogi_xylty-60-2F+dlshogi+xylty+20210718131042.csa')
    # floodgate
    csaFile = CsaFile.load('floodgate', 'http://wdoor.c.u-tokyo.ac.jp/shogi/LATEST/2021/08/10/wdoor+floodgate-300-10F+Kristallweizen-Core2Duo-P7450+YaOu_V603_nnue_0721+20210810203012.csa')

    # Windows用のコマンド　コンソール消去
    os.system('cls')

    # 残り時間の算出
    hours = [0, csaFile.remainingTime[1]//60, csaFile.remainingTime[2]//60]
    seconds = [0, csaFile.remainingTime[1]%60, csaFile.remainingTime[2]%60]

    # 時計表示
    # そんなに精度出ないから、秒は消すのもあり
    print(f'') 
    print(f'') 
    print(f'    先手 {hours[1]: >3}分{seconds[1]: >2}秒        後手 {hours[2]: >3}分{seconds[2]: >2}秒')
    print(f'') 
    print(f'') 
    # デバッグ用情報
    print(f'    持ち時間　先手 {csaFile.timeLimit[1]:02}秒    後手 {csaFile.timeLimit[2]:02}秒') 
    print(f'    加算時間　先手 {csaFile.incrementalTime[1]:02}秒    後手 {csaFile.incrementalTime[2]:02}秒') 
    print(f'    消費時間　先手 {csaFile.erapsed[1]:02}秒    後手 {csaFile.erapsed[2]:02}秒') 
    print(f'    残り時間　先手 {csaFile.remainingTime[1]:02}秒    後手 {csaFile.remainingTime[2]:02}秒') 
    print(f'    URL {csaFile.url}') 
    print(f'    ハートビート {heartBeatSeconds}') # 生きてますよ

    heartBeatSeconds += intervalSeconds
    time.sleep(intervalSeconds)
