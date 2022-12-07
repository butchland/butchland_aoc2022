import pytest
from butchland_aoc2022.day7 import *
import fastcore.all as fc

data = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""

@pytest.fixture()
def samples():
    yield data.splitlines()

expected_results =  [
        ("$ cd /", ("cd", "/")), 
        ("$ ls", ("ls",)), 
        ("dir a", ("dir", "a")), 
        ("14848514 b.txt", ("size",14_848_514,"b.txt"))
]
@pytest.mark.parametrize(
    "test_input, expected",expected_results)
def test_parse_line(test_input, expected):
    assert parse_line(test_input) == expected


def test_generate_tokens(samples):
    token_gen = generate_tokens(samples)
    for expected in fc.L(expected_results).itemgot(1):
        token = next(token_gen)
        assert token == expected

def test_process_commands(samples):
    nodes = process_commands(samples)
    lnodes = fc.L(nodes)
    tsize = lnodes.attrgot("size").filter(lambda o: o < 100_000).sum()
    assert tsize == 95_437


