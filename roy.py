import numpy as np

 
original_array = np.linspace(0, 9, 10, dtype=int)
print("Original Array:")
print(original_array)


modified_array = np.where(original_array % 2 != 0, -1, original_array)
print("\nModified Array (odd numbers replaced with -1):")
print(modified_array)

reshaped_array = original_array.reshape(2, 5)
print("\nReshaped Array (2 rows):")
print(reshaped_array)


even_sum = sum(x for x in original_array if x % 2 == 0)
print("\nSum of even elements in original array:", even_sum)
