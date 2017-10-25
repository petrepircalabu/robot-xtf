from subprocess import Popen, PIPE, call as subproc_call

import imp
import pexpect
import time

class XLException(Exception):
    """ Errors relating to xtf-runner itself """

class XLVMInfo(object):
    def __init__(self, config_file):
        code = open(config_file)
        self.config = imp.new_module(config_file)
        exec code in self.config.__dict__

# TODO: Add base class
class XLManager:
    def __init__(self):
        self._vms = {}

    def Create(self, config_file):
        cmd = ['xl', 'create', '-p', config_file]

        vm_info = XLVMInfo(config_file)

        create = Popen(cmd, stdout = PIPE, stderr = PIPE)
        _, stderr = create.communicate()

        if create.returncode:
            raise XLException("Failed to create VM", stderr)

        domid = self.GetDomID(vm_info.config.name)

        vm_info.console = pexpect.spawn('xl console ' + str(domid))

        self._vms[domid] = vm_info

        return domid

    def GetDomID(self, name):
        cmd = ['xl', 'domid', name]

        getdomid = Popen(cmd, stdout = PIPE, stderr = PIPE)
        _, stderr = getdomid.communicate()

        if getdomid.returncode:
            raise XLException("Failed to get VM's DomID", stderr)

        return long(_)

    def WaitForPattern(self, domid, pattern, timeout):
        vm_info = self._vms[domid]

        vm_info.console.expect(pattern, long(timeout))

    def Destroy(self, domid):
        cmd = ['xl', 'destroy', str(domid)]

        while self._vms[domid].console.isalive():
            print "Waiting...."
            time.sleep(1)

        if not self._vms[domid].console.isalive():
            print "Process exited"
            return

        print "destroying process"

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

