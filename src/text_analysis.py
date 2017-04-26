from textblob import TextBlob
import pandas
from collections import Counter
from wordcloud import (WordCloud, get_single_color_func)
import matplotlib.pyplot as plt

p1 = pandas.read_excel('Amazon Reviews.xlsx', sheetname='Lindt')
p2 = pandas.read_excel('Amazon Reviews.xlsx', sheetname='Godiva')
p3 = pandas.read_excel('Amazon Reviews.xlsx', sheetname='Ferrero Rocher')

def analysis(prod):
    data = str()
    for r in prod.Review:
        data +=str(r)
    pnc = ['\r', '\n', '.', ')', '(', '?', '!', ',', ':', ';', "'", '"']
    for p in pnc:
        data = data.replace(p, '')


    text = TextBlob(data)
    feeling = text.sentiment.polarity
    frequencies = Counter(text.noun_phrases)
    print(frequencies)
    return frequencies, feeling


def word_cloud(frequencies):
    wordcloud = WordCloud(max_words=500, width=1200, height=700, min_font_size=12, background_color='#ccc')\
        .generate_from_frequencies(frequencies=frequencies, max_font_size=100)
    wordcloud.recolor(4500)
    wordcloud.to_file('godiva.png')
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()

if __name__  == '__main__':
    fq, sent = analysis(p2)
    if sent >0 :
        print('Positive', sent)
    word_cloud(fq)