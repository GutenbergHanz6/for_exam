import sys
sys.setrecursionlimit(10**9)

# print('x,y,z,w')
# for x in range(0,2):
#     for y in range(0,2):
#         for z in range(0,2):
#             for w in range(0,2):
#                 if ((x and not(y)) or (y == z) or w)==0:
#                     print(x,y,z,w)


# print('x , m')
# x=1
# for x in range(0,11):
#     suka = (6*17**4+x*17**3+2*17**2+7*17+2) 
#     suka2 =  (x*13**4 + 4*13**3+1*13**2+5*17+6)
#     blayt = suka + suka2
#     suka_blayt = x*11**5 + 0*11**4 + 0*11**3 + 4*11**2 + 5*11 + 6
#     if (suka == suka_blayt):
#         print(suka, suka_blayt)

# print(blayt, '=', suka_blayt)


# main = int(input('введите число : '))

# _full = ''

# main_bin = bin(main)[2:]
# ter = list(main_bin)

# if ter[0] == '1':
#     _full  = _full + '1'


# for i in range( 1  , len(ter)):
#     if i % 2 == 1 and ter[i] == '0':
#         main_bin += '0'

#     if i  % 2 != 0 and ter[i] == '1':
#         main_bin += '1'   



# _last = int(main_bin ,2)

# print(_last)


# for i in range(1000 , 10000):
#     main = 1025

#     tot = ''

#     n1 = int(str(main)[0])
#     n2 = int(str(main)[1])
#     n3 = int(str(main)[2])
#     n4 = int(str(main)[3])

#     sum1 = n1 + n3
#     sum2 = n2 + n4

#     if sum1 > sum2:
#         tot = str(sum2) + str(sum1)
    
#     else:
#         tot = str(sum1) + str(sum2)

#     if tot == '35':
#         print(i)


# for i in range(0 , 10000):

#     main_bin = bin(i)[2:]

#     if i % 2 == 0:
#         main_bin = main_bin + '11'
#     else:
#         main_bin = '1'+main_bin+'10'

#     mbin = int(main_bin , 2)
#     if mbin > 632:
#         print(i)
#         break

# for i in range(100 , 1000):

#     tot = ''

#     n1 = int(str(i)[0])
#     n2 = int(str(i)[1])
#     n3 = int(str(i)[2])

#     summ1 = n1 + n2
#     summ2 = n2 + n3

#     if summ1 > summ2:
#         tot = str(summ1) + str(summ2)

#     else:
#         tot = str(summ2) + str(summ1)

#     if tot == '86':
#         print(i)


# num0 = int(input())

# bin_num0 = bin(num0)[2:]

# sus = ''

# if num0 % 2 == 0:

#     sus = bin_num0 + (bin_num0 * 2)
# if num0 % 2 != 0 :
    
#     sus = '10' + bin_num0 + '110'

# t = int(sus , 2)
# print(t)


# i  = int(input())


# bin_i = int(bin(i)[2:])
# str_bin_i = str(bin_i)
# print(str_bin_i)


# last_bin_i = str(bin_i % 10)
# print(last_bin_i)

# bin_i_last_i = str_bin_i + last_bin_i
# print(bin_i_last_i)


# count_0 = bin_i_last_i.count('0')
# print(count_0)
# count_1 = bin_i_last_i.count('1')
# print(count_1)

# if count_1 % 2 == 0:
#     bin_i_last_i = bin_i_last_i + '0'
#     print(bin_i_last_i)

# if count_1 % 2 != 0:
#     bin_i_last_i = bin_i_last_i + '1'
#     print(bin_i_last_i)

# count_0_1 = bin_i_last_i.count('0')
# print(count_0_1)
# count_1_1 = bin_i_last_i.count('1')
# print(count_1_1)


# if count_1_1 % 2 == 0:
#     bin_i_last_i = bin_i_last_i + '0'
#     print(bin_i_last_i)

# if count_1_1 % 2 != 0:
#     bin_i_last_i = bin_i_last_i + '1'
#     print(bin_i_last_i)

# super_last_bin_i = int(bin_i_last_i , 2)
# print(super_last_bin_i)

# print('ответ на первую задачу 15')


# for y in range(0 ,100):
#     l=0 

#     bin_n = bin(y)[2:]

#     tot_bin_n = 0
#     ny_tot_bin_n = 0
#     super_bin_n = 0


#     if y % 2 == 0:
#         for i in range(len(bin_n)):
#             ny = int(str(bin_n)[i])
#             tot_bin_n = tot_bin_n + ny



#         ny_tot_bin_n = 2*tot_bin_n
#         bin_ny_tot = bin(ny_tot_bin_n)[2:]
#         bin_n = bin_n + bin_ny_tot




#     if y  % 2 != 0:
#         bin_n  = '10' + bin_n + '110'



#     bin_tot_n = int(bin_n , 2)
#     if (bin_tot_n <= 1000) or (bin_tot_n >= 1500):
#         l = l+1
#         print(l)



# print('ответ на вторую задачу 10  но я не уверен')
# n = int(input())
# list_1 = []


# total = ''
# n1 = int(str(n)[0])
# n2 = int(str(n)[1])
# n3 = int(str(n)[2])
# n4 = int(str(n)[3])

# sum1 = n1 + n2
# sum2 = n2 + n3
# sum3 = n3 + n4

# list_1.append(sum1)
# list_1.append(sum2)
# list_1.append(sum3)
 
# y = min(list_1)

# i = list_1.index(y)
 
# list_1.pop(i)


# t = str(list_1[0])
# t_1 = str(list_1[1])

# if t > t_1:
#     total = t + t_1
# if t_1 > t:
#     total = t_1 + t
#     print(total)


# def decTobin(integer):
#     return bin


# decTobin(3)
# decTobin(4)
# decTobin(5)

# from turtle import * 

# k = 20

# left(90)
# for i in range(0,13):
#     right(60)
#     forward(1 * k)
#     right(60)
#     forward(1 * k) 
#     right(270)

# up()


# for x in range(-11 ,11):
#     for y in range(-11 , 11):
#         goto(x * k , y * k)
#         dot(3)

# input()\
# def syka(n):
#     if n >= 2000:
#         return 2000
#     if n < 2000 and n % 2==1 :
#         return n * syka(n + 1)
#     if n < 2000 and n % 2==0:
#         return n * (syka(n + 1)/2)
    
# print(syka(1998) / syka(2001))
# k = 0 
# def f(n):
#     if n == 0:
#         return 0
#     return f(n -1) + n

# for n in range(237567892 , 1134567005):
#     if f(n) % 3 == 0:
#         k = k +1
# print(k)

def count_of_stupenki(n):
    if n_stupenek == 0 or n_stupenek == 1:
        return 1

    puti = [0] * (n + 1)
    puti[0] = puti[1] = 1

    for i in range(2, n + 1):
        puti[i] = puti[i - 1] + puti[i - 2]

    return puti[n]

n_stupenek = int(input())

if 0 < n_stupenek < 31:

    print(count_of_stupenki(n_stupenek))
else:
    print("кол-во ступенек должно быть от 1 до 30")