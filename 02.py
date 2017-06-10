# 02. 「パトカー」＋「タクシー」＝「パタトクカシーー」
# 「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ

taxi = list('タクシー')
poli = list('パトカー')
s = ''
for i in range(0, len(poli)):
    s = s + poli[i] + taxi[i]
print(s)
