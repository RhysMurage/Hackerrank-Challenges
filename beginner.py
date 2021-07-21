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
# n = int(input())
# arr = map(int, input().split())

# #create list object
# list1 = list(arr)

# #create a set object that is iterable and removes duplicates, then convert to a sorted list
# new_list = sorted(list(set(list1)))

# #print
# print(new_list[-2])

## Nested Lists
# record=[]
# names =[]
# scores = []
# for _ in range(int(input())):
#     name = input()
#     score = float(input())
#     record.append([name,score])
#     record.sort(key=lambda x: x[1], reverse=True)


# for x in record:
#     for y in x:
#         if isinstance(y,float) is True:
#             scores.append(y)


# secondLastIndex = scores.index(min(scores)) - 1
# secondLastScore = record[secondLastIndex][-1]

# for x in record:
#     for y in x:
#         if secondLastScore == y:
#             names.append(x[0])
#             names.sort()
#         else:
#             pass

# for name in names:
#     print(name)


## WORKINGS FOR NESTED LISTS
# records = [['Harsh',20],['Beria',20],['Varun',19],['Kakunami',19],['Vikas',21]]
# records.sort(key=lambda name: name[1], reverse=True)
# scores = []
# print(records)
# for x in records:
#     for y in x:
#         if isinstance(y,int) is True:
#             scores.append(y)
# print(scores)
# print(scores.index(min(scores)))
# secondLastIndex = scores.index(min(scores)) - 1
# print(scores[secondLastIndex])
# for x in record:
#     if secondLastScore == x[:4]:
#         print(x)
#     else:
#         print('nono')
# print(secondLastScore)
# print(secondLastName)

## LAMDA FUNCTIONS TO SORT BY LAST NAME
# scifi_authors = ['Issac Asimov', 'Ray Bradbury', 
#     'Robert Heinlein', 'Arthus C. Clarke', 'Frank Herbert',
#     'Orson Scott Card', 'Douglas Adams', 'H. G. Wells', 'Leigh Brackett']
# help(scifi_authors.sort)
# name = "Rhys Murage"
# print(name.split()[-1].lower()) 
# scifi_authors.sort(key=lambda name: name.split(' ')[-1].lower()) SPLIT NAMES WHERE THERE ARE SPACES
# print(scifi_authors)

##Solution from discussion
# marksheet = []
# for _ in range(0,int(input())):
#     marksheet.append([input(), float(input())])

# second_highest = sorted(list(set([marks for name, marks in marksheet])))[1]
# print('\n'.join([a for a,b in sorted(marksheet) if b == second_highest]))

## Finding the percentage
import statistics
n = int(input())
student_marks = {}

for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
print(student_marks[query_name])

average = round(statistics.mean(student_marks[query_name]))
print('%.2f'%average)

## Setting Precision from GeeksforGeeks
### using '%'
## print('%.2f'$<variable>)

### using format()
## print('{0:.2f}'.format(<variable>))
 
### using round() <though float like 56 will be 56.0 rather than 56.00
## print(round(<variable>, 2))




# name1 = 'Rhys 78 96 65'
# name2 = 'James 87 98 54'
# score=[]
# score.append(name1)
# score.append(name2)
# print(score)
# specificScore=[]
# for x in score:
#    studentAndScores = x.split()
#    student, scores = studentAndScores[0], studentAndScores[1:]
#    scores = map(float, scores)
#    student_marks[student] = list(scores)
# print(student_marks)
# print(student_marks['Rhys'])