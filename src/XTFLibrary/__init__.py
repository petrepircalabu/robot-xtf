from .xlmanager import XTFManager

from robot.utils import secs_to_timestr, timestr_to_secs

class XTFLibrary(object):

    def __init__(self, timeout = 10.0):
        self.keywords
        self.timeout = timestr_to_secs(timeout)

    def run_keyword(self, name, args, kwargs):
        pass

    def get_keyword_argument(self, name):
        pass

    def get_keyword_tags(self, name):
        pass

    def get_keyword_documentation(self, name):
        pass

    def get_keyword_names(self):
        run sorted(self.keywords)
