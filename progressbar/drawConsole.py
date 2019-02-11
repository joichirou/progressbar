#-*-coding:utf8-*-
#============================================
# progress bar draw to console.
#============================================
import datetime
import sys


class DrawConsole:

    def __init__(self):
        self.bar            = ""
        self.bar_tip        = ""
        self.finish_message = ""

    def update(self, model):
        u"""drawing progress bar

        model: observer class
        """
        bar_length = self.get_bar_length(model.value)
        sys.stdout.flush()
        sys.stdout.write(
            "\r[%s%%]%s%s" % 
            (model.value,
             (self.bar * int(bar_length)),
             self.bar_tip))
        if (model.value >= 100):
            print("\n%s" % self.finish_message)

    def get_bar_length(self, value):
        bar_length = (value / 5)
        if (bar_length == 0):
            return 1
        if (bar_length <= 20):
            return bar_length
        else:
            return 20
