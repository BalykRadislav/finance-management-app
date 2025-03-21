def sum_of_numbers(n):

    if n == 0:
        return 0
    else:
        return n + sum_of_numbers(n - 1)

N = 10 
print(f"Сума чисел від 1 до {N} дорівнює {sum_of_numbers(N)}")

#------------------------------------------------------

def reverse_string(s):

    if len(s) <= 1:
        return s
    return s[-1] + reverse_string(s[:-1])


text = "hello"
print(reverse_string(text))

#------------------------------------------------------

def count_x(s):

    if not s:
        return 0
    
    return (1 if s[0] == 'x' else 0) + count_x(s[1:])


text = "xXxoxoxX"
print(count_x(text))  

