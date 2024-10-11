import typing
from dataclasses import dataclass

from Options import TextChoice, Range, Toggle, PerGameCommonOptions, ItemSet, OptionSet, Choice


class DoubleStarShards(Toggle):
    """"If you receive double gold"""
    display_name = "Double star shards"
    option_true = 1
    option_false = 0
    default = 0

class WinsRequire(Range):
    """Number of wins required. Must be less than or equal to number of player Oracles"""
    display_name = "Wins required"
    min_value = 1
    max_value = 6
    default = 1

class DifficultFightRewards(Choice):
    """
    Items that will be placed as the bonus reward for difficult fights

    As these fights are optional, if these are skipped the items in them will not be sent until either a win
    or restarting the run and returning to the fight
    """
    display_name = "Difficult fights rewards"
    option_any = 0
    option_filler = 1
    option_progression = 2
    option_local = 3
    option_none = 4 #difficult fights grant no bonus
    option_shards = 5 # difficult fights will grant bonus shards (in addition to the existing bonus)

class RewardPoolPowerLevel(Choice):
    """
    How good the players items will be.

    - **Standard** Items will closely match what a normal run of Astrea will be.
    - **Powerful** Item pool will grant more items like epic dice and blessings, and fewer generic dice
    - **Weaker** Item pool will grant less powerful items
    """
    option_standard = 1

class RewardPoolAmount(Choice):
    """
    How many rewards are given after each fight.
    More rewards means each fight will have more locations, and more of your rewards will be across the AP
    More rewards will likely make the game easier as you'll receive more

    - **Stanard** Reward number will match base game (2 for a normal fight, 3 for difficult, ect)
    - **Extra** Rewards
    """
    option_standard = 1

class PlayerOracles(OptionSet):
    """Which oracles are playable in the world.
     """
    display_name = "Player Oracles"
    # option_true = 1
    # option_false = 0
    default = {}
    valid_keys = [""] #fill in once I have the names right

class SharedItemPool(Toggle):
    """
    If items are shared across all oracles for a multi run world

    This will make earlier runs more difficult and later runs easier
    """
    display_name = "Shared Reward Pool"

class RewardOrder(Choice):
    """When receiving items, if the order received changes.
    As rewards are granted post battle, multiple rewards are often gained at once.

    - **Received**: Items are gained in the order they were sent/received.
    - **Benificial**: Items are gained in an order that is more useful.
    e.g. if receiving a forge and a duplicate, the forge will be given before duplication
    - **Random**: When receiving items, they are shuffled randomly
    """
    display_name = "Reward Order"
    option_received: 0
    option_benifical: 1
    option_random: 2

class ArchipelagoDiePool(Choice):
    option_disabled = 0
    option_shared_pool = 1
    option_unique_oracle_pool = 2


class MaxChoiceRewards(Range):
    """
    As rewards are gained post battle, it's possible to receive a large number of rewards at once.
    This is especially true if requiring multiple wins, having to restart, or playing async.
    Reducing this can be useful to not have to start each run with a ton of choices
    Or if you want to avoid getting too powerful after the very first battle

    This does not have any validation regarding the total items,
    so if this is set too low its possible items won't be received at all

    This does not consider rewards without a choice (star shards, for example)

    Setting to 0 will have no limit
    """
    default = 10
    display_name = "Max Choice Rewards"
    min_value = 0
    max_value = 99

@dataclass
class AstreaOptions(PerGameCommonOptions):
    double_shards: DoubleStarShards
    wins_required: WinsRequire
    player_oracles: PlayerOracles
    shared_item_pool: SharedItemPool
    reward_order: RewardOrder
    max_choice_rewards: MaxChoiceRewards
