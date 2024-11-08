
def shifr(n):
    string = ''
    for k in range(1,n):
        for v in range(k+1,n):
            if n % (k + v) == 0:
                string += str(k) + str(v)
    print(f"{n} - {string}")

num = int(input("Введите число "))
shifr(num)



#         print(3)
#         break
#     if i == 4:
#         print('1+3')
#         break
#     if i == 5:
#         print('1+4 2+3')
#         break
#     if i == 6:
#         print('1+2 1+5 2+4')
#         break
#     if i == 7:
#         print('1+6 2+5 3+4')
#         break
#     if i == 8:
#         print('1+3 1+7 2+6 3+5')
#         break
#     if i == 9:
#         print('1+2 1+8 2+7 3+6 4+5')
#         break
#     if i == 10:
#         print('1+4 1+9 2+3 2+8 3+7 4+6')
#         break
#     if i == 11:
#         print('1+10 2+9 3+8 4+7 5+6')
#         break
#     if i == 12:
#         print('1+2 1+3 1+5 1+11 2+4 2+10 3+9 4+8 5+7')
#         break
#     if i == 13:
#         print('1+12 2+11 3+10 4+9 5+ 6+7')
#         break
#     if i == 14:
#         print('1+6 1+13 2+5 2+12 3+4 3+11 4+10 5+9 6+8')
#         break
#     if i == 15:
#         print('1+2 1+4 1+14 2+3 2+13 3+12 4+11 5+10 6+9 7+8')
#         break
#     if i == 16:
#         print('1+3 1+7 1+15 2+6 2+14 3+5 3+13 4+12 5+11 6+10 7+9')
#         break
#     if i == 17:
#         print('1+16 2+15 3+14 4+13 5+12 6+11 7+10 8+9')
#         break
#     if i == 18:
#         print('1+2 1+5 1+8 1+17 2+4 2+7 2+16 3+6 3+15 4+5 4+14 5+13 6+12 7+11 8+10')
#         break
#     if i == 19:
#         print('1+18 2+17 3+16 4+15 5+14 6+13 7+12 8+11 9+10')
#         break
#     if i == 20:
#         print('1+3 1+4 1+9 1+19 2+3 2+8 2+18 3+7 3+17 4+6 4+16 5+15 6+14 7+13 8+12 9+11')
#         break
# result = i


