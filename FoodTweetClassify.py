#!/usr/bin/python
#coding:utf-8

"""
classiasにいれるmodel fileを作るプログラム

実行方法
python FoodTweetClassify.py --input [csv形式のfile名] --output [output filename]
"""

__author__ = "@Ace12358"
__version__ = "0.0"
__date__ = "2014/10/14"

import sys
import re
import argparse
import csv

def getArgs():
    """
    オプションを選択
    """
    parser = argparse.ArgumentParser(description="make classias model")

    parser.add_argument(
        "-i", "--input",
        dest="train_file",
        type=argparse.FileType("r"),
        required=True,
        help="input filename as train data"
    )

    parser.add_argument(
        "-o", "--output",
        dest="model_file",
        type=argparse.FileType("w"),
        default=sys.stdout,
        help="output filename as classias model"
    )

    return parser.parse_args()

def FeatureUrl(tweet):
    """
    urlの有無を返す関数
    入力: tweet
    出力: 0 or 1
    """
    re_url = re.compile("https?://[\w/:%#\$&\?\(\)~\.=\+\-]+") #URLの正規表現
    re_url_search = re_url.search(tweet)
    if re_url_search == None:
        return 0
    else:
        return 1

def FeatureMention(tweet):
    """
    Mention（@がついているか）なのかそうでないかを返す関数
    入力：tweet
    出力：0 or 1
    """
    re_account = re.compile("@[0-9a-zA-Z_]{1,15}")
    re_account_search = re_account.search(tweet)
    if re_account_search == None:
        return 0
    else:
        return 1

def FeatureBagOfWords(tweet):
    """
    入力:tweet
    出力:word_list
    """
    word_list=list()
    word_list=tweet.strip().split()    
    return word_list

def main():
    """
    main関数
    classiasのモデルを作れるような形式でfileを作成
    """
    Reader = csv.reader(args.train_file)
    for itemList in Reader:
        flag = itemList[0] #-1 or 1
        data = itemList[1] #日付
        unix_time = itemList[2] # unix_time
        latitude = itemList[3] #緯度
        longitude = itemList[4] #経度
        account_name = itemList[5] #アカウントの名前
        lang = itemList[6] #言語
        tweet = itemList[7] #tweet本文
        #素性の抽出
        f_url = FeatureUrl(tweet)
        f_mention = FeatureMention(tweet)
        f_bow_list = FeatureBagOfWords(tweet)

        args.model_file.write("# %s\n" %tweet)
        args.model_file.write("%s " %flag) 
        for f_bow in f_bow_list:
            args.model_file.write("bow=%s " %f_bow)
        args.model_file.write("url=%d " %f_url)
        args.model_file.write("mentoin=%d\n" %f_mention)

if __name__=="__main__":
    args=getArgs()
    main()
