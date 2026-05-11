# Topic = Loops

# 1) Predict the output
for i in range(1, 10):
    if i % 3 == 0:
        continue    # It'll skip the 3 and continue to the next iterable
    if i > 7:
        break       # the loop will exist when this condition will meet
    print(i, end=" ")

print()   # To add a new line between the 2 loops

# 2) write the code using enumerate and zip
names = ["Alice", "Bob", "Carol"]
scores = [88, 72, 95]

for i, (name, score) in enumerate(zip(names, scores), start=1):
    label = "Pass" if score >= 75 else "Fail"
    print(f"{i}. {name}: {score} -> {label}")



# 3) write a code using while loop:
total = 0
count = 0
while True:
    try:
        num = int(input("Enter your number (or negative number to exit): "))
        if num < 0: break

        total += num
        count += 1
    
    except ValueError:
        continue

print(f"Sum of all the numbers: {total}")
print(f"Count of all the valid numbers: {count}")