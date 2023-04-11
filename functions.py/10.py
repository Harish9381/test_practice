#Given a string, return a list containing the characters of the string. If a character in the string is a space or a digit greater than 5, remove them and do not include them in the array. Note: the initial code in the editor uses tabs for indentation. Don't mix it with spaces. 
# Examples: 
# 	Input: "my string" 
# 	Output: ["m","y","s","t","r","i","n","g"] 
# 	Input: "5 dollar" 
# 	Output: ["5","d","o","l","l","a","r"] 
# 	Input: "6 cents" 
# 	Output: ["c","e","n","t","s"]

def filter_string(s):
    filtered_list = []
    for char in s:
        if char != ' ' and (not char.isdigit() or int(char) <= 5):
            filtered_list.append(char)
    return filtered_list
s1 = "my string"
result1 = filter_string(s1)
print(result1)  
s2 = "5 dollar"
result2 = filter_string(s2)
print(result2) 

s3 = "6 cents"
result3 = filter_string(s3)
print(result3)  
