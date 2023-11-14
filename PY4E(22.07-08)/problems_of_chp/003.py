# Chp3. 연습문제 002
h = input('Enter Hours: ')
r = input('Enter Rate: ')
try:
    hval = float(h)
    rval = float(r)
except:
    print('Error, please enter numeric input')
    quit()

if hval > 40 :
    print('Pay: ', (hval*rval)+((hval-40.0)*(rval*0.5)))
else :
    print('Pay: ', hval*rval)
