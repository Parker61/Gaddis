import turtle
turtle.circle(100)
turtle.penup()
turtle.forward(30)
turtle.setheading(270)
turtle.forward(5)
turtle.pendown()
turtle.circle(100)

turtle.penup()
turtle.forward(30)
turtle.setheading(270)
turtle.forward(5)
turtle.pendown()
turtle.circle(100)





#15
import turtle
turtle.fillcolor('red')
turtle.begin_fill()
turtle.setheading(315)
turtle.forward(100)
turtle.setheading(45)
turtle.forward(100)
turtle.setheading(315)
turtle.forward(100)
turtle.setheading(45)
turtle.forward(100)
turtle.setheading(135)
turtle.forward(100)
turtle.setheading(225)
turtle.forward(100)
turtle.setheading(135)
turtle.forward(100)
turtle.setheading(225)
turtle.forward(100)
turtle.end_fill


#14
P=int(input("enter P(main sum): "))
r=int(input("enter r(interest rate): "))
r_=r/100
n=int(input("enter n(frequence accrual): "))
t=int(input("enter t(years): "))
A=P*(1+r_/n)**n*t

print("total sum money: ",format(A,'.2f'))

#13
R=int(input("enter R: "))
E=int(input("enter E: "))
S=int(input("enter S: "))
V=int(R-2*E)/S
print("V: ",format(V,'.1f'))

#12
ost1=2000*40-2000*40*0.03
ost2=2000*42.5-2000*42.5*0.03
print("result: ",(ost2-ost1))

#11
boy=int(input("enter boys: "))
girl=int(input("enter girls: "))
boys=(boy/(boy+girl))
girls=(girl/(boy+girl))
print("boys: ",format(boys,'.0%'),"girls: ",format(girls,'.0%'))

#10
oil=1
sugar=1.5
flour=2.5
x=int(input("enter newcookies: "))
new_norm=x/48
oil_=oil*new_norm
sugar_=sugar*new_norm
flour_=flour*new_norm
print(format(oil_,'.2f'),sugar_,flour_)



#9
celsi=int(input("type text celsi"))
farengate=int((9*celsi/5)+32)
print("temperature on farengate: ", farengate)




#8
cost_food=int(input("cost_food: "))
tips=cost_food*0.18
tax=cost_food*0.07
food=int(cost_food+tips+tax)
print(" tax", format(tax,',.0f'),
      "\n", "tips", format(tips,',.0f'),
      "\n", "foood",food)



#7
consumption=int(input("what is consumption L/100 km: "))
distance=int(input("How far have you traveld km: "))
consumption_fuel=int(distance*consumption/100)
print("you fuel consumption was: ", consumption_fuel)
price_fuel=48.5
volume_of_the_tank=40
print("number of gas station: ", consumption_fuel//volume_of_the_tank)
print("money spend: ", int(consumption_fuel*price_fuel))
                




#6
purchace=int(input("enter purchace: "))
fed=0.05
tax_fed=float(purchace*fed)
reg=0.025
tax_reg=float(purchace*reg)
sum=float(tax_fed+tax_reg+purchace)
print (" you are sum of buy: ", format(sum,',.0f'),
       "\n","tax_fed: ",format(tax_fed,',.1f'), 
       "\n","tax_reg: ",format(tax_reg,',.1f'))



#5
velocity=70 #km/h
distance_6=6*velocity
distance_10=10*velocity
distance_15=15*velocity
distance_=int(input("enter time: "))
distance=distance_*velocity
print( "",distance_6,"\n",distance_10,"\n",distance_15,"\n",distance)

#4
price1=int(input("enter goods1: "))
price2=int(input("enter goods2: "))
price3=int(input("enter goods3: "))
sum=price1+price2+price3
tax =float(0.13*sum)
print("prices on sum: ", sum)
print("taxes", tax )
print("total sum: ",tax+sum )


#3
square_m=int(input("enter you meters: "))
print("You acros: ",format(square_m/4047,',.0f'), "square acros")

#2
value=int(input("enter you sales: "))
print("You profit: ",int(value*0.23))


#1
name = 'Pavel'
adress='VD, 347383'
number='89885864419'
print("my name is:",name,"\ncity",adress,"\nnumber",number)
