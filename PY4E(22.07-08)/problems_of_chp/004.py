# Chp4. 연습문제 001
# h = input('Enter Hours: ')
# r = input('Enter Rate: ')

h=45
r=10

def computepay(h, r):
        if hval > 40 :
            print('Pay: ', (hval*rval)+((hval-40.0)*(rval*0.5)))
        else :
            print('Pay: ', hval*rval)

try:
    hval = float(h)
    rval = float(r)
    computepay(hval, rval)
except:
    print('Error, please enter numeric input')
    quit()
