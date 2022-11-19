import rooms, sys
from room import Room, Direction, Portal

#attemp to move in a direction from the current room


def move(room, dir):
    #print("Dir Test: " + str(dir))
    #check for a matching portal direction
    for m_portal in room.portals:
        #print("Portal Dir: " + str(m_portal))
        #print("Dir Compare: " + str(m_portal.direction))
        if m_portal.direction == dir:
            #print("You exited " + str(dir))
            return rooms.room_from_id(m_portal.destination_id)

    print("Ouch! You bonked into a wall.")
    return room

def quit():
    sys.exit()

def print_help():
    print('''Commands:
    N or North - go north
    S or South - go south
    E or East -  go east
    W or West - go west
    U or Up - go up / climp ladder or rope up
    D or Down - go down / climp ladder or rope down
    H or Help - view commands
    C or Credits - view credits
    Q Quit - quit game
    ''')

def print_credits():
    print('''
    Lead Designer:  Simon
    Technology Consultant:  Simon's Dad
    Inspiration: Zork
    Ideas for rooms: Simon's Mom and Simon's Dad
    ''')

running = True

room_current = rooms.rooms[0]
#print(Direction.NORTH)

while (running):
    print('')
    print(room_current.description)
    if room_current.id != 'B11' or room_current.id != 'D8' or room_current.id != 'EXIT':
        portal_str = 'Exits: '
        for portal in room_current.portals:
            portal_str += portal.exit_str
            if portal != room_current.portals[-1]:
                portal_str += " , "
        print(portal_str)

    if room_current.id == 'EXIT':
        running = False
    else:
        command = input("enter command >")
        command = command.upper()
        if command == 'EXIT':
            running = False
            quit()
        elif command == 'NORTH' or command == 'N':
            room_current = move(room_current, Direction.NORTH)
        elif command == 'SOUTH' or command == 'S':
            room_current = move(room_current, Direction.SOUTH)
        elif command == 'EAST' or command == 'E':
            room_current = move(room_current, Direction.EAST)
        elif command == 'WEST' or command == 'W':
            room_current = move(room_current, Direction.WEST)
        elif command == 'UP' or command == 'U':
            room_current = move(room_current, Direction.UP)
        elif command == 'DOWN' or command == 'D':
            room_current = move(room_current, Direction.DOWN)
        elif command == 'HELP' or command == 'H' or command == '?':
            print_help()
        elif command == 'CREDITS' or command == 'C':
            print_credits()
        elif command == 'QUIT' or command == 'Q':
            running = False
            quit()
        else:
            print("That Is Not A Valid Command.")
