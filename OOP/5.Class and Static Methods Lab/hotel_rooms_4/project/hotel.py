from typing import List

from room import Room


class Hotel:
    def __init__(self,name:str):
        self.name = name
        self.rooms:List[Room] = []
    
    @property
    def guests(self):
        return sum([g.guests for g in self.rooms])

    @classmethod
    def from_stars(cls,stars_count:int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self,room:Room)->None:
        self.rooms.append(room)

    def take_room(self,room_number,people):
        room = [rn for rn in self.rooms if rn.number == room_number][0]
        room.take_room(people)


    def free_room(self,room_number):
        room = [rn for rn in self.rooms if rn.number == room_number][0]
        room.free_room()

    def status(self):
        return  f"Hotel {self.name} has {self.guests} total guests\n"\
                f"Free rooms: {', '.join([str(fr.number) for fr in self.rooms if not fr.is_taken])}\n"\
                f"Taken rooms: {', '.join([str(fr.number) for fr in self.rooms if fr.is_taken])}"




