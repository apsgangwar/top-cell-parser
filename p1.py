import math

def customDecorator(func):
    print("hello")
    func()

@customDecorator
def printWorld():
    print("world")

strN = "randomstring"
print(strN[:6])

dict1 = {'a':'ABC', 'b': 'HWYR', 'c':1234 }
dict2 = {'a':'CBA', 'd': 'KIJD', 'c':4321 }

def reverseString(s1):
    s2 = ""
    l = len(s1)
    for i in range(l):
        s2 = s2 + s1[l-i-1]
    return s2

def reverseNumber(n1):
    n2 = 0
    while(n1>0):
        n2 = n2*10 + n1%10
        n1 = math.floor(n1/10)
    return n2

for key in dict1:
    value1 = dict1[key]
    if key in dict2: 
        value2 = dict2[key]

        reversedValue = str(value1)[-1::-1]
        if str(value2) == reversedValue:
            print(key)


a = [1, 2, [[8,3,5],[3,4,5,6]],[5,6]]

def sumList(list):
    sum = 0
    for i in list:
        t = type(i)
        if(t.__name__ == 'list'):
            sum = sum + sumList(i)
        else:
            sum = sum + i  
    return sum

print(sumList(a))


# api - 3000
# web - 4200
# demo-host.com
# nginx proxy - 
#     /api - 3000
#     /* - 4200


# emp_name, department, svc_exp, 
# 1, x, 3
# 1, y, 2
# select emp_name, sum(svc_exp) as total_exp from table_emp
# # where emp_name = 1
# group by emp_name
# [{emp_name, total_exp}]


# .txt

# a = [1,2,3,10, 40,45,46,70,80,90]
# b = sumList(a)
# print(b/10)
