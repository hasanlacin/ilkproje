liste = [3,7,8,130,17,53,60,1,8,23,45,0]

enbuyuk = 0
for eleman in liste:
    if(eleman>enbuyuk):
        enbuyuk = eleman


print(enbuyuk)

enkucuk = 99999999

for a in liste:
    if(a<enkucuk):
        enkucuk = a
print(enkucuk)