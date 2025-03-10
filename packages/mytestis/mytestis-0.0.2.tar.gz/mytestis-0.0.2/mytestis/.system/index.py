from imports import *


class index:
    ####################################################################################// Load
    def __init__(self, app="", args=[]):
        self.app, self.args = app, args
        # ...
        pass

    ####################################################################################// Main
    def demo(self, param=""):  # <param> - Test demo method with param
        if not param:
            return "Invalid param!"

        cli.hint(param)

        return self.__helper()

    def test(self):  # Test method
        cli.info("Hi There")
        return self.__helper()

    ####################################################################################// Helpers
    def __helper(self):
        return jobs.test()
