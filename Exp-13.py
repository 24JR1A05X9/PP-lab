str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

if len(str1) != len(str2):
    print("The strings are not of the same length.")
else:
    result = "".join(a + b for a, b in zip(str1, str2))
    print("Alternated string:", result)
