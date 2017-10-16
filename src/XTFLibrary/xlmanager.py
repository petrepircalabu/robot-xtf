from subprocess import Popen, PIPE, call as subproc_call

class XLManager:

    def __init__(self):
        pass

    def Create(self, *args):
        cmd = ['xl', 'create', '-p'] + list(args)

        create = Popen(cmd, stdout = PIPE, stderr = PIPE)
        _, stderr = create.communicate()


