# -*- coding: utf-8 -*-
#定义cars为100
cars = 100
#定义 每车辆的空间为4 下划线"_"当空格使用，为了更好的表达意思。
space_in_a_car = 4.0
#定义司机人数
drivers = 30
#定义乘客人数
passengers = 90
#不到运行的车数等于车数减去司机数，定义加下运算
cars_not_driven = cars - drivers
#能出动的车等于司机数
cars_driven = drivers
#载客能力等于出动车数乘以车内空间数
carpool_capacity = cars_driven * space_in_a_car
#每辆车平均载客数等于乘客数除以载客能力
average_passengers_per_car = passengers / cars_driven

#打印
print("There are ", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be",cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers,"to carpool today.")
print("We need to put about",average_passengers_per_car, "in each car.")
