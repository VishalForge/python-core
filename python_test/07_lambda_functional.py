# Topic = Lambda, Map, Filter, Reduce

# 1) Predict the output:
from functools import reduce

nums = [1, 2, 3, 4, 5]

result1 = list(map(lambda x: x * 2, filter(lambda x: x % 2 != 0, nums)))
result2 = reduce(lambda acc, x: acc * x, nums, 1)

print(result1)  # Python evaluates from the innermost function outward, so it'll first filter all the odd no. and then give squares of those
print(result2)  # This will give the product after multiplying all the numbers in the lst



# 2) write a code:
students = [{"name" : "A", "score" : 88}, {"name": "B", "score" : 55}, {"name" : "C", "score" : 72}]

sorted_students = sorted(students, key=lambda x: x["score"], reverse=True)
passing_students = list(filter(lambda x: x["score"] >= 60, students))
names = list(map(lambda x: x["name"], passing_students))

print(sorted_students)
print(passing_students)
print(names)