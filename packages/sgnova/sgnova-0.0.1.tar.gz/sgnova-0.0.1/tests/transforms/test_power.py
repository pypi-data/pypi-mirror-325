"""Unit tests for the power module
"""

from sgnova import Power


class TestPower:
    """Test group for Power transformations
    """

    def test_init(self):
        """Test create a Power transform"""
        p = Power()
        assert isinstance(p, Power)
