import types
import random
import re
import smtplib

fromaddr = ""	#auto.amigoocutlo@gmai.com

username = ""
password = ""

def sendMail(fromaddr,username,password,alist):
	server = smtplib.SMTP("smtp.gmail.com:587")
	server.starttls()
	server.login(username,password)
	for w in range(0,len(alist)):
		msg = "\nAmigo Oculto:"
		msg = msg + "\nVoce tirou %s \n\nEssa mensagem e automatica e nao deve ser respondida." % alist[w].getFriend()
		server.sendmail(fromaddr,alist[w].getEmail(),msg)
	server.quit()

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
			current.setFriend(tmp)	 			# set as friend
			new_list.remove(tmp)						# removes from list
			current = tmp							#update current person

		current.setFriend(first)
	else:
		print("Something went wrong! Check your data.")

# Checks if the order is ok (1 cicle)
def testResult(alist):
	current = alist[random.randrange(0,len(alist))]
	first = current
	counter = 0
	while current.getFriend() != first:
		counter += 1
		current = current.getFriend()

	if counter == len(alist)-1:
		print("------ Result is OK! ")
		return 1
	else:
		print("---------- ERROR")
		return 0


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
wrong_email_counter = 0	# counts misspelled emails
overall_data = 1		# Marks if the data is OK
with open("example.txt","r") as afile:
	
	data = afile.readlines()
	EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")
	for line in data:
		word = line.split()
		if len(word) == 2:
			if EMAIL_REGEX.match(word[1]):
				alist.append(Person(word[0],word[1]))
			else:
				wrong_email_counter += 1
				overall_data = 0 # False
		else:
			overall_data = 0 # False
			print("Something is wrong with the data")

if overall_data:
	createList(alist)
	if testResult(alist):
		#sendMail(fromaddr,username,password,alist)
		for x in range(0,len(alist)):
			print "%d %s -> %s" % (x,alist[x].getName(),alist[x].getFriend().getName())
if wrong_email_counter > 0:
	print("There is(are) %d email(s) misspelled" % wrong_email_counter)