import os
import ast
import sys

class Bag:
	def __init__(self):	
		pass

	def add_to_bag(self, toy, name):
		'''Adds a Child to Children.log with default delivered status to False
		 and creats {name}.log to hold the child's list of toys
		
		Arguments:
		toy -- a string of the child's toy
		name -- a string of the child's name
		 '''
		with open('{}.log'.format(name), 'a') as santa:
			if os.stat("{}.log".format(name)).st_size == 0:
				santa.write('{}'.format(toy))
			else:
				santa.write('\n{}'.format(toy))
		with open('children.log', 'a') as santa:
			if name not in self.list_children():
				if os.stat('children.log').st_size == 0:
					child_string = "False---{}".format(name)
					santa.write(child_string)
				else:
					child_string = "\nFalse---{}".format(name)
					santa.write(child_string)

	def list_children(self):
		'''Returns a set that contains the children's names'''
		with open("children.log", 'r') as santa:
			children_list = set()
			for line in santa:
				if '---' not in line:
					pass
				else:
					delivered, name = line.split('---')
					name = name.replace('\n', '')
					children_list.add(name)
			return children_list

	def list_toys(self, name):
		'''Returns a list of all of the toys for a specific child
		
		Arguments:
		name -- a string of the child's name
		 '''
		with open('{}.log'.format(name), 'r') as santa:
			toy_list = (santa.read()).split('\n')
			return toy_list
	
	def remove_from_bag(self, toy, name):
		'''Removes a toy from a child's list
		
		Arguments:
		toy -- a string of the child's toy
		name -- a string of the child's name
		 '''
		with open('{}.log'.format(name), 'r') as santa:
			toy_list = (santa.read()).split('\n')
			toy_list.remove(toy)
			toy_string = '\n'.join(toy_list)
		with open('{}.log'.format(name), 'w') as santa:
			santa.write(toy_string)

	def get_single_child(self, name):
		'''Returns a dict for a specific child containing their deliverd status
		
		Arguments:
		name -- a string of the child's name
		 '''
		with open("children.log", 'r') as santa:
			children_dict = dict()
			for line in santa:
				if '---' not in line:
					pass
				else:	
					delivered, name = line.split('---')
					name = name.replace('\n', '')
					delivered = delivered.replace('\n', '')
					children_dict[name] = {}
					children_dict[name]['delivered'] = ast.literal_eval(delivered) 
			return children_dict[name]

	def deliver_toys_to_child(self, name):
		'''Changes child's delivered status from False to True
		
		Arguments:
		name -- a string of the child's name
		 '''
		with open('children.log', 'r') as santa:
			new_string = ''
			for line in santa:
				if name in line:
					line = line.replace('False', 'True')
				new_string += line			
		with open('children.log', 'w') as santa:
			santa.write(new_string)

	def remove_child_from_list(self, name):
		'''Removes a child from children.log and deletes the {name}.log file
		
		Arguments:
		name -- a string of the child's name
		 '''		
		with open('children.log', 'r') as santa:
			lines = santa.readlines()
			new_lines = list()
			for line in lines:
				if name not in line:
					new_lines.append(line)
		with open('children.log', 'w') as santa:	
			for line in new_lines:
				santa.write(line)
		os.remove('{}.log'.format(name))

if __name__ == '__main__':
	lootBag = Bag()
	sys_arg_list = "Commands for Module:\n-------------------\nadd {toy} {child} - Adds toy to child's list and child to Santa's list, \nremove {toy} {name} - Removes a toy from a child's list, \nls - List's all children on Santa's list, \nls {name} - List's all the toys for a child, \ndelivered - Delivers a child's toys, \nbad {name} - Removes all toys from child and takes child off list"
	if sys.argv[1] == 'add':
		lootBag.add_to_bag(sys.argv[2], sys.argv[3])
	if sys.argv[1] == 'remove':
		lootBag.remove_from_bag(sys.argv[2], sys.argv[3])
	if sys.argv[1] == 'ls' and len(sys.argv) == 2:
		print(lootBag.list_children())
	if sys.argv[1] == 'ls':
		try:
			print(lootBag.list_toys(sys.argv[2]))
		except IndexError:
			pass
	if sys.argv[1] == 'delivered':
		lootBag.deliver_toys_to_child(sys.argv[2])
	if sys.argv[1] == 'bad':
		lootBag.remove_child_from_list(sys.argv[2])		
	if sys.argv[1] == 'help':
		print(sys_arg_list)
