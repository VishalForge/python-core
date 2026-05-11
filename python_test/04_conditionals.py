# Topic = Conditionals

# 1) Predict the output
x = 15
label = "big" if x > 10 else "small"
print(label)     # big

y = []
if y:
    print("has items")
else:
    print("empty")   # empty

z = None
print("exists" if z is not None else "nothing")   # nothing



# 2) write a function:
def grade(score: int) -> str:
    if not isinstance(score, int) or score < 0 or score > 100:
        raise ValueError("Invalid score")
    
    match score:
        case s if s >= 90:
            return "A"
        case s if s >=75:
            return "B"
        case s if s >= 60:
            return "C"
        case _:
            return "F"

print(grade(100))
print(grade(101))
print(grade(1))
