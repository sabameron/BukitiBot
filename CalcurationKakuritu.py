from byAllWeapon import bukiRandom

def hensaNoNijyoList(list):
    nijyoList = []
    for e,t in enumerate(list):
        nijyoList.append(t**2)
    #print(nijyoList)
    return nijyoList

def calcurationKakuritu(times):
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

    #検証用
    # print(hensa[1])
    # print(hensaNoNijyoList(hensa)[1])

calcurationKakuritu(15000)
