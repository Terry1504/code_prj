#
# h = t0 + t1 * x
# cost = 1/(2 * m) * SUM{(h - y)^2}
# t0 = t0 - a * 1/m * SUM{(h - y) * 1}
# t1 = t1 - a * 1/m * SUM{(h - y) * x}
#

from datetime import datetime
print("======== START ======== ", datetime.today())

x_train = [1, 2, 3, 4]
y_train = [0, -1, -2, -3]

t0 = 100
t1 = 200
a = 0.01

m = len(x_train)

i = 1

# - loop xxx times
#
# print("loop 100000 times")
# while i < 100000:
#
# - or loop until cost < xxx
#
# print("loop until cost < 0.000001")
# cost = 1
# while cost > 0.00001:
#
# - or until parameter converge
#
print("loop parameter converge, < 0.000001 ")
epsilon = 0.000001
reach_converge = False
while not reach_converge:
    t0_partial_derivative = 0
    t1_partial_derivative = 0

    for j in range(m):
        h = t0 + t1 * x_train[j]
        variance = h - y_train[j]
        t0_partial_derivative = t0_partial_derivative + variance * 1
        t1_partial_derivative = t1_partial_derivative + variance * x_train[j]

    t0_diff = a * 1/m * t0_partial_derivative
    t0 = t0 - t0_diff
    t1_diff = a * 1/m * t1_partial_derivative
    t1 = t1 - t1_diff

    if (abs(t0_diff) < epsilon) and (abs(t1_diff) < epsilon) :
        reach_converge = True

    cost_sum = 0
    for j in range(m):
        h = t0 + t1 * x_train[j]
        variance = h - y_train[j]
        cost_sum = cost_sum + variance * variance
    cost = 1/(2 * m) * cost_sum

    i = i + 1

print("after loop ", i, " times", "cost is ", cost, "t0, t1: ", t0, t1)

print("======== END ======== ", datetime.today())

'''
======== START ========  2017-12-12 18:36:25.914264
loop 100000 times
after loop  100000  times cost is  6.656013887802287e-28 t0, t1:  1.0000000000000888 -1.000000000000031
======== END ========  2017-12-12 18:36:26.727089


======== START ========  2017-12-12 18:37:35.823916
loop until cost < 0.000001
after loop  5227  times cost is  9.976203192244169e-06 t0, t1:  1.0109300816032205 -1.0037175606323205
======== END ========  2017-12-12 18:37:35.869657


======== START ========  2017-12-12 18:51:44.737707
loop parameter converge, < 0.000001
after loop  7094  times cost is  3.71199182916524e-08 t0, t1:  1.0006667212035536 -1.000226766513649
======== END ========  2017-12-12 18:51:44.801428

'''
