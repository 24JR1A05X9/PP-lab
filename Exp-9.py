str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

if len(str1) != len(str2):
    print("The strings are not of the same length. Program exiting.")
else:  
     result = ""

    for i in range(len(str1)):
        result += str1[i] + str2[i]

    print("Alternated string:", result)
