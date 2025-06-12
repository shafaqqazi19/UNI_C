#write a program to reverse an array using the stack data structure 
def reverse_array_with_stack(arr):
    stack = []

    # Push all elements onto the stack
    for item in arr:
        stack.append(item)

    # Pop all elements back into the array
    for i in range(len(arr)):
        arr[i] = stack.pop()

    return arr

# Example usage
input_array = [10, 20, 30, 40, 50]
print("Original array:", input_array)

reversed_array = reverse_array_with_stack(input_array)
print("Reversed array:", reversed_array)




#OUTPUT

Original array: [10, 20, 30, 40, 50]
Reversed array: [50, 40, 30, 20, 10]




#write program to match the parenthesess stored in  a string  using  stack data structure

def is_parentheses_balanced(expression):
    stack = []
    # Dictionary to hold matching pairs
    matching_pairs = {')': '(', '}': '{', ']': '['}

    for char in expression:
        # Push opening brackets onto stack
        if char in '({[':
            stack.append(char)
        # Check matching closing brackets
        elif char in ')}]':
            if not stack or stack[-1] != matching_pairs[char]:
                return False
            stack.pop()

    # If stack is empty at the end, all brackets matched
    return len(stack) == 0

# Example usage
test_str = "{ [ ( ) ] ( ) }"
print("Expression:", test_str)
result = is_parentheses_balanced(test_str)
print("Balanced:" if result else "Not Balanced")



Expression: { [ ( ) ] ( ) }
Balanced:
     
     
     
     
     
     
     
     




#write a program to calculate the sum of integer elements in an integer array by implementing  arecursive sum method or a function

def recursive_sum(arr, index=0):
    # Base case: if index reaches end of array
    if index == len(arr):
        return 0
    # Recursive case: current element + sum of rest
    return arr[index] + recursive_sum(arr, index + 1)

# Example usage
numbers = [5, 10, 15, 20]
print("Array:", numbers)

total = recursive_sum(numbers)
print("Sum of elements:", total)




