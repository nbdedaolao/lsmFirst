from flask import Flask, render_template, request
import sys
import config
import re

cem = Flask(__name__)
cem.config.from_object(config)


@cem.route('/')
def home():
    word = []
    interpretation = []
    wDic = {}
    with open(sys.argv[1], 'r+', encoding='utf_8') as f:
        txtList = f.readlines()
        word = map(lambda s: s.split(',')[0], txtList)
        interpretation = map(lambda s: s.split(',')[1], txtList)
        wDic = zip(word, interpretation)
        f.close()

    print("___________________________________________________")
    return render_template('cem.html', wDic=wDic)


@cem.route('/', methods=['POST'])
def add():
    word = []
    interpretation = []
    wDic = {}
    if (re.match(r'[a-z]+,[\u4e00-\u9fa5]+', request.form.get('add'))):
        with open(sys.argv[1], 'a', encoding='utf_8') as f:
            f.write('\n'+request.form.get('add'))
            f.close()
    with open(sys.argv[1], 'r', encoding='utf_8') as f1:
        txtList = f1.readlines()
        word = map(lambda s: s.split(',')[0], txtList)
        interpretation = map(lambda s: s.split(',')[1], txtList)
        wDic = zip(word, interpretation)
        f1.close()

    print("___________________________________________________")
    return render_template('cem.html', wDic=wDic)


if __name__ == "__main__":
    cem.run()
