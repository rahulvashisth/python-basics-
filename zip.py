#zip will make the pair for you from your lists like---
#index0 from list1(b) and index0 from list2(c) and so on.
#once any one list will finished or completed it will terminate --
#--or leave the other elements from other lists.
# if you want to check you can edit list b one with one more element and run it.
#here one more interesting thing which i've done is i am storing the value of
# zip in variable a. otherwise it will give you the index for the zip value
# after print.

a= zip()
b = [1,3,5,4,5,8,7]
c = [5,4,7,8,9,9,5]
print('the classs of the zip is', type(a))
a= zip(b,c)
print(a)
for values in a:
    print(values)
