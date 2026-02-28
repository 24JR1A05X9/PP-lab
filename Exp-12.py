input_string = input("Enter a string: ")

split_result = input_string.split()
join_result = "-".join(split_result)
result_dict = {
    "original_string": input_string,
    "split_output": split_result,
    "joined_output": join_result
}
print("\nDictionary Output:")
for key, value in result_dict.items():
    print(f"{key}: {value}")
