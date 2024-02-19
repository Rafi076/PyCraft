#Import in python is the process of loading code from python module into the curresnt script.
# This allow you  to use differrent function and variable defined in the module in ypur current script,as well as any
# additional modules that the imported module may depand on.#
import math
result = math.sqrt(9)
print(result)

#from Keyword :
# you can import specific function or variavle from the modulse using from keyword.
# for example,to import onlt the sqrt function from the math module,you would write:#
from math import sqrt,pi
result = sqrt(9)
print(result)
print(round(sqrt(pi)),2)


#its also possible to import all function and variables from a module using the * wildcad
# however,this is generally not recommanded as it can kead a confuse and make it harder to unnderstand
# where specific function and variable are coming from.#
from math import *
print(dir(math))

# imported function-->
# ['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan',
# 'atan2', 'atanh', 'cbrt', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 
# 'erf', 'erfc', 'exp', 'exp2', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 
# 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'lcm', 
# 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'nextafter', 
# 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 
# 'tan', 'tanh', 'tau', 'trunc', 'ulp','perm', 'pi', 'pow',] #


# importing specific portion from rafi file#
from Rafi import welcome,Rafi
welcome() ## which is a function
print(Rafi) # which is a variable