print(2**-5)

# nums = [4, 3, 2, 3]
# # nums = list(A)


# def fd(nums):
#     nums.sort()
#     l = []
#     # print(2^2)
#     i = 0
#     # lx = 0
#     # rx = 0
#     B = -1
#     j = len(nums)-1

#     c = 0
#     while(i-1 < j+1):
#         # if(nums[i])
#         if(nums[i]+1 != nums[i+1] and nums[i] != nums[i+1]):
#             # print("1")
#             B = nums[i]+1
#             c += 1
#         elif(nums[j-1]+1 != nums[j] and nums[j-1] != nums[j]):
#             # print("2")
#             B = nums[j-1]+1
#             c += 1

#         if(nums[i] == nums[i+1]):
#             A = nums[i]
#             c += 1

#         elif(nums[j] == nums[j-1]):
#             A = nums[j]
#             c += 1
#         if(c == 2):
#             # print(A, B)
#             return [A, B]
#         i += 1
#         j -= 1
#     return [A, B]


# print(fd(nums))
# print(A, B)
# return [A, B]
# print(i)
# fg = []

# def nav(ls, ep, ix, fg):
#     if(ix > len(ls)-1):
#         return

#     ep.append(ls[ix])
#     nav(ls, ep, ix+1, fg)
#     ep.pop()
#     nav(ls, ep, ix+1, fg)
#     l = []
#     jt = []
#     for i in range(len(ep)):
#         for j in range(i+1, len(ep)):
#             jt.append((ep[i], ep[j]))
#             l.append(abs(ep[i]-ep[j]))
#     if(len(set(l)) == 1):
#         fg.append(jt)
#         return

# x = 7
# nav([1, 5, 3, 4, 5, 5, 4], [], 0, fg)
# print(x-len(list(max(fg, key=lambda gh: len(gh)))))

# x = 7
# y = [1, 5, 3, 4, 5, 5, 4]
# l = []
# for i in range(x):
#     for j in range(i+1, x):

#         l.append(abs(y[i]-y[j]))
#         if(abs(y[i]-y[j]) == 1):
#             print(y[i], y[j])
# print(max(l, key=lambda y: l.count(y)))

# while(i < len(height)):
#     # print(i)
#     gh = height[i]
#     l = []
#     # if(gh > 0):
#     i += 1
#     print(gh, height[i])
#     while(gh < height[i] and i < len(height)):
#         # print(i)
#         l.append(height[i])
#         i += 1
#     l.append(height[i])
#     i += 1
# print(l)

# i = 0
# j = len(x)-1
# mx = 0
# while(i < j):
#     mx = max(min(x[i], x[j])*(j-i), mx)
#     if(x[i] < x[j]):
#         i += 1
#     else:
#         j -= 1
# print(mx)
# # y = 11
# dct = {}
# for i in range(len(x)):
#     if(x[i] in dct):
#         print(dct[x[i]], i)
#         break
#     else:
#         ntf = y-x[i]
#         dct[ntf] = i

#     # else:

# print(dct)
# for i in range(len(x)):
#     for j in range(i+1, len(x)):
#         if(x[i]+x[j] == y):
#             print(i, j)
#             break
# x = sorted(x)
# # print(x)
# i = 0
# j = len(x)-1

# while(i < j):
#     if(x[i]+x[j] == y):
#         print(i, j)
#         break
#     elif(x[i]+x[j] > y):
#         j += 1
#     else:
#         i += 1

# x = list(map(int, input().split(" ")))
# y = int(input())

# def rec(lst, tsu, emp, i):
#     if(sum(emp) == tsu):
#         print(*emp)
#         return
#     elif(sum(emp) > tsu or i > len(lst)-1):
#         return

#     emp.append(lst[i])
#     # print(emp)

#     rec(lst, tsu, emp, i+1)
#     emp.pop()
#     rec(lst, tsu, emp, i+1)

# rec(x, y, [], 0)

# x = list(map(int, input().split(" ")))
# y = list(map(int, input().split(" ")))
# z = x+y
# z = sorted(z)
# print(*z)

# y = int(input())
# def fec(y):
#     if(y == 0):
#         return 1
#     if(y < 0):
#         return 0
#     return fec(y-1)+fec(y-2)
# print(fec(y))

# def solve(N, S, D, power):
#     def sve(S, power, i):

#         if(S <= 0):
#             return 0

#         if(i > len(power)-2):
#             i = power.index(max(power))
#         S = S-power[i]
#         power[i] = power[i]//2

#         return 1+sve(S, power, i+1)
#     print(sve(S, power, 0))

# print(solve(3, 20, 5, [5, 7, 3]))

#     st = str(x)
#     if(len(st) == 1):
#         if(st == '1'):
#             print("Happy")
#             return True
#         else:
#             print(ls)
#             for i in range(len(ls)-1):
#                 if(st == ls[i]):
#                     print("Not Happy")
#                     return False
#     s = 0
#     for i in (st):
#         s = s+int(i)*int(i)
#     ls.append(str(s))
#     return hap(s, ls)

# print(hap(2, []))
