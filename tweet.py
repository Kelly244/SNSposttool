import tweepy
import requests
import random

# Twitter API設定
API_KEY = 
API_SECRET_KEY = 
ACCESS_TOKEN_SECRET = 
AFFILIATE_ID = 

# Tweepyを使用して認証
client = tweepy.Client(consumer_key=API_KEY, consumer_secret=API_SECRET_KEY, access_token=ACCESS_TOKEN, access_token_secret=ACCESS_TOKEN_SECRET)

# 楽天のジャンルIDと対応するジャンル名の辞書
genres = {
    100371: "レディースファッション",
    551177: "メンズファッション",
    100433: "インナー・下着・ナイトウェア",
    216131: "バッグ・小物・ブランド雑貨",
    558885: "靴",
    558929: "腕時計",
    216129: "ジュエリー・アクセサリー",
    100533: "キッズ・ベビー・マタニティ",
    566382: "おもちゃ",
    101070: "スポーツ・アウトドア",
    562637: "家電",
    211742: "TV・オーディオ・カメラ",
    100026: "パソコン・周辺機器",
    564500: "スマートフォン・タブレット",
    565004: "光回線・モバイル通信",
    100227: "食品",
    551167: "スイーツ・お菓子",
    100316: "水・ソフトドリンク",
    510915: "ビール・洋酒",
    510901: "日本酒・焼酎",
    100804: "インテリア・寝具・収納",
    215783: "日用品雑貨・文房具・手芸",
    558944: "キッチン用品・食器・調理器具",
    200162: "本・雑誌・コミック",
    101240: "CD・DVD",
    101205: "テレビゲーム",
    101164: "ホビー",
    112493: "楽器・音響機器",
    101114: "車・バイク",
    503190: "車用品・バイク用品",
    100939: "美容・コスメ・香水",
    100938: "ダイエット・健康",
    551169: "医薬品・コンタクト・介護",
    101213: "ペット・ペットグッズ",
    100005: "花・ガーデン・DIY",
    101438: "サービス・リフォーム",
    111427: "住宅・不動産",
    101381: "カタログギフト・チケット",
    100000: "百貨店・総合通販・ギフト"
}

def create_affiliate_link(item_url):
    # 楽天商品のアフィリエイトリンクを生成
    affiliate_url = f"https://hb.afl.rakuten.co.jp/hgc/{AFFILIATE_ID}/?pc={item_url}&m={item_url}"
    return affiliate_url

def get_random_rakuten_items(genre):
    # 楽天API設定
    RAKUTEN_APP_ID = ''  # 楽天APIキー
    SEARCH_URL = 'https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706'

    params = {
        'applicationId': RAKUTEN_APP_ID,
        'keyword': '1000円',
        'genreId': genre,  # ジャンルIDを指定
        'minPrice': 1000,
        'maxPrice': 1000,
        'hits': 30,  # 複数の商品を取得してランダムに選択するためにhitsを増やす
    }
    response = requests.get(SEARCH_URL, params=params)
    items = response.json().get('Items')

    return items

if __name__ == "__main__":
    # ジャンルをランダムに選択
    random_genre = random.choice(list(genres.keys()))

    items = get_random_rakuten_items(random_genre)
    if items:
        print("Items全体:", items)
        print("\n個別アイテム:")
        
        for item in items:
            item_name = item['Item']['itemName']
            item_url = item['Item']['itemUrl']
            affiliate_link = create_affiliate_link(item_url)
            print(f"商品名: {item_name}")
            print(f"商品URL: {item_url}")
            print(f"アフィリエイトリンク: {affiliate_link}\n")
            print(f"詳細: {item}\n")

        random_item = random.choice(items)
        item_name = random_item['Item']['itemName']
        item_url = random_item['Item']['itemUrl']
        affiliate_link = create_affiliate_link(item_url)
        tweet_text = f"{item_name}\n{affiliate_link}"
        client.create_tweet(text=tweet_text)  # 実際のツイートを投稿する場合はコメントアウトを外します
        print("ツイート内容:", tweet_text)
    else:
        print("No items found")
