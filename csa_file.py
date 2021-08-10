import urllib.request as urlreq
import re
import datetime

class CsaFile:
    # 持ち時間（秒）
    # 電竜戦では、$TIME_LIMIT（持ち時間）ではなく、$EVENT（イベント名）の方に持ち時間が書かれている。単位は秒だろうか？
    # また - _ の取り扱いが不確かなので、うしろからパースすること。
    # Example: $EVENT:dr2tsec+buoy_james8nakahi_dr2b3-11-bottom_43_dlshogi_xylty-60-2F+dlshogi+xylty+20210718131042
    __patternTimeLimit = re.compile(r"^\$EVENT:.+-(\d+)-\d+F\+[0-9A-Za-z_-]+\+[0-9A-Za-z_-]+\+\d{14}$")

    # 手番。1が先手、2が後手。配列の添え字に使う
    # Example: +2726FU
    __patternPhase = re.compile(r"^([+-])\d{4}\w{2}$")

    # 開始時間
    # Example: $START_TIME:2021/07/18 13:10:42
    __patternStartTime = re.compile(r"^\$START_TIME:(\d{4})/(\d{2})/(\d{2}) (\d{2}):(\d{2}):(\d{2})$")

    # 加算時間
    # Example: 'Increment:2
    __patternIncrement = re.compile(r"^'Increment:(\d+)$")

    # 消費時間
    # Example: T2
    __patternErapsed = re.compile(r"^T(\d+)$")

    def __init__(self):
        # 持ち時間（秒）
        self._timeLimit = [0,0,0] # [未使用,先手,後手]

        # 手番。1が先手、2が後手。配列の添え字に使う
        self._phase = 0

        # 開始時間
        self._startTime = None

        # 加算時間
        self._increment = 0

        # 消費時間
        self._erapsed = [0,0,0] # [未使用,先手,後手]

    @staticmethod
    def load(csaUrl):
        csaFile = CsaFile()

        # 棋譜ファイル（CSA形式）を読む
        f = urlreq.urlopen(csaUrl)
        csa = f.read().decode("utf8")
        # print(__csa) # 開いたファイルの中身を表示する
        f.close()

        for line in csa.split('\n'):
            result = CsaFile.__patternPhase.match(line)
            if result:
                print(f"Phase {result.group(1)}")
                sign = result.group(1)
                if sign=='+':
                    csaFile._phase = 1
                elif sign=='-':
                    csaFile._phase = 2
                else:
                    csaFile._phase = 0 # Error
                continue

            result = CsaFile.__patternErapsed.match(line)
            if result:
                print(f"Erapsed {result.group(1)}")
                csaFile._erapsed[csaFile.phase] += int(result.group(1))
                continue

            result = CsaFile.__patternTimeLimit.match(line)
            if result:
                print(f"TimeLimit Sec={result.group(1)}")
                # 先手と後手の持ち時間は同じ
                csaFile._timeLimit = [0, int(result.group(1)), int(result.group(1))]
                continue

            result = CsaFile.__patternStartTime.match(line)
            if result:
                print(f"StartTime [1]={result.group(1)} [2]={result.group(2)} [3]={result.group(3)} [4]={result.group(4)} [5]={result.group(5)} [6]={result.group(6)}")
                csaFile._startTime = datetime.datetime(
                    int(result.group(1)),
                    int(result.group(2)),
                    int(result.group(3)),
                    int(result.group(4)),
                    int(result.group(5)),
                    int(result.group(6)))
                continue

            result = CsaFile.__patternIncrement.match(line)
            if result:
                print(f"Increment {result.group(1)}")
                csaFile._increment = int(result.group(1))
                continue

            print(f"> {line}")

        return csaFile

    @property
    def timeLimit(self):
        """持ち時間（秒）[未使用,先手,後手]"""
        return self._timeLimit

    @property
    def phase(self):
        """手番。1が先手、2が後手。配列の添え字に使う"""
        return self._phase

    @property
    def startTime(self):
        """開始時間"""
        return self._startTime

    @property
    def increment(self):
        """加算時間"""
        return self._increment

    @property
    def erapsed(self):
        """消費時間 [未使用,先手,後手]"""
        return self._erapsed