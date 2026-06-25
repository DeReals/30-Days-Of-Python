import math

#Exercise 1
print("David Ogunbanjo")
print("Ogunbanjo")
print("USA")
print("I am enjoying 30 days of python")

#Exercise 2: Find an Euclidean distance between (2,3) and (10,8)
sum_total = (2-10)**2 + (3-8)**2
print(math.sqrt((sum_total)))

# update exercise 3 to take in any number
def EuclidenDistance(p1, p2, q1, q2):
    sum_total = (p1-q1)**2 + (p2-q2)**2
    print(math.sqrt((sum_total)))

EuclidenDistance(2,3,10,8)