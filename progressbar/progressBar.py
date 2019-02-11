#-*-coding:utf8-*-
#==================================================
# progress bar customize module.
#
# this program is designning of observer pattern.
#==================================================
from barDesignList import *
from sliderModel import SliderModel
from drawConsole import DrawConsole
import time
import sys


class ProgressBar():

    def __init__(
            self,
            value=None,
            bar_index=0,
            msg_index=0):
        self.__value = None
        self.bar_design = PROGRESS_PATTERNS[bar_index][BAR]
        self.bar_tip_design = PROGRESS_PATTERNS[bar_index][BAR_TIP]
        self.finish_message = FINISH_MESSAGES[msg_index]
        self.drawer = None
        self.slider_model = None
        self.set_observers()
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        if self.__value != value:
            self.__value = value
            # update progress bar
            self.slider_model.value = value

    def print_bar_list(self):
        print("[PROGRESS BAR DESIGN PATTERNS]")
        for i in range(len(PROGRESS_PATTERNS)):
            print("%s: [50%%]%s%s" % 
                (i,
                 PROGRESS_PATTERNS[i][BAR] * 5,
                 PROGRESS_PATTERNS[i][BAR_TIP]))

    def print_msg_list(self):
        print("[FINISH MESSAGE PATTERNS]")
        for i in range(len(FINISH_MESSAGES)):
            print("%s: %s" % (i, FINISH_MESSAGES[i]))

    def set_observers(self):
        self.drawer = DrawConsole()
        self.drawer.bar = self.bar_design
        self.drawer.bar_tip = self.bar_tip_design
        self.drawer.finish_message = self.finish_message
        self.slider_model = SliderModel(0)
        self.slider_model.observers_add(self.drawer)

    @staticmethod
    def is_contains_bar_list(index):
        try:
            return PROGRESS_PATTERNS[index][BAR]
        except IndexError:
            return False

    @staticmethod
    def is_contains_msg_list(index):
        try:
            return FINISH_MESSAGES[index]
        except IndexError:
            return false


if __name__ == "__main__":
    from optparse import OptionParser
    opt_parser = OptionParser()
    opt_parser.add_option(
       '--test',
       dest='test_flag',
       type='int',
       help='test flag',
       default=0)
    opt_parser.add_option(
       '--bar_design',
       dest='bar_design',
       type='int',
       help='bar design',
       default=0)
    opt_parser.add_option(
       '--fin_msg',
       dest='fin_msg',
       type='int',
       help='finish message',
       default=0)
    opt_parser.add_option(
       '--value',
       dest='value',
       type='int',
       help='progress value',
       default=0)
    options, args = opt_parser.parse_args()
    if (options.test_flag):
        print("[TEST MODE]")
        # debug
        progress_bar = ProgressBar()
        for i in range(10):
            progress_bar.value = (i + 1) * 10
            time.sleep(0.1)
        progress_bar.print_bar_list()
        progress_bar.print_msg_list()
    else:
        if not (ProgressBar.is_contains_bar_list(options.bar_design)):
            print("[PROGRESS BAR LIST] index error.")
            sys.exit()
        if not (ProgressBar.is_contains_msg_list(options.fin_msg)):
            print("[FINISH MESSAGE LIST] index error.")
            sys.exit()
        progress_bar = ProgressBar(
                options.value,
                options.bar_design,
                options.fin_msg)
