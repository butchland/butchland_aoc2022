__all__ = [
    "get_range",
    "get_assign_ranges",
    "contains",
    "contains_each_other",
    "get_overlapping",
    "partly_contains",
    "partly_or_fully_contains_each_other",
    "get_partly_overlapping"
]

# day4


def get_range(
        assgn:str, # a range of sections split by a dash(-)
    ) -> range:
    """Return a range object covering the range assignment"""
    ranges = [int(o) for o in assgn.split("-")]
    assert len(ranges) == 2
    return range(*ranges)


def get_assign_ranges(
        sample: str, # a set of assignments for a pair of elves
    ) -> list[range]:
    """Return a list of range assignments, one each for a pair of elves"""
    assgns = sample.split(",")
    assert len(assgns) == 2
    return [get_range(assgn) for assgn in assgns]


def contains(
        r1:range, # a range to check
        r2:range, # the range it contains or not
    ) -> bool:
    """Returns whether the first range contains the other range"""
    return r1.start <= r2.start and r1.stop >= r2.stop


def contains_each_other(
        r1:range, # a range to check
        r2:range, # another range 
    ) -> bool:
    """Returns whether the either range contains the other"""

    return contains(r1, r2) or contains(r2, r1)


def get_overlapping(
        samples:list[str], # a list of section assignments for a pair of elves
    ) -> list[list[range]]:
    """Return a list of overlapping pairs of ranges"""
    assign_ranges = [get_assign_ranges(o) for o in samples]
    overlapping = [o for o in assign_ranges if contains_each_other(*o)]
    return overlapping

def partly_contains(
        r1:range, # a range to check
        r2:range, # the range it contains or not
    ) -> bool:
    """Returns whether the first range partially contains the other range"""
    return ( (r1.start <= r2.start and r1.stop >= r2.start) 
           or(r1.start <= r2.stop  and r1.stop >= r2.stop))


def partly_or_fully_contains_each_other(
        r1:range, # a range to check
        r2:range, # another range 
    ) -> bool:
    """Returns whether the either range partly or fully contains the other"""

    return partly_contains(r1, r2) or partly_contains(r2, r1)

def get_partly_overlapping(
        samples:list[str], # a list of section assignments for a pair of elves
    ) -> list[list[range]]:
    """Return a list of partially or fully overlapping pairs of ranges"""
    assign_ranges = [get_assign_ranges(o) for o in samples]
    partly_overlapping = [o for o in assign_ranges if partly_or_fully_contains_each_other(*o)]
    return partly_overlapping




