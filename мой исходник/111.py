def main():
    inf=open(r'c:\Users\Павел\Desktop\t.txt','r')
    tex=inf.read()
    print(tex)
    li=tex.split()
    print(li)
    s=set(li)
    print('s:',s)
    dct={}
    for i in s:  # Добавить каждое уникальное слово в словарь со счетчиком 0
        dct[i] = 0
    print('dct', dct)

    for i in li:
        if  i  in li:# перебор-опрос отдельно каждого слова по всему списку
            dct[i]+=1

    print(sorted(dct.items()))
    for k,v in sorted(dct.items()):
        print(k,v)
main()