import random

num = str(random.randint(100, 999))
# if (num[0] and num[1] and num[2] != '7'):
#     print(num)
# else:
#     print('invalid number')



if ( '8' not in num ):
    if ('9' not in num ):
        print(num)
        
else:
    print('invalid')