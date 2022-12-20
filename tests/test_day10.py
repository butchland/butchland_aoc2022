import pytest
from butchland_aoc2022.day10 import *

vs_input = """noop
addx 3
addx -5"""

md_input = """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop"""

@pytest.fixture()
def vs_sample():
    yield vs_input.splitlines()

@pytest.fixture()
def md_sample():
    yield md_input.splitlines()

def test_cycle_vs_sample(vs_sample):
    cpu = CPU(vs_sample)
    g = cpu.cycles()
    assert (1,1) == next(g)
    assert (2,1) == next(g)
    assert (3,1) == next(g)
    assert (4,4) == next(g)
    assert (5,4) == next(g)
    assert cpu.X == -1

def test_cycle_vs_sample2(vs_sample):
    vs2_sample = vs_sample.extend(["noop"])
    cpu = CPU(vs_sample)
    g = cpu.cycles()
    assert (1,1) == next(g)
    assert cpu.X == 1
    assert (2,1) == next(g)
    assert cpu.X == 1
    assert (3,1) == next(g)
    assert cpu.X == 4
    assert (4,4) == next(g)
    assert (5,4) == next(g)
    assert cpu.X == -1
    assert (6,-1) == next(g)

def test_cycle_vs_sample2(vs_sample):
    vs2_sample = vs_sample.extend(["noop"])
    cpu = CPU(vs_sample)
    g = cpu.cycles()
    assert (1,1) == next(g)
    assert cpu.X == 1
    assert (2,1) == next(g)
    assert cpu.X == 1
    assert (3,1) == next(g)
    assert cpu.X == 4
    assert (4,4) == next(g)
    assert (5,4) == next(g)
    assert cpu.X == -1
    assert (6,-1) == next(g)

def test_strength_md_sample(md_sample):
    cpu = CPU(md_sample)
    g = cpu.signal_strengths()
    assert 420 == next(g)
    assert 1140 == next(g)
    assert 1800 == next(g)
    assert 2940 == next(g)
    assert 2880 == next(g)
    assert 3960 == next(g)

def test_sum_strengths(md_sample):
    assert sum_strengths(md_sample) == 13140

sm_pixel_screen = """##..##..##..##..##..##..##..##..##..##..
###...###...###...###...###...###...###.
####....####....####....####....####....
#####.....#####.....#####.....#####.....
######......######......######......####
#######.......#######.......#######....."""

@pytest.fixture()
def sample_sm_pixels():
    lines = sm_pixel_screen.splitlines()
    samples = []
    for line in lines:
        samples.append(list(line))
    yield samples

def test_pixels(md_sample, sample_sm_pixels):
    assert len(sample_sm_pixels) == 6
    assert len(md_sample) == 146
    all_pixels = []
    for line in sample_sm_pixels:
        assert len(line) == 40
        all_pixels.extend(line)
    cpu = CPU(md_sample)
    cycles = list(cpu.cycles())
    assert 240 == len(cycles)
    assert 240 == len(all_pixels)
    debug_pixels = list(cpu.debug_draw_pixel())
    assert 240 == len(debug_pixels)
    cpu2 = CPU(md_sample)
    outputs = list(cpu2.draw_pixel())
    assert outputs == all_pixels
