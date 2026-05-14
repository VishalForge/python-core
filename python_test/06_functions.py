# Topic = Functions

# 1) Solve the bug:
def add_item(item, collection=None):   # The bug was that an empty lst was defined at the func definition time which leds to the same lst being used for every call
    if collection is None:
        collection = []
    collection.append(item)
    return collection

print(add_item("a"))
print(add_item("b"))
print(add_item("c"))


# 2) Predict the output:
x = "global"

def outer():
    x = "outer"
    def inner():
        print(x)
    inner() 

outer()   # outer
print(x)  # global


# 3) write a code:
def flatten(lst):
    '''Recursively flattens a list of any depth
    and returns a flattened lst containing all elements'''
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

a = [1, [2, [3, 4]], 5]
print(flatten(a))