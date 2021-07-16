# a = int(input())
# # b = int(input())
# n = 1
# while a:
#     print(n**2)
#     n += 1
#     if n == a:
#         break


# Leap year
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


# Print Function

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
# # print(comb[132])
# print(icomb_even)
# print(icomb_odd)

# # print(comb[134])

# # comb=['1','5','8']
# # x = enumerate(comb)
# # print([x for x in x])


print(*range(1, int(input())+1), sep='')