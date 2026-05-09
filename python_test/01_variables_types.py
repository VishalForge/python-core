# Topic = Variables and Data Types
'''
 Test = 1) Predict before running
        2) solve Bug
        3) write code
'''

#---My Answers---
# 1)
print(type(10/2))     #output = float
print(type(10//2))    #output = int
print(bool(0))        #output = false
print(bool("False"))  #output = True

# 2)
'''
user_input = "3.14"
result = int(user_input)
print(result)
'''

# In this code, the python will raise ValueError because first, we have to convert the string into float and then the int
user_input = "3.14"
result = int(float(user_input))
print(result)

# 3)
def describe(x):
    print(f"value: {x}, Type: {type(x)}, {bool(x)}")

describe(0)
describe("")
describe([])
describe(42)
describe(None)
describe("False")