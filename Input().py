#HackerRank Python(Basic) İnput() Solution
#Python 2'de input() ifadesinin eşdeğerinin eval(raw_input(prompt)) olduğu problemin başında bize belirtilmiş.
#Görev: Tek değişkenli (x) polinomu verilmiştir. Aynı zamanda k ve x değerleri de verilmiştir. 
#P(x) = k denkliğini kontrol ediniz. 
#Kısıtlamalar: Polinom P'nin üm katsayıları tam sayılardır. 
#Input Format: Girişteki ilk satır x ve k'nın değerlerini boşlukla ayrılmış şekilde içerir. İkinci satır ise Polinom P'yi içerir. 
#Çözümü Python 3 kullanarak yapıyoruz. 

xk = list(map(int, input().split()))
x = xk[0]
k = xk[1]
P = input()
if eval(P) == k:
    print("True")
else:
    print("False")
