import random

random_number = random.randint(0, 1)
page = "最初" if random_number == 0 else "最後"
position = random.randint(1, 8)
position2 = random.randint(1, 12)

fraseList = ["『一番かっこいい武器』","『一番強い武器』",f"左上から[{position2}]番目の武器"]
comment = random.randint(1, 50)
frase = fraseList[comment] if comment <= 2 else fraseList[2]

# 結果の表示
print(f"「{page}」から[{position}]ページ目の、{frase}を選択するでし！")
