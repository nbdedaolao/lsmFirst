from flask import Flask, render_template, request
import sys
import re

cem = Flask(__name__)


def readOrWriteFile(mode, *inputString):
    txtList = []
    if (mode == 'r'):
        try:
            f = open(sys.argv[1], mode, encoding='utf_8')
            temp = f.readlines()
            for i in temp:
                if (re.match(r'[a-z]+,[\u4e00-\u9fa5]+', i)):
                    txtList.append(i)
            f.close()
        except:
            print("_____________________________文件不存在!_____________________________")
        return txtList
    elif (mode == 'a'):
        try:
            f = open(sys.argv[1], 'r', encoding='utf_8')
            f.close()
            f = open(sys.argv[1], mode, encoding='utf_8')
            f.write('\n'+inputString[0])
            f.close()
        except:
            print("_____________________________添加失败!_____________________________")
    else:
        print('目前不支持该读写模式！')


def listToMap(txtList):
    return zip(map(lambda s: s.split(',')[0], txtList), map(
        lambda s: s.split(',')[1], txtList))


@cem.route('/')
def home():
    wDic = listToMap(readOrWriteFile(mode='r'))
    return render_template('cem.html', wDic=wDic)


@cem.route('/', methods=['POST'])
def add():
    if (re.match(r'[a-z]+,[\u4e00-\u9fa5]+', request.form.get('add'))):
        readOrWriteFile('a', request.form.get('add'))
    wDic = listToMap(readOrWriteFile(mode='r'))
    return render_template('cem.html', wDic=wDic)


if __name__ == "__main__":
    cem.run()
