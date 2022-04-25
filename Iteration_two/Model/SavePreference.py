from Preference import *


class SavePreference(object):
    """
    This is the system model
    """

    list_preference: list = []
    current_preference: Preference = None


def save_preference(cls, p):
    cls.list_preference.append(p)


def set_current_preference(cls, p):
    cls.current_preference = p


def get_current_preference(cls):
    return cls.current_preference


def get_preference_list(cls):
    return cls.list_preference


