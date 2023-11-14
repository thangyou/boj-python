# padding 과 소수점 아래 2자리만 출력
number = 3.141592653589793
print('%08.2f' % (number))
print('{:08.2f}'.format(number))
print(f'{number:08.2f}')
# 00003.14

# padding 과 Integer
number = 12
print('%04d' % (number))
print('{:04d}'.format(number))
print(f'{number:04d}')
# 0012

# 양수에 + 함께 출력
number = 12
print('%+04d' % (number))
print('{:+04d}'.format(number))
print(f'{number:+04d}')
# +012
