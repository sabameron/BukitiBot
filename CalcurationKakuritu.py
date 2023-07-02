from byAllWeapon import bukiRandom
from tqdm import tqdm

def hensaNoNijyoList(list):
    nijyoList = []
    for e, t in enumerate(list):
        nijyoList.append(t**2)
    return nijyoList

def calcurationKakuritu(times):
    weaponDic = {}
    n = 0
    pbar = tqdm(total=times, ncols=80)  # 進捗バーを表示
    while n < times:
        buki = bukiRandom("Calcuration")
        if buki in weaponDic.keys():
            weaponDic[buki] = weaponDic[buki] + 1
        else:
            weaponDic[buki] = 0
        n += 1
        pbar.update(1)  # 進捗バーを更新
    pbar.close()  # 進捗バーを閉じる
    heikin = sum(weaponDic.values()) / len(weaponDic)
    print(f"平均：{heikin}")
    weaponList = weaponDic.keys()
    hensa = []
    for e, t in enumerate(weaponList):
        hensa.append(heikin - weaponDic[t])
    heikinHensa = sum(hensaNoNijyoList(hensa)) / len(hensaNoNijyoList(hensa))
    print(f"検証回数{times}")
    print(f"分散：{heikinHensa}")
    print(f"標準偏差：{heikinHensa**(1/2)}")
    print(f"変動変数：{heikinHensa**(1/2)/len(hensaNoNijyoList(hensa))}")
    print("----------------------")
    print(weaponDic)

calcurationKakuritu(90)
