from typing import Dict, NamedTuple, Set, Optional

from BaseClasses import Location
starting_location_id = 119201851000

class AstreaLocationData(NamedTuple):
    chapter: int
    battle: int
    difficult: bool
    boss: bool


pratice_location_table = {f'Location {x}': x for x in range(1, 60)}


location_table ={
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

location_name_to_id: Dict[str, int] = {name: starting_location_id + index for index, name in enumerate(location_table)}


class AstreaLocation(Location):
    game: str = "Astrea"