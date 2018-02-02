#bulletPointAdder.py - クリップボードのテキストの各行に
#点を売って。Wikipediaの箇条書きにする

import pyperclip
# クリップボードのテキストを、１つの長い文字列として返す。
text = pyperclip.paste()

lines = text.split('\n')
for i in range(len(lines)): #"lines"リストの各要素をループする
    lines[i] = '* '+lines[i]   #"lines"の要素に"* "を追加する

text='\n'.join(lines)
# todo: 行を分割して,'*'を追加する

pyperclip.copy(text)
