# כתוב פונקציה שמחזירה את הסכום של המספרים מאחד עד 100 ללא שימוש בלולאה
# sum to 100 without loops

def sum_to_hundred(): # main function
    return recursion(0, destination=100)


def recursion(n, destination = 100):
    return (n if n == destination else n + recursion(n+1, destination=destination))


#TEST
print(sum_to_hundred()) # Output: 5050