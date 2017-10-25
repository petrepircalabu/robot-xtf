from xlmanager import XLManager

class XTFLibrary:

    def __init__(self):
        #TODO: Singleton this
        self._manager = XLManager()

    def Create(self, config_file):
        return self._manager.Create(config_file)

    def GetDomID(self, name):
        return self._manager.GetDomID(name)

    def Destroy(self, domid):
        return self._manager.Destroy(domid)

    def Resume(self, domid):
        return self._manager.Resume(domid)

    def WaitForPattern(self, domid, pattern, timeout):
        return self._manager.WaitForPattern(domid, pattern, timeout)
