


# Find the youngest sibling from a given dictionary of { name : age}

def find(dict1: dict):
    # my solution
    return min(
        dict1, key=dict1.get
    )



# TEST

values = {
    "Nave" : 17,
    "Old guy": 69,
    "Youngest" : 5,
    "Mom" : 57
}
print(find(values)) # Output: Youngest
