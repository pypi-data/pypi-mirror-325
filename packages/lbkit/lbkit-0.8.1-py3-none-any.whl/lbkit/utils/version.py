"""环境准备"""
import re

X_VER = 0x7fff_ffff

class Version():
    def __init__(self, ver_str):
        if not re.match("^([0-9]|([1-9][0-9]*))\\.([0-9]|([1-9][0-9]*))$", ver_str):
            raise Exception("Version string {ver_str} not match with regex ^([0-9]|([1-9][0-9]*))\\.([0-9]|([1-9][0-9]*))$")
        chunks = ver_str.split(".")
        self.major = int(chunks[0])
        self.minor = int(chunks[1])
        self.str = str(self.major) + "." + str(self.minor)

    def bt(self, next_ver):
        next = Version(next_ver)
        if self.major > next.major or (self.major == next.major and self.minor > next.minor):
            return True
        return False

    def be(self, next_ver):
        next = Version(next_ver)
        if self.major > next.major or (self.major == next.major and self.minor >= next.minor):
            return True
        return False

    def lt(self, next_ver):
        next = Version(next_ver)
        if self.major < next.major or (self.major == next.major and self.minor < next.minor):
            return True
        return False

    def le(self, next_ver):
        next = Version(next_ver)
        if self.major < next.major or (self.major == next.major and self.minor <= next.minor):
            return True
        return False

