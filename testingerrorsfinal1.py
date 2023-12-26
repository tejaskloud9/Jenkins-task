# 2. Write a Python program to get a string made of the first 2 and last 2 characters of a given string. 
# If the string length is less than 2, return the empty string

def get_first_last_chars(input_string)
if len(input_string) < 2:
         return ""
                else:
    return input_string[:2] + input_string[-2:]

# Example usage:
input_str = input("Enter a string: ")
result = get_first_last_chars(input_str);

print("Result:", result)
