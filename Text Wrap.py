#İnput olarak bir string s ve genişlik w veriliyor.
#Görev, verilmiş olan dizeyi w genişliğinde satırlara bölerek bir paragrafa dönüştürmek.
#Editörde verilmiş olan wrap fonksiyonunu tamamlamamız isteniyor.
#Wrap fonksiyonunun izlediği parametreler ise şu şekildedir: string string: uzun bir string, int max_width:Dönüştürülecek olan paragrafın genişliği

import textwrap

def wrap(string, max_width):
    return textwrap.fill(string, max_width)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
