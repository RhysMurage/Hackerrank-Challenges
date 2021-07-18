# a = int(input())
# # b = int(input())
# n = 1
# while a:
#     print(n**2)
#     n += 1
#     if n == a:
#         break


## Leap year
# def is_leap(year):
#     leap = False
    
#     if year <= 1900 or year >= 10**5:
#         return leap
#     elif year % 100 == 0 and year % 400 == 0:
#         return not leap
#     elif year % 4 == 0 and year % 100 != 0:
#         return not leap
#     else:
#         return leap

# year = int(input())
# print(is_leap(year))


## Print Function

# n = int(input())
# a = 0
# numb =[]
# comb = []
# fcomb = []

# while n<=150:
#     # y = str(a)
#     numb.append(str(a))
#     a += 1
#     if len(numb) > 1:
#         comb.append(numb[a-2]+numb[a-1])
#         if a > n:
#             break

# icomb_even = [x for x in range(0,n) if x%2 == 0]
# icomb_odd = [x for x in range(0,n) if x%2 != 0]

# if n%2 == 0:
#     for y in icomb_odd:
#         fcomb.append(comb[y])
#     print(''.join(fcomb))

# elif n%2 != 0:
#     for y in icomb_even:
#         fcomb.append(comb[y])
#     print(''.join(fcomb)[1:])
    

# # print(numb)
# print(fcomb)  
# print(comb)  
# print(icomb_even)
# print(icomb_odd)

## Hackerrank solution to Print Function from Discussion section
# print(*range(1, int(input())+1), sep='')

## List comprehensions

# x = int(input())
# y = int(input())
# z = int(input())
# n = int(input())

# cartesian_product = [[a,b,c] for a in range(0,x+1) for b in range(0,y+1) for c in range(0,z+1) if a+b+c != n]
# print(cartesian_product)

# ##remove duplicates
# # 1: (doesn't work for list of lists because list is not hashable)
# # final_cartesian_product = list(dict.fromkeys(cartesian_product))
# # print(final_cartesian_product)

# # 2: from note.nkmk.me
# def get_unique_list(seq):
#     seen = []
#     return [x for x in seq if x not in seen and not seen.append(x)]

# print(get_unique_list(cartesian_product))

## Hackerrank tip to avoid repetitive input calls from Discussion section
# x, y, z, n = (int(input()) for _ in range(4))

## Find the Runner-up Score!
n = int(input())
arr = map(int, input().split())

list1 = list(arr)
new_list = sorted(list(set(list1)))
print(new_list)
print(new_list[-2])