__all__ = [
    "common_item",
    "priority",
    "sum_priorities",
    "generate_group",
    "find_group_badge",
    "sum_badge_priorities",
]

from typing import Generator


def common_item(
    sample: str,  # a sample rucksack containing items from 2 compartments
) -> str:
    """Find the common item in the 2 compartments"""
    half = len(sample) // 2
    return list(set(sample[:half]).intersection(set(sample[half:])))[0]


def priority(
    item: str,  # return the priority of an item (single char)
) -> int:
    """Return the priority of an item"""
    if item.islower():
        return ord(item) - ord("a") + 1
    return ord(item) - ord("A") + 27


def sum_priorities(
    inputs: list[str],  # a list of rucksacks, each containing 2 compartments
) -> int:
    """Return the sum of priorities of the common item for all the rucksacks"""
    return sum([priority(common_item(o)) for o in inputs])


def generate_group(
    inputs: list[str],  # a list of rucksacks
    sz: int = 3,  # group size
) -> Generator[list[str], None, None]:
    """Generate a subsetted list of rucksacks of size sz"""
    for i in range(0, len(inputs), sz):
        yield inputs[i : i + sz]


def find_group_badge(
    group: list[str],  # group of rucksacks
) -> str:
    """Return the common item for the group of rucksacks"""
    return list(set.intersection(*[set(o) for o in group]))[0]


def sum_badge_priorities(
    inputs: list[str],  # list of rucksacks
    sz: int = 3,  # group size
) -> int:
    """Return the sum of the priorities of the group badges for all inputs"""
    return sum(
        [priority(find_group_badge(group)) for group in generate_group(inputs, sz=sz)]
    )
