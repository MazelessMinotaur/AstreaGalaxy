from typing import Dict, NamedTuple, Set, Optional
from BaseClasses import Item, ItemClassification
from enum import Enum, IntEnum

from worlds.astrea.Locations import LocationCharacter

starting_item_id = 119201851000

class AstreaItemClassification(IntEnum):
    Dice = 1
    StarShards = 2
    Blessing = 3
    Forge = 4
    DuplicateDice = 5
    Event = 11

class AstreaItemData(NamedTuple):
    astrea_classification: AstreaItemClassification
    archipelago_classification: ItemClassification
    pool_amount: int
    id_offset: int
    character: LocationCharacter = 1


class AstreaItem(Item):
    game = "Astrea"

testing_item_table = {
    "77 Star Shards": AstreaItemData(AstreaItemClassification.StarShards, ItemClassification.filler, 1, 0), # dumb testing
    "Epic Dice Choice": AstreaItemData(AstreaItemClassification.Dice, ItemClassification.useful, 5, 1),
    "Standard Dice Choice": AstreaItemData(AstreaItemClassification.Dice, ItemClassification.filler, 5, 2), # this is fixed?
    "Regular Blessing": AstreaItemData(AstreaItemClassification.Blessing, ItemClassification.progression, 6, 3),
    "BlackHole Blessing": AstreaItemData(AstreaItemClassification.Blessing, ItemClassification.useful, 4, 4),
    "Duplicate Dice": AstreaItemData(AstreaItemClassification.DuplicateDice, ItemClassification.filler, 2, 5),
    "Forge Draw": AstreaItemData(AstreaItemClassification.Forge, ItemClassification.filler, 2, 6),
}

base_item_table = {
    "Epic Dice Choice": AstreaItemData(AstreaItemClassification.Dice, ItemClassification.useful, 3, 1),
    "Standard Dice Choice": AstreaItemData(AstreaItemClassification.Dice, ItemClassification.filler, 20, 2),
    "Regular Blessing": AstreaItemData(AstreaItemClassification.Blessing, ItemClassification.useful, 4, 3),
    "BlackHole Blessing": AstreaItemData(AstreaItemClassification.Blessing, ItemClassification.useful, 3, 4),
    "Sentinel": AstreaItemData(AstreaItemClassification.Blessing, ItemClassification.useful, 3, 4),
}

item_table = testing_item_table

item_name_to_id: Dict[str, int] = {name: starting_item_id + data.id_offset for name, data in item_table.items()}
