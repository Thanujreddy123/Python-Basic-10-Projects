def right_turn():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if right_is_clear():
        right_turn()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
        
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
