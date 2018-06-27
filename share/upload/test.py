# x=input("请输入字符串x：")
# a=len(x)
# b=x[0:1]
# c=x[a-1]
# d=x[a//2]
# print(b,c,d)

# x=input("请输入字符串x：")
# if x is not None:
#     a=ord(x[0:1])
# print(a)

# x=int(input("请输入整数x："))
# print(chr(x))
# x=input("请输入字符串x：")
# count=0
# for c in x:
#     if ord(c)==32:
#        count+=1
# print('(1)的答案:',count)
# a=x.isdigit()
# print('(2)的答案:',a)
# try: 
#    b=float(x)
#    print('(3)的答案:',True)
# except ValueError:
#    print('(3)的答案:',False)
# a=input()
# b=input()
# c=input()
# d=max(len(a),len(b),len(c))
# # e='%'+str(d)+'s'
# # print(e % a)
# # print(e % b)
# # print(e % c)
# print('%*s' % (d,a))
# print('%*s' % (d,b))
# print('%*s' % (d,c))

# #第一题
# x=int(input("请输入整数x："))
# i=0
# while i<x:
#     print("hello world!")
#     i=i+1
#第二题
# i=20
# while i>0:
#     print(i)
#     i=i-1
# x=int(input())
# i=1
# while i<x+1:
#     a=0
#     while a<x:
#         print(i,end='')
#         i+=1
#         a+=1
#     i=i-(x-1)
#     print()
# sum=0
# while True:
#     a=int(input())
#     if a==0:
#         break
#     else:
#         sum+=a
# print(sum)
# begin='A'
# sum=''
# i=0
# while i<26:
#     a=ord(begin)+32
#     begin1=chr(a)
#     sum=sum+begin+begin1
#     b=ord(begin)+1
#     begin=chr(b)
#     i+=1
# print(sum)
# a=input()
# count=0
# kong=0
# for i in a:
#     if i=='a':
#         count+=1
#     if i==' ':
#         kong+=1
# print('a的个数为:',count)
# print('空格的个数为:',kong)
# begin=int(input())
# begin1=begin
# for i in range(begin):
#     for j in range(begin1):
#         print(i+1+j,end='')
#     print()
#     begin=begin+1
# sum=0
# for i in range(1,100,2):
#     sum=sum+i
# print(sum)
# x=input('请输入:')
# y=input('请输入:')
# z=input('请输入:')
# L=[x,y,z]
# count=0
# for i in L:
#     for j in i:
#         count+=1
# print(L,'总字符为:',count)
# L=[]
# while True:
#     a=input()
#     if a=='':
#         break
#     #L.append(a)
#     L += [a]
# count=0
# zifu=0
# for i in L:
#     zifu+=len(i)
#     count+=1

# print('行数:',count,'字符数是:',zifu)
# x=int(input('请输入整数三角形高度:'))
# L=[]
# a=x
# for i in range(x):
#     s=(a-i-1)*' '
#     s1=(i*2+1)*'*'
#     ss=s+s1
#     print(ss)
# for i in range(100,1000):
#     a=i//100
#     b=(i%100)//10
#     c=i%10
#     d=a**3+b**3+c**3
#     if i==d:
#         print(i)
# for i in range(3,100):
#     f=True
#     for a in range(2,i):
#         if i%a==0:
#             f=False
#             break
#     if f==True:
#         print(i) 
# L=[3,5]
# L[0:0]=[1,2]
# L[3:]=[4,5,6]
# print(L)
# #L2=list(reversed(L))
# # a=len(L2)
# # del(L2[a-1])
# # print(L2)
# L[:]=L[::-1]
# del(L[-1])
# print(L)

#第一题
# L=[1,1]
# for i in range(2,100):
#     a=L[i-1]+L[i-2]
#     L+=[a]
# print(L,end=' ')
# print()
# print(sum(L)/100)

# #第二题
# begin=int(input('请输入起始值：'))
# end=int(input('请输入终止值：'))
# print('十进制','十六进制','文字')
# for i in range(begin,end):
#     print(i,' '*3,hex(i),' '*3,chr(i))
# s="ABC"
# S2="123"
# L=[y+x for y in s for x in S2]
# print(L)

# L=[n for n in range(1,101,3)]
# print(L)

# a=input()
# b=sorted(a,reverse=False)
# print(b)

# a=input()
# b={}
# for i in a:
#     if i in b:
#         b[i]+=1
#     else:
#         b[i]=1
# for i in b.items():
#     print(i)

# d={}
# L=['tarena','xiaozhang','hello']
# d={x:len(x) for x in L}
# print(d)

# numbers=[1001,1002,1003,1004]
# names=['Tom','Jerry','Spike','Tyke']
# d={numbers[i]:names[i] for i in range(4)}
# print(d)

# 奇数偶数序列
# odd=[]
# evens=[]
# i=1
# while i<=100:
#     if i%2==0:
#         evens.append(i)
#     else:
#         odd.append(i)
#     i+=1
# print('奇数:',odd)
# print('偶数:',evens)

# #猴子吃桃
# i=1
# a=i
# for i in range(9):
#     a=(a+1)*2
# print(a)

# #完全数
# i=1
# count=0
# for i in range(1,10000):
#     L=[]
#     for x in range(1,i):
#         if(i%x==0):
#             L.append(x)
#     if i==sum(L):
#         print(i)

# manager={'曹操','刘备','周瑜'}
# jishu={'曹操','张飞','周瑜','赵云'}
# #1
# print('1:',manager&jishu)
# print('2:',manager-jishu)
# print('3:',jishu-manager)
# a='张飞' in manager
# print('4:',a)
# print('5:',manager^jishu)
# c=manager|jishu
# print('6:',len(c))

# def mymax(a,b,c):
#     return max(a,b)
# print(mymax(100,200))
# print(mymax(34,23))
# print(mymax('田','刘'))

# def mymax(a,b,c):
#     print(a,b,c)
# mymax(100,*[200,300])
# mymax(*[10,20],30)
# mymax(*[100],200,*[300])
# mymax(100,c=300,b=200)
# #mymax(b=200,c=300,100)
# mymax(100,**{"c":300,"b":200})
# mymax(**{"c":300,"b":200},a=100)
# L=[]
# def fn(x):
#     L=[x]
# fn(10)
# print(L)
# L1=[]
# L2=[]
# def liang():
#     a=input()

#     for i in a:
#         if int(i)%2==0:
#             L2.append(i)
#         else:
#             L1.append(i)
# liang()
# print('奇数',L1)
# print('偶数',L2)





# def test(x,y=1,*a,**b):
#     print(x,y,a,b)
# test(1)                 #   1 1 () {}
# test(1,2)                   #   1 2 () {}
# test(1,2,3)             #   1 2 (3,) {}
# test(1,2,3,4)               #   1 2 (3, 4) {}
# test(x=1,y=2)               #   1 2 () {}
# test(1,a=2)             #   1 1 () {'a': 2}
# test(1,2,3,a=4)             #   1 2 (3,) {'a': 4}
# test(1,{'a':4,'b':5})
# #test(x=1,2)

# v=100
# def f1():
#     #v=200
#     print("f1内v:",v)
#     def f2():
#         #v=300
#         print("f2:",v)
#     f2()
# f1()
# print("waimian:",v)
# v=100
# def f1():
#     v=200
#     def f2():
#         nonlocal v
#         v=300
#         print("f2:",v)
#     f2()
#     print("f1:",v)
# f1()
# print("quanbu:",v)

# a=1
# b=2
# c=3
# def f1(c,d):
#     e=300
#     print("locals:",locals())
#     print("globals:",globals())
#     print("全局c:",globals()['c'])
#     print("局部c:",locals()['c'])
# f1(100,200)

# myadd =lambda x,y :x+y
# print("20+30=",myadd(20,30))

# mymod = lambda x,y:x**2%y
# print(mymod(4,5))

# n=[1,2]
# print(sum(map(lambda x:x**x,n)))




#闭包
# def make_power(y):
#     print(y)
#     def f(x):
#         return x**y
#     return f
# pow2=make_power(2)
# print('5的平方是:',pow2(5))
# pow3=make_power(3)
# print('6的立方:',pow3(3))

# def power2(x,y):
#     return x**y
 
# L=[]
# mit=map(power2,range(1,10))
# for x in mit:
#     L.append(x)
# print(L)
# mit=map(power2,range(1,10),range(9,0,-1))
# print(mit)

# mit=map(lambda x,y:x**y,range(1,10),range(9,0,-1))
# print(sum(mit))

# s='ABCDEFG'
# L=[1,2,3,4,5,6,7]
# l=[]
# def sum(x,y):
#     return str(x)+str(y)
# mit=map(sum,s,L)
# for i in mit:
#     l.append(i)
# print(l)
# L=[]
# def sushu(x):
#     if i<=1:
#         return False
#     for i in range(2,x):
#         if x%i==0:
#             return False
#     return True
# L=[x for x in filter(sushu,range(1,100))]
# print(L)
# L=[]
# names=['Tom','Jerry','Spike','Tyke']
# for i in names:
#     a=i[::-1]
#     L.append(a)
# print(sorted(L))

# def k(x):
#     return x[::-1]
# L2=sorted(names,key=k)
# print(L2)

# L = [
#      {"name": "Python基础教程",
#       'price': 58,
#       'pages': 866
#      },
#      {"name": "C语言教程",
#       'price': 98,
#       'pages': 982
#      },
#      {"name": "C++",
#       'price': 56,
#       'pages': 1024
#      },
#      {"name": "Java",
#       'price': 79,
#       'pages': 691
#      }
#   ]
# def k(d):
#     return d['price']
# L2=sorted(L,key=k)
# print(L2)
# def k1(d):
#     return d['pages']
# L3=sorted(L,key=k1)
# print(L3)

# def ll(x):
#     x=x+1
#     print(x)
#     if x<10:
#         ll(x)
# ll(0)

# L=[[[2,4],[6,8],[10]],0,[1,2,3,[7,9]]]
# def p(L):
#     for i in L:
#         if type(i)==list:
#             p(i)
#         else:
#             print(i)
# p(L)
# def myfac(x):
#     if x==1:
#         return 1
#     else:
#         return x*myfac(x-1)
# print(myfac(3))
#输入函数
# # L=[]
# def input_student():  
#     while True:
#         d={}
#         name=input('name:')
#         if name=='':
#             break
#         age=int(input('age:'))
#         score=int(input('score:')) 
       
#         d={'name':name,'age':age,'score':score}
#         L.append(d)
#     return L



# #打印函数
# def output_student(lst):
#     print(' '*6,'name',' '*3,'age',' '*3,'score')
#     for i in range(len(lst)):
#         print("%10s%10s%10s"% (lst[i]['name'],lst[i]['age'],lst[i]['score']))
# #删除函数
# def delete_student(lst):
#     a=input("请输入要删除学生的姓名:")
#     for i in range(len(lst)):
#         if lst[i]['name']==a:
#             del lst[i]
#             break
# #修改函数
# def update_student(lst):
#     a=input("请输入要修改学生的姓名:")
    
#     for i in range(len(lst)):
#         if lst[i]['name']==a:
#             print(lst[i])
#             name=input('name:')
#             age=int(input('age:'))
#             score=int(input('score:'))
#             d={'name':name,'age':age,'score':score}
#             lst.append(d)
#             del lst[i]
#             break
# #按成绩打印
# def score(d):
#     return d['score']  
# #按年龄打印
# def age(d):
#     return d['age']

# def jiemian():
#     print('+----------------------+')
#     print('|  1)添加学生信息      |')
#     print('|  2)显示学生信息      |')
#     print('|  3)修改学生信息      |')
#     print('|  4)删除学生信息      |')
#     print('|  5)按成绩高到低打印  |')
#     print('|  6)按成绩低到高打印  |')
#     print('|  7)按年龄高到低打印  |')
#     print('|  8)按年龄低到高打印  |')
#     print('|  q)退出程序          |')
#     print('+----------------------+')
#     print("请选择:")
#     a=input()
#     if a=='1': 
#         global lst
#         lst=input_student()
#         jiemian()
#     elif a=='2':
#         output_student(lst)
#         jiemian()
#     elif a=='3':
#         update_student(lst)
#         jiemian()
#     elif a=='4':
#         delete_student(lst)
#         jiemian()
#     elif a=='5':
#         m=sorted(lst,key=score)
#         output_student(m)
#         jiemian()
#     elif a=='6':
#         m=sorted(lst,key=score,reverse=True)
#         output_student(m)
#         jiemian()
#     elif a=='7':
#         m=sorted(lst,key=age)
#         output_student(m)
#         jiemian()
#     elif a=='8':
#         m=sorted(lst,key=age,reverse=True)
#         output_student(m)
#         jiemian()
#     else:
#         return
# jiemian()

