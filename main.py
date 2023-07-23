combined = float(input("How much they cost combined: "))
difference = int(input("How much the bat is more expensive than the ball: "))

def solve():
    global combined, difference
    ball = round((combined - difference) / 2, 2)
    bat = round(ball + difference, 2)
    return f"Ball is {ball}, and a bat is {bat}. Together {combined}"




print(solve())





# ball = 0
# bat = ball + 1

# def solve():
#     global ball, bat, combined
#     difference =combined - bat
#     without_difference = round(combined - (combined - bat ), 2)
#     ball = without_difference / 2
#     bat = without_difference / 2 + difference
#     return f"Ball is {ball}, and a bat is {bat}. Together {combined}"

# print(solve())