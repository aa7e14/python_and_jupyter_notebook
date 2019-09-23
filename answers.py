# Exercise 1
string1,string2='Hello ','world'
print(string1+string2)

# Exercise 2
var1,var2=5,4
var3=var1-var2
var4=var1*var2-var1/var2
print('var1=',var1,'var2=',var2,'var3=',var3,'var4=',var4)

# Exercise 3
list1=['Hello','World'] # create an empty list
list2=[5,4,7] # create a list with 3 elements
list1.append(2) # add a 2 to the first empty list
list1.append(6) # add a 6 to the first list which currently has one element in
print(list1)
print(list2)
print(list1[1])

# Exercise 4
var1,var2=4,6
print(var1<2)
print(var1<=4)
print(var1!=var2)
print(var1>=var2-2)

# Exercise 5
name='Aru'
age=72
myName='Alex'
if name=="Arup" and age==75:
    print('Your company is called',name,'and was founded',age,'years ago')
elif myName=='Steven':
    print('My name is Alex')
else:
    print('Nothing is true!')


# Exercise 6
list1=[4,6,2,3,6]
for i in range(len(list1)):
    print(list1[i])

# Exercise 7
def function1(list1):
    list2=[]
    for i in range(len(list1)):
        print(list1[i])
        list2.append(list1[i]*2)
    return list2

list1=[1,3,2,1,2]
list2=function1(list1)
print(list2)

# Exercise 8
a = np.array([1,2,3])
a[0] = 9
print(a)
print(a[1])

# Exercise 9
n,xmin,xmax=10,1,100
x=np.linspace(xmin,xmax,n)
y=np.linspace(xmin,xmax,n)+np.random.normal(loc=0,scale=8,size=n)

plt.figure(1)
plt.plot(x,y,'go')
plt.plot(x,x,'m-',linewidth=2)
plt.plot(x,x*x,'m-',linewidth=2)
plt.xlabel('x value')
plt.ylabel('y value')

# Exercise 10
a=np.array([1,2,3]) # array a, has 3 elements - it is a 1-d array
b=np.array([[1,2,3],[4,5,6]]) # array b, has 6 elements, 2 rows and 3 columns - it is a 2-d array
c=np.array([[1,2],[4,5],[1,2]])
d=np.matmul(b,c)
e=np.array([3,1,2])
f=a*e
print(d)
print(f)

# Exercise 11
x=np.linspace(0,1,12)
y=np.random.uniform(0,1,size=(12))
plt.figure(4)
plt.plot(x,y,'k--')
plt.plot(x,y*y,'b--')
plt.plot(x,y*y*y,'g--')
plt.plot(x,y*y*y*y,'r--')

z=np.random.uniform(0,1,size=(30,30))

plt.figure(5)
plt.imshow(z)
