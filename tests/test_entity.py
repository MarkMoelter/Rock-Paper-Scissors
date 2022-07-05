import unittest
from entities import Entities


# fixme not implemented
class TestEntity(unittest.TestCase):
    def test_entities(self):
        """test Entities class and int_to_entity function"""
        assert Entities.ROCK == 0
        assert Entities.PAPER == 1
        assert Entities.SCISSORS == 2


if __name__ == '__main__':
    unittest.main()
