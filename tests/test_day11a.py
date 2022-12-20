import pytest
from numba import jit
from typing import Callable

@jit(nopython=True)
def xfm(n:int) -> int:
    return n * 9

@jit(nopython=True)
def get_answer(m:int, mxfm:Callable[[int],int]) -> list[int]:
    data = [5] * m
    return [mxfm(d) for d in data] 

# @jit(nopython=True)
# def get_answer(m:int) -> list[int]:
#     data = [5] * m
#     return [xfm(d) for d in data]
  
def test_jit():  
    
    # def xfm(n:int) -> int: return n * 9
    # jxfm = jit(xfm,nopython=True)
    m = 100000000
    # jit_answer = jit(get_answer,nopython=True)
    answer = get_answer(m,mxfm=xfm)
    # answer = jit_answer(m, mxfm=jxfm) # type: ignore
    assert sum(answer) == 45 * m
    assert len(answer) == m

# def test_dynamic_jit():
#     xfm = eval("def xfm(old:int) -> int: return old * 9", __globals=globals(), __locals=locals())
#     jxfm = jit(xfm,nopython=True)
#     def get_answer(m:int, mxfm:Callable[[int],int]) -> list[int]:
#         data = [5] * m
#         return [mxfm(d) for d in data] 
#     m = 100000000
#     jit_answer = jit(get_answer,nopython=True)
#     # answer = get_answer(m)
#     answer = jit_answer(m, mxfm=jxfm) # type: ignore
#     assert sum(answer) == 45 * m
#     assert len(answer) == m
