import json

Jplist = []#JSONを行ごとに読み取る
listrows = []#テキスト出力用

f = open('任意の.jsonファイル', 'r' ,encoding='utf-8')
jsn = json.load(f)#JSONファイルを開く

for key in jsn:#JSONファイルを読み取る
    if key['country'] == 'JP':#日本のみに絞る
        for value in key:#日本の内容を行ごとに読み取る
            Jplist.append(str(value) + ':' + str(key[value]))#行毎に読み取る
        listrows.extend(Jlist)#リストを二次元配列として追記

with open("任意の.txtファイル", 'w', encoding='utf-8') as tx:
    for values in listrows:#行ごとにテキスト出力する
        tx.write(str(values) + '\n')#テキストファイルに書き込む
print('完了')