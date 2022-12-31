import numpy as np

my_array = np.random.rand(100)
print(np.max(my_array), np.min(my_array))
print(my_array)


my_array = np.random.randint(0, 50, size = (5,6))
selected_column = np.max(my_array, 0)
print('Shape: ',my_array.shape)
print('Array')
print(my_array)
print(selected_column)


def get_unique_rows(X):
    from itertools import chain
    X_unique = list(set(chain(*X)))
    return X_unique
    
    
X = np.random.randint(4, 6, size=(10,3))
print(X)
print(get_unique_rows(X))
