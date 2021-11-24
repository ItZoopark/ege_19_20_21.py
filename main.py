# 1 куча ----------------------------
# a = [0] * 25
#
# for i in range(len(a)):
#     if i * 2 >= 25:
#         a[i] = 1
#     else:
#         a[i] = 0
#
# print(list(range(len(a))))
# print()
# print(a)
# while 0 in a:
#     for i in range(len(a)):
#         if a[i] == 0:
#             if a[i + 2] > 0 and a[2 * i] > 0:
#                 a[i] = max(a[i + 2], a[i * 2]) * (-1)
#             elif a[i + 2] < 0 or a[2 * i] < 0:
#                 a[i] = abs(min(a[i + 2], a[2 * i])) + 1
#
# print(a)
# print(a[4])

# 2 кучи ---------------------------
# a = [[0] * 20 for i in range(20)]
# for i in range(20):
#     for j in range(20):
#         if 2 * i + j >= 20 or 2 * j + i >= 20:
#             a[i][j] = 1
#         else:
#             a[i][j] = 0
#
# for k in range(100):
#     for i in range(20):
#         for j in range(20):
#             if a[i][j] == 0:
#                 if a[i + 1][j] > 0 and a[i][j + 1] > 0 and a[2 * i][j] > 0 and a[i][2 * j] > 0:
#                     a[i][j] = max(a[i + 1][j], a[i][j + 1], a[2 * i][j], a[i][2 * j]) * (-1)
#                 elif a[i + 1][j] < 0 or a[i][j + 1] < 0 or a[2 * i][j] < 0 or a[i][2 * j] < 0:
#                     a[i][j] = abs(min(a[i + 1][j], a[i][j + 1], a[2 * i][j], a[i][2 * j])) + 1
#
# for i in range(1, 20):
#     if a[1][i] == 1:
#         print(i, end=' ')

# print(a)
# 1 куча -----------------------------------
# a = [0]*100
# for i in range(len(a)):
#   if 2*i >= 48:
#     a[i] = 1
#   else:
#     a[i] = 0
# while 0 in a:
#   for i in range(len(a)):
#     if a[i] == 0:
#       if a[i+1] > 0 and a[i+3] > 0 and a[2*i] > 0:
#         a[i] = max(a[i+1], a[i+3], a[2*i]) * (-1)
#       elif a[i+1] < 0 or a[2*i] < 0 or a[i+3] < 0:
#         a[i] = abs(min(a[i+1], a[i+3], a[2*i])) + 1
#
# print(a)
# for i in range(len(a)):
#   if a[i] == -2:
#     print(i, end=' ')
# 2 кучи (решу егэ: 27760) -----------------------------------
# N = 100
# win_sum = 41
# a = [[0]*N for i in range(N)]
# # for row in range(len(a)):
# #   print(a[row])
# for i in range(N):
#   for j in range(N):
#     if 2*i + j >= win_sum or 2*j + i >= win_sum:
#       a[i][j] = 1
#     else:
#       a[i][j] = 0
#
# for k in range(200):
#   for i in range(N):
#     for j in range(N):
#       if a[i][j] == 0:
#         if a[i+1][j+2] > 0 and a[i][2*j] > 0 and a[2*i][j] > 0 and a[i+2][j+1] > 0:
#           a[i][j] = max(a[i+1][j+2], a[i][2*j], a[2*i][j], a[i+2][j+1])*(-1)
#         elif a[i+1][j+2] < 0 or a[i][2*j] < 0 or a[2*i][j] < 0 or a[i+2][j+1] < 0:
#           a[i][j] = abs(min(a[i+1][j+2], a[i][2*j], a[2*i][j], a[i+2][j+1])) + 1
#
# for i in range(1, 32+1):
#     if a[8][i] == -2:
#       print(i, end=' ')
# print()

def f(num, turns, winner, max_n):
    a = [0] * num * max_n
    for i in range(len(a)):
        if 2 * i >= num:
            a[i] = 1
        else:
            a[i] = 0
    while 0 in a:
        for i in range(len(a)):
            if a[i] == 0:
                if eval(' and '.join([x + '>0' for x in turns])):
                    a[i] = max(eval(', '.join(turns))) * (-1)
                elif eval(' or '.join([x + '<0' for x in turns])):
                    a[i] = abs(min(eval(', '.join(turns)))) + 1
    print(a)
    for i in range(len(a)):
        if a[i] == winner:
            print(i, end=' ')


print('Введите ходы через пробел')
turns = input().split()
max_n = max([int(x[1:]) for x in turns if x[0] == "*"])
for k in range(len(turns)):
    turns[k] = 'a[i' + turns[k] + ']'
print('Введите необходимое кол-во камней')
num = int(input())
print('Введите победный ход')
win = int(input())
print('Чей ход')
if input() == "Вани":
    win *= -1
f(num, turns, win, max_n)


