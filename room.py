from enum import Enum


class Direction(Enum):
    NORTH = 0
    SOUTH = 1
    EAST = 2
    WEST = 3
    UP = 4
    DOWN = 5
    PULL = 6

# Class for Room Portals - door / hallway / stairs / teleporter


class Portal:
    def __init__(self, direction, destination_id):
        self.direction = direction
        self.destination_id = destination_id

    def __str__(self):
        return "[" + str(self.direction) + " -> " + str(self.destination_id) + "]"

    # Direction to walk to go through portal - east, west, north, south, up, down / e, w, n, s, u, d
    @property
    def direction(self):
        return self.__direction

    @direction.setter
    def direction(self, value):
        self.__direction = value

    # Room ID that the portal goes too
    @property
    def destination_id(self):
        return self.__destination_id

    @destination_id.setter
    def destination_id(self, value):
        self.__destination_id = value

    @property
    def exit_str(self):
        if self.direction == Direction.NORTH:
            return "(N)orth"
        elif self.direction == Direction.EAST:
            return "(E)ast"
        elif self.direction == Direction.WEST:
            return "(W)est"
        elif self.direction == Direction.SOUTH:
            return "(S)outh"
        elif self.direction == Direction.UP:
            return "(U)p"
        elif self.direction == Direction.DOWN:
            return "(D)own"

class Room:
    def __init__(self, id, description, portals, items):
        self.__id = id
        self.description = description
        self.portals = portals
        self.items = items

    def __str__(self):
        return str(self.id) + ", " + str(self.description) + ", Exits:" + self.portal_list() + ", Items: " + str(self.items) + "\n"
    # Room ID Code - Has to be unique

    @property
    def id(self):
        return self.__id

    # Short Room Name
    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, value):
        self.__description = value


    @property
    def portals(self):
        return self.__portals

    @portals.setter
    def portals(self, value):
        self.__portals = value

    # returns a portal if the room contains portal in the direction else None
    def portal_check(self, dir_check):
        print("Check Dir: " + str(dir_check))
        for m_portal in self.__portals:
            print("Portal Dir: " + str(m_portal))
            if m_portal.direction == dir_check:
                return m_portal
        #print("No Portal")
        return None

    @property
    def items(self):
        return self.__items

    @items.setter
    def items(self, value):
        self.__items = value

    def portal_list(self):
        portal_str = ''
        for portal in self.portals:
            portal_str = portal_str + " " + str(portal)
        return portal_str
