ID = input('请输入十八位身份证号码: ')
if len(ID) == 18:
  print("你的身份证号码是 "+ID)
else:
  print("错误的身份证号码")

#解析身份证号是否符合国家校验标准
ID_check=ID[17]
C=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
ID_num=[18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2]
ID_CHECK=['1','0','X','9','8','7','6','5','4','3','2']
ID_sum=0
for i in range(len(C)):
  ID_sum=ID_sum+int(ID[i])*C[i]
ID_Check=ID_sum%11
if ID_check!=ID_CHECK[ID_Check]:
  print('错误的身份证号码')
  sys.exit(0)
else:
  print('正确的身份证号码')

#解析出生日期和性别       
ID_add = ID[0:6]
ID_birth = ID[6:14]
ID_sex = ID[14:17]
ID_check = ID[17]
year = ID_birth[0:4]
month = ID_birth[4:6]
day = ID_birth[6:8]
print("出生日期: "+year+'年'+month+'月'+day+'日')
if int(ID_sex) % 2 == 0:
    print('性别：女')
else:
    print('性别：男')

import re
dict_temp = {}
areacode = open('HW02.txt','r')
for line in areacode.readlines():
    line = line.strip()
    k = line.split('\t')[0]
    v = line.split('\t')[1]
    dict_temp[k] = v
print("出生地：", end='')
print(dict_temp[(ID)[0:6]])
print('')