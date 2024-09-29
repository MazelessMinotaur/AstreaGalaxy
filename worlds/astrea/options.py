import typing
from dataclasses import dataclass

from Options import TextChoice, Range, Toggle, PerGameCommonOptions

class DoubleStarShards(Toggle):
    """"If you receive double gold"""
    display_name = "Double star shards"
    option_true = 1
    option_false = 0
    default = 0

@dataclass
class AstreaOptions(PerGameCommonOptions):
    double_shards: DoubleStarShards