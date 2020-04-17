from karel.stanfordkarel import *

"""
File: MidpointKarel.py
----------------------
When you finish writing it, MidpointKarel should
leave a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.
"""


def main():
    """
    Trying out midpoint
    """
    put_all_beepers()
    collecting_beepers()
    turn_around()
    if front_is_clear():
        move()
        put_beeper()
    if front_is_blocked():
        if no_beepers_present():
            put_beeper()

"""
Dropping all beepers on the line first
"""


def put_all_beepers():
    while front_is_clear():
        put_beeper()
        move()
    if front_is_blocked():
        #put_beeper()
        turn_around()


"""
Starting to collect beepers one by one from the edges.
"""


def collecting_beepers():
    while front_is_clear():
        move()
    if front_is_blocked():
        if beepers_present():
            pick_beeper()                   # Collecting left-most beeper first
        turn_around()
        if front_is_clear():
            move()
    """while beepers_present():
        while front_is_clear():
            move()
        if front_is_blocked():
            pick_beeper()
            turn_around()
            if front_is_clear():
                move()"""
    while beepers_present():
        if front_is_clear():
            move()
        if no_beepers_present():
            turn_around()
            if front_is_clear():
                move()
            if beepers_present():
                pick_beeper()
            move()



def turn_around():
    turn_left()
    turn_left()


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
