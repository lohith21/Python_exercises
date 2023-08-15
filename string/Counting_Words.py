def keyword(string):
    count =0
    ## counting the length using loop
    for i in string:
        count = count + 1
    print(count)
### using single built-in length function
    print(len(string))


keyword("Lohith Ujjannappa")

## Second Example

def string_length(str1):
    count = 0
    for char in str1:
        count += 1
    return count
print(string_length('w3resource.com'))