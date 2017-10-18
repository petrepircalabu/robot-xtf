from subprocess import Popen, PIPE, call as subproc_call

class XLException(Exception):
    """ Errors relating to xtf-runner itself """

# TODO: Add base class
class XLManager:

    def __init__(self):
        pass

    def CreateVM(self, *args):
        cmd = ['xl', 'create', '-p'] + list(args)

        create = Popen(cmd, stdout = PIPE, stderr = PIPE)
        _, stderr = create.communicate()

        if create.returncode:
            raise XLException("Failed to create VM", stderr)

    def GetDomID(self, name):
        cmd = ['xl', 'domid', name]

        getdomid = Popen(cmd, stdout = PIPE, stderr = PIPE)
        _, stderr = getdomid.communicate()

        if getdomid.returncode:
            raise XLException("Failed to get VM's DomID", stderr)

        return long(_)

    def DestroyVM(self, domid):
        cmd = ['xl', 'destroy', str(domid)]

        if domid == 0:
            raise XLException("DestroyVM: Cannot destroy Dom0");
        print domid

        destroy = Popen(cmd, stdout = PIPE, stderr = PIPE)
        _, stderr = destroy.communicate()

        if destroy.returncode:
            raise XLException("Failed to get VM's DomID", stderr)

