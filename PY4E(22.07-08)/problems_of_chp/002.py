# Chp3. 연습문제 001
h = input('Enter Hours: ')
r = input('Enter Rate: ')
hval = float(h)
rval = float(r)
if h > 40 :
    print('Pay: ', (hval*rval)+((hval-40.0)*(rval*0.5)))
else :
    print('Pay: ', hval*rval)
