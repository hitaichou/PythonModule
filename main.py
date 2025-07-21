#programa principal
import math_operations
from math_operations import multiply, divide

import string_utils

print(math_operations.sum(5, 3))
print(math_operations.subtract(5, 3))

#usando o from "função" import, é possível chamar diretamente as funções
print(multiply(5, 3)) 
print(divide(5, 3))  


print(string_utils.capitalize("hello"))
print(string_utils.reverse_string("python"))
print(string_utils.count("apple"))

