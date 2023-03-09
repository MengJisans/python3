#!/usr/bin/python3

from wordcloud import WordCloud
import jieba
import numpy as np

import PIL.Image as Image

#1.将字符串切分

def chinese_jieba(text):

wordlist_jieba=jieba.cut(text)

space_wordlist=" ".join(wordlist_jieba)

return space_wordlist

with open("test.txt" ,encoding="utf-8")as file:

text=file.read()

text=chinese_jieba(text)

#2.图片遮罩层

mask_pic=numpy.array(Image.open("china.jpg"))

#3.将参数mask设值为：mask_pic

wordcloud = WordCloud(font_path="C:/Windows/Fonts/simfang.ttf",mask=mask_pic).generate(text)

image=wordcloud.to_image()

image.show()
