

# Find the 2 neighbor numbers in list that makes the biggest multiplication in the list

def neighbor_mul(lst):
    return max([
        lst[idx] * lst[idx + 1] for idx in range( len(lst) - 1 )
    ])



# TESTS
lst1 = [1, 2, 3]
print(neighbor_mul(lst1)) # Output: 6 (2 * 3)

lst2 = [-23,-5, 99, -27, 329, -2, 7] 
print(neighbor_mul(lst2)) # Output: 115 (-23 * -5)