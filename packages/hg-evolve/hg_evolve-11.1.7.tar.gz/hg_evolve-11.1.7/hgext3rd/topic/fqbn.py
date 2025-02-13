# fqbn.py - code related to FQBN (fully qualified branch name)
#
# This software may be used and distributed according to the terms of the
# GNU General Public License version 2 or any later version.
from mercurial import (
    util,
)

class fqbn(object):
    def __init__(self, s):
        self._value = s

    @util.propertycache
    def branch(self):
        return b'default'

    @util.propertycache
    def topic_namespace(self):
        return b'none'

    @util.propertycache
    def topic(self):
        return b''

    @util.propertycache
    def short(self):
        return b''

    @util.propertycache
    def normal(self):
        return b''

    @util.propertycache
    def full(self):
        return b''
