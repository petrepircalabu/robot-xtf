
class XTFResult:
    SUCCESS, SKIP, ERROR, FAILURE, CRASH, TIMEOUT = range(6)

    def __init__(self, Type):
        if Type not in range(6):
            raise ValueError

        self.value = Type

    def __str__(self):
        names = {   XTFResult.SUCCESS   : "SUCCESS",
                    XTFResult.SKIP      : "SKIP",
                    XTFResult.ERROR     : "ERROR",
                    XTFResult.FAILURE   : "FAILURE",
                    XTFResult.CRASH     : "CRASH",
                    XTFResult.TIMEOUT   : "TIMEOUT" }
        return names[self.value]

    def __eq__(self, y):
        if type(y) == XTFResult:
            return self.value == y.value

        if y not in range(6):
            raise ValueError

        return self.value == y
