import random
import pickle
import sys

if len(sys.argv) < 2:
    id = "0"
else :
    id = str(sys.argv[1])


buki_all = ['わかばシューター',
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
