# count = len
# list = [1,2,2,2,2]
# print(count(list))


string_methods={
    'upper' : str.upper,
    'lower' : str.lower,
}
a= input("Enter a choice upper or lower: ")
b= input("Enter your string: ")
print(string_methods[a](b))
