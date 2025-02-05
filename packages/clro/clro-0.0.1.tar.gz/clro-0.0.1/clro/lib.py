import builtins as __builtins__
from subpr.lib import subpr as _s
from subpr.lib import partial as _p

__buitinset__ = _p(setattr, __builtins__)
__onbuiltin__ = lambda ob : __buitinset__(ob.__name__, ob)

class __clrocls__(type):
    def __new__(metacls, name : str, supers : tuple, value : dict):
        return super().__new__(metacls, name, supers, value)
    
    __neg__ = lambda self : __buitinset__('x', self(input('clear command : ')))

@__onbuiltin__
class c(metaclass = __clrocls__):
    __slots__ = ('__clrcmd', )
    
    def __init__(self, clrcmd : str):
        self.__clrcmd = clrcmd
    
    __neg__ = lambda self : (None, _s(self.__clrcmd)())[0]