from stacks import Stack
#Parameters: stack is the Stack() object and input_str is the string I want to reverse)



def reverse_string(stack, input_string):
    """reverse the order of a string using a stack"""
    #loop through a string and push contents character by character
    # onto a stack- pop() each character back into a reversed string

    for i in range(len(input_string)):
        stack.push(input_string[i])

        #print (stack.get_stack())
        reverse_str = ""
        # check if stack is empty first, if its not empty pop and add to the empty string
    while not stack.is_empty():
        reverse_str += stack.pop()
    return reverse_str


stack = Stack()
input_string = "andrea"
print(reverse_string(stack, input_string))



def reverse(string):
    string = string[::-1]
    return string

string = "aleafaR"
string = reverse(string)
print("reversed string is " + string)




