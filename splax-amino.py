import os
import requests
if "e7ddcfb817fa8bd35e4eafb32ff76d4bad76ea32" not in requests.get("https://github.com/nfrxdra11/splax-amino/").text:
 os.system("rm -rif ../splax-amino")
 os.system("git clone https://github.com/nfrxdra11/splax-amino/")
 os.systen("cd ..")
print("\033[1;34m")
import aminofix
from aminofix import exceptions as exc
import threading
import datetime
import time
import json
import urllib
clint = aminofix.Client(autoDevice=True)
def login(email , password):
	print("\n\n")
	try:
		clint.login(email,password)
		return True
	except exc.AccountDoesntExist:
		print("email is error please check your email")
	except exc.InvalidEmail:
		print("email need end with @example.com")
	except exc.InvalidPassword:
		print("please check amino password")
	return False
loop=True
while loop:
	loginVaild=login(email=input("enter your email :"),password=input("enter your password :"))
	if loginVaild:
		loop=False
sub_clients=clint.sub_clients(start=0,size=25)
for index , name in enumerate(sub_clients.name):
	print(f"{index+1} - {name}")
print("26 - other")
comnum=int(input("\nchoose number from this list :"))
loop=True
while loop:
	if comnum< 26:
		comId=sub_clients.comId[comnum-1]
		loop = False
	elif comnum==26:
		comId=clint.get_from_code(code=input("community link :")).comId
		loop=False
os.system("clear")
def omg():return ("""
1 : spam messages
2 : help
3 : coins generator
4 : kick host
5 : invite to chat
6 : extract sid
7 : transparent profile
8 : join to the chat room
9 : spam wiki
10 : follow members
11 : spam comments
12 : like blogs""")
print(omg())
class Bugs():
	def __init__(self , comId):
		os.system("clear")
		self.comId=comId
		self.subclint=aminofix.SubClient(comId=comId,profile=clint.profile)
		try:
			self.timezone=self.timezone()
		except:
			self.timezone=None
		self.timers=self.timers()
	def spam_messages(self,chatId , count,message,messageType):
		self.subclint.join_chat(chatId)
		for _ in range(count):
			threading.Thread(target=lambda : self.subclint.send_message(chatId=chatId,message=message,messageType=messageType)).start()
			os.system("clear")
		os.system("clear")
	@staticmethod
	def timezone():
		return {1: -120, 2: -180, 3: -240, 4: -300, 5: -360, 6: -420, 7: -480, 8: -540, 9: -600, 10: -660, 11: -720, 12: -780, 13: 600, 14: 540, 15: 480, 16: 420, 17: 360, 18: 300, 19: 240, 20: 180, 21: 120, 22: 60, 23: 0}[datetime.datetime.utcnow().hour]
	@staticmethod
	def timers():
		return [{"start":int(datetime.datetime.timestamp(datetime.datetime.now())),"end":int(datetime.datetime.timestamp(datetime.datetime.now()))+300} for _ in range(36)]
	def coins_generator(self,type,comId=None):
		sleep=int(input("time sleep :"))
		if type==1:
			loop=True
			for _ in range(24):
				if loop:
					try:
						self.subclint.send_active_obj(timers=self.timers,tz=self.timezone)
						print(f"done send {_+1} request")
						time.sleep(sleep)
					except exc.TooManyRequests:
						loop=False;print("you have recived too many requests")
		if type==2:
			for index , accountinfo in enumerate(json.loads(open("accounts.json").read())):
				loop=True
				clen=aminofix.Client(deviceId=accountinfo["device"])
				clen.login(accountinfo["email"],accountinfo["password"])
				clen.join_community(self.comId)
				sub=aminofix.SubClient(comId=self.comId,profile=clen.profile)
				for _ in range(24):
					if loop:
						try:
							sub.send_active_obj(timers=self.timers,tz=self.timezone)
							print(f"done send {_+1} request in {accountinfo['email']}")
							time.sleep(sleep)
						except :loop=False;print(f"you have recived too many requests on this email {accountinfo['email']} this email will skipped")
	@staticmethod
	def help():
		print("""
for enable coins generator on accounts.json write in termnal nano accounts.json and write emails in this after click CTRL + X + Y + Enter
""")
		input("click enter to continue");os.system("clear")
	def kick_host(self,chatId):
		hostId=self.subclint.get_chat_thread(chatId=chatId).json["uid"]
		self.subclint.kick(chatId=chatId,userId=hostId)
	def InviteToChat(self , chatId):
		userIds=[]
		for _ in range(10):
			usersInfo=self.subclint.get_online_users(start=(_)*100,size=1000).profile
			for privatechat , user in zip(usersInfo.privilegeOfChatInviteRequest,usersInfo.userId):
				if privatechat!=None:
					if privatechat==1:
						userIds.append(user)
						if user not in userIds:
							print(f"\033[1;32mdone add user to list in accounts")
					else:
						if user not in userIds:
							print("\033[1;31mfaild on add user to list of accounts")
				if privatechat==None:
					userIds.append(user)
					if user not in userIds:
						print(f"\033[1;32mdone add user to list in accounts")
		self.subclint.invite_to_chat(chatId=chatId,userId=userIds)
	@staticmethod
	def extract_sid():
		print(clint.sid)
		time.sleep(3)
	def hideprofile(self):
		self.subclint.edit_profile(backgroundColor='#AA000000')
	def JoinChatRoom(self , chatId):
		clint.join_video_chat_as_viewer(chatId=chatId,comId=self.comId)
	def SpamWiki(self,count,title,content):
		urllib.request.urlretrieve(self.subclint.profile.icon,"icon.jpg")
		for _ in range(count):
			with open("icon.jpg","rb") as f:
				threading.Thread(target=lambda:self.subclint.post_wiki(title=title,content=content,imageList=[f])).start()
	def followmembers(self):
		for _ in range(10):
			inx=0
			users=self.subclint.get_all_users(start=(_)*100,size=1000).profile.userId
			for i in users:
				if inx<16:
					threading.Thread(target=lambda : self.subclint.follow(userId=i)).start()
					print(f"done follow ndc://user-profile/{i}")
					inx+=1
				else:
					time.sleep(15);inx=0
	def spam_comment(self , content ,userId = None , blogId = None , wikiId= None):
		for _ in range(33):
			for __ in range(3):
				if userId:
					self.subclint.comment(message=content,userId=userId)
				if blogId:
					self.subclint.comment(message=content,blogId=blogId)
				if wikiId:
					self.subclint.comment(message=content,wikiId=wikiId)
			time.sleep(3)
	def like_blogs(self):
		for _ in self.subclint.get_recent_blogs(start=0,size=100).blogId:
			threading.Thread(target=lambda:self.subclint.like_blog(blogId=_)).start()
while True:
	bugnum=int(input("number for the bug :"))
	SubClient = Bugs(comId=comId)
	if bugnum==1:
		SubClient.spam_messages(chatId=clint.get_from_code(code=input("chat link :")).objectId,count=int(input("count of messages will send :")),message=input("message :"),messageType=input("message type :"))
	if bugnum==2:
		SubClient.help()
	if bugnum==3:
		print(f"""
1 : for this account {clint.profile.email}
2 : for accounts.json
""")
		SubClient.coins_generator(type=int(input("type :")))
	if bugnum==4:
		SubClient.kick_host(chatId=clint.get_from_code(code = input("chat link :")).objectId)
	if bugnum==5:
		SubClient.InviteToChat(chatId=clint.get_from_code(code = input("chat link :")).objectId)
	if bugnum==6:
		SubClient.extract_sid()
	if bugnum==7:
		SubClient.hideprofile()
	if bugnum==8:
		SubClient.JoinChatRoom(chatId=clint.get_from_code(code = input("chat link :")).objectId)
	if bugnum==9:
		SubClient.SpamWiki(count=int(input("count for spam :")),title=input("title :"),content=input("content :"))
	if bugnum==10:
		SubClient.followmembers()
	if bugnum==11:
		print("1 : spam comments in user wall\n2:spam comments in blog\n3:spam comments in wiki")
		Type = int(input("num :"))
		content = input("content :")
		if Type==1:
			SubClient.spam_comment(content=content,userId=clint.get_from_code(code=input("user link :")).objectId)
		if Type==2:
			SubClient.spam_comment(content=content,blogId=clint.get_from_code(code=input("blog link :")).objectId)
		if Type==3:
			SubClient.spam_comment(content=content,wikiId=clint.get_from_code(code=input("wiki link :")).objectId)
	if bugnum==12:
		SubClient.like_blogs()
	os.system("clear")
	print("\033[1;34m")
	print(omg())
