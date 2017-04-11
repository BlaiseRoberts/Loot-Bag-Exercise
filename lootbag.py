import os
import ast

class Bag:
	def __init__(self):	
		pass

	def add(self, toy, name):
		if os.stat("{}.log".format(name)).st_size == 0:
			with open('{}.log'.format(name), 'a') as santa:
				santa.write('{}'.format(toy))
		else:
			with open('{}.log'.format(name), 'a') as santa:
				santa.write('\n{}'.format(toy))
		if os.stat('children.log').st_size == 0:
			if name not in self.list_children():
				with open('children.log', 'a') as santa:
					child_string = "False---{}".format(name)
					santa.write(child_string)
		else:
			if name not in self.list_children():
				with open('children.log', 'a') as santa:
					child_string = "\nFalse---{}".format(name)
					santa.write(child_string)

	def list_children(self):
		with open("children.log", 'r') as santa:
			children_list = set()
			for line in santa:
				delivered, name = line.split('---')
				name = name.replace('\n', '')
				children_list.add(name)
			return children_list

	def list_toys(self, name):
		with open('{}.log'.format(name), 'r') as santa:
			toy_list = (santa.read()).split('\n')
			return toy_list
	
	def remove(self, toy, name):
		with open('Blaise.log', 'r') as santa:
			toy_list = (santa.read()).split('\n')
			toy_list.remove(toy)
			toy_string = '\n'.join(toy_list)
		with open('{}.log'.format(name), 'w') as santa:
			santa.write(toy_string)

	def get_single_child(self, name):
		with open("children.log", 'r') as santa:
			children_dict = dict()
			for line in santa:
				delivered, name = line.split('---')
				name = name.replace('\n', '')
				devlivered = delivered.replace('\n', '')
				children_dict[name] = {}
				children_dict[name]['delivered'] = ast.literal_eval(delivered) 
			return children_dict[name]

	def deliver_toys_to_child(self, name):
		with open('children.log', 'r') as santa:
			new_string = ''
			for line in santa:
				if name in line:
					line = line.replace('False', 'True')
				new_string = new_string+line			
		with open('children.log', 'w') as santa:
			santa.write(new_string)

