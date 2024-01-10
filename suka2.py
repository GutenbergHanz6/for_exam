# from turtle import *

# k = 15

# left(90)

# for i in range(0,7):
#     forward(10 * k)
#     right(90)
#     forward(9 * k)
#     right(90)
# up()

# forward(3*k)
# right(90)
# forward(2*k)
# left(90)
# down()

# for i in range(0,13):
#     forward(7*k)
#     left(90)

# up()
# for x in range(-11 ,11):
#     for y in range(-11,11):
#         goto(x * k , y  * k)
#         dot(3)

# input()


# list_num_4 = []

# for i in range(2,5000):
#     if (i % 1 == 0) and (i % 2 == 0) and (i % 3 == 0) and (i % 4 == 0):
#         list_num_4.append(i) 

# print(list_num_4)


# import datetime
# import ctypes

# SPI_SETDESKWALLPAPER = 20

# def get_season(month):
#     if month in range(3, 6):
#         return "весна"
#     elif month in range(6, 9):
#         return "лето"
#     elif month in range(9, 12):
#         return "осень"
#     else:
#         return "зима"

# today = datetime.date.today()
# current_month = today.month

# meciz = get_season(current_month)
# print(meciz)



# def change_oboi():

#     if meciz == "зима":
#         ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, "image.jpg" , 0)
#     if meciz == "весна":
#         ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, "image.jpg" , 0)
#     if meciz == "лето":
#         ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, "image.jpg" , 0)
#     if meciz == "осень":
#         ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, "image.jpg" , 0)

# change_oboi()