import random
import pickle
import sys

if len(sys.argv) < 2:
    id = "0"
else :
    id = str(sys.argv[1])


buki_all = [
 'スプラシューター',
 'ヒーローシューター レプリカ',
 'スプラシューターコラボ',
 'オーダーシューター レプリカ',
 'オクタシューター レプリカ',
 '.96ガロン',
 '.96ガロンデコ',
 'シャープマーカー',
 'シャープマーカーネオ',
 'わかばシューター',
 'もみじシューター',
 '.52ガロン',
 '.52ガロンデコ',
 'H3リールガン',
 'H3リールガンD',
 'L3リールガン',
 'L3リールガンD',
 'N-ZAP85',
 'N-ZAP89',
 'ジェットスイーパー',
 'ジェットスイーパーカスタム',
 'プライムシューター',
 'プライムシューターコラボ',
 'プロモデラーMG',
 'プロモデラーRG',
 'ボールドマーカー',
 'ボールドマーカーネオ',
 'ボトルガイザー',
 'ボトルガイザーフォイル',
 'スペースシューター',
 'スペースシューターコラボ',
 'ロングブラスター',
 'ホットブラスター',
 'ホットブラスターカスタム',
 'クラッシュブラスター',
 'クラッシュブラスターネオ',
 'Rブラスターエリート',
 'Rブラスターエリートデコ',
 'ノヴァブラスター',
 'ノヴァブラスターネオ',
 'オーダーブラスター レプリカ',
 'ラピッドブラスター',
 'ラピッドブラスターデコ',
 'S-BLAST92',
 'S-BLAST91',
 'ロングブラスターカスタム',
 'ダイナモローラー',
 'ダイナモローラーテスラ',
 'スプラローラー',
 'スプラローラーコラボ',
 'オーダーローラー レプリカ',
 'ヴァリアブルローラー',
 'ヴァリアブルローラーフォイル',
 'カーボンローラー',
 'カーボンローラーデコ',
 'ワイドローラー',
 'ワイドローラーコラボ',
 'パブロ',
 'パブロ・ヒュー',
 'ホクサイ',
 'ホクサイ・ヒュー',
 'オーダーブラシ レプリカ',
 'フィンセント',
 'フィンセント・ヒュー',
 'リッター4K',
 'リッター4Kカスタム',
 '4Kスコープカスタム',
 'スプラチャージャー',
 'スプラチャージャーコラボ',
 'オーダーチャージャー レプリカ',
 '14式竹筒銃・甲',
 'スクイックリンα',
 'スクイックリンβ',
 'ソイチューバー',
 'ソイチューバーカスタム',
 'スプラスコープ',
 'スプラスコープコラボ',
 '4Kスコープ',
 'R-PEN/5H',
 'R-PEN/5B',
 '14式竹筒銃・乙',
 'スクリュースロッシャー',
 'スクリュースロッシャーネオ',
 'エクスプロッシャー',
 'エクスプロッシャーカスタム',
 'オーバーフロッシャー',
 'オーバーフロッシャーデコ',
 'バケットスロッシャー',
 'バケットスロッシャーデコ',
 'オーダースロッシャー レプリカ',
 'ヒッセン',
 'ヒッセン・ヒュー',
 'モップリン',
 'モップリンD',
 'ハイドラント',
 'クーゲルシュライバー',
 'クーゲルシュライバー・ヒュー',
 'スプラスピナー',
 'スプラスピナーコラボ',
 'ノーチラス47',
 'ノーチラス79',
 'バレルスピナー',
 'バレルスピナーデコ',
 'オーダースピナー レプリカ',
 'イグザミナー',
 'イグザミナー・ヒュー',
 'ハイドラントカスタム',
 'ケルビン525',
 'ケルビン525デコ',
 'クアッドホッパーブラック',
 'クアッドホッパーホワイト',
 'スパッタリー',
 'スパッタリー・ヒュー',
 'スプラマニューバー',
 'スプラマニューバーコラボ',
 'オーダーマニューバー レプリカ',
 'デュアルスイーパー',
 'デュアルスイーパーカスタム',
 'ガエンFF',
 'ガエンFFカスタム',
 'スパイガジェット',
 'スパイガジェットソレーラ',
 'キャンピングシェルター',
 'キャンピングシェルターソレーラ',
 'パラシェルター',
 'パラシェルターソレーラ',
 'オーダーパラシェルター レプリカ',
 '24式張替傘・甲',
 '24式張替傘・乙',
 'トライストリンガー',
 'トライストリンガーコラボ',
 'オーダーストリンガー レプリカ',
 'LACT-450',
 'LACT-450デコ',
 'フルイドV',
 'フルイドVカスタム',
 'ドライブワイパー',
 'ドライブワイパーデコ',
 'ジムワイパー',
 'ジムワイパー・ヒュー',
 'オーダーワイパー レプリカ',
 'デンタルワイパーミント',
 'デンタルワイパースミ',
 'ヒッセン',
 'ヒッセン・ヒュー',
 'モップリン',
 'モップリンD',
 'ハイドラント',
 'クーゲルシュライバー',
 'クーゲルシュライバー・ヒュー',
 'スプラスピナー',
 'スプラスピナーコラボ',
 'ノーチラス47',
 'ノーチラス79',
 'バレルスピナー',
 'バレルスピナーデコ',
 'オーダースピナー レプリカ',
 'イグザミナー',
 'イグザミナー・ヒュー',
 'ハイドラントカスタム',
 'ケルビン525',
 'ケルビン525デコ',
 'クアッドホッパーブラック',
 'クアッドホッパーホワイト',
 'スパッタリー',
 'スパッタリー・ヒュー',
 'スプラマニューバー',
 'スプラマニューバーコラボ',
 'オーダーマニューバー レプリカ',
 'デュアルスイーパー',
 'デュアルスイーパーカスタム',
 'ガエンFF',
 'ガエンFFカスタム',
 'スパイガジェット',
 'スパイガジェットソレーラ',
 'キャンピングシェルター',
 'キャンピングシェルターソレーラ',
 'パラシェルター',
 'パラシェルターソレーラ',
 'オーダーパラシェルター レプリカ',
 '24式張替傘・甲',
 '24式張替傘・乙',
 'トライストリンガー',
 'トライストリンガーコラボ',
 'オーダーストリンガー レプリカ',
 'LACT-450',
 'LACT-450デコ',
 'フルイドV',
 'フルイドVカスタム',
 'ドライブワイパー',
 'ドライブワイパーデコ',
 'ジムワイパー',
 'ジムワイパー・ヒュー',
 'オーダーワイパー レプリカ',
 'デンタルワイパーミント',
 'デンタルワイパースミ',
]



def bukiRandom(id):
    # ファイルパス
    cache_file = f"w_cache_{id}.pkl"

    # wの初期化
    def initialize_w():
        return [1] * len(buki_all)
    
    # wの読み込み
    def load_w():
        try:
            with open(cache_file, "rb") as file:
                return pickle.load(file)
        except FileNotFoundError:
            return initialize_w()

    # wの保存
    def save_w(w):
        with open(cache_file, "wb") as file:
            pickle.dump(w, file)


    w = load_w()  # wの読み込み

    buki = random.choices(buki_all, k=1, weights=w)
    buki = ' '.join(buki)
    buki_num = buki_all.index(buki)
    #print(w)
    #print(buki)
    #print(buki_num)

    w[buki_num] = w[buki_num] / 2

    save_w(w)  # wの保存
    
    return buki

if __name__ == "__main__": 
    print(f"||『{bukiRandom(id)}』||を使うでし！")
    #print(len(buki_name))
