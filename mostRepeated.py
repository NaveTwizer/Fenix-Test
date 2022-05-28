# פונקציה המחזירה את האות שמופיעה הכי הרבה במחרוזת
# Find most repeated char in string
def mostRepeated(str1):
    all = dict()
    for char in str1:
        if char in all: # התו נמצא כבר במילונית
            all[char] += 1
        else:
            all[char] = 1 # הופעה ראשונה של תו
    return max(all, key = all.get)

str1 = input('Enter your string: ')
print(f'Most repeated character in {str1}: {mostRepeated(str1)}')