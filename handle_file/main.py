from handle_file import HandleFile

path = "numbers.txt"
numbers = HandleFile().read_formatted_numbers(path)
print(numbers)
total_sum = sum(numbers)
print("\nTotal sum: " + str(total_sum))