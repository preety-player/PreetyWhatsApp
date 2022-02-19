#>>>>>>>>>>>>>>>>>>>>>>>Whats App Cli<<<<<<<<<<<<<<<<<<<<<<<<<<
#PreetyPlayer tool for firefox
from time import sleep as slp          
from selenium import webdriver as web
from os import system as s
from sys import stdout
driver=web.Firefox()
driver.get('https://web.whatsapp.com')
slp(30)
class whatsapp:
	def __init__(self):
			pass
	def initial(self,cho):
		try:
			name=input("\n\t\t\tEnter Name/Group Name:")
			self.name=name
			victm=driver.find_element_by_xpath("//span[@title='{}']".format(self.name))
			self.victm=victm
			self.victm.click()
			self.msg_box=self.victm.find_element_by_xpath("//div[@spellcheck='true']")
			if self.cho==2:
				what.single(self.victm,self.msg_box)
			elif self.cho==3:
				what.multi(self.victm,self.msg_box)
			elif self.cho==4:
				what.long(self.victm,self.msg_box)
			else:
				print("Unknown Error Here")
		except(Exception):
			s('clear' or 'cls')
			st="Sorry {} Name Not in Your List Wait Your Redirect Again Try....".format(self.name)
			for x in range(len(st)):
				stdout.write(st[x])
				stdout.flush()
				slp(0.01)
			what.initial(self.cho)
		finally:
			pass
	def home(self):
		s('clear' or 'cls')
		try:
			cho=int(input("\t\t1.Home\n\t\t2.Single Chat\n\t\t3.Multi Chat\n\t\t4.Long Chat\n\t\t5.Clear\n\t\t6.Exit\n\t\t:"))
			self.cho=cho
			if self.cho==6:
				s('reset')
				exit()
			elif self.cho==2 or self.cho==3 or self.cho==4:
				what.initial(self.cho)
			elif cho==5:
				s('clear' or 'cls')
				what.home()
			elif self.cho==1:
				what.home()
			else:
				s('clear' or 'cls')
				print("\n\n\t\t\tYou Enter Invalid Option Try Again...\n\n\t\t\tWhat your redirect Home Page")
				slp(3)
				what.home()
		except(Exception):
			print("Error",Exception)
		finally:
			pass
	def single(self,name,msg_box):
		while(True):
			s('clear' or 'cls')
			print("\t\t\t\t\t333 -->Home")
			value=input("\t\t\tEnter Your Words:")
			if(str(value)=="333"):
				what.home()
			else:
				self.msg_box.send_keys(value)
				self.victm.find_element_by_xpath("//button[@class='_4sWnG']").click()
				print("msg sended...")
				slp(1.3)
	def multi(self,victm,msg_box):
		s('clear' or 'cls')
		try:
			tim=int(input("\t\t\tEnter How Many times:"))
			for x in range(1,tim+1):
				s('clear' or 'cls')
				value=input("{}.Enter Words:".format(x))
				self.msg_box.send_keys(value)
				self.victm.find_element_by_xpath("//button[@class='_4sWnG']").click()
				print("msg sended...")
				slp(0.9)
			what.home()
		except(Exception):
			s('clear' or 'cls')
			print("\n\t\t\tMost Enter Numbers on How Many Times fields...")
			err="Wait you redirect to this page."
			for x in range(len(err)):
				stdout.write(err[x])
				stdout.flush()
				slp(0.3)
			slp(2)
			what.multi(self.victm,self.msg_box)
		finally:
			pass
	def long(self,name,msg_box):
		s('clear' or 'cls')
		try:
			i=1
			tim=int(input("How Many Times:"))
			value=input("ReEntry\t\t-->333\n\n\t\t\tEnter Words:")
			if value=="333":
				what.long(self.name,self.msg_box)
			else:
				for x in range(0,tim+1):
					self.msg_box.send_keys(value)
					print(i)
					i+=1
				self.victm.find_element_by_xpath("//button[@class='_4sWnG']").click()
				s('clear' or 'cls')
				print("\n\t\t\tSended...")
				slp(2)
				con=input("You Want to Continue:")
				if con=="y" or con=="Y":
					what.long(self.victm,self.msg_box)
				else:
					what.home()
		except(Exception):
			print(Exception)
			what.long(self.name,self.msg_box)
		finally:
			pass
what=whatsapp()
if __name__=="__main__":
		what.home()
