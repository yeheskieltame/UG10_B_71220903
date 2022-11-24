print("~~selamat datang di program pengurutan bilangan~~")
print ("Tentukan Pilihan Anda!! [1/2]")
print ("1. Ascending")
print ("2. Descending")
pilihan= int(input("masukkan pilihan yang anda inginkan:"))
a = int(input("masukkan bilangan pertama:"))
b = int(input("masukkan bilanganh kedua:"))
c = int(input("masukkan bilangan ketiga:"))
d = int(input("masukkan bilangan keempat:"))
if pilihan == 1:
    if a<b<c<d:
        print(a,b,c,b)
    else:
        print(d,a,b,c)
else :
    print(c,b,a,d)
