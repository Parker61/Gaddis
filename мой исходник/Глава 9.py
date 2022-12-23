

##################### 10 v2
def main():
    inf=open(r'c:\Users\Павел\Desktop\Kennedy.txt')
    list_gen=inf.readlines()
    inf.close()
    for i in  range(len((list_gen))):
        list_gen[i]=list_gen[i].rstrip('\n')

    dct=get_dct(list_gen)
    print('dct: ',dct)
    get_ind(dct)

    ############   сортировка  ########
    dct_list = sorted(dct)  # передаём в список ключи отсортированные из словаря
    for k in dct_list:
        print(k, ':', dct[k])  # поочерёдный перебор отсортированных ключей и соответствующих им значений из словаря


def get_dct(list_gen):
    count=0 #номер строки, первая строка 0+1,каждая новая строка на 1 больше
    dct={}
    for i in list_gen: #обойти список построчно
        #print('i:',i)     #строка
        words=i.split(' ')  # Разбить строку на слова и передать её в список
        #print('words:',words)  #строка в этом списке разбитая по словам
        for j in words: #перебрать все слова из этого списка
            #print('j:',j)
            if j in dct:
                dct[j].add(count+1) # если есть слово в этой строке добавить номер строки (0+1)
            else:
                dct[j]=set([count+1]) # если слова нет в этой строке записать поверх множество значением в виде списка,передать списком новую строку в множество для того чтобы дописывать новые строки по мере обхода
        count+=1
    return dct

def get_ind(dct): # не вижу смысла т.к. здесь на сортируется
    #for k in dct: #перебрать ключи
        #print(k,': ', end='')
        #for val in dct[k]:
            #print(val,'',end='') #перебрать значения к этому ключу
        #print()
    outf = open(r'c:\Users\Павел\Desktop\index.txt', 'w')
    for k in dct:
        outf.write(k+': ')
        for val in dct[k]:
            outf.write(str(val)+' ')
        outf.write('\n')
    outf.close()
    #return dct
main()

#################################### 10 v1
def main():
    inf = open(r'c:\Users\Павел\Desktop\Kennedy.txt', 'r')
    tex = inf.readlines() #считать в список tex

    s=setf(tex) # создать общее множество всех уникальных слов
    list_gen=list_genf(tex)  # создать общий список list_gen
    dct=dctf(list_gen,s)  # создать словарь где ключ-уникальное слово i, значения - список в котором указаны номера строк где есть это слово
    print('# dct # : ',dct)

    #print(sorted(dct))
    dct_list=sorted(dct) #передаём в список ключи отсортированные из словаря
    for k in dct_list:
        print(k,':',dct[k]) #поочерёдный перебор отсортированных ключей и соответствующих им значений из словаря


def dctf(list_gen,s): # создать словарь где ключ-уникальное слово i, значения - список в котором указаны номера строк где есть это слово
    dct = {}
    for i in s:
        li_i = []
        for j in range(len(list_gen)): #обойти каждую строку одним уникальным словом i из множества S
            if i in list_gen[j]:
                li_i.append(j+1)# если совпадение к номеру строки списка начиная с 0 + 1
                dct[i]=li_i
                #print(dct)
        del li_i   #после обхода всего списка одним уникальным словом удалить список, чтобы в начале создать новый пустой список для нового обхода и так для каждого уникального слова
    return dct


def setf(tex):# создать общее множество всех уникальных слов
    s = set()
    for i in range(len(tex)):
        n = tex[i].split()  # разбить каждую строку в списке по словам
        for j in range(len(n)):
            s.add(n[j])  # записать во множество уникальные слова со всего списка
    print('s:', len(s), s)
    return s


def list_genf(tex):  # создать общий список list_gen
    list_gen = []
    for i in range(len(tex)):
        list_gen.append(tex[i].split())  # разбить список построчно и добавить каждую строку в список отдельно
    print('list_gen:', len(list_gen), list_gen)
    return list_gen

main()

####### 9 v1
import random
def main():
    deck=deckf()
    again=0
    p1 = 0
    p2=0
    c=0
    while again!=99:
        c+=1
        print('cycle:', c) # № раздачи карт
        x=iter(deck) # создаём итератор и присваиваем его переменной для игрока х
        index=(random.randint(1,len(deck))-1 )   # создаёт значение в диапозоне от 1 до 52
        for i in range(index):
            i=x.__next__()      #перебор этих значений ч/з next() и останавливаемся на последнем i
        #i=str(x.__next__())
        print('i_1:',i, 'len(deck)_1_before:',len(deck))
        if deck[i]==11 and p1>10:
            deck[i]=1
            print('!!!!!!!val1: ',deck[i])
        p1+=deck[i]
        del deck[i]
        print('p1: ',p1,'len(deck)_1_after:',len(deck))

        y = iter(deck) # создаём итератор и присваиваем его переменной для игрока y
        index = (random.randint(1, len(deck))-1 ) # создаёт значение в диапозоне от 1 до 51 на одну карту меньше т.к. до этого выше удалили один ключ для Х игрока
        for i in range(index):
            i = y.__next__()
        cur = str(i)
        print('i_2: ',i,'len(deck)_2_before:',len(deck))
        if deck[cur]==11 and p2>10:
            deck[cur]=1
            print('!!!!!!!val2: ',deck[cur])
        p2 += deck[cur]
        del deck[cur]
        print('p2: ',p2,'len(deck)_2_after:',len(deck))

        if p1>21 and p2<=21:
            print('p2-win')
            again = 99
        elif p2>21 and p1<=21:
            print('p1-win')
            again = 99
        elif p2>21 and p1>21:
            print('p1,p2-game over')
            again=99
        else:
            again = 0
def deckf():
    deck = {'Туз пик':11, '2 пик':2, '3 пик':3,
            '4 пик':4, '5 пик':5, '6 пик':6,
            '7 пик':7, '8 пик':8, '9 пик':9,
            '10 пик':10, 'Валет пик':10,
            'Дама пик':10, 'Король пик': 10,

            'Туз червей':11, '2 червей':2, '3 червей':3,
            '4 червей':4, '5 червей':5, '6 червей':6,
            '7 червей':7, '8 червей':8, '9 червей':9,
            '10 червей':10, 'Валет червей':10,
            'Дама червей':10, 'Король червей': 10,

            'Туз треф':11, '2 треф':2, '3 треф':3,
            '4 треф':4, '5 треф':5, '6 треф':6,
            '7 треф':7, '8 треф':8, '9 треф':9,
            '10 треф':10, 'Валет треф':10,
            'Дама треф':10, 'Король треф': 10,

            'Туз бубей':11, '2 бубей':2, '3 бубей':3,
            '4 бубей':4, '5 бубей':5, '6 бубей':6,
            '7 бубей':7, '8 бубей':8, '9 бубей':9,
            '10 бубей':10, 'Валет бубей':10,
            'Дама бубей':10, 'Король бубей': 10}
    return deck
main()

############################# 9 v2
import random
MAX=21
def main():
    deck=creat_deck()
    p1 = 0
    p2=0

    while p1<=MAX or p2<=MAX:
        card1,val1=deck.popitem() # берём пару карта и значение
        p1=update_deck(p1,card1,val1)

        card2,val2=deck.popitem()
        p2=update_deck(p2,card2,val2)
        print(card1,card2)

        if p1>MAX and p2>MAX:
            print("Победителя нет.")
        if p1>21:
            print('p2 - win')
        else:
            print('p1-win')

def update_deck(p,card,val):
    if not card.startswith('туз'): #если карта  не начинается с туза
        return p+val
    elif p>10: #либо начинается с туза и >10 по умолчанию туз=1
        return p+val
    else:
        return p+11
def creat_deck():  #создать колоду
    #list_must = ['пик', 'червей', 'крестей', 'бубей']
    #dct_spec = {'туз': 1, 'король': 10, 'дама': 10, 'валет': 10}
    #cards=['туз', 'король', 'дама', 'валет']
    #for i in range(1,11):
        #cards.append(str(i))#добавить к тузам коро дамам цифры
   # deck={}
    #for piki in list_must:
        #for card in cards:
            #if card.isnumeric():       #если цифра # Значения 2-10.
                #deck[card+' '+piki]=int[card]
            #else:
                #deck[card+' '+piki]=dct_spec[card]   # Туз, король, дама или валет.

    suits = ['пик','червей','крестей','бубей']
    special_values = {'туз':1, 'король':10, 'дама':10, 'валет':10}

    # Создать список всех достоинств карт
    numbers = ['туз', 'король', 'дама', 'валет']
    for i in range(2,11):
        numbers.append(str(i))

    # Инициализировать колоду
    deck = {}
    for suit in suits:
        for num in numbers:
            # Значения 2-10.
            if num.isnumeric():
                deck[num + ' ' + suit] = int(num)
            # Туз, король, дама или валет.
            else:
                deck[num + ' ' + suit] = special_values[num]
    return deck
main()

####################### 8 v2
import pickle
LOOK = 1# Глобальные константы для элементов меню
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5
FILE=r'dct.dat'# Глобальная константа с именем файла
def main():
    dct=mail()
    ch=0# Инициализировать переменную для выбора пользователя.
    while ch!= QUIT:
        #print(dct)
        ch=get_user()#выбор значения ch
        if ch==LOOK:
            look(dct)
        elif ch==ADD:
            add(dct)
        elif ch==CHANGE:
            change(dct)
        elif ch == DELETE:
            delete(dct)
        print(dct)
        #print(dct)
        save(dct) # Законсервировать результирующий словарь.

def save(dct):
    inf=open('dct.dat','wb')
    pickle.dump(dct,inf)
    inf.close()

def look(dct):
    name=input('key name: ')
    if name in dct:
        print(dct[name])
    else:
        print('key incorrect')

def change(dct):
    name=input('enter name(key) to change mail: ')
    if name in dct:# Изменить адрес, если имя существует.
        adress = input('adress: ')
        dct[name]= adress

def delete(dct):
    name=input('name for delete: ')
    if name in dct:
        del dct[name]
    else:
        print('this name is not')

def add(dct):
    name = input('add name: ')
    if name not in dct:# Добавить новый адрес, если имя не существует.
        mail = input('enter mail: ')
        dct[name]=mail
    else:
        print('there is name in dct')

def mail():
    try:
        inf=open(FILE,'rb') # Расконсервировать словарь.
        dct=pickle.load(inf)
        inf.close()
        print(dct)
    except IOError:
        dct={}
    return dct

def get_user():
    ch = int(input('enter choice: '))
    while ch<LOOK or ch >QUIT:
        ch=int(input('enter correct : '))
    return ch
main()


####################### 8 v1
def main():
    import pickle
    inff=open('dct.dat','rb')
    dct=pickle.load(inff)
    print(dct)
    #dct={'kov':'@mail','par':'@gmai','kpas':'yand'}

    again = int(input('enter - 0-mail, 1-изм почту, 2-del  :'))
    while again==0 or again==1 or again==2:

        if again==0:
         y=input('Which show mail:')
         print('mail:',dct[y])

        if again==1:
            z=input('new name: ')
            w=input('mail: ')
            dct[z]=w

        if again==2:
            w=input('enter key for del: ')
            dct.pop(w,'no')
        again=input('again? ')

    #print(dct)
    inf=open('dct.dat','wb')
    pickle.dump(dct,inf)
    inf.close()

####### 7 v1
def main():
    inf = open(r'c:\Users\Павел\Desktop\WorldSeriesWinners.txt', 'r')
    tex = inf.readlines()  # # Прочитать все строки из файла в список
    for i in range(len(tex)):
        tex[i] = tex[i].rstrip('\n')  # убрать \n
    # print('tex' ,tex)
    # print('tex[0]: ' ,tex[0])

    dct1 = {}  # ключи-команды, значения-кол-во побед
    for i in tex:  # заносим в словарь ключи команды и значения 0
        dct1[i] = 0
    # print(dct1)

    for i in dct1:  # ОБХОДИМ список каждым значением из словаря при повторении +1
        for j in range(len(tex)):
            if i in tex[j]:
                dct1[i] += 1
            # else:
            # dct1[i]=1
    # print(dct1) #ключи-команды, значения-кол-во побед
    # print('tex: ',len(tex))
    dct2 = {}  # ключи-годы, значения-команды

    for i in range(len(tex)):  # запись в словарь ключей по годам, кроме 1904 и 1994
        year = 1903 + i
        if year >= 1904:  # запись к ключу соотв значения из списка tex
            year += 1

        if year >= 1994:
            year += 1

        dct2[year] = tex[i]  # значение соотв команды из списка tex

    x = int(input('введите год: '))
    # print('dct2',dct2) #ключи-годы, значения-команды
    if x == 1904 or x == 1994:
        print('no game this year')
    else:
        print('this year team won:', dct2[x], 'its team win', dct1[dct2[x]], 'try')
        print(' #ключи-команды, значения-кол-во побед: ', dct1, '\n', '#ключи-годы, значения-команды: ', dct2)
main()

######### 7 v2
def main():
    dct_y={} # ключи-годы, значения-команды
    dct_count={} # ключи-команды, значения-кол-во побед
    inf =open(r'c:\Users\Павел\Desktop\WorldSeriesWinners.txt' ,'r')
    win =inf.readlines()  # # Прочитать все строки из файла в список

    for i in range(len(win)):
        team=win[i].rstrip('\n') # удалить переход но новую строку запись по одной команде team из списка win

        year=1903+i
        if year>=1904: # если 1904 или 1994 год которого нету то перескакиваем на следующий
            year+=1
        if year>=1994:
            year+=1
        #dct_y[str(year)]=team  #занести в словарь ключ-год и значение-команду team
        dct_y[year] = team # ключи-годы, значения-команды

        if team in dct_count: #и сразу добавляем в словарь ключ-команду и знач-кол-во раз побед
            dct_count[team]+=1
        else:
            dct_count[team]=1 #добавить по разу, если повтор команды то +1

    print('dct_y: ',dct_y, '\n','dct_count: ',dct_count)

    x = int(input('введите год: '))
    #x = input('введите год: ') # в случае если в dct_y[str(year)]=team писать str
    # print('dct2',dct2) #ключи-годы, значения-команды
    if x == 1904 or x == 1994:
        print('no game this year')
    else:
        print('this year team won:', dct_y[x], 'its team win', dct_count[dct_y[x]], 'try')
        print(' #ключи-команды, значения-кол-во побед: ', dct_count, '\n', '#ключи-годы, значения-команды: ', dct_y)
main()

########  6
def main():
    inf = open(r'c:\Users\Павел\Desktop\t.txt', 'r')
    t1 = inf.read()
    inf = open(r'c:\Users\Павел\Desktop\tt.txt', 'r')
    t2 = inf.read()
    l1 = t1.split()
    l2 = t2.split()
    s1 = set(l1)
    s2 = set(l2)
    print(s1, '\n', s2)

    su = s1 | s2
    print('su: ', end='')
    for i in su:
        print(i, end=' ')
    print()

    print(s1 & s2)
    print(s1 - s2)
    print(s2 - s1)
    print(s1 ^ s2)


main()

#############  5 v1
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

########### 5 v2
def main():
    inf = open(r'c:\Users\Павел\Desktop\t.txt', 'r')
    tex = inf.read()
    li = tex.split()
    print(li)
    s = set(li)
    dct = {}
    for i in s:  # Добавить каждое уникальное слово в словарь со счетчиком 0
        dct[i] = 0
    print('dct', dct)

    for i in li:  # обходим список и добавляем +1 в словарь если повтор слова
        dct[i] += 1
    print('dct', dct)

    #for k,v in dct.items(): # вывод всех значений словаря
        #print("k,v: ",k,v)
    while len(dct)>0: # вывод вместо for///
        x=dct.popitem()
        print(format(x[0],'10'),format(x[1],'20'))
main()


############## 4
def main():
    inf=open(r'c:\Users\Павел\Desktop\text.txt','r')
    text=inf.read()
    li=text.split() #создать список со словами
    print(li)
    s=set(li) # перенести в множество и сделать слова уникальными
    print(s)
    for i in s:
        print(i)
main()

######## 3 v1
def main():
    codes = {'A': '%', 'V': '9', ' ': '@'}
    x = open(r'c:\Users\Павел\Desktop\t.txt', 'r')
    t = x.read()
    text = []
    for i in range(len(t)):  # перевести строку в список
        print(t[i], end='')

        text.append(t[i])
    print()

    cryp = []
    y = open(r'c:\Users\Павел\Desktop\tcr.txt', 'w')
    for i in range(len(text)):  # перекодировать в соотв со словарём codes
        cryp.append(codes[text[i]])  # добавить кодировку в список
        y.write(str(cryp[i]))  # записать кодировку в файл tcr.txt
    y.close()

    z = open(r'c:\Users\Павел\Desktop\tcr.txt', 'r')
    cr = z.read()
    print('cr: ', cr)


main()

############ 3 v2!!!!!!!!!!!
def main():
    codes = {'A': '%', 'V': '9', ' ':'@'}

    res=convert(codes)
    print(res)
    #wfile=input('write file: ')
    #file=open(r'c:\Users\Павел\Desktop\\'+wfile,'w')# tcr.txt
    file = open(r'c:\Users\Павел\Desktop\tcr.txt','w')
    file.write(res) # записать кодировку
    file.close()
    deconvert(codes) # раскодировка

def convert(codes):
    namef=input('namef:') #  t.txt
    file=open(r'c:\Users\Павел\Desktop\\' + namef,'r')
    text=file.read()
    print(text)
    result=''  #создать строковую перем для записи кодировки
    for i in text:
        if i.isspace():  # если пробел то просто добавить пробел
            result+=i
        else:
            result+=codes[i] #перекодировать в соотв с ключом в слове codes
    return result

def deconvert(codes):
    file = open(r'c:\Users\Павел\Desktop\tcr.txt','r')
    text=file.read() #прочесть закодированный текст
    detex=''
    print('text crypto: ',text) #зашифрованныей текст
    x=codes.keys() # вывод ключей
    print('x: ',x)
    for i in text:
        for j in codes.keys():
            if i.isspace(): # если пробел
                detex += i # просто запись в строковую переменнную
            elif i==codes[j]: #сравнение зашифрованного символа и значения в словаре с ним
                detex+=j #если совпадают значит добавляем в строковую переменную ключ от этого значения
    print('detex: ',detex)

main()

################# 3 v3
def main():
    codes={'A':'%','V':'9',' ':'@'}
    x=open(r'c:\Users\Павел\Desktop\t.txt','r')
    t=x.read()
    print(t)

    y = open(r'c:\Users\Павел\Desktop\tcr.txt', 'w')
    for i in t: # перебор строки и перекодировать в соотв со словарём codes
        y.write(str(codes[i]))  #записать кодировку в файл tcr.txt
    print(y)
    y.close()

    z = open(r'c:\Users\Павел\Desktop\tcr.txt', 'r')
    cr=z.read()
    print('cr: ',cr)
main()


######## 2 v1
def main():
    dct = {'rus': 'mos', 'ger': 'ber', 'usa': 'wash',
           'ang': 'lon', 'chi': 'pekin'}
    t = 0
    f = 0
    st = '0'
    while st == '0':
        counry, capital = dct.popitem()   # перебор идёт с конца словаря по порядку
        print(counry)
        us = input("enter capital: ")

        if capital == us:
            t += 1
        else:
            f += 1
        st = input('0-continue or next any num: ')
    print('right ', t, '\n', 'WRONG ', f, sep='')


main()

####### 2 v2
def main():
    import random
    dct = {'rus': 'mos', 'ger': 'ber', 'usa': 'wash',
           'ang': 'lon', 'chi': 'pekin'}
    again = True
    wrong = 0
    correct = 0

    while again:
        str_state = iter(dct)  # создаём итератор и присваиваем его переменной str_state
        index = (random.randint(1, 5) - 1)  # Получить индекс - произвольное название страны, но т.к. индекс начинается с "0" то нужно отнять "1"
        for i in range(index - 1):
            #i = str_state.__next__()  # i необязательно
            str_state.__next__() # перебрать с помощью next()

        cur = str(str_state.__next__())

        user = input('capital ' + cur + ': '+'(or exit num  "0":) ' )  # Получить решение пользователя.

        if user == '0':
            print('correct', correct, 'wrong', wrong)
            again = False
        elif user == dct[cur]:
            correct += 1
        else:
            wrong += 1


main()

##### # 1
def main():
    rooms = {'CS101':3004, 'CS102':4501, 'CS103':6755,
             'NT110':1244, 'CM241':1411}
    instructors = {'CS101':'Хайнс', 'CS102':'Альварадо',
                   'CS103':'Рич', 'NT110':'Берк',
                   'CM241':'Ли'}
    times = {'CS101':'8:00', 'CS102':'9:00',
             'CS103':'10:00', 'NT110':'11:00',
             'CM241':'12:00'}
    w=input("enter: ")
    if w not in rooms:
        print('none')
    else:        
        print(rooms[w],instructors[w],times[w])
main()
