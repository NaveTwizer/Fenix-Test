# כתוב פונקציה המקבלת מערך דו מימדי המייצג לוח ומחזירה את המנצח, אם יש. אחרת החזר שקר

# Write a function to find the winner in Tic Tac Toe (2D list board)
def tic_tac_toe(lst1):
    positions_groups = (
    [[(x, y) for y in range(3)] for x in range(3)] + # horizontals
    [[(x, y) for x in range(3)] for y in range(3)] + # verticals
    [[(d, d) for d in range(3)]] + # diagonal from top-left to bottom-right
    [[(2-d, d) for d in range(3)]] # diagonal from top-right to bottom-left
    )
    for positions in positions_groups:
        values = [lst1[x][y] for (x, y) in positions]
        if len(set(values)) == 1 and values[0]:
            return values[0]
    return False # No winner