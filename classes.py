#this is the main class and their child or subclass programm.
class stud:
    pass

std1 = stud()
std2 = stud()
std1.first = 'rahul'
std1.last = 'sharma'
std1.email = std1.first +'.'+std1.last +'@dav.com'

print(std1.email)



class vd:
    def __init__(self, first, last, marks):
        self.first = first
        self.last = last
        self.marks = marks

std3 = vd('rahul', 'sharma', 98)
std4 = vd('shivam', 'goyal', 95)
std3.email = std3.first +'.'+std3.last+ str(int(17))+'@dav.com'
std4.email = std4.first +'.'+std4.last+ str(int(17)) +'@dav.com'

print(std4.email)
