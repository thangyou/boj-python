dict_var = {'csev' : 2, 'cwen' : 2, 'zqian' : 1}

for out,out2 in dict_var.items(): print(out)
# csev, cwen, zqian
print("------")

for out in dict_var: print(out)
# csev : 2, cwen : 2, zqian : 1
print("------")

for out in dict_var.keys(): print(out)
# csev, cwen, zqian
print("------")

for out in dict_var.values(): print(out)
# 2, 2, 1
print("------")

for out,out2 in dict_var.items(): print(out2)
# 2, 2, 1

# 딕셔너리명.items()
# 해당 딕셔너리의 key와 value의 쌍을 튜플로 묶은 값을 dict_items 객체로 돌려줌
