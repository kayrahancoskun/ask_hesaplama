isim1 = (input("Kendi İsminiz: "))
isim2 = (input("kiz arkadasinizin / Erkek arkadasinizin ismi: "))

love = len(isim1) + len(isim2)

if len(isim1) > len(isim2):
    love -= 5
else:
    love += 3

love *= 42
love = love / (100 + len(isim2))

love = 10 if love > 10 else round(love, 0)

print("{} and {} score is {} out of 10".format(isim1, isim2, love))