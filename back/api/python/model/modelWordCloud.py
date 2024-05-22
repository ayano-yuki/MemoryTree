import matplotlib
matplotlib.use('Agg')

from janome.analyzer import Analyzer
from janome.tokenfilter import POSKeepFilter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

def analyze(src):
    token_filters = [POSKeepFilter(['名詞'])]
    an = Analyzer(token_filters=token_filters)
    toks = an.analyze(src)
    text = ' '.join([tok.surface for tok in toks])
    return text

def get_wordcrowd_mask( text, imgpath ):
    img_color = np.array(Image.open( imgpath ))
    wc = WordCloud(
        background_color="white",
        width=800,
        height=600,
        font_path = "C:\Windows\Fonts\meiryob.ttc",
        mask=img_color,
        collocations=False,
        min_font_size=15,
        ).generate( text )

    plt.figure(figsize=(80,60))
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.savefig("WC.png", transparent=True)

def create_wordcrowd(src):
    data = analyze(src)
    get_wordcrowd_mask(data, "tree.png")

"""
- [Pythonによるワードクラウドの作成方法](https://analysis-navi.com/?p=2295)
- [Masked wordcloud — wordcloud 1.8.1 documentation](https://amueller.github.io/word_cloud/auto_examples/masked.html#sphx-glr-auto-examples-masked-py)
- [テキストマイニング：WordCloudで文系女子と理系女子のツイートを可視化してみた](https://www.pc-koubou.jp/magazine/2646)
- [PythonのWordCloudで「こころ」の頻出単語を可視化する【形態素解析, 自然言語処理】](https://yu-nix.com/archives/python-word-cloud/)
- [matplotlibで出力される画像のサイズを変更する](https://www.solima.net/python/archives/179)
- [Python, matplotlibで背景が透明なグラフを作成する](https://tsudango-tech.com/56/)
"""