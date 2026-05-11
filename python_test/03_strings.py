# Topic = Strings

# 1) What does each line print
s = "Machine Learning"

print(s[8])     # It will print string from 0 to 7 index
print(s[-8:])   # It will print string slice from L to the last index position -1
print(s[::2])   # It will follow start, stop(exclusive) and step
print(s[::-1])  # It will reverse the string
print(s.replace("Learning", "Reliability").upper())  # It will replace learning with reliability and apply upper func


# 2) Solve the bug

sentence = "ML systems fail silently"
words = sentence.split()
words.reverse()           # It was just missing the parenthesis in the reverse function, so without them it was just refering to the func instead of calling
result = " ".join(words)
print(result)


# 3) Write a func:
def clean_and_format(text: str) -> str:
    result = text.strip().replace("  ", " ").title()
    return(f"Cleaned: {result} {len(result)} chars")

print(clean_and_format("  ML systems fail silently!"))
