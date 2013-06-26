c=0         # choice number
i=39.3701   # inches per meter
f=3.28084   # feet per meter
x=1         # outer while loop
r=13.29     # pesos per dollar
l=3.785417  # liters per gallon
k=1.60934   # kilometers per mile
p=2.20462   # pounds per kilogram
s='-'*70    # seperator line
def multiply(a,b):
    a=float(a)
    b=float(b)
    return round(a*b,2)
def divide(a,b):
    a=float(a) 
    b=float(b) 
    return round(a/b,2)

def temp(x,y):
    """ converts between centgrade and fahrenheit 
    x=temp to convert y='f'or'c'for desired return type"""
    x=float(x)
    if y=='c':
        return round((x-32)*5/9,1)
    elif y=='f':
        return round(x * 9/5+32,1)
    else:
        return ' pick f or c to get an answer'

while x == 1:
    w= s,'\nBad entry. Try again.\n',s
    y=1         # inner while loop
    print s,'\n',r,'Pesos per Dollar\n',s
    print "*** Main Menu ****\n1. Dollar/Peso\n2. Gallons/Liters\n3. Pounds/Kilograms"
    print "4. Inches/Feet/Meters\n5. Miles/Kilometers\n6. Temperature"
    print "7. Dollars/Gallons <=> Pesos/Liters\n8. Change Pesos per Dollar rate"
    a=raw_input("9. Exit\nSelect a number =>")
    while y==1:
        if a =='1':
            print s,'\n **** Dollar/Peso ****'
            print "1. Dollars to Pesos\n2. Pesos to Dollars"
            b=raw_input("3. Main Menu\nSelect a number =>")
            if b == '1':
                d=raw_input("enter dollars =>")
                print s,'\n ',d,' dollars = ',multiply(d,r),' pesos'
            elif b=='2':
                d=raw_input("enter pesos =>")
                print s,'\n ',d,' pesos = ',divide(d,r),' dollars'
            elif b=='3':
                y=0
            else:
                print s,'\nBad entry. Try again.'
                break
                a=raw_input("enter pesos =>")
                print s,'\n ',a,' pesos = ',divide(a,r),' dollars'
        elif a=='2':
            print s,'\n **** Gallons/Liters ****'
            print "1. Gallons to Liters\n2. Liters to Gallons"
            b=raw_input("3. Main Menu\nSelect a number =>")
            if b == '1':
                d=raw_input("enter gallons =>")
                print s,'\n ',d,' gallons = ',multiply(d,l),' liters'
            elif b=='2':
                d=raw_input("enter liters =>")
                print s,'\n ',d,' liters = ',divide(d,l),' gallons'
            elif b=='3':
                y=0
            else:
                print s,'\nBad entry. Try again.'
                break
        elif a=='3':
            print s,'\n **** Pounds/Kilograms ****'
            print "1. Pounds to Kilograms\n2. Kilograms to Pounds"
            b=raw_input("3. Main Menu\nSelect a number =>")
            if b == '1':
                d=raw_input("enter pounds =>")
                print s,'\n ',d,' pounds = ',divide(d,p),' kilograms'
            elif b=='2':
                d=raw_input("enter kilograms =>")
                print s,'\n ',d,' kilograms = ',multiply(d,p),' pounds'
            elif b=='3':
                y=0
            else:
                print 'Bad entry. Try again'
        elif a=='4':
            print s,'\n **** Inches/Feet/Meters ****'
            print "1. Inches to Meters\n2. Meters to Inches"
            print "3. Feet to Meters\n4. Meters to Feet"
            b=raw_input("5. Main Menu\nSelect a number =>")
            if b == '1':
                d=raw_input("enter inches =>")
                print s,'\n ',d,' inches = ',divide(d,i),' meters'
            elif b=='2':
                d=raw_input("enter meters =>")
                print s,'\n ',d,' meters = ',multiply(d,i),' inches'
            elif b=='3':
                d=raw_input("enter feet =>")
                print s,'\n ',d,' feet = ',divide(d,f),' meters'
            elif b=='4':
                d=raw_input("enter meters =>")
                print s,'\n ',d,' meters = ',multiply(d,f),' feet'             
         
            elif b=='5':
                y=0
            else:
                print s,'\nBad entry. Try again.'
                break
                print 'Bad entry. Try again'
        elif a=='5':
            print s,'\n **** Miles/Kilometers ****'
            print "1. Miles to Kilometers\n2. Kilometers to Miles"
            b=raw_input("3. Main Menu\nSelect a number =>")
            if b == '1':
                d=raw_input("enter miles =>")
                print s,'\n ',d,' miles = ',multiply(d,k),' kilometers'
            elif b=='2':
                d=raw_input("enter kilometers =>")
                print s,'\n ',d,' kilometers = ',divide(d,k),' miles'
            elif b=='3':
                y=0
            else:
                print s,'\nBad entry. Try again.'
                break
                print 'Bad entry. Try again'
        elif a=='6':
            print s,'\n **** Temperatue ****'
            print "1. Fahrenheit to Centigrade\n2. Centigrade to Fahrenheit"
            b=raw_input("3. Main Menu\nSelect a number =>")
            if b == '1':
                d=raw_input("enter fahrenheit =>")
                print s,'\n ',d,' fahrenheit = ',temp(d,'c'),' centigrade'
            elif b=='2':
                d=raw_input("enter centigrade =>")
                print s,'\n ',d,' centigrade = ',temp(d,'f'),' fahrenheit'
            elif b=='3':
                y=0
            else:
                print s,'\nBad entry. Try again.'
                break
        elif a=='7':
            print s,'\n * Dollars/Gallons <=> Pesos/Liters *'
            print "1.  Dollars/Gallons to Pesos/Liters"
            print "2.  Pesos/Liters to Dollars/Gallons "
            b=raw_input("3. Main Menu\nSelect a number =>")
            if b == '1':
                d=raw_input("enter dollars per gallon =>")
                e=float(d)*r/3.75                
                print s,"\n",d,"dollars per gallon = ",round(e,2),"pesos per liter"
            elif b=='2':
                d=raw_input("enter pesos per liter =>")
                e=float(d)*3.75/r
                print  s,"\n",d,"pesos per liter = ",round(e,2),"dollars per gallon" 
            elif b=='3':
                y=0
            else:
                print s,'\nBad entry. Try again.'
                break
        elif a=='8':
            d = raw_input('enter new rate => ')
            r = d
            break
        elif a=='9':
            x=0
            y=0
            print 'program ended'
        else:
            print s,'\nBad entry. Try again.'