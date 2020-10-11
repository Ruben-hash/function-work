##def exercice1(a):
##    return a**2 - a + 1

#ex2
##def vitesse(d,t):
##    return d/t

#ex3
from random import randint
def exercice3():
    return randint(1,6)

#ex4
##def  prix():
##    solde = int(input())
##    prix = int(input())
##    solde = solde/100 * prix
##    return solde

#ex5 pas reussi
##def pop(annee):
##    popu = 3000
##    for loops in range(annee):
##        popu = popu - (2/100 * popu)
##    if popu <= 1500 :
##        print("dans", annee, "ans, il y aura moins de 1500 habitants")
##    return popu

#ex 6
##
##def pA(nbentrées):
##    price = nbentrées * 5.25
##    return price
##
##def pB(nbentrées):
##    price = 12 + 3.5 * nbentrées
##    return price
# c'est à partir de 7 entrées




#ex7
#•def major(age):
#    if age >= 18:
 #       print("vous etes majeur")
 #   else:
 #       print('vous etes mineur')

#ex8
def conversion1(h, m, s):
    result = h * 3600 + m *60 + 2 
    return result


def conversion2():
    con1 = int(input())
    con2 = int(input())
    return con1 - con2


def conversion3():
    con1 = int(input())
    con2 = int(input())
    return con1 - con2
    if con1 < con2:
        print(con2, con1)
    else:
        print(con1, con2)
    return result
 #ex10
def div(n):
    nub = 0
    for loops in range(1,n+1):
        nub = nub + 1
        if n%nub == 0:
            print(nub)
        else:
            print("")
  #ex9
def premier(n):
    if n==2:
        return True
    if n%2==0 or n==1:
        return False
    for i in range (3,n,2):
        if n%i ==0 :
            return False
    return True


#ex11

num = int(input(""))

# Changed num variable to string, 
# and calculated the length (number of digits)
order = len(str(num))

# initialize sum
sum = 0

# find the sum of the cube of each digit
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** order
   temp //= 10

# display the result
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")

   
