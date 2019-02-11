#-*-coding:utf8-*-
from observed import Observed

class SliderModel(Observed):

    def __init__(self, value):
        super().__init__()
        # this setting need a finished
        # must be before calling setter of property.
        self.__value            = None
        self.value              = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        if self.__value != value:
            self.__value = value
            self.observers_notify()
