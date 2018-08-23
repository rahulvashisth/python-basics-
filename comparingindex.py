s = [1,6,7,1]
t = [1,2,4,4]
u = s[0]+s[1]==8
v = s[0]+s[2]==8
w = s[0]+s[3]==8
if u== True:
    print(u)
else:
    print('try again')
if v== True:
    print(s[0],s[2])
else:
    print('try next')
if w== True:
    print(w)
else:
    print('try diff pair')
a = s[1]+s[2]==8
b = s[1]+s[3]==8
if a == True:
    print(a)
else:
    print('not here')
if b == True:
    print('yes')
else:
    print('no')
c= s[2]+s[3]==8
if c == True:
    print(s[2],s[3])
else:
    print('not here')
    
l = t[0]+t[1]==8
m = t[0]+t[2]==8
n = t[0]+t[3]==8
if l== True:
    print(t[0],t[1])
else:
    print('try again')
if m== True:
    print(t[0],t[2])
else:
    print('try next')
if n== True:
    print(t[0],t[3])
else:
    print('try diff pair')
q = t[1]+t[2]==8
r = t[1]+t[3]==8
if q == True:
    print(t[1],t[2])
else:
    print('not here')
if r == True:
    print(t[1],t[3])
else:
    print('no')
k= t[2]+t[3]==8
if k == True:
    print(t[2],t[3])
else:
    print('not here')
