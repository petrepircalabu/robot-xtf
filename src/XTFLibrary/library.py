from xlmanager import XLManager

from robot.utils import secs_to_timestr, timestr_to_secs

class XTFLibrary:

    def __init__(self):
        #TODO: Singleton this
        self._manager = XLManager()

    def Create(self, config_file):
        return self._manager.Create(config_file)

    def GetDomID(self, name):
        return self._manager.GetDomID(name)

    def Cleanup(self, domid, timeout):
        return self._manager.Cleanup(domid, timestr_to_secs(timeout))

    def Resume(self, domid):
        return self._manager.Resume(domid)

    def WaitForPattern(self, domid, pattern, timeout):
        return self._manager.WaitForPattern(domid, pattern, timestr_to_secs(timeout))
