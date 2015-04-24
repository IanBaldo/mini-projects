import types
import random

def createList(original_list):
	if isinstance(original_list, types.ListType):
		# Data is OK
		new_list = []
		for y in range(0,len(original_list)):
			new_list.append(original_list[y])

		first = new_list[random.randrange(0,len(new_list))]
		new_list.remove(first)
		current = first
		while len(new_list) > 0:
			tmp = new_list[random.randrange(0,len(new_list))]		# chooses random person
			current.setFriend(tmp.getName())	 			# set as friend
			new_list.remove(tmp)						# removes from list
			current = tmp							#update current person

		current.setFriend(first.getName())
	else:
		print("Something went wrong! Check your data.")

def testResult(alist):
	current = alist[random.randrange(0,len(alist))]
	first = current
	print("--------------")
	print(first.getName())
	print("--------------")
	counter = 0
	while current.getFriend() != first.getName():
		i = 0
		counter += 1
		while alist[i].getName() != current.getFriend():
			print "%s = %s ???" % (current.getFriend(),alist[i].getName())
			i += 1
		current = alist[i]
	print(counter)
	if counter == len(alist)-1:
		print("OK")
	else:
		print("ERROR")



class Person(object):
	__name =  ""
	__email = ""
	__friend = None
	def __init__(self, name, email):
		self.__name = name
		self.__email = email

	def getName(self):
		return self.__name

	def getEmail(self):
		return self.__email

	def getFriend(self):
		return self.__friend
	
	def setName(self, name):
		self.__name = name

	def setEmail(self, email):
		self.__email = email

	def setFriend(self, friend):
		self.__friend = friend


alist = []
with open("example.txt","r") as afile:
	
	data = afile.readlines()
	for line in data:
		word = line.split()
		alist.append(Person(word[0],word[1]))


createList(alist)
testResult(alist)
for x in range(0,len(alist)):
	print "%d %s -> %s" % (x,alist[x].getName(),alist[x].getFriend())

