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
}

location_name_to_id: Dict[str, int] = {name: starting_location_id + index for index, name in enumerate(location_table)}


class AstreaLocation(Location):
    game: str = "Astrea"