import random
print("hey sen,san vericeğim kelimelerden bazılarının türkçesini merak ediyorsan evet yaz yada istemiyorsan hayı lol,rolf,sheesh,cheepy,aggro")
a = input()
list = ["lol =  komik bir şeye verilen cevap","rolf =  komik bir şakaya verilen cevap","rolf = bir şakaya karşılık cevap","sheesh = onaylamamak"," cheepy = korkunç","aggro = agresifleşmek/sinirlenmek"]
if a == "evet":
    print(random.choice(list))
