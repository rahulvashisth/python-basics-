print('your value')
n= int(input())
if n%4==0:
    if n%100==0:
        if n%400==0:
            print('yes it is, let me try one more time')
        else:
            print('no')
    else:
        print('yes')
else:
    print("no")
