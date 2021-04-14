"""sc-githooks - The base check class

Copyright (c) 2021 Scott Lau
Portions Copyright (c) 2021 InnoGames GmbH
Portions Copyright (c) 2021 Emre Hasegeli
"""
import datetime as dt


from enum import IntEnum


class Logging:
    def __init__(self):
        self._dt = dt.datetime.today().strftime('%Y%m%d')

    def write(self, log_str):
        with open(f"{self._dt}-pre-receive.log", "a+", encoding="utf-8") as f_log:
            f_log.write(log_str)


logging = Logging()


class CheckState(IntEnum):
    NEW = 0
    CLONED = 1
    DONE = 2
    FAILED = 3


class Severity(IntEnum):
    # The numbers are selected to match the Syslog standard.
    ERROR = 3
    WARNING = 4
    NOTICE = 5
    NOTE = 5
    INFO = 6

    def translate(self):
        if self.__eq__(Severity.ERROR):
            return "错误"
        elif self.__eq__(Severity.WARNING):
            return "警告"
        elif self.__eq__(Severity.NOTICE):
            return "注意"
        elif self.__eq__(Severity.NOTE):
            return "注意"
        elif self.__eq__(Severity.INFO):
            return "信息"
        else:
            return "未知"

    @classmethod
    def split(cls, line):
        """Search the severities in the beginning of the string

        It returns the highest severity when non match.
        """
        for name, severity in cls._member_map_.items():
            if line.upper().startswith(name):
                line = line[len(name):].strip(' :-')
                break
        return severity, line


class BaseCheck:
    """The parent class of all checks

    Checks are expanded to different objects by cloning. The subclasses
    has to override prepare() method to clone the check at appropriate
    stage.
    """
    preferred_checks = []
    state = CheckState.NEW
    ERROR_MSG_PREFIX = "GL-HOOK-ERR:"
    NOW_TIME = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            # We expect all of the arguments to be initialized with defaults
            # on the class.
            assert hasattr(type(self), key)
            if value:
                setattr(self, key, value)

    def clone(self):
        new = type(self)(**vars(self))
        new.state = CheckState.CLONED
        return new

    def set_state(self, state):
        assert state > CheckState.CLONED
        self.state = max(self.state, state)

    def prepare(self, obj):
        for check in self.preferred_checks:
            if check.prepare(obj):
                return None
        return self

    def print_problems(self):
        header_printed = False
        for severity, problem in self.evaluate_problems():
            if not header_printed:
                print('{} === {} ==='.format(BaseCheck.ERROR_MSG_PREFIX, self))
                logging.write('{} === {} ===\n'.format(BaseCheck.NOW_TIME, self))
                header_printed = True
            print('{} {}: {}'.format(BaseCheck.ERROR_MSG_PREFIX, severity.translate(), problem))
            logging.write('{} {}: {}\n'.format(BaseCheck.NOW_TIME, severity.translate(), problem))
        # if header_printed:
        #     print('{}'.format(BaseCheck.ERROR_MSG_PREFIX))
        self.set_state(CheckState.DONE)

    def evaluate_problems(self):
        assert self.state == CheckState.CLONED
        for severity, problem in self.get_problems():
            if severity <= Severity.ERROR:
                self.set_state(CheckState.FAILED)
            yield severity, problem

    def __str__(self):
        return type(self).__name__


def prepare_checks(checks, obj, next_checks=None):
    """准备检查对象

    它产生准备就绪的checks。不符合要求的checks准备好了吗？
    下一张check list上会有。
    """
    for check in checks:
        prepared_check = check.prepare(obj)
        if prepared_check:
            cloned = prepared_check.state >= CheckState.CLONED
            assert next_checks is not None or cloned

            if cloned:
                yield prepared_check
            else:
                next_checks.append(prepared_check)
