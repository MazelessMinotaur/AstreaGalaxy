import string

from BaseClasses import Entrance, Item, ItemClassification, Location, MultiWorld, Region, Tutorial
from .Items import item_table, AstreaItem, AstreaItemData, item_name_to_id
from .Locations import location_table, AstreaLocation, location_name_to_id
from .Regions import create_regions
from .options import AstreaOptions
from ..AutoWorld import WebWorld, World


class AstreaWeb(WebWorld):
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up Slay the Spire for Archipelago. "
        "This guide covers single-player, multiworld, and related software.",
        "English",
        "slay-the-spire_en.md",
        "slay-the-spire/en",
        ["Phar"]
    )]


starting_item_id = 119201851000


class AstreaWorld(World):
    """
    Astrea is a DICE-deck-building roguelike that flips the script on deckbuilders by using dice instead of cards
     and an unique dual “damage” system: Purification vs Corruption.
     Build a dice pool strong enough to purify Astrea's out-of-control corruption and save the Star System.
    """

    options_dataclass = AstreaOptions
    options: AstreaOptions
    game = "Astrea"
    topology_present = False
    web = AstreaWeb()
    required_client_version = (0, 5, 0)

    item_table = item_table
    item_name_to_id = item_name_to_id
    location_name_to_id = location_name_to_id

    def create_item(self, name: string, item_data: AstreaItemData = None) -> AstreaItem:
        return AstreaItem(name, item_data.archipelago_classification, item_data.id_offset + starting_item_id, self.player)

    def create_items(self):
        # Fill out our pool with our items from item_pool, assuming 1 item if not present in item_pool
        pool = []
        for name, data in item_table.items():
            for _ in range(data.pool_amount):
                item = self.create_item(name, data)
                pool.append(item)

        self.multiworld.itempool += pool

    def set_rules(self):
        return

    def create_regions(self):
        create_regions(self.multiworld, self.player)

    def fill_slot_data(self) -> dict:
        slot_data = {
            'seed': "".join(self.random.choice(string.ascii_letters) for i in range(16))
        }
        return slot_data

    def get_filler_item_name(self) -> str:
        return self.random.choice(["77 Star Shards"])


def create_region(world: MultiWorld, player: int, name: str, locations=None, exits=None):
    ret = Region(name, player, world)
    if locations:
        for location in locations:
            location_data= location_table.get(location, 0)
            location_id = location_name_to_id[location]
            location = AstreaLocation(player, location, location_id, ret)
            ret.locations.append(location)
    if exits:
        for exit in exits:
            ret.exits.append(Entrance(player, exit, ret))

    return ret

