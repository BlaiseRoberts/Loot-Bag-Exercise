import unittest
from lootbag import *

class TestLootBagMethods(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.lootBag = Bag()

    def test_add_to_bag(self):
        self.lootBag.add('car', 'Blaise')
        self.assertIn('car', self.lootBag.list_toys('Blaise'))

    def test_remove_from_bag(self):
        self.lootBag.add('slinky', 'Blaise')
        self.lootBag.remove('slinky', 'Blaise')
        self.assertNotIn('slinky', self.lootBag.list_toys('Blaise'))

    def test_list_all_children(self):
        self.lootBag.add('barbie', 'Adam')
        children = self.lootBag.list_children()
        self.assertIsInstance(children, set)

    def test_list_all_toys_for_child(self):
        toy = 'Slime'
        self.lootBag.add(toy, 'Blaise')
        self.assertIsInstance(self.lootBag.list_toys("Blaise"), list)  
        self.assertIn('Slime', self.lootBag.list_toys("Blaise"))

    def test_set_delivered(self):
        toy = 'Pony'
        self.lootBag.add(toy, 'Blaise')
        
        blaise = self.lootBag.get_single_child('Blaise')
        
        self.assertIsInstance(blaise, dict)
        self.assertFalse(blaise['delivered'])

        self.lootBag.deliver_toys_to_child('Blaise')
        blaise = self.lootBag.get_single_child('Blaise')
        
        self.assertTrue(blaise['delivered'])

if __name__ == '__main__':
    unittest.main()