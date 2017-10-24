from subprocess import Popen, PIPE, call as subproc_call

import imp

class XLException(Exception):
    """ Errors relating to xtf-runner itself """

# TODO: Add base class
class XLManager:

    def __init__(self):
        pass

    def _get_config(self, config_file):
        code = open(config_file)
        module = imp.new_module(config_file)
        exec code in module.__dict__
        return module

    def Create(self, config_file):
        cmd = ['xl', 'create', '-p', config_file]
        config = self._get_config(config_file)

        create = Popen(cmd, stdout = PIPE, stderr = PIPE)
        _, stderr = create.communicate()

        if create.returncode:
            raise XLException("Failed to create VM", stderr)

        return self.GetDomID(config.name)

    def GetDomID(self, name):
        cmd = ['xl', 'domid', name]

        getdomid = Popen(cmd, stdout = PIPE, stderr = PIPE)
        _, stderr = getdomid.communicate()

        if getdomid.returncode:
            raise XLException("Failed to get VM's DomID", stderr)

        return long(_)

    def Destroy(self, domid):
        cmd = ['xl', 'destroy', str(domid)]

        if domid == 0:
            raise XLException("DestroyVM: Cannot destroy Dom0");

        destroy = Popen(cmd, stdout = PIPE, stderr = PIPE)
        _, stderr = destroy.communicate()

        if destroy.returncode:
            raise XLException("Failed to get VM's DomID", stderr)

    def Resume(self, domid):
        cmd = ['xl', 'unpause', str(domid)]

        if domid == 0:
            raise XLException("Resume: Invalid parameter");

        resume = Popen(cmd, stdout = PIPE, stderr = PIPE)
        _, stderr = resume.communicate()

        if resume.returncode:
            raise XLException("Failed to resume VM", stderr)

