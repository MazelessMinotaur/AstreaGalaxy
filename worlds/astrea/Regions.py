

def create_regions(world, player: int):
    from . import create_region
    from .Locations import location_table

    # arr = []
    # locs = list(location_table.keys())
    # chunk_size = len(locs)
    #
    # for i in range (3):
    #     arr.append(locs[i*chunk_size:(i+1) * chunk_size])
    #
    # arr.append(locs[3*chunk_size:])

    locations = (location for location in location_table)

    world.regions += [
        create_region(world, player, 'Menu', None, ['C1']),
        create_region(world, player, 'Chapter 1', locations, ['C2']),
        create_region(world, player, 'Chapter 2', None, ['C3']),
        create_region(world, player, 'Chapter 3', None, ['H']),
        create_region(world, player, 'Heart', None)
    ]

    world.get_entrance('C1', player).connect(world.get_region('Chapter 1', player))
    world.get_entrance('C2', player).connect(world.get_region('Chapter 2', player))
    world.get_entrance('C3', player).connect(world.get_region('Chapter 3', player))
    world.get_entrance('H', player).connect(world.get_region('Heart', player))