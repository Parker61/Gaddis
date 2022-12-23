##########  3v2
import person
def main():
    sent = False
    name='jon'
    id='id - 999'
    number='001'
    ch=input('sent: (y/n)')

    if ch=='y':
        sent=True
    p = person.Customer(name, number, id, sent)
    if p.get_sent()==True:
        print(p.get_id())

main()

############  3 v1
import person
def main():
    per=person.Customer('Jon',111,'001')
    ch='p'  #input('choice: ')
    if ch=='p':
        #print(per.get_id(),per.get_name())
        show(per)
def show(per):
    if isinstance(per,person.Customer):
        print(per.get_id())
        print(per.get_name())
    else:
        print('no want')
main()

######  2
import shiftSupervisor
def main():

    #name=input('name: ')
    #id = input('id: ')
    #shift = input('shift: ')
    #rate = input('rate: ')
    pr = shiftSupervisor.ShiftSupervisor('names', '22', '300', '400') # Создать экземпляр класса ProductionWorker
    print(pr.get_salary())
    print(pr.get_premium())
    print(pr.get_name())
    print(pr.get_id())
    print(pr) #без строковой функции __str__

main()

#############  1
import person #вызов модуля productionWorker в котором Employer надкласс и подкласс ProductionWorker
def main():

    #name=input('name: ')
    #id = input('id: ')
    #shift = input('shift: ')
    #rate = input('rate: ')
    pr = person.ProductionWorker('names', '22', '33', '44') # Создать экземпляр класса ProductionWorker
    pro=person.Employer('zzz', '22') # для каждого класса передаёт только для атрибутов своего класса
    print(pr.get_rate()) #вывод толлько через функцию get...
    print(pr.get_shift())
    print(pr.get_name())
    print(pr.get_id())
    print('pro: ',pro) #такой вывод тоько для классов в которых аргументы родные а не переданы из надкласса

main()
