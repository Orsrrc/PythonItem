
def two_number_max(a, b):
    if a > b:
        return a
    if b > a:
        return b

def three_number_max(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

print(two_number_max(5,6))
print(three_number_max(5,6,7))