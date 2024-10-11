from typing import Dict, NamedTuple, Set, Optional

from BaseClasses import Location
from enum import Enum, IntEnum
from copy import deepcopy

starting_location_id = 119201851000

class LocationCharacter(IntEnum):
    Any = 1
    Moonie = 2
    Cellierues = 3
    Hellevius = 4
    Austra = 5
    Sothis = 6
    Orion = 7


class AstreaLocationData(NamedTuple):
    chapter: int
    battle: int
    difficult: bool = False
    boss: bool = False
    event: bool = False
    character: LocationCharacter = 1

pratice_location_table = {f'Location {x}': x for x in range(1, 60)}

base_location_table ={
    "Tainted Reef Fight 1 - First reward": AstreaLocationData(1,1, False, False),
    "Tainted Reef Fight 1 - Second reward": AstreaLocationData(1,1, False, False),
    "Tainted Reef Fight 2 - First reward": AstreaLocationData(1,2, False, False),
    "Tainted Reef Fight 2 - Second reward": AstreaLocationData(1,2, False, False),
    "Tainted Reef Fight 3 - First reward": AstreaLocationData(1,3, False, False),
    "Tainted Reef Fight 3 - Second reward": AstreaLocationData(1,3, False, False),
    "Tainted Reef Fight 3 - Hard reward": AstreaLocationData(1,3, True, False),
    "Tainted Reef Boss Fight - First reward": AstreaLocationData(1,4, False, True),
    "Tainted Reef Boss Fight - Second reward": AstreaLocationData(1,4, False, True),
    "Tainted Reef Boss Fight - Third reward": AstreaLocationData(1,4, False, True),
    "Astropolis Ruins Fight 1 - First reward": AstreaLocationData(2, 1, False, False),
    "Astropolis Ruins Fight 1 - Second reward": AstreaLocationData(2, 1, False, False),
    "Astropolis Ruins Fight 2 - First reward": AstreaLocationData(2, 2, False, False),
    "Astropolis Ruins Fight 2 - Second reward": AstreaLocationData(2, 2, False, False),
    "Astropolis Ruins Fight 2 - Hard reward": AstreaLocationData(2, 2, True, False),
    "Astropolis Ruins Boss Fight - First reward": AstreaLocationData(2, 3, False, True),
    "Astropolis Ruins Boss Fight - Second reward": AstreaLocationData(2, 3, False, True),
    "Astropolis Ruins Boss Fight - Third reward": AstreaLocationData(2, 3, False, True),
    "Ground Zero Fight 1 - First reward": AstreaLocationData(3, 1, False, False),
    "Ground Zero Fight 1 - Second reward": AstreaLocationData(3, 1, False, False),
    "Ground Zero Fight 1 - Hard reward": AstreaLocationData(3, 1, True, False),
    "Ground Zero Fight 2 - First reward": AstreaLocationData(3, 2, False, False),
    "Ground Zero Fight 2 - Second reward": AstreaLocationData(3, 2, False, False),
    "Ground Zero Fight 2 - Hard reward": AstreaLocationData(3, 2, True, False),
    "Ground Zero Boss Fight - First reward": AstreaLocationData(3, 3, False, True),
    "Ground Zero Boss Fight - Second reward": AstreaLocationData(3, 3, False, True),
    "Ground Zero Boss Fight - Third reward": AstreaLocationData(3, 3, False, True),
}

event_table = {
    "Tainted Reef Boss Victory": AstreaLocationData(1,4),
    "Astropolis Ruins Boss Victory": AstreaLocationData(2,3),
    "Ground Zero Boss Victory": AstreaLocationData(3,3),
    "Astrea Purified": AstreaLocationData(4,2),
}

location_table = base_location_table
for x in range(7):
    name = LocationCharacter(x).name
    for k, v in base_location_table.items():
        key = k + " - " + name
        value = deepcopy(v)
        value.character = x
        location_table[key] = value


location_name_to_id: Dict[str, int] = {name: starting_location_id + index for index, name in enumerate(location_table)}


class AstreaLocation(Location):
    game: str = "Astrea"