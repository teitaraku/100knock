# 04. 元素記号
# "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
# という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，
# それ以外の単語は先頭に2文字を取り出し，取り出した文字列から単語の位置
# （先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ．

sentense = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
initial = [1, 5, 6, 7, 8, 9, 15, 16, 19]
element_dict = {}
for i, e in enumerate(sentense.split()):
    element = e.strip(',.')[0:1] if i+1 in initial else e.strip(',.')[0:2]
    element_dict.update({element: i+1})
print(element_dict)
