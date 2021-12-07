#[]Python, temel veriler için yerleşik dize doğrulama yöntemlerine sahiptir. 
#Bir dizenin alfabetik karakterlerden, alfanümerik karakterlerden, rakamlardan vb. oluşup oluşmadığını kontrol edebilir.
#str.isalnum() Bu yöntem bir dizenin tüm karakterlerinin alfasayısal olup olmadığını kontrol eder.(a-z, A-Z veya 0-9)
#str.isalpha() Bu yöntem bir dizenin tüm karakterlerinin alfabetik olup olmadığını kontrol eder.
#str.isdigit() Bu yöntem bir dizenin tüm karakterlerinin rakam olup olmadığını kontrol eder.
#str.islower() Bu yöntem, bir dizenin tüm karakterlerinin küçük harfli olup olmadığını kontrol eder.
#str.isupper() Bu yöntem, bir dizenin tüm karakterlerinin büyük harfli olup olmadığını kontrol eder.
#Task(Görev): Size verilen bir stringin Size bir S dizisi verilir. Göreviniz, S dizisinin şunları içerip içermediğini bulmaktır: 
#alfasayısal karakterler, alfabetik karakterler, rakamlar, küçük ve büyük harfler.
#Bu problemde input olarak verilmiş olan string bir karakterin içerisinde alfasayısal, alfabetik, rakamlar, küçük ve büyük harf var mı onlar kontrol edilmiştir.

if __name__ == '__main__':
    s = input()
    print(any([i.isalnum() for i in s]))
    print(any([i.isalpha() for i in s]))
    print(any([i.isdigit() for i in s]))
    print(any([i.islower() for i in s]))
    print(any([i.isupper() for i in s]))
    
    
