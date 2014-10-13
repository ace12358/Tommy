####TommyProgram

---
tommyと一緒に書いたやつ


Help on module FoodTweetClassify:

NAME
    FoodTweetClassify - classiasにいれるmodel fileを作るプログラム

FILE
    /Users/kitagawayoshiaki/Works/Tommy/FoodTweetClassify.py

DESCRIPTION
    実行方法
    python FoodTweetClassify.py --input [csv形式のfile名] --output [output filename]

FUNCTIONS
    FeatureBagOfWords(tweet)
        入力:tweet
        出力:word_list
    
    FeatureMention(tweet)
        Mention（@がついているか）なのかそうでないかを返す関数
        入力：tweet
        出力：0 or 1
    
    FeatureUrl(tweet)
        urlの有無を返す関数
        入力: tweet
        出力: 0 or 1
    
    getArgs()
        オプションを選択
    
    main()
        main関数
        classiasのモデルを作れるような形式でfileを作成

DATA
    __author__ = '@Ace12358'
    __date__ = '2014/10/14'
    __version__ = '0.0'

VERSION
    0.0

DATE
    2014/10/14

AUTHOR
    @Ace12358


