#İnput olarak verilmiş olaran string bir verinin swap_case fonksiyonu tanımlanarak büyük harflerinin küçük harfe, 
#küçük harflerinin ise büyük harfe dönüştürülmesi istenmektedir.

def change(c):
    if str.islower(c):
        return str.upper(c)
    else:
        return str.lower(c)



def swap_case(s):
    return "".join(map(change,s))

if __name__ == '__main__':