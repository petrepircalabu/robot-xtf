from xlmanager import XLManager

class XTFLibrary:

    def __init__(self):
        #TODO: Singleton this
        self._manager = XLManager()

    def CreateVM(self, *args):
        self._manager.CreateVM(*args)

    def GetDomID(self, name):
        return self._manager.GetDomID(name)

    def DestroyVM(self, domid):
        return self._manager.DestroyVM(domid)
