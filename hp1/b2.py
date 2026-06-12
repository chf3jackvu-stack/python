# # b = "xin chao"
# # for i,v in enumerate(b):
# #     print(f"day la vi tri{i}: {v}")

# # """bai 1"""
# # a = input("nhap ky tu: ")
# # # print(a[0])
# # # print(a[-1])
# # x = len(a)
# # y = x // 2
# # if x % 2 == 0:
# #     print(a[y-1:y+1])
# # else:
# #     print(a[y])



# # """""Bai 2"""""
# mk = (input("nhap mat khau: "))

# while len(mk) < 8:
#     mk = input("nhap lai mat khau")

# c =mk[0:4]+"#"*( len(mk)-4)
# print(c)

## """""""" bai so dien thoai"""""""
# while True:
#     sdt = input("nhap so dien thoai cua ban")
#     for v in sdt:
#         if v.isdigit():
#             continue
#         else:
#             print("nhap sai so dien thoai")
#             break
#     if len(sdt) == 10:
#         break

# x = "(+84)" + sdt[1:4] + " " + sdt[4:7] + "-"+ sdt[7:10]
# print(x)

# # """""""" tinh tien dien """"""""
# dien =  int(input("nhap Kw/h dien ban su dung: "))
# muc1 = dien * 2000
# muc2 = (dien - 50) * 2500 + (50* 2000)
# muc3 = (dien - 100) * 3500 + 50 * 2500 + (50* 2000)
# if dien <= 50:
#     print(muc1,"VND")
# elif dien > 50 and dien <101:
#     print(muc2,"VND")
# else:
#     print(muc3,"VND")


# #"""""" IN HOA CHU DAU VA CHU SAU DAU CACH"""""""""""

# chu = input("nhap chu: ")
# chu=chu.strip()
# chu = chu.capitalize()
# for i,v in enumerate(chu):
#     if v == " ": 
#         chu = chu[:i+1] + chu[i+1].upper() + chu[i+2:]

# chu = chu.replace(" ","")


# print(chu)
