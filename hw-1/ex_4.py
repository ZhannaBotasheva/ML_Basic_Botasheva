import numpy as np

def cal_euclidean(a, b):    
    s_sq_difference = 0
    for a_i,b_i in zip(a,b):
        s_sq_difference += (a_i - b_i)**2
        distance = s_sq_difference**0.5
    return distance


def cal_manhattan(a, b): 
    distance = 0
    for a_i, b_i in zip(a,b):
        distance += abs(a_i - b_i)
    return distance


from scipy import spatial

def cal_cosine(a, b):
    distance = 1 - spatial.distance.cosine(a, b)
    return distance  

a = np.random.randint(-10, 10, size=10)
b = np.random.randint(-10, 10, size=10)
print(cal_euclidean(a, b))
print(cal_manhattan(a, b))
print(cal_cosine(a, b))