# num1 = 10
# num2 = 20
# print("Num1 + Num2=", num1 + num2)
# print("Num1 - Num2=", num1 - num2)
# print("Num1 / Num2=", num1 / num2)
# print("Num1 * Num2=", num1 * num2)
# print('5 ^ 3=', 5 ** 3)
# print("20 % 3=", 20 % 3)
# print("3.8//2=", 3.8 // 2)
#
# # Asignement operators
# num3 = num1 + num2
# print(num3)
# num3 += num2
# print(num3)
#
# print("Ankit\'sLaptop")
# print('c:\aniket\new folder')
# print(r'c:\aniket\new folder')
# # comparision assignment
# print("Is num 3 > num 2?", num3 > num2)
# print("Is num 2 == num 3?", num2==num3)
#
# #logical operator
# x=True
# y=False
# print("X and y",x and y)
# print("x or y",x or y)
# print("not of x",not x)
# # bitwise
# num4 = 6
# num5 = 2
# print("Bitwise and =", num4 & num5)
# print("bitwise or=", num4 | num5)
# print("bitwise Xor=", num4 ^ num5)
# print("num5 right shift by 2", num4>>2)
# print("num5 left shift by 3",num5<<3)
#
# #
# string1 ='python'
# string2 = 'Tutorial'
# print(string1+string2)
# print(string1*3)
# print(string2[-4])
#
# print(string1.count('p',0,5))
# print(string2.find('or'))
# print(string1.upper())
# print(string1.isalpha())
#
# #tuple
# my_tup = ('Ash','spru','piu')
#
# print(my_tup * 2 )
# print(my_tup[1:3])
#
# my_list=['green','pink','red']
# my_list.append('grey')
# print(my_list)
# my_list.extend(['white'])
# print(my_list)
#
# my_Dict={1:'apple',2:'ball'}
# print(my_Dict[1])
# len(my_Dict)
# my_Dict.get(2)
# print(my_Dict.keys())
# print(my_Dict.values())
# my_Dict.update({1:'lolo'})
# print(my_Dict)
#
# #set
#
# my_set={1,2,3,4,2}
# print(my_set)
# s1={1,2,3,'c'}
# s2={3,4,'o'}
# print(s1|s2)
# print(s1 &s2)
# print(s1-s2)
#
# marks=75
# if(marks>80):
#     print("Grade A")
# elif(marks >60) and (marks<=80):
#  print("Grade B")
# elif(marks>40) and (marks<=60):
#  print("Grade c")
# else:
#  print("Grade D")
''''''''''''''''''''''
#while
num=int(input('enter the value of n='))
if (num<=0):
 print("enter valid number")
else:
 sum=0
 while(num>0):
     sum+=num
     num-=1
     print(sum)

for quant in range(99,0,-1):
         if quant >1:
             print(quant,"bottle of beer on the wall,", quant,"bottles of beer")
             if quant >2:
                 suffix=str(quant)+ "bottles of beer on the wall"
             else:
                    suffix = '1 bottle of beer on the wall'
         elif quant ==1:
            print("1 bottle of beer on the wall, 1 bottles of beer")
            suffix="no more beer on the wall"
print('take 1 down and pass it around', suffix)
'''''''''''''''''''''''
for x in range(20):
    if (x%2)==0:
        continue
    print(x)

