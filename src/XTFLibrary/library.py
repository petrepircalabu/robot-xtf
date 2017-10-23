from xlmanager import XLManager

class XTFLibrary:

    def __init__(self):
        #TODO: Singleton this
        self._manager = XLManager()

    def Create(self, *args):
        return self._manager.Create(*args)

    def GetDomID(self, name):
        return self._manager.GetDomID(name)

    def Destroy(self, domid):
        return self._manager.Destroy(domid)

    def Resume(self, domid):
        return self._manager.Resume(domid)
