class Callable:
    """
    Pattern found here:
        http://code.activestate.com/recipes/52304-static-methods-aka-class-methods-in-python/
    """
    def __init__(self, anycallable):
        self.__call__ = anycallable
