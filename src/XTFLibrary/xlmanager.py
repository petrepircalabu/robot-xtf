from subprocess import Popen, PIPE, call as subproc_call

class XLException(Exception):
    """ Errors relating to xtf-runner itself """

# TODO: Add base class
class XLManager:

    def __init__(self):
        pass

    def Create(self, *args):
        cmd = ['xl', 'create', '-p'] + list(args)

        create = Popen(cmd, stdout = PIPE, stderr = PIPE)
        _, stderr = create.communicate()

        if create.returncode:
            raise XLException("Failed to create VM", stderr)

