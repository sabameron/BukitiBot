import random

buki_name = ['わかばシューター',
'もみじシューター',
'スプラシューター',
'スプラシューターコラボ',
'N-ZAP85',
'N-ZAP89',
'プロモデラーMG',
'プロモデラーRG',
'ボールドマーカー',
'ボールドマーカーネオ',
'シャープマーカー',
'シャープマーカーネオ',
'.52ガロン',
'.96ガロン',
'.96ガロンデコ',
'L3リールガン',
'L3リールガンD',
'H3リールガン',
'H3リールガンD',
'プライムシューター',
'プライムシューターコラボ',
'ジェットスイーパー',
'ジェットスイーパーカスタム',
'ボトルガイザー',
'スペースシューター',
'スペースシューターコラボ',
'スプラローラー',
'スプラローラーコラボ',
'カーボンローラー',
'カーボンローラーデコ',
'ヴァリアブルローラー',
'ダイナモローラー',
'ワイドローラー',
'ワイドローラーコラボ',
'ドライブワイパー',
'ドライブワイパーデコ',
'ジムワイパー',
'パブロ',
'パブロ・ヒュー',
'ホクサイ',
'フィンセント',
'ホットブラスター',
'ロングブラスター',
'ノヴァブラスター',
'ノヴァブラスターネオ',
'クラッシュブラスター',
'クラッシュブラスターネオ',
'ラピッドブラスター',
'ラピッドブラスターデコ',
'Rブラスターエリート',
'Rブラスターエリートデコ',
'S-BLAST92',
'バケットスロッシャー',
'バケットスロッシャーデコ',
'ヒッセン',
'ヒッセン・ヒュー',
'スクリュースロッシャー',
'エクスプロッシャー',
'オーバーフロッシャー',
'スプラマニューバー',
'スパッタリー',
'スパッタリー・ヒュー',
'クアッドホッパーブラック',
'クアッドホッパーホワイト',
'ケルビン525',
'デュアルスイーパー',
'デュアルスイーパーカスタム',
'パラシェルター',
'キャンピングシェルター',
'キャンピングシェルターソレーラ',
'スパイガジェット',
'トライストリンガー',
'LACT-450',
'スプラスピナー',
'スプラスピナーコラボ',
'バレルスピナー',
'バレルスピナーデコ',
'クーゲルシュライバー',
'ノーチラス47',
'ハイドラント',
'スプラチャージャー',
'スプラチャージャーコラボ',
'スプラスコープ',
'スプラスコープコラボ',
'リッター4K',
'4Kスコープ',
'スクイックリンα',
'ソイチューバー',
'14式竹筒銃・甲',
'R-PEN/5H']

def bukiRandom():
    buki_all = len(buki_name)-1
    buki = random.randint(0, buki_all)
    return buki_name[buki]

if __name__ == "__main__": 
    print(f"||『{bukiRandom()}』||を使うでし！")
    #print(len(buki_name))
