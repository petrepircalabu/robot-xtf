from xlmanager import XLManager

class XTFLibrary:

    def __init__(self):
        #TODO: Singleton this
        self._manager = XLManager()

    def Create(self, *args):
        self._manager.Create(*args)

    def aaabp(self):
        print "create guest "
