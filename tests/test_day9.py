import pytest
from butchland_aoc2022.day9 import *
sm_input = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""

md_input = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20"""

@pytest.fixture()
def sm_samples():
    yield sm_input.splitlines()

@pytest.fixture()
def md_samples():
    yield md_input.splitlines()

def test_process_moves(md_samples):
    rope = init_rope(knots=10, init_pos=Pos(16,12))
    final_rope, all_occupieds = process_moves(md_samples,rope=rope)
    assert len(final_rope) == 10
    assert len(all_occupieds) == 36
    assert final_rope == tuple([Pos(1,1),Pos(2,1),Pos(3,1),Pos(4,1),Pos(5,1),
                                    Pos(6,1),Pos(7,1),Pos(8,1),Pos(9,1),Pos(10,1)])

    assert all_occupieds.issuperset(
            set([Pos(16,12),Pos(15,13),Pos(14,14),Pos(13,13),])
            )


def test_process_moves2(sm_samples):
    rope = init_rope(knots=2, init_pos=Pos(5,1))
    final_rope, all_occupieds = process_moves(sm_samples,rope=rope)
    assert len(final_rope) == 2
    assert len(all_occupieds) == 13
    assert final_rope == tuple([Pos(3,3),Pos(3,2)])
    assert all_occupieds.issuperset(
            set([Pos(5,1),Pos(5,2),Pos(5,3),Pos(5,4),
                 Pos(4,5),
                 Pos(3,2),Pos(3,3),Pos(3,4),Pos(3,5),
                 Pos(2,4),Pos(2,5),
                 Pos(1,3),Pos(1,4)])
            )

def test_process_moves3(sm_samples):
    rope = init_rope(knots=10, init_pos=Pos(5,1))
    final_rope, all_occupieds = process_moves(sm_samples,rope=rope)
    assert len(final_rope) == 10
    assert len(all_occupieds) == 1
    assert final_rope == tuple([Pos(3,3),Pos(3,2),Pos(3,3),Pos(3,4),Pos(3,3),
                                Pos(4,2),Pos(5,1),Pos(5,1),Pos(5,1),Pos(5,1)])
    assert all_occupieds.issuperset(
            set([Pos(5,1)])
            )

def test_process_moves3a(sm_samples):
    rope = init_rope(knots=10, init_pos=Pos(5,1))
    final_rope, all_occupieds = process_moves(sm_samples[:-1],rope=rope)
    assert len(final_rope) == 10
    assert len(all_occupieds) == 1
    assert final_rope == tuple([Pos(3,1),Pos(3,2),Pos(3,3),Pos(3,4),Pos(3,3),
                                Pos(4,2), # wrong = Pos(3,2)
                                Pos(5,1),Pos(5,1),Pos(5,1),Pos(5,1)])
    assert all_occupieds.issuperset(
            set([Pos(5,1)])
            )


def test_process_moves3b(sm_samples):
    rope = init_rope(knots=10, init_pos=Pos(5,1))
    final_rope, all_occupieds = process_moves(sm_samples[:1],rope=rope)
    assert len(final_rope) == 10
    assert len(all_occupieds) == 1
    assert final_rope == tuple([Pos(5,5),Pos(5,4),Pos(5,3),Pos(5,2),Pos(5,1),
                                Pos(5,1), 
                                Pos(5,1),Pos(5,1),Pos(5,1),Pos(5,1)])
    assert all_occupieds.issuperset(
            set([Pos(5,1)])
            )
    
def test_process_moves3b1():
    rope = tuple([Pos(5,5),Pos(5,4),Pos(5,3),Pos(5,2),Pos(5,1),
                                Pos(5,1), 
                                Pos(5,1),Pos(5,1),Pos(5,1),Pos(5,1)])
    final_rope, all_occupieds = process_moves(["U 1"],rope=rope)
    assert len(final_rope) == 10
    assert len(all_occupieds) == 1
    assert final_rope == tuple([Pos(4,5),Pos(5,4),Pos(5,3),Pos(5,2),Pos(5,1),
                                Pos(5,1), 
                                Pos(5,1),Pos(5,1),Pos(5,1),Pos(5,1)])
    assert all_occupieds.issuperset(
            set([Pos(5,1)])
            )

def test_process_moves3b2():
    rope = tuple([Pos(4,5),Pos(5,4),Pos(5,3),Pos(5,2),Pos(5,1),
                                Pos(5,1), 
                                Pos(5,1),Pos(5,1),Pos(5,1),Pos(5,1)])
    final_rope, all_occupieds = process_moves(["U 1"],rope=rope)
    assert len(final_rope) == 10
    assert len(all_occupieds) == 1
    assert final_rope == tuple([Pos(3,5),Pos(4,5),Pos(4,4),Pos(4,3),Pos(4,2),
                                Pos(5,1), 
                                Pos(5,1),Pos(5,1),Pos(5,1),Pos(5,1)])
    assert all_occupieds.issuperset(
            set([Pos(5,1)])
            )
def test_process_moves3b3():
    rope = tuple([Pos(3,5),Pos(4,5),Pos(4,4),Pos(4,3),Pos(4,2),
                                Pos(5,1), 
                                Pos(5,1),Pos(5,1),Pos(5,1),Pos(5,1)])
    final_rope, all_occupieds = process_moves(["U 1"],rope=rope)
    assert len(final_rope) == 10
    assert len(all_occupieds) == 1
    assert final_rope == tuple([Pos(2,5),Pos(3,5),Pos(4,4),Pos(4,3),Pos(4,2),
                                Pos(5,1), 
                                Pos(5,1),Pos(5,1),Pos(5,1),Pos(5,1)])
    assert all_occupieds.issuperset(
            set([Pos(5,1)])
            )
    
def test_move_rope3b4():
    rope =  tuple([Pos(2,5),Pos(3,5),Pos(4,4),Pos(4,3),Pos(4,2),
                                Pos(5,1), 
                                Pos(5,1),Pos(5,1),Pos(5,1),Pos(5,1)])
    final_rope = move_rope(rope, "U")
    assert len(final_rope) == 10
    assert final_rope == tuple([Pos(1,5),Pos(2,5),Pos(3,5),Pos(3,4),Pos(3,3),
                                Pos(4,2), # wrong Pos(3,2)
                                Pos(5,1),Pos(5,1),Pos(5,1),Pos(5,1)])


def test_process_moves3b4():
    rope =  tuple([Pos(2,5),Pos(3,5),Pos(4,4),Pos(4,3),Pos(4,2),
                                Pos(5,1), 
                                Pos(5,1),Pos(5,1),Pos(5,1),Pos(5,1)])
    final_rope, all_occupieds = process_moves(["U 1"],rope=rope)
    assert len(final_rope) == 10
    assert len(all_occupieds) == 1
    assert final_rope == tuple([Pos(1,5),Pos(2,5),Pos(3,5),Pos(3,4),Pos(3,3),
                                Pos(4,2), 
                                Pos(5,1),Pos(5,1),Pos(5,1),Pos(5,1)])
    assert all_occupieds.issuperset(
            set([Pos(5,1)])
            )

def test_process_moves3c(sm_samples):
    rope = init_rope(knots=10, init_pos=Pos(5,1))
    final_rope, all_occupieds = process_moves(sm_samples[:2],rope=rope)
    assert len(final_rope) == 10
    assert len(all_occupieds) == 1
    assert final_rope == tuple([Pos(1,5),Pos(2,5),Pos(3,5),Pos(3,4),Pos(3,3),
                                Pos(4,2), 
                                Pos(5,1),Pos(5,1),Pos(5,1),Pos(5,1)])
    assert all_occupieds.issuperset(
            set([Pos(5,1)])
            )

