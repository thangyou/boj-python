# dictionary
fname = input('Enter file:')
if len(fname) < 1: fname = 'clown.txt'
hand = open(fname)

di = dict() # {}
for lin in hand:
    lin = lin.rstrip()
    wds = lin.split()
    for w in wds:
        di[w] = di.get(w,0) + 1

largest = -1
theword = None
for k,v in di.items():
    print(k,v)
    if v > largest:
        largest = v
        theword = k

print('Done', theword, largest)
'''
the 7
clown 2
ran 2
after 1
car 3
and 3
into 1
tent 2
fell 1
down 1
on 1
Done the 7
'''

info = { 'Jeong' : 314, 'Jay' : 214, 'Hyuk' : 32 }
print(list(info))
print(info.keys())
print(info.values())
print(info.items())
'''
['Jeong', 'Jay', 'Hyuk']
dict_keys(['Jeong', 'Jay', 'Hyuk'])
dict_values([314, 214, 32])
dict_items([('Jeong', 314), ('Jay', 214), ('Hyuk', 32)])
'''

# name = input('Enter file:')
# handle = open(name)
handle = '''Writing programs (or programming) is a very creative and rewarding activity.
You can write programs for many reasons ranging from making your living to solving a
difficult data analysis problem to having fun to helping someone else solve a problem.
This book assumes that everyone needs to know how to program and that once you know
how to program, you will figure out what you want to do with your newfound skills.'''

counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1
        # counts 딕셔너리에 name키가 존재하면 name에 대한 값을 불러오고,
        # 그렇지 않다면 name이라는 키에 0이라는 값을 갖는 데이터를 추가

bigcount = None
bigword = None
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word # count가 가장 큰 단어
        bigcount = count # 그 단어의 빈도수

print(bigword, bigcount)

# tuple
fhand = open('romeo.txt')
counts = {}
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
# ---------------------------->dictionary 생성
lst = [] # list
for key, val in counts.items():
    newtup = (val, key)
    lst.append(newtup)

lst = sorted(lst, reverse=True)

for val, key in lst[:10]:
    print(key, val)

'''
the 3
is 3
and 3
sun 2
yonder 1
with 1
window 1
what 1
through 1
soft 1
'''

fname = input('Enter File:')
if len(fname) < 1: fname = 'intro.txt'
hand = open(fname)

di = dict()
for lin in hand:
    lin = lin.rstrip()
    wds = lin.split()
    for w in wds:
        di[w] = di.get(w,0) + 1

tmp = list()
for k,v in di.items():
    newt = (v,k)
    tmp.append(newt)

tmp = sorted(tmp, reverse=True) # 내림차순

for v,k in tmp[:5]:
    print(k,v)
'''
the 226
to 204
a 165
and 160
you 130
'''
