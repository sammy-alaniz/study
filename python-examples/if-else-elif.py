def isValid(s):

    stack = []

    mapping = { ")":"(" , "}":"{" , "]":"[" }

    for char in s:
        if char in mapping:
            # how is this if statment working
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)

    return not stack


if __name__ == "__main__":
    #print(isValid("()"))
    
    stack = ['s']
    #top_element = stack.pop() if stack else '#'
    top_element = stack.pop() if None else '#'

    print(top_element)
