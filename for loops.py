#program to find the mininum and maximum number in a list:

a=[1,8,6,7,9]

min=a[0]
for i in a:
    if i<min:
        min=i
print("The minimum no is ",min)

#max..
x=[4,2,8,9,1,7]
max=a[0]
for i in a:
    if i> max:
        max=i
print("The maximum no is",max)

#new one..
for l in 'jhon':
    if l =="n":
        pass
    print(l)

#program to sum the first 10 even numbers..
sum=0

for i in range(2,22,2):
    sum=sum+i
print(sum)

#program to find the sum and average of the list

a=[2,3,5,6,7]
sum=0
n=len(a)
for i in a:
    sum=sum+i
    avg=sum/n
print('The sum of the list',sum)
print('The avg of the list',avg)

#multiplication 

a=[1,2,4,5]
mul=1
for i in a:
    mul=mul * i
print(mul)

# Return the product if the product is <= 1000 else return the sum
n1=20
n2=60
mul=n1*n2
sum=n1+n2
if mul<=1000:
    print("it returns the product coz it is less than 1000:",mul)
else:
    print("It returns the sum coz it is greater than 1000:",sum)


#program to print the current and previous number.
prev=0
for i in range(10):
    print('previous number',i-1)
    print('current number',i)
    sum=i-1+i
    print("the sum",sum)

#print only even indexes...

s='manusha pothuganti'

n=len(s)

for i in range(0,n,2):
    print(s[i])

#check if the first and last no is a list...

a=[2,3,5,8,0,2]

if a[0]==a[-1]:
    print('same')
else:
    print('Not same')


list1=[10,20,25,30,35]
list2=[40,45,60,75,90]
res=[]

for i in list1:
    if i%2==0:
        res.append(i)
for j in list2:
    if j%2!=0:
        res.append(j)
print(res)


#program to count the total digits in the number..
n=1528547
count=0
while n!=0:
    n=n//10
    count+=1
print(count)


#program to find the matching characters in a string..

n="swamypatel"

set1=set()

for i in n:
    if n.count(i)>1:
        set1.add(i)
print(set1)

#program to find the prime no.s from 1 to 100..
p=2
q=100

numbers=[]
for i in range(p,q+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)
        numbers.append(i)

print('The primenumbers from 1 to 100 are:',len(numbers))