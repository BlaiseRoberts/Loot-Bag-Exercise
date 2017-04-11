import unittest
from lootbag import *

class TestLootBagMethods(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.lootBag = Bag()

    def test_add_to_bag(self):
        self.lootBag.add_to_bag('car', 'Blaise')
        self.assertIn('car', self.lootBag.list_toys('Blaise'))

    def test_remove_from_bag(self):
        self.lootBag.add_to_bag('slinky', 'Blaise')
        self.lootBag.remove_from_bag('slinky', 'Blaise')
        self.assertNotIn('slinky', self.lootBag.list_toys('Blaise'))

    def test_list_all_children(self):
        self.lootBag.add_to_bag('barbie', 'Adam')
        children = self.lootBag.list_children()
        self.assertIn('Adam',children)

    def test_list_all_toys_for_child(self):
        toy = 'Slime'
        self.lootBag.add_to_bag(toy, 'Blaise')
        self.assertIn('Slime', self.lootBag.list_toys("Blaise"))

    def test_set_delivered(self):
        toy = 'Pony'
        self.lootBag.add_to_bag(toy, 'Angela')
        
        angela = self.lootBag.get_single_child('Angela')  
        self.assertFalse(angela['delivered'])

        self.lootBag.deliver_toys_to_child('Angela')

        angela = self.lootBag.get_single_child('Angela')

        self.assertTrue(angela['delivered'])

    def test_remove_child_from_list(self):
        toy = 'Slime'
        self.lootBag.add_to_bag(toy, 'Angela')
        self.lootBag.remove_child_from_list('Angela')

        self.assertNotIn('Angela', self.lootBag.list_children())        

if __name__ == '__main__':
    unittest.main()