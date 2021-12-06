#Bir öğrenci listesi isin öğrenci isimleri ve öğrenci notlarını içeren bir dictionary kalıbı input olarak okunacaktır.  
# [Marks] Belirtilen öğrenci adı için notlar dizisinin ortalamasını ondalıktan sonra 2 basamak göstererek yazdırın.(Float)
#Input:İlk satır, öğrenci kayıtlarının sayısı olan n tamsayısını içerir. Sonraki n satır, bir öğrenci tarafından elde edilen adları 
#ve işaretleri içerir, her değer bir boşlukla ayrılır. Son satırda sorgulanacak öğrencinin adı olan quert_name bulunur.
#Constrains(Sınırlamalar): Öğrenci sayısı n: 2<=n<=10, Notlar(marks): 0<=mark<=100, Notlar dizi uzunluğu(Lenght array marks):3
#Output:Çıkış çıtısı tek satır olacaktır. Belirli bir öğrencinin not ortalamasınının float(ondalıklı) olarak çıktısını verecektir.

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    student = 0
    for i in student_marks[query_name]:
        student=student+i
    print("{0:.2f}".format(student/3))