"""
Definition of SUT Software under test.
"""


class Sut:
    """Model for SUT"""

    def __init__(self, a):
        """Create SUT with data specified by a"""
        self.a = a

    def get(self):
        """Return available data"""
        return self.a

    def get_prefix(self, prefix):
        """Get processed prefixed data"""
        return f"{prefix}{self.a}"
