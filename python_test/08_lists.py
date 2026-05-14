# Topic = Lists

# 1) solve the bug:
'''
nums = [1, 2, 3, 4, 5, 6]
for n in nums:
    if n % 2 == 0:
        nums.remove(n)
print(nums)

bug = modifying a lst while iterating over it with a for loop
'''

# solution
nums = [1, 2, 3, 4, 5, 6]
odd = [n for n in nums if n%2 != 0]
print(odd)


# 2) write a function:
def merge_sorted(a: list, b: list) -> list:
    result = []
    i = 0
    j = 0

    while i<len(a) and j<len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    
    result.extend(a[i:])
    result.extend(b[j:])

    return result

a = [5, 6, 7]
b = [1, 2, 3, 4]
print(merge_sorted(a, b))
