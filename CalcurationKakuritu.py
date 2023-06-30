from byAllWeapon import bukiRandom

def hensaNoNijyoList(list):
    nijyoList = []
    for e,t in enumerate(list):
        nijyoList.append(t**2)
    #print(nijyoList)
    return nijyoList

def calcurationKakuritu(times):
    print(f"検証回数{times}")
    weaponDic = {}
    n = 0
    while n < times:
        buki = bukiRandom()
        #print(bukiRandom())
        if buki in weaponDic.keys():
            weaponDic[buki] = weaponDic[buki] + 1
        else :
            weaponDic[buki] = 0
        n += 1
    #print(len(weaponDic))
    heikin = sum(weaponDic.values())/len(weaponDic)
    print(f"平均：{heikin}")
    weaponList = weaponDic.keys()
    hensa = []
    #print(weaponDic.keys())
    for e,t in enumerate(weaponList):
        hensa.append(heikin - weaponDic[t])
    heikinHensa = sum(hensaNoNijyoList(hensa))/len(hensaNoNijyoList(hensa))
    print(f"分散：{heikinHensa}")
    print(f"標準偏差：{heikinHensa**(1/2)}")
    print(f"変動変数：{heikinHensa**(1/2)/len(hensaNoNijyoList(hensa))}")
    print("----------------------")
    #print(f"回数：{weaponDic}")
    #print("----------------------")
    #print(f"偏差：{hensa}")
    #検証用
    # print(hensa[1])
    # print(hensaNoNijyoList(hensa)[1])

calcurationKakuritu(15000)

