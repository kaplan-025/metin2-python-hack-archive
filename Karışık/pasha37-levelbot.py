import app
import ui
import player
import chr
import chat
import chrmgr
import time
import skill
import nonplayer
import net
import snd
import item
import math
import miniMap
import uiminimap
import background
import exception
import uiCommon
import grp
import os
import shop
import ServerInfo
import game
import chat
import thread

import urllib2
import re
import md5

VidList = []
PickUpList = []
PickUpListNames = []
PrivateMessages = {}
AnswerTuple = {}
TmpMessageDict = []

OldHPTargetBoard = game.GameWindow.SetHPTargetBoard
OldOnRecvWhisper = game.GameWindow.OnRecvWhisper
OldOpenTargetBoard = game.GameWindow.SetPCTargetBoard

HookedVid = [0, 0]
MinimizedWhisper = 0

BuffVid = 0

## Item Pickup Save
try:
	lines = open("lib/pickuplist.save", "r+").readlines()
	for drop in lines:
		try:
			PickUpList.append(int(drop))

			ItemName = item.GetItemName(item.SelectItem(int(drop)))
			try:
				if ItemName.lower().find("stein ") != -1 or ItemName.lower().find("stone ") != -1: 
					pass
				else:
					int(ItemName.split("+")[1])
					ItemName = ItemName.split("+")[0]
			except:
				pass
			
			PickUpListNames.append(ItemName)
		except:
			pass
	chat.AppendChat(1, "Gespeicherte Item PickUp Informationen wurden geladen!")
except:
	pass

## Whisperbot Save
try:
	lines = open("lib/whisperanswers.save", "r+").readlines()
	for line in lines:
		(KeyWord, Answer) = line.split("#")
		if not KeyWord in AnswerTuple:
			AnswerTuple[KeyWord] = []
		
		AnswerTuple[KeyWord].append(Answer.split("\n")[0])
	chat.AppendChat(1, "Whisper Einstellungen wurden erfolgreich geladen.")
except:
	pass
	
class NewLevelBotDialog(ui.Window):

	MobList = []
	VidList = []
	
	SkillList = []
	SkillIconList = []
	SkillIconIndex = []
	ActiveSkillList = []
	vid = 0

	ConfigArray = [10, 50, 50, 0]
	Buttons = [["Activate Log", 1], ["Use Attack Packets", 1], ["Auto Revive (75%)", 1], ["Attack Metin", 0], ["Attack Boss", 0], ["Walk to Mob", 1], ["Range (40)", 0], ["Item Pickup", 1], ["Buffmodus", 0], ["Range Pickup(walk)", 0]]
	IsBuff = { "1": {"IsBuff": 0}, "2": {"IsBuff": 0}, "3": {"IsBuff": 1}, "4": {"IsBuff": 1}, "5": {"IsBuff": 0}, "6": {"IsBuff": 0}, "16": {"IsBuff": 0}, "17": {"IsBuff": 0}, "18": {"IsBuff": 0}, "19": {"IsBuff": 1}, "20": {"IsBuff": 0}, "21": {"IsBuff": 0}, "31": {"IsBuff": 0}, "32": {"IsBuff": 0}, "33": {"IsBuff": 0}, "34": {"IsBuff": 1}, "35": {"IsBuff": 0}, "36": {"IsBuff": 0}, "46": {"IsBuff": 0}, "47": {"IsBuff": 0}, "48": {"IsBuff": 0}, "49": {"IsBuff": 1}, "50": {"IsBuff": 0}, "51": {"IsBuff": 0}, "61": {"IsBuff": 0}, "62": {"IsBuff": 0}, "63": {"IsBuff": 1}, "64": {"IsBuff": 1}, "65": {"IsBuff": 1}, "66": {"IsBuff": 0}, "76": {"IsBuff": 0}, "77": {"IsBuff": 0}, "78": {"IsBuff": 0}, "79": {"IsBuff": 1}, "80": {"IsBuff": 1}, "81": {"IsBuff": 0}, "91": {"IsBuff": 0}, "92": {"IsBuff": 0}, "93": {"IsBuff": 0}, "94": {"IsBuff": 1}, "95": {"IsBuff": 1}, "96": {"IsBuff": 1}, "106": {"IsBuff": 0}, "107": {"IsBuff": 0}, "108": {"IsBuff": 0}, "109": {"IsBuff": 1}, "110": {"IsBuff": 1}, "111": {"IsBuff": 1}}
	
	FarmmodeStamp = 0
	Farmmode = ""

	CheckDelayStamp = 0
	
	ProcessTimeStamp = 0
	ReviveTimeStamp = 0
	BannedMobs = []
	RangeCheckVids = []
	Position = (0, 0, 0)
	
	State = "Stop"
	WaitForPercent = 0
	
	ItemData = []
	Itemmode = ""
	
	BuffVid = 0
	BuffState = "Stop"
	
	def __init__(self):
		ui.Window.__init__(self)
		VidList = GetVidList()
		for vid in VidList:
			Instance = chr.GetInstanceType(vid)
			if Instance != chr.INSTANCE_TYPE_PLAYER:
				VidList.remove(vid)
				m2botlibpadmak.DeleteVIDFromList(vid)
				
		self.BackUpState = "nothing"
		self.AddSkillIcons()
		self.AddPotionBar()
		self.AddGUI()
		
		try:
			import m2botlibpadmak
			m2botlibpadmak.RegisterVIDCallback(self.OnRegisterVID)
			m2botlibpadmak.FireRegisteredVIDs()
		except:
			chat.AppendChat(1, "Levelbot konnte nicht gestartet werden.")
			self.__del__()
			return
			
		try:
			import m2BotLib
			m2BotLib.EnableWallhack()
		except:
			chat.AppendChat(1, "Wallhack Module konnte nicht geladen werden.")
			
		try:
			import api
			api.SetHandlers(self.OnRegisterItemVid, self.DeleteItemTestFunc)
		except:
			chat.AppendChat(1, "Item Module konnte nicht geladen werden.")

	def DeleteItemTestFunc(self, vid):
		chat.AppendChat(1, "Remove: " + str(vid))
	
	def AskBuffCharacter(self, vid):
		self.BuffState = "Start"
		chat.AppendChat(1, "Du hast " + chr.GetNameByVID(vid) + "(" + str(vid) + ") ausgewählt.")
		self.AskBuffCharacterDialog.Close()
	
	def OnUpdate(self):
		## BuffMode:
		global BuffVid
		if self.IsBuffMode():
			if self.BuffState == "Stop":
				self.BuffState = "Select"
				HookOpenTargetBoard()
				chat.AppendChat(1, "Bitte visiere den zu buffenden Charakter an.")
			if BuffVid != self.BuffVid and self.BuffState != "Start":
				self.BuffVid = BuffVid
				if self.BuffState == "Select":
					self.AskBuffCharacterDialog = uiCommon.QuestionDialog()
					self.AskBuffCharacterDialog.SetText("Willst du " + chr.GetNameByVID(BuffVid) + " buffen?")
					self.AskBuffCharacterDialog.SetAcceptEvent(lambda : self.AskBuffCharacter(self.BuffVid))
					self.AskBuffCharacterDialog.SetCancelEvent(lambda : self.AskBuffCharacterDialog.Close())
					self.AskBuffCharacterDialog.Open()					
		else:
			if self.BuffState != "Stop":
				chat.AppendChat(1, "Buffmode wurde deaktiviert.")
				self.BuffState = "Stop"
				self.BuffVid = 0
				self.vid = 0
				UnHookOpenTargetBoard()
	
		## Item Pickup
		ItemList = []
		
		for Item in self.ItemData:
			try:
				(x, y, vid, vnum) = Item
				if GetDistance(x, y) < 50:
					net.SendItemPickUpPacket(vid)
					self.ItemData.remove(Item)
					if self.BackUpState != "nothing":
						self.State = self.BackUpState
						self.BackUpState = "nothing"
				else:
					if self.IsItemPickUp():
						ItemList.append(GetDistance(x, y))
			except:
				pass
		try:
			smallest = min(ItemList)
			Index = ItemList.index(smallest)
			
			if GetDistance(self.ItemData[Index][0], self.ItemData[Index][1]) >= 800:
				if not self.IsRangePickUp():
					if self.Itemmode == "mount":
						net.SendChatPacket("/ride")
						self.Itemmode = ""
					return
			
			if self.BackUpState == "nothing":
				self.BackUpState = self.State
				self.State = "Stop"
				
			if player.IsMountingHorse():
				net.SendChatPacket("/unmount")
				self.Itemmode = "mount"
				
			player.SetAttackKeyState(FALSE)
			chr.MoveToDestPosition(player.GetMainCharacterIndex(), self.ItemData[Index][0], self.ItemData[Index][1])
		except:
			if self.Itemmode == "mount":
				net.SendChatPacket("/ride")
				self.Itemmode = ""
			pass
	
	def OnRegisterItemVid(self, x, y, vid, vnum):
		LocalX, LocalY = background.GlobalPositionToLocalPosition(x, y)
		if self.IsLogActivated():
			chat.AppendChat(1, "Append Item VID: " + str(LocalX) + ", " + str(LocalY) + ", " + str(vid) + ", " + str(vnum))
			chat.AppendChat(1, "Item Distance: " + str(GetDistance(LocalX, LocalY)))
			chat.AppendChat(1, "Item Name: " + str(item.GetItemName(item.SelectItem(vnum))))
		PickUpListNames = GetPickUpListNames()
		try:
			ItemName = item.GetItemName(item.SelectItem(vnum))
			try:
				if ItemName.lower().find("stein ") != -1: 
					pass
				else:
					int(ItemName.split("+")[1])
					ItemName = ItemName.split("+")[0]
			except:
				pass
			
			PickUpListNames.index(ItemName)
			
			if GetDistance(LocalX, LocalY) >= 250:
				if self.IsLogActivated():
					chat.AppendChat(1, "Item liegt zu weit weg")
				if not [LocalX, LocalY, vid, vnum] in self.ItemData:
					self.ItemData.append([LocalX, LocalY, vid, vnum])
			else:
				net.SendItemPickUpPacket(vid)
			
			if BackUpState != "Stop":
				self.State = BackUpState
				
		except:
			pass
	
	def OnRegisterVID(self, vid):
		VidList = GetVidList()
		try:
			VidList.index(vid)
		except:
			if self.IsLogActivated() and self.State != "Stop":
				chat.AppendChat(chat.CHAT_TYPE_INFO, str(app.GetTime()) + ": Caught VID: " + str(vid))
			if not player.GetMainCharacterIndex() == vid:
				VidList.append(vid)
	
	def Config(self, arg):
		global Options
		self.ConfigGui = []
		self.Board = ui.BoardWithTitleBar()
		self.Board.SetSize(249, 55 + 25 * len(Options))
		self.Board.SetCenterPosition()
		self.Board.AddFlag("movable")
		self.Board.AddFlag("float")
		self.Board.SetCloseEvent(self.HideConfig)
		self.Board.Show()
		
		if arg != "Configure":
			self.Board.SetTitleName("Options Levelbot")
			
			y = 45
			for bla in Options:
				Text = ui.TextLine()
				Text.SetDefaultFontName()
				Text.SetParent(self.Board)
				Text.SetPosition(25, y)
				Text.SetText(str(bla[0]))
				Text.Show()
				
				Button = ui.Button()
				Button.SetParent(self.Board)
				Button.SetUpVisual("d:/ymir work/ui/public/large_button_01.sub")
				Button.SetOverVisual("d:/ymir work/ui/public/large_button_02.sub")
				Button.SetDownVisual("d:/ymir work/ui/public/large_button_03.sub")
				Button.SetPosition(130, y - 3)
				if isinstance(bla[1], str):
					Button.SetText("deaktiviert")
				else:
					Button.SetText("öffnen")
					Button.SetEvent(lambda event = bla[1]: event().Show())
				Button.Show()			
				y += 25
				self.ConfigGui.append([Button, Text])
		else:
			self.Board.SetTitleName("Configurations Levelbot")
			
			y = 45
			for bla in self.Buttons:
				Text = ui.TextLine()
				Text.SetDefaultFontName()
				Text.SetParent(self.Board)
				Text.SetPosition(25, y)
				Text.SetText(str(bla[0]))
				Text.Show()
				
				Button = ui.Button()
				Button.SetParent(self.Board)
				Button.SetUpVisual("d:/ymir work/ui/public/large_button_01.sub")
				Button.SetOverVisual("d:/ymir work/ui/public/large_button_02.sub")
				Button.SetDownVisual("d:/ymir work/ui/public/large_button_03.sub")
				if bla[1] == 1:			
					Button.SetText("on")
				else:
					Button.SetText("off")
				Button.SetPosition(130, y - 3)
				Button.SetEvent(lambda arg = bla: self.ChangeConfig(arg))
				Button.Show()			
				y += 25
				self.ConfigGui.append([Button, Text])
			
	def ChangeState(self, arg):
		self.State = arg
		chat.AppendChat(chat.CHAT_TYPE_INFO, str(app.GetTime()) + " : " + str(arg) + " Levelbot.")
		if arg == "Start":
			self.Position = player.GetMainCharacterPosition()
			HookSetHPTargetBoard()
			self.AddMobData()
		else:
			player.SetAttackKeyState(FALSE)
			UnHookSetHPTargetBoard()
			self.BackUpState = "nothing"
			
	def ChangeOptions(self, arg):
		chat.AppendChat(1, str(arg))
	
	def ChangeConfig(self, arg):
		Index = self.Buttons.index(arg)
		State = 1
		if arg[1] == 1:
			State = 0
		self.Buttons[Index] = [arg[0], State]
		
		if Index == 5:
			self.RangeCheckVids = []
		
		if State == 0:
			self.ConfigGui[Index][0].SetText("off")
		else:
			self.ConfigGui[Index][0].SetText("on")
		self.ConfigGui[Index][0].SetEvent(lambda arg = [arg[0], State]: self.ChangeConfig(arg))
		
	def HideConfig(self):
		self.Board.Hide()

	def IsLogActivated(self):
		if self.Buttons[0][1] == 1:
			return 1
	
	def UseAttackPackets(self):
		if self.Buttons[1][1] == 1:
			return 1

	def IsAutoRevive(self):
		if self.Buttons[2][1] == 1:
			return 1
			
	def IsAttackMetin(self):
		if self.Buttons[3][1] == 1:
			return 1
			
	def IsAttackBoss(self):
		if self.Buttons[4][1] == 1:
			return 1
			
	def IsWalkToMob(self):
		if self.Buttons[5][1] == 1:
			return 1
			
	def IsRangeCheck(self):
		if self.Buttons[6][1] == 1:
			return 1

	def IsItemPickUp(self):
		if self.Buttons[7][1] == 1:
			return 1

	def IsBuffMode(self):
		if self.Buttons[8][1] == 1:
			return 1
			
	def IsRangePickUp(self):
		if self.Buttons[9][1] == 1:
			return 1

	def AddGUI(self):
		Text = ["Configure", "Options"]
		State = ["Stop", "Start"]
		self.GUI = []
		x = 133
		y = len(self.items) * - 60 + 90
		for i in xrange(2):
			ConfigButton = ui.Button()
			ConfigButton.SetUpVisual("d:/ymir work/ui/public/large_button_01.sub")
			ConfigButton.SetOverVisual("d:/ymir work/ui/public/large_button_02.sub")
			ConfigButton.SetDownVisual("d:/ymir work/ui/public/large_button_03.sub")
			ConfigButton.SetText(Text[i])
			ConfigButton.SetPosition(wndMgr.GetScreenWidth() - x, wndMgr.GetScreenHeight() / 2 - y)
			ConfigButton.SetEvent(lambda arg = Text[i]: self.Config(arg))
			ConfigButton.Show()
			x += 88
			self.GUI.append(ConfigButton)
		
		x = 133
		y = len(self.items) * - 60 + 50
		for i in xrange(2):
			ConfigButton = ui.Button()
			ConfigButton.SetUpVisual("d:/ymir work/ui/public/large_button_01.sub")
			ConfigButton.SetOverVisual("d:/ymir work/ui/public/large_button_02.sub")
			ConfigButton.SetDownVisual("d:/ymir work/ui/public/large_button_03.sub")
			ConfigButton.SetText(State[i])
			ConfigButton.SetPosition(wndMgr.GetScreenWidth() - x, wndMgr.GetScreenHeight() / 2 - y)
			ConfigButton.SetEvent(lambda arg = State[i]: self.ChangeState(arg))
			ConfigButton.Show()
			x += 88
			self.GUI.append(ConfigButton)
	
	def AddPotionBar(self):
		self.Sliderbars = []
		self.items = [item.GetItemName(item.SelectItem(int(70038))), item.GetItemName(item.SelectItem(int(27006))), item.GetItemName(item.SelectItem(int(27003))), "Level"]
		IconData = [item.GetIconImageFileName(item.SelectItem(int(70038))), item.GetIconImageFileName(item.SelectItem(int(27006))), item.GetIconImageFileName(item.SelectItem(int(27003))), "d:/ymir work/ui/game/quest/questicon/level_18.sub"]
		Description = [["Deaktiviert", 0.0], ["50%", 0.5], ["50%", 0.5], ["10 Level", 0.5]]
		x = 150
		y = 160 - (len(IconData) * 60)
		for bla in IconData:
			try:
				Index = IconData.index(bla)
			except:
				return
				
			Image = ui.ExpandedImageBox()
			Image.SetPosition(wndMgr.GetScreenWidth() - x, wndMgr.GetScreenHeight() / 2 - y)
			if self.items[IconData.index(bla)] == "Level":
				Image.SetPosition(wndMgr.GetScreenWidth() - x - 33, wndMgr.GetScreenHeight() / 2 - y)
			Image.LoadImage(str(bla))
			Image.Show()
		
			Text = ui.TextLine()
			Text.SetDefaultFontName()
			Text.SetPosition(wndMgr.GetScreenWidth() - 120, wndMgr.GetScreenHeight() / 2 - (y - 10))
			if self.items[IconData.index(bla)] == "Level":
				Text.SetPosition(wndMgr.GetScreenWidth() - 150, wndMgr.GetScreenHeight() / 2 - (y - 10))
			Text.SetFeather()				
			Text.SetText(Description[IconData.index(bla)][0])
			Text.SetOutline()
			Text.Show()

			Slider = ui.SliderBar()
			Slider.SetPosition(wndMgr.GetScreenWidth() - 220, wndMgr.GetScreenHeight() / 2 - (y - 40))
			Slider.SetEvent(ui.__mem_func__(self.SetPotion))
			Slider.SetSliderPos(Description[IconData.index(bla)][1])
			Slider.Show()
			
			self.Sliderbars.append([self.items[IconData.index(bla)], Slider, Text, Image])
			y += 60

	def SetPotion(self):
		for Array in self.Sliderbars:
			ItemName = Array[0]
			Slider = Array[1]
			TextLine = Array[2]
			SliderPos = Slider.GetSliderPos() * 100
			
			if ItemName == item.GetItemName(item.SelectItem(int(70038))):
				if int(Slider.GetSliderPos() * 30 + 9) == 9:
					TextLine.SetText("Deaktiviert")
					Puller = 0
				else:
					TextLine.SetText(str(int(Slider.GetSliderPos() * 30 + 9)) + "s")
					Puller = int(Slider.GetSliderPos() * 30 + 9)
			elif ItemName == "Level":
				TextLine.SetText(str(int(Slider.GetSliderPos() * 20)) + " Level")
				Level = int(Slider.GetSliderPos() * 20)
				self.BannedMobs = []
			else:
				TextLine.SetText(str(int(SliderPos)) + "%")
				if ItemName == item.GetItemName(item.SelectItem(int(27003))):
					PotionRed = SliderPos
				else:
					PotionBlue = SliderPos
			
		self.ConfigArray = [Level, PotionRed, PotionBlue, Puller]
	
	def AddMobData(self):
		if self.BuffState == "Start":
			try:
				(x, y, z) = chr.GetPixelPosition(self.BuffVid)
				self.WalkToMob(x, y, z, self.BuffVid)
			except:
				self.ChangeState("Stop")
				chat.AppendChat(1, "Der ausgewählte Charakter ist entweder offline oder außer Reichtweite.")
			return

		self.MobList = []
		Count = 0
		VidList = GetVidList()
		if len(VidList) >= 1000:
			TmpList = []
			for vid in VidList:
				if not chr.GetInstanceType(vid) == chr.INSTANCE_TYPE_PLAYER:
					TmpList.append(vid)
					
			while len(TmpList) > 500:
				VidList.remove(TmpList[0])
				m2botlibpadmak.DeleteVIDFromList(TmpList[0])
				TmpList.remove(TmpList[0])
		
		if len(self.BannedMobs) >= 400:
			while len(self.BannedMobs) > 150:
				self.BannedMobs.remove(self.BannedMobs[0])
				
		for mob in VidList:
			if chr.GetInstanceType(mob) == chr.INSTANCE_TYPE_ENEMY or nonplayer.GetGradeByVID(mob) >= 5 and chr.GetInstanceType(mob) != chr.INSTANCE_TYPE_NPC:
				if nonplayer.GetGradeByVID(mob) >= 4:
					if chr.GetInstanceType(mob) == chr.INSTANCE_TYPE_ENEMY:
						type = "Boss"
					else:
						type = "Metin"
				else:
					type = "Monster"
				chr.SelectInstance(mob)
				level = nonplayer.GetLevelByVID(mob)
				if self.IsRangeCheck():
					if not self.CheckDistance(mob):
						self.RangeCheckVids.append(mob)
				if level > self.ConfigArray[0] + player.GetStatus(player.LEVEL):
					if self.IsLogActivated():
						chat.AppendChat(chat.CHAT_TYPE_INFO, "High level Mob registered: " + str(chr.GetNameByVID(mob)))
					self.BannedMobs.append(mob)
				if self.CheckBannedVids(mob) and self.CheckRangeVids(mob):
					vid = int(mob)
					vnum = chr.GetRace(mob)
					mobX, mobY, mobZ = chr.GetPixelPosition(mob)
					Distance = player.GetCharacterDistance(mob)
					MobData = { 
						"VNUM":vnum,
						"LEVEL":level,
						"X":mobX,
						"Y":mobY,
						"Z":mobZ,
						"VID":vid,
						"COUNT":Count,
						"DISTANCE":Distance,
						"TYPE":type
						}
					self.MobList.append(MobData)
					Count += 1
		
		if len(self.MobList) != 0:
			self.CheckNearestMob()
			
		## needs a 100% working IsMobAlive Func!
		else:
			player.SetAttackKeyState(FALSE)
			chr.MoveToDestPosition(int(player.GetMainCharacterIndex()), int(self.Position[0]), int(self.Position[1]))
		
	def CheckDistance(self, vid):
		(mobX, mobY, mobZ) = chr.GetPixelPosition(vid)
		(botX, botY, botZ) = self.Position
		
		if GetPositiveValue(botX - mobX) < 40 * 100 and GetPositiveValue(botY - mobY) < 40 * 100:
			return 1
		
	def CheckRangeVids(self, vid):
		try:
			if self.RangeCheckVids.index(vid) != -1:
				return 0
		except:
			return 1
			
	def CheckBannedVids(self, vid):
		try:
			if self.BannedMobs.index(vid) != -1:
				return 0
		except:
			return 1
			
	def CheckNearestMob(self):
		MetinList = []
		BossList = []
		MonsterList = []
		Pattern = []
		
		for data in self.MobList:
			Distance = data["DISTANCE"]
			Type = data["TYPE"]
			if Type == "Metin" and self.IsAttackMetin():
				MetinList.append(Distance)
			if Type == "Boss" and self.IsAttackBoss():
				BossList.append(Distance)
			if Type == "Monster":
				MonsterList.append(Distance)
			
		for i in MetinList:
			Pattern.append(i)
		for i in BossList:
			Pattern.append(i)
		if len(Pattern) == 0:
			for i in MonsterList:
				Pattern.append(i)
		
		try:
			SmallestDistance = (min(Pattern))
		except:
			return
		
		for data in self.MobList:
			Distance = data["DISTANCE"]
			if float(SmallestDistance) == float(Distance):
				x = int(data["X"])
				y = int(data["Y"])
				z = int(data["Z"])
				vid = int(data["VID"])
				break

		if self.IsLogActivated():
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Next Mob: " + str(chr.GetNameByVID(vid)))

		self.WalkToMob(x, y, z, vid)
		
	def SendAttackPackets(self):
		ranking40 = []
		MobList = []
		for mob in self.MobList:
			if self.CheckBannedVids(mob["VID"]):	
				MobList.append(mob["DISTANCE"])
		if len(self.MobList) >= 40:
			for i in xrange(40):
				try:
					smallest = min(MobList)
					MobList.remove(smallest)
					ranking40.append(smallest)
				except:
					pass
				
			for mob in self.MobList:
				try:
					ranking40.index(mob["DISTANCE"])
					m2BotLib.SendAttackPacket(mob["VID"])
				except:
					pass
		else:
			for mob in self.MobList:
				m2BotLib.SendAttackPacket(mob["VID"])
		
	def WalkToMob(self, x, y, z, vid):
		self.vid = vid
		myVid = player.GetMainCharacterIndex()
		myx, myy, myz = player.GetMainCharacterPosition()
		distance = 135
		
		if myx < x:
			self.aimx = int(x) - distance
		else:
			self.aimx = int(x)  + distance
		if myy < y:
			self.aimy = int(y) - distance
		else:
			self.aimy = int(y) + distance
			
			
		if self.IsWalkToMob():
			chr.MoveToDestPosition(int(myVid), int(self.aimx), int(self.aimy))
		else:
			chr.SelectInstance(myVid)
			chr.SetPixelPosition(int(x), int(y), int(z))
			self.Debug()
			
	def Debug(self):
		player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
		player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
	
	def PursuitMob(self):
		if self.vid == 0:
			return
		
		if self.BuffState == "Start":
			self.vid = self.BuffVid
		
		(myx, myy, myz) = player.GetMainCharacterPosition()
		try:	
			(mobX, mobY, mobZ) = chr.GetPixelPosition(self.vid)
		except:
			self.AddMobData()
			return
		
		if player.GetCharacterDistance(self.vid) >= 210:
			self.WalkToMob(mobX, mobY, mobZ, self.vid)
			player.SetAttackKeyState(FALSE)
#			chat.AppendChat(chat.CHAT_TYPE_INFO, "Information: Mob out of range")
		else:
			chr.SelectInstance(player.GetMainCharacterIndex())
			chr.SetRotation(GetDegree(mobX, mobY, myx, myy))
			if self.BuffState != "Start":
				player.SetAttackKeyState(TRUE)
#			chat.AppendChat(chat.CHAT_TYPE_INFO, "Information: Mob in range")
			return

	def CheckMobLife(self):
		if not IsMobAlive(self.vid):
			if self.IsLogActivated():
				chat.AppendChat(chat.CHAT_TYPE_INFO, "Dead Mob registered: " + str(chr.GetNameByVID(self.vid)))
			try:
				VidList = GetVidList()
				VidList.remove(self.vid)
				m2botlibpadmak.DeleteVIDFromList(self.vid)
			except:
				pass
			player.SetAttackKeyState(FALSE)
			self.AddMobData()
		
	def CheckPlayerLife(self):
		if player.GetStatus(player.HP) <= 0:
			self.State = "Revive"
			self.ReviveTimeStamp = app.GetTime() + 15
			if self.IsLogActivated():
				chat.AppendChat(chat.CHAT_TYPE_INFO, str(app.GetTime()) + ": Player Character dead, restarting in 15 seconds")
		
	def OnRender(self):
		if app.GetTime() >= self.CheckDelayStamp + 1 and self.CheckDelayStamp != 0:
			self.CheckDelayStamp = 0
			self.AddMobData()
	
		if app.GetTime() >= self.FarmmodeStamp + 1 and self.Farmmode == "Remount" and not player.IsMountingHorse():
			self.Farmmode = ""
			for Item in self.ItemData:
				self.ItemData.remove(Item)
			net.SendChatPacket("/ride")
			self.CheckDelayStamp = app.GetTime()
			player.SetAttackKeyState(TRUE)
	
		if self.ReviveTimeStamp != 0 and self.ReviveTimeStamp < app.GetTime():
			self.ReviveTimeStamp = 0
			VidList = GetVidList()
			net.SendChatPacket("/restart_here")
			for vid in VidList:
				Instance = chr.GetInstanceType(vid)
				if Instance != chr.INSTANCE_TYPE_PLAYER:
					VidList.remove(vid)
					m2botlibpadmak.DeleteVIDFromList(vid)
			player.SetAttackKeyState(FALSE)
			self.WaitForPercent = 75
	
		if self.State == "Revive" and player.GetStatus(player.HP) > 0:
			if not self.BuffState == "Start":
				self.State = "Waiting"
	
		if self.State == "Waiting" and player.GetStatus(player.HP) < 0:
			self.CheckPlayerLife()		
			
		if self.State == "Waiting" and self.WaitForPercent > 0:
			if DivideToFloat(player.GetStatus(player.HP), player.GetStatus(player.MAX_HP)) * 100 >= int(self.WaitForPercent):
				if self.IsLogActivated():
					chat.AppendChat(chat.CHAT_TYPE_INFO, str(app.GetTime()) + ": 75 percent of max HP reached, restarting Levelbot")
				self.WaitForPercent = 0
				self.ProcessTimeStamp = app.GetGlobalTimeStamp()
				self.ChangeState("Start")
			else:
				if self.ConfigArray[1] > 0:
					for i in xrange(player.INVENTORY_PAGE_SIZE*2):
						ItemValue = player.GetItemIndex(i)
						if ItemValue == 27001 or ItemValue == 27002 or ItemValue == 27003:
							net.SendItemUsePacket(i)

		if self.State != "Start":
			return
			
		self.CheckMobLife()

		if self.IsAutoRevive():
			self.CheckPlayerLife()

		if self.vid != 0:
			self.PursuitMob()

		for Skills in self.ActiveSkillList:
			SkillIndex = int(Skills["INDEX"])
			SlotIndex = int(Skills["COUNT"])
			BuffDuration = skill.GetDuration(SkillIndex, player.GetSkillCurrentEfficientPercentage(SlotIndex))
			SkillDuration = skill.GetSkillCoolTime(SkillIndex, player.GetSkillCurrentEfficientPercentage(SlotIndex))
			IsBuffSkill = self.IsBuff[str(SkillIndex)]["IsBuff"]
			
			if IsBuffSkill:
				SkillDuration = BuffDuration + 0.5
			if player.GetSkillCoolTime(SlotIndex)[1] >= SkillDuration:
				if player.IsMountingHorse():
					if IsBuffSkill:
						for Item in self.ItemData:
							self.ItemData.remove(Item)
						net.SendChatPacket("/unmount")
						player.ClickSkillSlot(int(Skills["COUNT"]))
						self.Farmmode = "Remount"
						self.FarmmodeStamp = app.GetTime()
				else:
					if self.BuffState == "Start":
						if IsBuffSkill:
							net.SendOnClickPacket(self.BuffVid)
							player.ClickSkillSlot(int(Skills["COUNT"]))
					else:
						player.ClickSkillSlot(int(Skills["COUNT"]))

		PotionRed = self.ConfigArray[1]
		PotionBlue = self.ConfigArray[2]
		Puller = self.ConfigArray[3]
		
	##Auto Potions:
		#Auto Potion Red
		Maximum_TP = player.GetStatus(player.MAX_HP)
		Actual_TP = player.GetStatus(player.HP)
		if (float(Actual_TP) / (float(Maximum_TP)) * 100) < int(PotionRed):
			for i in xrange(player.INVENTORY_PAGE_SIZE*2):
				ItemValue = player.GetItemIndex(i)
				if ItemValue == 27001 or ItemValue == 27002 or ItemValue == 27003:
					net.SendItemUsePacket(i)
					
		#Auto Potion Blue
		Maximum_MP = player.GetStatus(player.MAX_SP)
		Actual_MP = player.GetStatus(player.SP)
		if (float(Actual_MP) / (float(Maximum_MP)) * 100) < int(PotionBlue):
			for i in xrange(player.INVENTORY_PAGE_SIZE*2):
				ItemValue = player.GetItemIndex(i)
				if ItemValue == 27004 or ItemValue == 27005 or ItemValue == 27006:
					net.SendItemUsePacket(i)
			
		#Mob Puller
		if int(Puller) > 0:
			if int(int(self.ProcessTimeStamp) + int(Puller)) < int(app.GetGlobalTimeStamp()):

				#Attack Packets
				if self.UseAttackPackets:
					self.SendAttackPackets()
				
				#Tapferkeitsumhänge
				else:				 
					for i in xrange(player.INVENTORY_PAGE_SIZE*2):
						ItemValue = player.GetItemIndex(i)
						if ItemValue == 70038:
							net.SendItemUsePacket(i)
							break
				
				self.ProcessTimeStamp = app.GetGlobalTimeStamp()
				if self.IsLogActivated():
					chat.AppendChat(chat.CHAT_TYPE_INFO, "Attack Packets: Process Timestamp: " + str(self.ProcessTimeStamp) + ", Next Pullertimestamp: " + str(int(int(self.ProcessTimeStamp) + int(Puller))))

	def AddSkillIcons(self):
		self.SkillList = []
		try:
			handle = app.OpenTextFile(app.GetLocalePath() + "/skilldesc.txt")
			count = app.GetTextFileLineCount(handle)
		except IOError:
			chat.AppendChat(1, "Could not load " + app.GetLocalePath() + "/skilldesc.txt")

		for i in xrange(count):
			line = app.GetTextFileLine(handle, i)
			if str(line).count("\t") >= 21:
				SkillData = str(line).split("\t")
				SkillName = str(SkillData[2])
				SkillIconName = str(SkillData[12])
				SkillIndex = str(SkillData[0])
				SkillData = { 
					"NAME":SkillName,
					"ICON":SkillIconName,
					"INDEX":SkillIndex,
					}
				self.SkillList.append(SkillData)
		
		RaceGroupInfo = GetClass()
		Class = str(RaceGroupInfo).split("/")[0]
		group = str(RaceGroupInfo).split("/")[1]
		if Class == "Warrior":
			SkillIndex = 1
			if int(group) == 2:
				SkillIndex = 16
		elif Class == "Assassin":
			SkillIndex = 31
			if int(group) == 2:
				SkillIndex = 46
		elif Class == "Sura":
			SkillIndex = 61
			if int(group) == 2:
				SkillIndex = 76
		elif Class == "Shaman":
			SkillIndex = 91
			if int(group) == 2:
				SkillIndex = 106
				
		self.SkillIconIndex = []
		Count = 0
		for SkillValue in xrange(NewSkillsEnable()):
			try:
				Skillname = skill.GetSkillName(int(SkillIndex))
				SkillIndex += 1
				for Skills in self.SkillList:
					SkillNameList = Skills["NAME"]
					if str(Skillname) == str(SkillNameList):
						Count += 1
						SkillName = Skills["NAME"]
						SkillIcon = Skills["ICON"]
						SkillIndexAppend = SkillIndex - 1
						PrivateSkillData = { 
							"NAME":SkillName,
							"ICON":SkillIcon,
							"INDEX":SkillIndexAppend,
							"COUNT":Count,
							}
						self.SkillIconIndex.append(PrivateSkillData)
			except:
				pass
			
		self.GetSkillIcon()
		
	def GetSkillIcon(self):
		self.SkillIconList = []
		RaceGroupInfo = GetClass()
		Class = str(RaceGroupInfo).split("/")[0]
		x = 80
		i = 0
#		for Skills in self.SkillIconIndex:
#			chat.AppendChat(chat.CHAT_TYPE_INFO, "Skill Index: " + str(int(Skills["INDEX"]) - 1))
#			chat.AppendChat(chat.CHAT_TYPE_INFO, "Skill Name: " + str(Skills["NAME"]))
#			chat.AppendChat(chat.CHAT_TYPE_INFO, "Skill Icon: d:/ymir work/ui/skill/" + str(Class).lower() + "/" + str(Skills["ICON"]))

		for Skills in self.SkillIconIndex:
			SkillIconButton = SkillButton()
			SkillIconButton.SetPosition(wndMgr.GetScreenWidth() - x, wndMgr.GetScreenHeight() / 2 - 160)
			SkillIconButton.SetUpVisual("d:/ymir work/ui/skill/" + str(Class).lower() + "/" + str(Skills["ICON"]) + "_0" + str(self.GetSkillLevel(str(Skills["NAME"]))) + ".sub")
			SkillIconButton.SetOverVisual("d:/ymir work/ui/skill/" + str(Class).lower() + "/" + str(Skills["ICON"]) + "_0" + str(self.GetSkillLevel(str(Skills["NAME"]))) + ".sub")
			SkillIconButton.SetDownVisual("d:/ymir work/ui/skill/" + str(Class).lower() + "/" + str(Skills["ICON"]) + "_0" + str(self.GetSkillLevel(str(Skills["NAME"]))) + ".sub")
			SkillIconButton.SetText("Off")
			SkillIconButton.SetTextColor(0.1, 0.7, 1.0)
			SkillIconButton.SetButtonFontName("MAGNETO:16")
			SkillIconButton.SetTextPosition(0, 22)
			SkillIconButton.Show()
			
			SkillActivated = SkillButton()
			SkillActivated.SetPosition(wndMgr.GetScreenWidth() - x, wndMgr.GetScreenHeight() / 2 - 160)
			SkillActivated.SetUpVisual("d:/ymir work/ui/public/slot_cover_button_03.sub")
			SkillActivated.SetOverVisual("d:/ymir work/ui/public/slot_cover_button_03.sub")
			SkillActivated.SetDownVisual("d:/ymir work/ui/public/slot_cover_button_03.sub")
			SkillActivated.Hide()
			
			Mod = self.SkillIconIndex[i]			
			SkillIconButton.SetEvent(lambda arg = Mod: self.SelectSkill(arg))
			SkillActivated.SetEvent(lambda arg = Mod: self.SelectSkill(arg))
			self.SkillIconList.append(SkillIconButton)
			self.SkillIconList.append(SkillActivated)			
			x += 37
			i += 1
			
	def SelectSkill(self, skillindex):
		SkillEvent = skillindex["COUNT"]
		SkillIndex = skillindex["INDEX"]
		SkillName = skillindex["NAME"]

		Search = 0
		for test in self.ActiveSkillList:
			if test["INDEX"] == SkillIndex:
				Search = 1
		ActiveSkillData = { 
			"COUNT":SkillEvent,
			"INDEX":SkillIndex,
			"NAME":SkillName,
		}
		if Search == 0:
			self.ActiveSkillList.append(ActiveSkillData)
			chat.AppendChat(chat.CHAT_TYPE_INFO, str(SkillName) + " wurde aktiviert.")
			self.SkillIconList[(int(SkillEvent) - 1)*2].SetText("On")
			self.SkillIconList[(int(SkillEvent) - 1)*2 + 1].Show()
		else:
			self.ActiveSkillList.remove(ActiveSkillData)
			chat.AppendChat(chat.CHAT_TYPE_INFO, str(SkillName) + " wurde deaktiviert.")
			self.SkillIconList[(int(SkillEvent) - 1)*2].SetText("Off")
			self.SkillIconList[(int(SkillEvent) - 1)*2 + 1].Hide()
			
	def GetSkillLevel(self, skillname):
		SkillIconLevel = []
		for Skill in self.SkillIconIndex:
			Skillgrade = player.GetSkillGrade(Skill["COUNT"])
			Skilllevel = player.GetSkillLevel(Skill["COUNT"])
			Skillname = Skill["NAME"]
			SkillLevelData = { 
				"GRADE":Skillgrade,
				"LEVEL":Skilllevel,
				"NAME":Skillname,
			}
			SkillIconLevel.append(SkillLevelData)
			
		for SkillData in SkillIconLevel:
			Skillname = str(SkillData["NAME"])
			SkillLevel = SkillData["LEVEL"]
			if 1 == SkillData["GRADE"]:
				SkillLevel += 19
			elif 2 == SkillData["GRADE"]:
				SkillLevel += 29
			elif 3 == SkillData["GRADE"]:
				SkillLevel = 40
				
			if str(Skillname) == str(skillname):
				if int(SkillLevel) < 20:
					return 1
				elif int(SkillLevel) < 30:
					return 2
				else:
					return 3
		
	def __del__(self):
		ui.Window.__del__(self)

class SkillButton(ui.Window):

	def __init__(self, layer = "UI"):
		ui.Window.__init__(self, layer)

		self.eventFunc = None
		self.eventArgs = None

		self.ButtonText = None
		self.ToolTipText = None

	def __del__(self):
		ui.Window.__del__(self)

		self.eventFunc = None
		self.eventArgs = None

	def RegisterWindow(self, layer):
		self.hWnd = wndMgr.RegisterButton(self, layer)

	def SetUpVisual(self, filename):
		wndMgr.SetUpVisual(self.hWnd, filename)

	def SetOverVisual(self, filename):
		wndMgr.SetOverVisual(self.hWnd, filename)

	def SetDownVisual(self, filename):
		wndMgr.SetDownVisual(self.hWnd, filename)

	def SetDisableVisual(self, filename):
		wndMgr.SetDisableVisual(self.hWnd, filename)

	def GetUpVisualFileName(self):
		return wndMgr.GetUpVisualFileName(self.hWnd)

	def GetOverVisualFileName(self):
		return wndMgr.GetOverVisualFileName(self.hWnd)

	def GetDownVisualFileName(self):
		return wndMgr.GetDownVisualFileName(self.hWnd)

	def Flash(self):
		wndMgr.Flash(self.hWnd)

	def Enable(self):
		wndMgr.Enable(self.hWnd)

	def Disable(self):
		wndMgr.Disable(self.hWnd)

	def Down(self):
		wndMgr.Down(self.hWnd)

	def SetUp(self):
		wndMgr.SetUp(self.hWnd)

	def SAFE_SetEvent(self, func, *args):
		self.eventFunc = ui.__mem_func__(func)
		self.eventArgs = args
		
	def SetEvent(self, func, *args):
		self.eventFunc = func
		self.eventArgs = args

	def SetTextColor(self, r, b, g):
		if not self.ButtonText:
			return
		self.ButtonText.SetFontColor(r, g, b)

	def SetButtonFontName(self, font):
		if not self.ButtonText:
			return
		BackUpText = self.ButtonText.GetText()	
		self.ButtonText.SetFontName(font)
		self.ButtonText.SetText("")
		self.ButtonText.SetText(str(BackUpText))		
		
	def SetText(self, text, height = 4):
		if not self.ButtonText:
			self.ButtonText = ui.TextLine()
			self.ButtonText.SetParent(self)
			self.ButtonText.SetPosition(self.GetWidth() / 2, self.GetHeight() / 2)
			self.ButtonText.SetVerticalAlignCenter()
			self.ButtonText.SetHorizontalAlignCenter()
			self.ButtonText.Show()

		self.ButtonText.SetText(text)

	def SetTextPosition(self, x, y):
		self.ButtonText.SetPosition(self.GetWidth() / 2 + int(x), self.GetHeight() / 2 + int(y))		
		
	def SetFormToolTipText(self, type, text, x, y):
		if not self.ToolTipText:		
			toolTip = ui.createToolTipWindowDict[type]()
			toolTip.SetParent(self)
			toolTip.SetSize(0, 0)
			toolTip.SetHorizontalAlignCenter()
			toolTip.SetOutline()
			toolTip.Hide()
			toolTip.SetPosition(x + self.GetWidth()/2, y)
			self.ToolTipText=toolTip

		self.ToolTipText.SetText(text)

	def SetToolTipWindow(self, toolTip):		
		self.ToolTipText = toolTip		
		self.ToolTipText.SetParentProxy(self)

	def SetToolTipText(self, text, x=0, y = -19):
		self.SetFormToolTipText("TEXT", text, x, y)

	def CallEvent(self):
		snd.PlaySound("sound/ui/click.wav")

		if self.eventFunc:
			apply(self.eventFunc, self.eventArgs)

	def ShowToolTip(self):
		if self.ToolTipText:
			self.ToolTipText.Show()

	def HideToolTip(self):
		if self.ToolTipText:
			self.ToolTipText.Hide()
			
	def IsDown(self):
		return wndMgr.IsDown(self.hWnd)

class ChatspammerDialog(ui.ScriptWindow):
	Gui = []
	Chattype = ["Normal", "", "", "Gruppe", "Gilde", "", "Rufen"]
	ChatTypes = []
	state = "Stop"
	ProcessTimeStamp = app.GetTime()
	ShoutTimeStamp = -15
	
	CheckGM = 1
	
	Config = [15, 500]
	
	def __init__(self):
		self.Gui = []
		self.ChatTypes = []
		self.state = "Stop"
		ui.ScriptWindow.__init__(self)
		self.AddGui()
		
	def __del__(self):
		self.Gui[0].Hide()
		ui.ScriptWindow.__del__(self)

	def CheckGameMaster(self):
		return self.CheckGM
		
	def ChangeState(self, state):
		self.state = state
		chat.AppendChat(1, str(state) + " Chatspammer!")
		if state == "Start":
			self.ProcessTimeStamp = app.GetTime()

	def SendMessage(self):
		if self.Config[1] <= 0:
			self.state = "Stop"
			chat.AppendChat(1, "Chatspammer wurde erfolgreich ausgeführt und beendet.")
			return
		if self.ChatTypes == []:
			self.ChangeState("Stop")
			chat.AppendChat(1, "Es wurden keine Chattypes eingetragen.")
			return
		message = str(self.Gui[9].GetText())
		for chattype in self.ChatTypes:
			if chattype == 6:
				if player.GetStatus(player.LEVEL) >= 15:
					if int(self.Gui[10].GetSliderPos() * 25 + 2.5) >= 15:
						Delay = int(self.Gui[10].GetSliderPos() * 25 + 2.5)
					else:
						Delay = 15
					if int(int(self.ShoutTimeStamp) + Delay) < int(app.GetTime()):
						net.SendChatPacket(message, chattype)
						self.ShoutTimeStamp = app.GetTime()
				else:
					chat.AppendChat(1, "Du bist noch nicht Level 15.")
					chat.AppendChat(1, "Rufen wurde deaktiviert")
					self.ChatTypes.remove(chattype)
			if chattype == 4:
				if player.GetGuildID() != 0:
					net.SendChatPacket(message, chattype)
				else:
					chat.AppendChat(1, "Du bist in keiner Gilde.")
					chat.AppendChat(1, "Gildenchat wurde deaktiviert")
					self.ChatTypes.remove(chattype)
			if chattype == 3:
				if chr.IsPartyMember(player.GetMainCharacterIndex()):
					net.SendChatPacket(message, chattype)
				else:
					chat.AppendChat(1, "Du bist in keiner Gruppe.")
					chat.AppendChat(1, "Gruppenchat wurde deaktiviert")
					self.ChatTypes.remove(chattype)
			else:
				net.SendChatPacket(message, chattype)
		return 1
		
		if not self.CheckGameMaster():
			return
			
		VidList = GetVidList()
		for vid in VidList:
			Instance = chr.GetInstanceType(vid)
			if Instance == chr.INSTANCE_TYPE_PLAYER and chr.GetNameByVID(vid) != "None" and (chr.IsGameMaster(vid) or chr.GetNameByVID(vid)[0] == "["):
				self.state = "Stop"
				chat.AppendChat(1, "GameMaster: " + str(chr.GetNameByVID(vid)) + " gesichtet, Chatspammer wurde gestoppt!")
				break
		
	def AddGui(self):
		#[Type, Parentindex],[Sizex, Sizey], [Posx, Posy], [commands], [flags]
		Gui = [
			[[ui.ThinBoard, ""], [349, 330], [0,0], [["SetCenterPosition", [""]]], ["movable", "float"]],			
			[[ui.Button, 0], [0, 0], [313, 15], [['SetUpVisual', ["d:/ymir work/ui/public/close_button_01.sub"]],['SetOverVisual', ["d:/ymir work/ui/public/close_button_02.sub"]], ['SetDownVisual', ["d:/ymir work/ui/public/close_button_03.sub"]], ['SetToolTipText', ["Schließen", 0, - 23]], ['SetEvent', [lambda : self.__del__()]]], []],	
			[[ui.TextLine, 0], [0, 0], [90, 18], [["SetDefaultFontName", [""]],	["SetText", ["Hier könnte deine Werbung stehen!"]],	["SetFontColor", [0.1, 0.7, 1.0]]], []],			
			[[ui.Button, 0], [0, 0], [75, 290], [['SetUpVisual', ["d:/ymir work/ui/public/large_button_01.sub"]],['SetOverVisual', ["d:/ymir work/ui/public/large_button_02.sub"]], ['SetDownVisual', ["d:/ymir work/ui/public/large_button_03.sub"]], ["SetText", ["Start"]], ['SetEvent', [lambda : self.ChangeState("Start")]]], []],			
			[[ui.Button, 0], [0, 0], [168, 290], [['SetUpVisual', ["d:/ymir work/ui/public/large_button_01.sub"]],['SetOverVisual', ["d:/ymir work/ui/public/large_button_02.sub"]], ['SetDownVisual', ["d:/ymir work/ui/public/large_button_03.sub"]], ["SetText", ["Stop"]], ['SetEvent', [lambda : self.ChangeState("Stop")]]], []],			
			[[ui.TextLine, 0], [0, 0], [90, 40], [["SetDefaultFontName", [""]],	["SetText", ["Bitte geben sie hier ihren Text ein..."]],	["SetFontColor", [0.6, 0.7, 1.0]]], []],			
			[[ui.TextLine, 0], [0, 0], [150, 80], [["SetDefaultFontName", [""]],	["SetText", ["Chattyp"]],	["SetFontColor", [0.6, 0.7, 1.0]]], []],			
			[[ui.TextLine, 0], [0, 0], [139, 125], [["SetDefaultFontName", [""]],	["SetText", ["Messagedelay"]],	["SetFontColor", [0.6, 0.7, 1.0]]], []],			
			[[ui.SlotBar, 0], [290, 18], [30, 55], [], []],			
			[[ui.EditLine, 8], [290, 17], [10, 2], [["SetMax", [64]], ["SetFocus", [""]]], []],			
			[[ui.SliderBar, 0], [0, 0], [85, 145], [["SetEvent", [ui.__mem_func__(self.SetConfig)]], ["SetSliderPos", [0.5]]], []],			
			[[ui.TextLine, 0], [0, 0], [160, 160], [["SetDefaultFontName", [""]],	["SetText", ["15s"]]], []],		
			[[ui.TextLine, 0], [0, 0], [137, 180], [["SetDefaultFontName", [""]],	["SetText", ["Messagecount"]],	["SetFontColor", [0.6, 0.7, 1.0]]], []],			
			[[ui.SliderBar, 0], [0, 0], [85, 200], [["SetEvent", [ui.__mem_func__(self.SetConfig)]], ["SetSliderPos", [0.5]]], []],			
			[[ui.TextLine, 0], [0, 0], [160, 215], [["SetDefaultFontName", [""]],	["SetText", ["500x"]]], []],		
			[[ui.TextLine, 0], [0, 0], [140, 235], [["SetDefaultFontName", [""]],	["SetText", ["GM Detector"]],	["SetFontColor", [0.6, 0.7, 1.0]]], []],		
			]
		GuiParser(Gui, self.Gui)
		
		tmp = []
		x = 78
		for Chattype in self.Chattype:
			if Chattype != "":
				button = [[ui.Button, 0], [0, 0], [x, 95], [['SetUpVisual', ["d:/ymir work/ui/public/small_button_01.sub"]],['SetOverVisual', ["d:/ymir work/ui/public/small_button_02.sub"]], ['SetDownVisual', ["d:/ymir work/ui/public/small_button_03.sub"]], ['SetText', [Chattype]], ['SetEvent', [lambda arg = (self.Chattype.index(Chattype)): self.UseChatType(arg)]]], []]
				tmp.append(button)
				x += 48
				
		Modi = ["On", "Off"]		
		x = 120
		for mode in Modi:
			button = [[ui.Button, 0], [0, 0], [x, 255], [['SetUpVisual', ["d:/ymir work/ui/public/small_button_01.sub"]],['SetOverVisual', ["d:/ymir work/ui/public/small_button_02.sub"]], ['SetDownVisual', ["d:/ymir work/ui/public/small_button_03.sub"]], ['SetText', [mode]], ['SetEvent', [lambda arg = (Modi.index(mode)): self.GMDetector(arg)]]], []]
			tmp.append(button)
			x += 48
		GuiParser(tmp, self.Gui)
		
	def OnRender(self):
		if self.state == "Stop":
			return
			
		if float(self.ProcessTimeStamp) < float(app.GetTime()):
			if self.SendMessage():
				self.Config[1] -= 1
				self.Gui[13].SetSliderPos(DivideToFloat(self.Config[1], 1000))
				self.Gui[14].SetText(str(self.Config[1]) + "x")
				self.ProcessTimeStamp = app.GetTime() + float(self.Gui[10].GetSliderPos() * 25 + 2.5)
		
	def GMDetector(self, arg):
		if arg == 1:
			self.CheckGM = 0
			chat.AppendChat(1, "GameMaster Check wurde deaktiviert.")
		else:
			self.CheckGM = 1
			chat.AppendChat(1, "GameMaster Check wurde aktiviert.")
		
	def SetConfig(self):
		(Delay, Count) = self.Config
		if self.Gui[10].GetSliderPos() * 25 + 2.5 != Delay:
			self.Config[0] = self.Gui[10].GetSliderPos() * 25 + 2.5
			try:
				Tmp = str(self.Config[0]).split(".")
				Delay = str(Tmp[0]) + "." + Tmp[1][:1]
				self.ProcessTimeStamp = app.GetTime() + float(Delay)
			except:
				pass
			self.Gui[11].SetText(str(Delay) + "s")
		if int(self.Gui[13].GetSliderPos() * 1000) != Count:
			self.Config[1] = int(self.Gui[13].GetSliderPos() * 1000)
			self.Gui[14].SetText(str(self.Config[1]) + "x")
		
	def UseChatType(self, type):
		try:
			self.ChatTypes.index(type)
			self.ChatTypes.remove(type)
			chat.AppendChat(1, str(self.Chattype[type]) + " wurde deaktiviert.")
		except:
			self.ChatTypes.append(type)
			chat.AppendChat(1, str(self.Chattype[type]) + " wurde aktiviert.")

class WhisperspammerDialog(ui.ScriptWindow):
	Gui = []
	PlayerAskGui = []
	WhisperMode = ["Alle", "Player"]
	state = "Stop"
	ProcessTimeStamp = app.GetTime()
	Player	= ""
	CheckGM = 1
	WhisperType = 0
	
	Config = [15, 500]
	
	def __init__(self):
		self.Gui = []
		self.state = "Stop"
		ui.ScriptWindow.__init__(self)
		self.AddGui()
		
	def __del__(self):
		self.Gui[0].Hide()
		try:
			self.PlayerAskGui[0].Hide()
		except:
			pass
		ui.ScriptWindow.__del__(self)

	def CheckGameMaster(self):
		return self.CheckGM
		
	def ChangeState(self, state):
		self.state = state
		chat.AppendChat(1, str(state) + " Whisperspammer!")
		if state == "Start":
			self.ProcessTimeStamp = app.GetTime()

	def SendMessage(self):
		if self.Config[1] <= 0:
			self.state = "Stop"
			chat.AppendChat(1, "Whisperspammer wurde erfolgreich ausgeführt und beendet.")
			return
		message = str(self.Gui[9].GetText())
		
		if self.WhisperType == 0:
			VidList = GetVidList()
			for vid in VidList:
				if chr.GetInstanceType(vid) == 6 and chr.GetNameByVID(vid) != "None":
					if chr.IsGameMaster(vid) or chr.GetNameByVID(vid)[0] == "[" and self.CheckGameMaster():
						chat.AppendChat(1, "GameMaster: " + str(chr.GetNameByVID(vid)) + " gesichtet, Whisperspammer wurde gestoppt!")
					net.SendWhisperPacket(chr.GetNameByVID(vid), message)
			return 1
		else:
			if self.Player == "":
				return
			net.SendWhisperPacket(self.Player, message)
			return 1
			
	def AddGui(self):
		#[Type, Parentindex],[Sizex, Sizey], [Posx, Posy], [commands], [flags]
		Gui = [
			[[ui.ThinBoard, ""], [349, 330], [0,0], [["SetCenterPosition", [""]]], ["movable", "float"]],			
			[[ui.Button, 0], [0, 0], [313, 15], [['SetUpVisual', ["d:/ymir work/ui/public/close_button_01.sub"]],['SetOverVisual', ["d:/ymir work/ui/public/close_button_02.sub"]], ['SetDownVisual', ["d:/ymir work/ui/public/close_button_03.sub"]], ['SetToolTipText', ["Schließen", 0, - 23]], ['SetEvent', [lambda : self.__del__()]]], []],	
			[[ui.TextLine, 0], [0, 0], [90, 18], [["SetDefaultFontName", [""]],	["SetText", ["Hier könnte deine Werbung stehen!"]],	["SetFontColor", [0.1, 0.7, 1.0]]], []],			
			[[ui.Button, 0], [0, 0], [75, 290], [['SetUpVisual', ["d:/ymir work/ui/public/large_button_01.sub"]],['SetOverVisual', ["d:/ymir work/ui/public/large_button_02.sub"]], ['SetDownVisual', ["d:/ymir work/ui/public/large_button_03.sub"]], ["SetText", ["Start"]], ['SetEvent', [lambda : self.ChangeState("Start")]]], []],			
			[[ui.Button, 0], [0, 0], [168, 290], [['SetUpVisual', ["d:/ymir work/ui/public/large_button_01.sub"]],['SetOverVisual', ["d:/ymir work/ui/public/large_button_02.sub"]], ['SetDownVisual', ["d:/ymir work/ui/public/large_button_03.sub"]], ["SetText", ["Stop"]], ['SetEvent', [lambda : self.ChangeState("Stop")]]], []],			
			[[ui.TextLine, 0], [0, 0], [90, 40], [["SetDefaultFontName", [""]],	["SetText", ["Bitte geben sie hier ihren Text ein..."]],	["SetFontColor", [0.6, 0.7, 1.0]]], []],			
			[[ui.TextLine, 0], [0, 0], [150, 80], [["SetDefaultFontName", [""]],	["SetText", ["Whispertype"]],	["SetFontColor", [0.6, 0.7, 1.0]]], []],			
			[[ui.TextLine, 0], [0, 0], [137, 125], [["SetDefaultFontName", [""]],	["SetText", ["Whisperdelay"]],	["SetFontColor", [0.6, 0.7, 1.0]]], []],			
			[[ui.SlotBar, 0], [290, 18], [30, 55], [], []],			
			[[ui.EditLine, 8], [290, 17], [10, 2], [["SetMax", [64]], ["SetFocus", [""]]], []],			
			[[ui.SliderBar, 0], [0, 0], [85, 145], [["SetEvent", [ui.__mem_func__(self.SetConfig)]], ["SetSliderPos", [0.5]]], []],			
			[[ui.TextLine, 0], [0, 0], [160, 160], [["SetDefaultFontName", [""]],	["SetText", ["15s"]]], []],		
			[[ui.TextLine, 0], [0, 0], [137, 180], [["SetDefaultFontName", [""]],	["SetText", ["Whispercount"]],	["SetFontColor", [0.6, 0.7, 1.0]]], []],			
			[[ui.SliderBar, 0], [0, 0], [85, 200], [["SetEvent", [ui.__mem_func__(self.SetConfig)]], ["SetSliderPos", [0.5]]], []],			
			[[ui.TextLine, 0], [0, 0], [160, 215], [["SetDefaultFontName", [""]],	["SetText", ["500x"]]], []],		
			[[ui.TextLine, 0], [0, 0], [140, 235], [["SetDefaultFontName", [""]],	["SetText", ["GM Detector"]],	["SetFontColor", [0.6, 0.7, 1.0]]], []],		
			]
		GuiParser(Gui, self.Gui)
		
		tmp = []
		x = 126
		for Whispertype in self.WhisperMode:
			button = [[ui.Button, 0], [0, 0], [x, 95], [['SetUpVisual', ["d:/ymir work/ui/public/small_button_01.sub"]],['SetOverVisual', ["d:/ymir work/ui/public/small_button_02.sub"]], ['SetDownVisual', ["d:/ymir work/ui/public/small_button_03.sub"]], ['SetText', [Whispertype]], ['SetEvent', [lambda arg = (self.WhisperMode.index(Whispertype)): self.SetWhisperType(arg)]]], []]
			tmp.append(button)
			x += 48
			
		Modi = ["On", "Off"]		
		x = 120
		for mode in Modi:
			button = [[ui.Button, 0], [0, 0], [x, 255], [['SetUpVisual', ["d:/ymir work/ui/public/small_button_01.sub"]],['SetOverVisual', ["d:/ymir work/ui/public/small_button_02.sub"]], ['SetDownVisual', ["d:/ymir work/ui/public/small_button_03.sub"]], ['SetText', [mode]], ['SetEvent', [lambda arg = (Modi.index(mode)): self.GMDetector(arg)]]], []]
			tmp.append(button)
			x += 48
		GuiParser(tmp, self.Gui)
		
	def OnRender(self):
		if self.state == "Stop":
			return
		if float(self.ProcessTimeStamp) < float(app.GetTime()):
			if self.SendMessage():
				self.Config[1] -= 1
				self.Gui[13].SetSliderPos(DivideToFloat(self.Config[1], 1000))
				self.Gui[14].SetText(str(self.Config[1]) + "x")
				self.ProcessTimeStamp = app.GetTime() + float(self.Gui[10].GetSliderPos() * 25 + 2.5)
		
	def GMDetector(self, arg):
		if arg == 1:
			self.CheckGM = 0
			chat.AppendChat(1, "GameMaster Check wurde deaktiviert.")
		else:
			self.CheckGM = 1
			chat.AppendChat(1, "GameMaster Check wurde aktiviert.")
		
	def SetConfig(self):
		(Delay, Count) = self.Config
		if self.Gui[10].GetSliderPos() * 25 + 2.5 != Delay:
			self.Config[0] = self.Gui[10].GetSliderPos() * 25 + 2.5
			try:
				Tmp = str(self.Config[0]).split(".")
				Delay = str(Tmp[0]) + "." + Tmp[1][:1]
				self.ProcessTimeStamp = app.GetTime() + float(Delay)
			except:
				pass
			self.Gui[11].SetText(str(Delay) + "s")
		if int(self.Gui[13].GetSliderPos() * 1000) != Count:
			self.Config[1] = int(self.Gui[13].GetSliderPos() * 1000)
			self.Gui[14].SetText(str(self.Config[1]) + "x")
		
	def SetWhisperType(self, type):
		self.WhisperType = int(type)
		if type == 1:
			self.PlayerAskGui = []
			tmp = [
			[[ui.BoardWithTitleBar, ""], [200, 120], [0,0], [["SetCenterPosition", [""]], ["SetCloseEvent", [self.HideAskPlayerBoard]], ["SetTitleName", ["Zielperson"]]], ["movable", "float"]],			
			[[ui.TextLine, 0], [0, 0], [70, 40], [["SetDefaultFontName", [""]],	["SetText", ["Playername:"]],	["SetFontColor", [0.6, 0.7, 1.0]]], []],
			[[ui.SlotBar, 0], [100, 18], [50, 60], [], []],			
			[[ui.EditLine, 2], [100, 17], [10, 2], [["SetMax", [16]], ["SetFocus", [""]]], []],			
			]

			Modi = ["Ok", "Abbrechen"]		
			x = 12
			for mode in Modi:
				button = [[ui.Button, 0], [0, 0], [x, 85], [['SetUpVisual', ["d:/ymir work/ui/public/large_button_01.sub"]],['SetOverVisual', ["d:/ymir work/ui/public/large_button_02.sub"]], ['SetDownVisual', ["d:/ymir work/ui/public/large_button_03.sub"]], ['SetText', [mode]], ['SetEvent', [lambda arg = (Modi.index(mode)): self.Decision(arg)]]], []]
				tmp.append(button)
				x += 88
			
			GuiParser(tmp, self.PlayerAskGui)
			chat.AppendChat(1, "Bitte wähle eine Zielperson.")
		else:
			chat.AppendChat(1, "Es werden alle gespeicherten Charaktere angeschrieben.")
		
	def Decision(self, arg):
		if arg == 0:
			self.Player = self.PlayerAskGui[3].GetText()
			chat.AppendChat(1, "Als Zielperson wurde: " + str(self.Player) + " ausgewählt.")
			self.HideAskPlayerBoard()
		else:
			self.PlayerAskGui = []
			
	def HideAskPlayerBoard(self):
		try:
			self.PlayerAskGui[0].Hide()
		except:
			pass
		
class FishingBot(ui.ScriptWindow):
	Gui = []
	state = "Stop"
	KillFishList = []
	TrashList = []
	Config = (3.5, 1.0)
	UseSmallFishAsBait = 0
	
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.AddGui()
		
	def __del__(self):
		self.Gui[0].Hide()
		ui.ScriptWindow.__del__(self)
		
	def AddGui(self):
		Gui = [
			[[ui.ThinBoard, ""], [349, 687], [0,0], [["SetCenterPosition", [""]]], ["movable", "float"]],			
			[[ui.Button, 0], [0, 0], [313, 15], [['SetUpVisual', ["d:/ymir work/ui/public/close_button_01.sub"]],['SetOverVisual', ["d:/ymir work/ui/public/close_button_02.sub"]], ['SetDownVisual', ["d:/ymir work/ui/public/close_button_03.sub"]], ['SetToolTipText', ["Schließen", 0, - 23]], ['SetEvent', [lambda : self.__del__()]]], []],	
			[[ui.Button, 0], [0, 0], [79, 645], [['SetUpVisual', ["d:/ymir work/ui/public/large_button_01.sub"]],['SetOverVisual', ["d:/ymir work/ui/public/large_button_02.sub"]], ['SetDownVisual', ["d:/ymir work/ui/public/large_button_03.sub"]], ["SetText", ["Start"]], ['SetEvent', [lambda : self.ChangeState("Start")]]], []],			
			[[ui.Button, 0], [0, 0], [172, 645], [['SetUpVisual', ["d:/ymir work/ui/public/large_button_01.sub"]],['SetOverVisual', ["d:/ymir work/ui/public/large_button_02.sub"]], ['SetDownVisual', ["d:/ymir work/ui/public/large_button_03.sub"]], ["SetText", ["Stop"]], ['SetEvent', [lambda : self.ChangeState("Stop")]]], []],			
			[[ui.TextLine, 0], [0, 0], [113, 18], [["SetDefaultFontName", [""]],	["SetText", ["Fishing Bot by DaRealFreak"]],	["SetFontColor", [0.1, 0.7, 1.0]]], []],			
			[[ui.TextLine, 0], [0, 0], [115, 40], [["SetDefaultFontName", [""]],	["SetText", ["First Fishing Bot in Python"]],	["SetFontColor", [0.6, 0.7, 1.0]]], []],			
			[[ui.TextLine, 0], [0, 0], [145, 475], [["SetDefaultFontName", [""]],	["SetText", ["Waitingdelay"]],	["SetFontColor", [0.6, 0.7, 1.0]]], []],			
			[[ui.SliderBar, 0], [0, 0], [85, 500], [["SetEvent", [ui.__mem_func__(self.SetConfig)]], ["SetSliderPos", [0.28]]], []],			
			[[ui.TextLine, 0], [0, 0], [165, 515], [["SetDefaultFontName", [""]],	["SetText", ["3.5 s"]]], []],
			[[ui.TextLine, 0], [0, 0], [150, 537], [["SetDefaultFontName", [""]],	["SetText", ["Tolerance"]],	["SetFontColor", [0.6, 0.7, 1.0]]], []],						
			[[ui.SliderBar, 0], [0, 0], [85, 557], [["SetEvent", [ui.__mem_func__(self.SetConfig)]], ["SetSliderPos", [0.5]]], []],			
			[[ui.TextLine, 0], [0, 0], [165, 572], [["SetDefaultFontName", [""]],	["SetText", ["1.0 s"]]], []],			
			[[ui.TextLine, 0], [0, 0], [143, 592], [["SetDefaultFontName", [""]],	["SetText", ["Use small fish"]],	["SetFontColor", [0.6, 0.7, 1.0]]], []],			
			]
		GuiParser(Gui, self.Gui)		
		self.fischies = []
		for i in xrange(27803, 27824):
			self.fischies.append(i)
		self.crap = [27987, 70201, 70202, 70203, 70204, 70205, 70206, 70048, 70049, 70050, 70051]
		for bla in self.crap:
			self.fischies.append(bla)
		tmp = []
		Modi = ["Use", "No Use"]		
		x = 125
		for mode in Modi:
			button = [[ui.Button, 0], [0, 0], [x, 615], [['SetUpVisual', ["d:/ymir work/ui/public/small_button_01.sub"]],['SetOverVisual', ["d:/ymir work/ui/public/small_button_02.sub"]], ['SetDownVisual', ["d:/ymir work/ui/public/small_button_03.sub"]], ['SetText', [mode]], ['SetEvent', [lambda arg = (Modi.index(mode)): self.UseSmallFishes(arg)]]], []]
			tmp.append(button)
			x += 48		
		x = 40
		y = 70
		for fish in self.fischies:
			Index = self.fischies.index(fish)
			if IsDivideAble(Index, 4):
				x = 40
				y += 50
			ItemName = item.GetItemName(item.SelectItem(fish))
			ItemIcon = item.GetIconImageFileName()
			button = [[ui.ExpandedImageBox, 0], [0, 0], [x, y], [['LoadImage', [ItemIcon]]], []]
			name = [[ui.Button, 0], [0, 0], [x - 15, y + 30], [['SetUpVisual', ["d:/ymir work/ui/public/middle_button_01.sub"]],['SetOverVisual', ["d:/ymir work/ui/public/middle_button_02.sub"]], ['SetDownVisual', ["d:/ymir work/ui/public/middle_button_03.sub"]], ["SetText", [ItemName]], ['SetEvent', [lambda arg = (self.fischies.index(fish)): self.SelectFish(arg)]]], []]
			tmp.append(button)
			tmp.append(name)
			x += 78					
		GuiParser(tmp, self.Gui)
		
	def UseSmallFishes(self, mode):
		if mode == 1:
			self.UseSmallFishAsBait = 0
			chat.AppendChat(1, "Nutze keine kleinen Fische als Köder.")
		else:
			self.UseSmallFishAsBait = 1
			chat.AppendChat(1, "Nutze kleine Fische als Köder.")
			
	def SelectFish(self, fish):
		try:
			self.fischies.index(27803 + fish)
			try:
				self.KillFishList.remove(int(27803 + fish))
				chat.AppendChat(1, item.GetItemName(item.SelectItem(27803 + fish)) + " wird nicht mehr sofort getötet.")
				self.Gui[15 + fish*2].LoadImage(item.GetIconImageFileName(item.SelectItem(27803 + fish)))
			except:
				self.KillFishList.append(int(27803 + fish))
				chat.AppendChat(1, item.GetItemName(item.SelectItem(27803 + fish)) + " wird direkt beim Fang getötet.")
				self.Gui[15 + fish*2].LoadImage(item.GetIconImageFileName(item.SelectItem(27833 + fish)))
		except:
			ItemName = item.GetItemName(item.SelectItem(self.crap[fish-len(self.fischies)]))
			try:
				self.KillFishList.remove(self.crap[fish-len(self.fischies)])
				if ItemName == item.GetItemName(item.SelectItem(27987)):
					chat.AppendChat(1, ItemName + " wird beim Erhalt nicht mehr geöffnet.")
				else:
					self.TrashList.remove(self.crap[fish-len(self.fischies)])
					chat.AppendChat(1, ItemName + " wird beim Erhalt behalten.")
			except:
				if ItemName == item.GetItemName(item.SelectItem(27987)):
					self.KillFishList.append(self.crap[fish-len(self.fischies)])
					chat.AppendChat(1, ItemName + " wird beim Erhalt geöffnet.")
				else:
					self.TrashList.append(self.crap[fish-len(self.fischies)])
					chat.AppendChat(1, ItemName + " wird beim Erhalt weggeworfen.")			

	def SetConfig(self):
		(Delay, Tolerance) = self.Config		
		if self.Gui[7].GetSliderPos() * 9 + 1 != Delay:
			Delay = self.Gui[7].GetSliderPos() * 9 + 1
			try:
				Tmp = str(Delay).split(".")
				Delay = str(Tmp[0]) + "." + Tmp[1][:1]
			except:
				pass
			self.Gui[8].SetText(str(Delay) + " s")			
		if self.Gui[10].GetSliderPos() * 2 != Tolerance:
			Tolerance = self.Gui[10].GetSliderPos() * 2
			try:
				Tmp = str(Tolerance).split(".")
				Tolerance = str(Tmp[0]) + "." + Tmp[1][:1]
			except:
				pass
			self.Gui[11].SetText(str(Tolerance) + " s")			
		self.Config = (Delay, Tolerance)
		
	def ChangeState(self, arg):
		chat.AppendChat(1, str(arg))
		self.state = arg
		if arg == "Start":
			if self.AddBait():
				self.ProcessTimeStamp = app.GetTime()
				self.FishAction()
				self.state = "Waiting"
		else:
			self.FishAction()
		
	def OnRender(self):
		if self.state == "Stop":
			return
		if self.state == "Start":
			if self.ProcessTimeStamp + 4.0 < app.GetTime():
				if self.AddBait():
					self.FishAction()
					self.ProcessTimeStamp = app.GetTime()
					self.state = "Waiting"
					chat.AppendChat(1, "Beginne eine neue Runde Fischen.")		
		if self.state == "Fish":
			if self.ProcessTimeStamp + float(self.Config[0]) < app.GetTime():
				self.FishAction()
				self.ProcessTimeStamp = app.GetTime()
				self.state = "Start"		
		if self.state == "Waiting":
			if not chrmgr.IsPossibleEmoticon(-1):
				chat.AppendChat(1, "Es hat etwas angebissen!")
				self.ProcessTimeStamp = app.GetTime() + float(self.RandomTolerance())
				self.state = "Fish"					
			if self.ProcessTimeStamp + 52.0 < app.GetTime():
				chat.AppendChat(1, "Du hast leider nichts gefangen.")
				self.ProcessTimeStamp = app.GetTime()
				self.state = "Start"	
	
	def RandomTolerance(self):
		Tolerance = float(self.Config[1])*10
		Rnd = app.GetRandom(0, int(Tolerance))
		return DivideToFloat(Rnd, 10)
	
	def FishAction(self):
		player.SetAttackKeyState(TRUE)
		player.SetAttackKeyState(FALSE)
		
	def UseFishBait(self):
		return self.UseSmallFishAsBait
		
	def AddBait(self):
		#Kill Selected Fish:
		for InventorySlot in xrange(player.INVENTORY_PAGE_SIZE*2):
			ItemValue = player.GetItemIndex(InventorySlot)
			try:
				self.KillFishList.index(ItemValue)
				net.SendItemUsePacket(InventorySlot)
			except:
				try:
					self.TrashList.index(ItemValue)
					net.SendItemDropPacketNew(InventorySlot, player.GetItemCount(InventorySlot))
				except:
					pass		
		#Use small fish first
		if self.UseFishBait():
			if player.GetItemCountByVnum(27802) > 0:
				for InventorySlot in xrange(player.INVENTORY_PAGE_SIZE*2):
					ItemValue = player.GetItemIndex(InventorySlot)
					if ItemValue == 27802:
						net.SendItemUsePacket(InventorySlot)
						chat.AppendChat(1, "Kleinen Fisch an der Angel befestigt.")
						return 1		
		#No small fish, other baits
		#Add Bait:
		Baits = [27800, 27801]
		Baitcount = 0
		for bait in Baits:
			Baitcount += player.GetItemCountByVnum(bait)	
		if Baitcount <= 0:
			chat.AppendChat(1, "Keine Köder mehr im Inventar")
			self.state = "Stop"
			return 0
		else:
			for InventorySlot in xrange(player.INVENTORY_PAGE_SIZE*2):
				ItemValue = player.GetItemIndex(InventorySlot)
				try:
					Baits.index(ItemValue)
					net.SendItemUsePacket(InventorySlot)
					chat.AppendChat(1, "Neuen Köder an der Angel befestigt.")
					return 1
				except:
					pass

class InventoryManagerDialog(ui.ScriptWindow):
	Gui = []
	type = 0
	
	def __init__(self):
		self.Gui = []
		ui.ScriptWindow.__init__(self)
		self.AddGui()
		
	def __del__(self):
		self.Gui[0].Hide()
		ui.ScriptWindow.__del__(self)
		
	def AddGui(self):
		Gui = [
			[[ui.ThinBoard, ""], [278, 370], [0,0], [["SetCenterPosition", [""]]], ["movable", "float"]],			
			[[ui.Button, 0], [0, 0], [243, 18], [['SetUpVisual', ["d:/ymir work/ui/public/close_button_01.sub"]],['SetOverVisual', ["d:/ymir work/ui/public/close_button_02.sub"]], ['SetDownVisual', ["d:/ymir work/ui/public/close_button_03.sub"]], ['SetToolTipText', ["Schließen", 0, - 23]], ['SetEvent', [lambda : self.__del__()]]], []],	
			[[ui.SlotBar, 0], [190, 225], [10, 35], [], []],			
			[[ui.ListBoxEx, 0], [0, 0], [15, 50], [["SetViewItemCount", [10]]], []],			
			[[ui.ScrollBar, 0], [0, 0], [180, 40], [["SetScrollBarSize", [220]]], []],			
			[[ui.TextLine, 0], [0, 0], [85, 18], [["SetDefaultFontName", [""]],	["SetText", ["Inventory Manager"]],	["SetFontColor", [0.4, 0.7, 1.0]]], []],			
			[[ui.TextLine, 0], [0, 0], [10, 37], [["SetDefaultFontName", [""]],	["SetText", ["			ID:			Name:"]],	["SetFontColor", [0.2, 0.2, 1.0]]], []],			
			[[ui.Button, 0], [0, 0], [218, 16], [['SetUpVisual', ["d:/ymir work/ui/game/guild/refresh_button_01.sub"]],['SetOverVisual', ["d:/ymir work/ui/game/guild/refresh_button_02.sub"]], ['SetDownVisual', ["d:/ymir work/ui/game/guild/refresh_button_03.sub"]], ['SetToolTipText', ["Aktualisieren", 0, - 23]], ['SetEvent', [lambda : self.UpdateFileList()]]], []],	
			[[ui.Button, 0], [0, 0], [15, 265], [['SetUpVisual', ["d:/ymir work/ui/public/Large_button_01.sub"]],['SetOverVisual', ["d:/ymir work/ui/public/Large_button_02.sub"]], ['SetDownVisual', ["d:/ymir work/ui/public/Large_button_03.sub"]], ["SetText", ["Upgrade"]], ['SetToolTipText', ["Schmied: Gegenstand aufwerten"]], ['SetEvent', [lambda : self.UpgradeSingleItem()]]], []],	
			[[ui.Button, 0], [0, 0], [110, 265], [['SetUpVisual', ["d:/ymir work/ui/public/Large_button_01.sub"]],['SetOverVisual', ["d:/ymir work/ui/public/Large_button_02.sub"]], ['SetDownVisual', ["d:/ymir work/ui/public/Large_button_03.sub"]], ["SetText", ["Upgrade All"]], ['SetToolTipText', ["Schmied: Verbessert Items auf der Schmied-Ebene"]], ['SetEvent', [lambda : self.UpgradeItemType()]]], []],	
			[[ui.Button, 0], [0, 0], [60, 290], [['SetUpVisual', ["d:/ymir work/ui/public/Large_button_01.sub"]],['SetOverVisual', ["d:/ymir work/ui/public/Large_button_02.sub"]], ['SetDownVisual', ["d:/ymir work/ui/public/Large_button_03.sub"]], ['SetText', ["Configuration"]], ['SetEvent', [lambda : self.ShowConfigurationBoard()]]], []],	
			[[ui.Button, 0], [0, 0], [15, 315], [['SetUpVisual', ["d:/ymir work/ui/public/Large_button_01.sub"]],['SetOverVisual', ["d:/ymir work/ui/public/Large_button_02.sub"]], ['SetDownVisual', ["d:/ymir work/ui/public/Large_button_03.sub"]], ['SetText', ["Drop Selected"]], ['SetEvent', [lambda : self.DropItem()]]], []],	
			[[ui.Button, 0], [0, 0], [110, 315], [['SetUpVisual', ["d:/ymir work/ui/public/Large_button_01.sub"]],['SetOverVisual', ["d:/ymir work/ui/public/Large_button_02.sub"]], ['SetDownVisual', ["d:/ymir work/ui/public/Large_button_03.sub"]], ['SetText', ["Drop All"]], ['SetEvent', [lambda : self.DropAllItemsRequest()]]], []],	
			[[ui.Button, 0], [0, 0], [15, 340], [['SetUpVisual', ["d:/ymir work/ui/public/Large_button_01.sub"]],['SetOverVisual', ["d:/ymir work/ui/public/Large_button_02.sub"]], ['SetDownVisual', ["d:/ymir work/ui/public/Large_button_03.sub"]], ['SetText', ["Sell Selected"]], ['SetEvent', [lambda : self.SellItem()]]], []],	
			[[ui.Button, 0], [0, 0], [110, 340], [['SetUpVisual', ["d:/ymir work/ui/public/Large_button_01.sub"]],['SetOverVisual', ["d:/ymir work/ui/public/Large_button_02.sub"]], ['SetDownVisual', ["d:/ymir work/ui/public/Large_button_03.sub"]], ['SetText', ["Sell All"]], ['SetEvent', [lambda : self.SellAllItems()]]], []],	
			[[ui.SlotBar, 0], [15, 18], [213, 265], [], []],			
			[[ui.EditLine, 15], [15, 17], [6, 2], [["SetMax", [1]], ["SetNumberMode", [""]], ["SetFocus", [""]]], []],
			]
		GuiParser(Gui, self.Gui)		

		self.Gui[3].SetScrollBar(self.Gui[4])
		
		self.UpdateFileList()
		
	def UpdateFileList(self):
		self.Gui[3].RemoveAllItems()
		for i in xrange(100):
			ItemIndex = player.GetItemIndex(i)
			if ItemIndex != 0:
				item.SelectItem(ItemIndex)
				item.GetItemName(ItemIndex)
				ItemName = item.GetItemName()
				self.Gui[3].AppendItem(Item(str(i) + "	" + str(ItemIndex) + "	" + ItemName))

	def UpgradeSingleItem(self):
		ItemIndex = self.Gui[3].GetSelectedItem()
		if ItemIndex:
			pass
		else:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Kein Item ausgewählt!")
			return
		SelectedItem = ItemIndex.GetText().split("	")
		Count = int(self.Gui[16].GetText())
		self.UpgradeItem(int(SelectedItem[0]), int(Count))
		
	def UpgradeItem(self, Slot, Count):
		self.BannedSlotIndex = []
		for i in xrange(Count):
			#Normal Upgrade
			if self.type == 0:
				net.SendRefinePacket(Slot, 0)
			
			#Guild Blacksmith Upgrade
			elif self.type == 1:
				net.SendRefinePacket(Slot, 1)
			
			#Bless Scroll Upgrade
			elif self.type == 2:
				for InventorySlot in xrange(player.INVENTORY_PAGE_SIZE*2):
					ItemValue = player.GetItemIndex(InventorySlot)
					if ItemValue == 25040 and not InventorySlot in self.BannedSlotIndex:
						self.BannedSlotIndex.append(InventorySlot)
						net.SendItemUseToItemPacket(InventorySlot, Slot)
						net.SendRefinePacket(Slot, 2)
						break
			
			#Magic Metal Upgrade
			elif self.type == 3:
				for InventorySlot in xrange(player.INVENTORY_PAGE_SIZE*2):
					ItemValue = player.GetItemIndex(InventorySlot)
					if ItemValue == 25041 and not InventorySlot in self.BannedSlotIndex:
						self.BannedSlotIndex.append(InventorySlot)
						net.SendItemUseToItemPacket(InventorySlot, Slot)
						net.SendRefinePacket(Slot, 3)
						break
						
			#Deviltower Upgrade
			elif self.type == 4:
				net.SendRefinePacket(Slot, 4)
				
	def UpgradeItemType(self):
		ItemIndex = self.Gui[3].GetSelectedItem()
		if ItemIndex:
			pass
		else:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Kein Item ausgewählt!")
			return
		try:
			SearchedName = ItemIndex.GetText().split("	")[2].split("+")[0]
		except:
			SearchedName = ItemIndex.GetText().split("	")[2]
		Count = int(self.Gui[16].GetText())
		for Slot in xrange(0, 90):
			ItemValue = player.GetItemIndex(Slot)
			try:
				ItemName = item.GetItemName(item.SelectItem(ItemValue)).split("+")[0]
			except:
				ItemName = item.GetItemName(item.SelectItem(ItemValue))
			if ItemName == SearchedName:
				self.UpgradeItem(Slot, Count)
		
	def SellItem(self):
		if not shop.IsOpen():
			chat.AppendChat(1, "Dafür musst du einen Shop geöffnet haben.")
			return
		ItemIndex = self.Gui[3].GetSelectedItem()
		if ItemIndex:
			pass
		else:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Kein Item ausgewählt!")
			return
			
		try:
			SearchedName = ItemIndex.GetText().split("	")[2].split("+")[0]
		except:
			SearchedName = ItemIndex.GetText().split("	")[2]

			
		for Slot in xrange(0, 90):
			ItemValue = player.GetItemIndex(Slot)
			try:
				ItemName = item.GetItemName(item.SelectItem(ItemValue)).split("+")[0]
			except:
				ItemName = item.GetItemName(item.SelectItem(ItemValue))
			if ItemName == SearchedName:
				net.SendShopSellPacket(Slot)

	def SellAllItems(self):
		if not shop.IsOpen():
			chat.AppendChat(1, "Dafür musst du einen Shop geöffnet haben.")
			return
		self.QuestionDialog = uiCommon.QuestionDialog()
		self.QuestionDialog.SetText("Willst du alle deine Items verkaufen?")
		self.QuestionDialog.SetAcceptEvent(ui.__mem_func__(self.SellAll))
		self.QuestionDialog.SetCancelEvent(ui.__mem_func__(self.CancelQuestionDialog))
		self.QuestionDialog.Open()
		
	def SellAll(self):
		for i in xrange(90):
			net.SendShopSellPacket(i)
		self.CancelQuestionDialog()
	
	def DropItem(self):
		ItemIndex = self.Gui[3].GetSelectedItem()
		if ItemIndex:
			pass
		else:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Kein Item ausgewählt!")
			return
		SelectedItem = ItemIndex.GetText().split("	")
		try:
			SearchedName = ItemIndex.GetText().split("	")[2].split("+")[0]
		except:
			SearchedName = ItemIndex.GetText().split("	")[2]

			
		for Slot in xrange(0, 90):
			ItemValue = player.GetItemIndex(Slot)
			try:
				ItemName = item.GetItemName(item.SelectItem(ItemValue)).split("+")[0]
			except:
				ItemName = item.GetItemName(item.SelectItem(ItemValue))
			if ItemName == SearchedName:
				net.SendItemDropPacket(Slot)
		
	def DropAllItemsRequest(self):
		self.QuestionDialog = uiCommon.QuestionDialog()
		self.QuestionDialog.SetText("Möchtest du all deine Items fallen lassen?")
		self.QuestionDialog.SetAcceptEvent(ui.__mem_func__(self.DropAllItems))
		self.QuestionDialog.SetCancelEvent(ui.__mem_func__(self.CancelQuestionDialog))
		self.QuestionDialog.Open()
			
	def DropAllItems(self):
		for i in xrange(90):
			net.SendItemDropPacket(i)
		self.CancelQuestionDialog()
		
	def CancelQuestionDialog(self):
		self.QuestionDialog.Close()
		self.QuestionDialog = None

	def ShowConfigurationBoard(self):
		self.UpgradeGui = []
		self.UpgradeTmpValue = self.type
		self.AddGuiUpgradeConfiguration()
		
	def HideConfigurationBoard(self):
		self.UpgradeGui[0].Hide()
		
	def AddGuiUpgradeConfiguration(self):
		Gui = [
			[[ui.BoardWithTitleBar, ""], [200, 220], [0,0], [["SetCenterPosition", [""]], ["SetCloseEvent", [self.HideConfigurationBoard]], ["SetTitleName", ["Upgrade Configuration"]]], ["movable", "float"]],			
			]
			
		GuiParser(Gui, self.UpgradeGui)
		
		tmp = []
		Modi = ["Ok", "Abbrechen"]		
		x = 12
		for mode in Modi:
			button = [[ui.Button, 0], [0, 0], [x, 185], [['SetUpVisual', ["d:/ymir work/ui/public/large_button_01.sub"]],['SetOverVisual', ["d:/ymir work/ui/public/large_button_02.sub"]], ['SetDownVisual', ["d:/ymir work/ui/public/large_button_03.sub"]], ['SetText', [mode]], ['SetEvent', [lambda arg = (Modi.index(mode)): self.Decision(arg)]]], []]
			tmp.append(button)
			x += 88
		
		GuiParser(tmp, self.UpgradeGui)
		
		self.RefreshUpgradeConfiguration()
		
	def Decision(self, index):
		if index == 0:
			self.type = self.UpgradeTmpValue
			chat.AppendChat(1, "Die Einstellungen wurden erfolgreich gespeichert.")
		else:
			chat.AppendChat(1, "Du hast die Änderungen der Einstellung abgebrochen.")
		self.HideConfigurationBoard()
			
	def UpgradeConfiguration(self, type):
		self.UpgradeTmpValue = type
		
		self.RefreshUpgradeConfiguration()
		
	def RefreshUpgradeConfiguration(self):
		while len(self.UpgradeGui) > 3:
			self.UpgradeGui.remove(self.UpgradeGui[3])
			
		tmp = []
		Modi = [["Dorfschmied", 0], [25040, 2], [25041, 3], ["Dt-Schmied", 4]]		
		y = 45
		for mode in Modi:
			if mode[1] == self.UpgradeTmpValue:
				Usage = "Use"
			else:
				Usage = "No Use"
			if isinstance(mode[0], str):
				desc = [[ui.TextLine, 0], [0, 0], [32, y], [["SetText", [mode[0]]]], []]
				button = [[ui.Button, 0], [0, 0], [102, y - 3], [['SetUpVisual', ["d:/ymir work/ui/public/middle_button_01.sub"]],['SetOverVisual', ["d:/ymir work/ui/public/middle_button_02.sub"]], ['SetDownVisual', ["d:/ymir work/ui/public/middle_button_03.sub"]], ['SetText', [Usage]], ['SetEvent', [lambda arg = (mode[1]): self.UpgradeConfiguration(arg)]]], []]
			else:
				desc = [[ui.ExpandedImageBox, 0], [0, 0], [32, y - 5], [['LoadImage', [item.GetIconImageFileName(item.GetItemName(item.SelectItem(mode[0])))]]], []]
				button = [[ui.Button, 0], [0, 0], [102, y], [['SetUpVisual', ["d:/ymir work/ui/public/middle_button_01.sub"]],['SetOverVisual', ["d:/ymir work/ui/public/middle_button_02.sub"]], ['SetDownVisual', ["d:/ymir work/ui/public/middle_button_03.sub"]], ['SetText', [Usage]], ['SetEvent', [lambda arg = (mode[1]): self.UpgradeConfiguration(arg)]]], []]
			tmp.append(desc)
			tmp.append(button)
			y += 35
		GuiParser(tmp, self.UpgradeGui)
		
TeleportHackMode = "Teleport"		

class NewTeleportHackDialog(ui.ScriptWindow):

	CurrentMapName = ""
	
	class AtlasRenderer(ui.Window):
		TeleportState = 1
		
		def __init__(self):
			ui.Window.__init__(self)
			self.AddFlag("not_pick")

		def OnUpdate(self):
			miniMap.UpdateAtlas()

		def OnRender(self):
			(PosX, PosY) = self.GetGlobalPosition()
			miniMap.RenderAtlas(float(PosX), float(PosY))
			
			if self.TeleportState == 0:
				self.Debug()
				
			if app.IsPressed(app.DIK_LSHIFT) and self.TeleportState == 1:
				(mouseX, mouseY) = wndMgr.GetMousePosition()
				(bFind, sName, iPosX, iPosY, dwTextColor, dwGuildID) = miniMap.GetAtlasInfo(mouseX, mouseY)
				
				(iSizeX, iSizeY, SizeX, SizeY) = GetCurrentMapSize()
				
				if not bFind:
					width = 6
					MapSizeX = miniMap.GetAtlasSize()[1]
					if MapSizeX == 0:
						size = 6
					else:
						size = DivideToFloat(SizeX * 256, miniMap.GetAtlasSize()[1])
					(sName, iPosX, iPosY, dwTextColor) = "", (mouseX - PosX) * size + width, (mouseY - PosY) * size, -8722595
				
				if iPosX < 0 or iPosY < 0 or iPosX > SizeX * 256 or iPosY > SizeY * 256:
					return

				self.TeleportState = 0
				
				self.TeleportToDest(iPosX*100, iPosY*100)

		def TeleportToDest(self, aimx, aimy):
			global TeleportHackMode
			if TeleportHackMode == "Walk":
				myVid = player.GetMainCharacterIndex()
				chr.MoveToDestPosition(int(myVid), int(aimx), int(aimy))
				self.TeleportState = 1
			else:		
				(TmpX, TmpY, Count) = GetTmpTeleport(aimx, aimy)
				TmpCount = 0
				
				while TmpCount < Count:
					(TmpX, TmpY, Crap) = GetTmpTeleport(aimx, aimy)
					chr.SetPixelPosition(int(TmpX), int(TmpY))
					TmpCount += 1
					self.Debug()
					
				chr.SetPixelPosition(int(aimx), int(aimy))
				self.Debug()
				self.TeleportState = 1

		def Debug(self):
			player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
			player.SetSingleDIKKeyState(app.DIK_UP, FALSE)			

		def ShowAtlas(self):
			miniMap.ShowAtlas()

		def HideAtlas(self):
			miniMap.HideAtlas()

	def __init__(self):
		self.tooltipInfo = uiminimap.MapTextToolTip()
		self.tooltipInfo.Hide()
		self.AtlasMainWindow = None
		self.board = 0
		self.CurrentMapName = background.GetCurrentMapName()
		ui.ScriptWindow.__init__(self)
		self.LoadWindow()

	def LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "UIScript/AtlasWindow.py")
		except:
			exception.Abort("AtlasWindow.LoadWindow.LoadScript")

		try:
			self.board = self.GetChild("board")
			self.board.SetTitleName("Teleportmodule")

		except:
			exception.Abort("AtlasWindow.LoadWindow.BindObject")

		self.AtlasMainWindow = self.AtlasRenderer()
		self.board.SetCloseEvent(self.Hide)
		self.AtlasMainWindow.SetParent(self.board)
		self.AtlasMainWindow.SetPosition(7, 30)
		self.tooltipInfo.SetParent(self.board)
		self.SetCenterPosition()
		
		self.Line = ui.Line()
		self.Line.SetParent(self)
		self.Line.SetColor(0xff777777)
		self.Line.Show()
		
		self.ModeText = ui.TextLine()
		self.ModeText.SetParent(self)
		self.ModeText.SetText("Mode:")
		self.ModeText.Show()

		self.PositionText = ui.TextLine()
		self.PositionText.SetParent(self)
		self.PositionText.SetFontColor(0.2, 0.2, 1.0)
		self.PositionText.SetText("(200, 800)")
		self.PositionText.Show()
		
		global TeleportHackMode
		self.ModeButton = ui.Button()
		self.ModeButton.SetParent(self)
		self.ModeButton.SetUpVisual("d:/ymir work/ui/public/middle_button_01.sub")
		self.ModeButton.SetOverVisual("d:/ymir work/ui/public/middle_button_02.sub")
		self.ModeButton.SetDownVisual("d:/ymir work/ui/public/middle_button_03.sub")
		self.ModeButton.SetText(TeleportHackMode)		
		self.ModeButton.SetEvent(lambda : self.ChangeMode())
		self.ModeButton.Show()
		
		self.Hide()

	def ChangeMode(self):
		global TeleportHackMode
		if TeleportHackMode == "Teleport":
			TeleportHackMode = "Walk"
		else:
			TeleportHackMode = "Teleport"
		self.ModeButton.SetText(TeleportHackMode)
		
	def Hide(self):
		ui.ScriptWindow.Hide(self)

	def Show(self):			
		if self.AtlasMainWindow:
			(iSizeX, iSizeY, SizeX, SizeY) = GetCurrentMapSize()
			self.SetSize(iSizeX + 15, iSizeY + 38 + 30)
			self.board.SetSize(iSizeX + 15, iSizeY + 38 + 30)
			self.Line.SetPosition(7, iSizeY + 31)
			self.Line.SetSize(iSizeX, 0)
			self.ModeText.SetPosition(15, iSizeY + 38)
			self.ModeButton.SetPosition(55, iSizeY + 36)
			self.PositionText.SetPosition(125, iSizeY + 38)
			
			self.AtlasMainWindow.ShowAtlas()
			self.AtlasMainWindow.Show()
		ui.ScriptWindow.Show(self)

	def OnUpdate(self):
		(PlayerX, PlayerY, PlayerZ) = player.GetMainCharacterPosition()
		self.PositionText.SetText("(%s, %s)" % (int(PlayerX / 100), int(PlayerY / 100)))
	
		if background.GetCurrentMapName() != self.CurrentMapName:
			self.Show()
			self.CurrentMapName = background.GetCurrentMapName()
	
		miniMap.ShowAtlas()
		if not self.tooltipInfo:
			return

		self.tooltipInfo.Hide()

		if FALSE == self.board.IsIn():
			return

		(mouseX, mouseY) = wndMgr.GetMousePosition()
		(bFind, sName, iPosX, iPosY, dwTextColor, dwGuildID) = miniMap.GetAtlasInfo(mouseX, mouseY)

		(PosX, PosY) = self.GetGlobalPosition()
		
		(iSizeX, iSizeY, SizeX, SizeY) = GetCurrentMapSize()
		if not bFind:
	
			#Thanks @musicinstructor for the displayed coordinates
			MapSizeX = miniMap.GetAtlasSize()[1]
			if MapSizeX == 0:
				size = 6
			else:
				size = DivideToFloat(SizeX * 256, miniMap.GetAtlasSize()[1])
			height = 30 * size
			width = 6 * size
			(sName, iPosX, iPosY, dwTextColor) = "", (mouseX - PosX) * size - width, (mouseY - PosY) * size - height, -8722595
			
		if iPosX < 0 or iPosY < 0 or iPosX > SizeX * 256 or iPosY > SizeY * 256:
			return

		self.tooltipInfo.SetText("%s(%d, %d)" % (sName, iPosX, iPosY))
		(x, y) = self.GetGlobalPosition()
		self.tooltipInfo.SetTooltipPosition(mouseX - x, mouseY - y)
		self.tooltipInfo.SetTextColor(dwTextColor)
		self.tooltipInfo.Show()
		self.tooltipInfo.SetTop()

	def OnPressEscapeKey(self):
		self.Hide()
		return TRUE
		
class Item(ui.ListBoxEx.Item):
	def __init__(self, fileName):
		ui.ListBoxEx.Item.__init__(self)
		self.canLoad=0
		self.text=fileName
		self.textLine=self.__CreateTextLine(fileName)          

	def __del__(self):
		ui.ListBoxEx.Item.__del__(self)

	def GetText(self):
		return self.text

	def SetSize(self, width, height):
		ui.ListBoxEx.Item.SetSize(self, 6*len(self.textLine.GetText()) + 4, height)

	def __CreateTextLine(self, fileName):
		textLine=ui.TextLine()
		textLine.SetParent(self)
		textLine.SetPosition(0, 0)
		textLine.SetText(fileName)
		textLine.Show()
		return textLine

class ItemPickUpHackDialog(ui.ScriptWindow):
	Gui = []
	
	def __init__(self):
		self.Gui = []
		ui.ScriptWindow.__init__(self)
		self.AddGui()
		
	def __del__(self):
		self.Gui[0].Hide()
		ui.ScriptWindow.__del__(self)	
	
	def AddGui(self):
		Gui = [
			[[ui.BoardWithTitleBar, ""], [278, 602], [0,0], [["SetCenterPosition", [""]], ["SetCloseEvent", [self.__del__]], ["SetTitleName", ["Item Pickup Board"]]], ["movable", "float"]],			
			[[ui.Button, 0], [0, 0], [25, 567], [['SetUpVisual', ["d:/ymir work/ui/public/large_button_01.sub"]],['SetOverVisual', ["d:/ymir work/ui/public/large_button_02.sub"]], ['SetDownVisual', ["d:/ymir work/ui/public/large_button_03.sub"]], ["SetText", ["Zurück"]], ['SetEvent', [lambda : self.SetPage("back")]]], []],			
			[[ui.Button, 0], [0, 0], [118, 567], [['SetUpVisual', ["d:/ymir work/ui/public/large_button_01.sub"]],['SetOverVisual', ["d:/ymir work/ui/public/large_button_02.sub"]], ['SetDownVisual', ["d:/ymir work/ui/public/large_button_03.sub"]], ["SetText", ["Weiter"]], ['SetEvent', [lambda : self.SetPage("next")]]], []],			
			[[ui.Button, 0], [0, 0], [211, 543], [['SetUpVisual', ["d:/ymir work/ui/public/small_button_01.sub"]],['SetOverVisual', ["d:/ymir work/ui/public/small_button_02.sub"]], ['SetDownVisual', ["d:/ymir work/ui/public/small_button_03.sub"]], ["SetText", ["Save"]], ['SetEvent', [lambda : self.SavePickUpArray()]]], []],			
			[[ui.Button, 0], [0, 0], [25, 543], [['SetUpVisual', ["d:/ymir work/ui/public/large_button_01.sub"]],['SetOverVisual', ["d:/ymir work/ui/public/large_button_02.sub"]], ['SetDownVisual', ["d:/ymir work/ui/public/large_button_03.sub"]], ["SetText", ["Alles"]], ['SetEvent', [lambda : self.AddPickUp()]]], []],			
			[[ui.Button, 0], [0, 0], [118, 543], [['SetUpVisual', ["d:/ymir work/ui/public/large_button_01.sub"]],['SetOverVisual', ["d:/ymir work/ui/public/large_button_02.sub"]], ['SetDownVisual', ["d:/ymir work/ui/public/large_button_03.sub"]], ["SetText", ["Nichts"]], ['SetEvent', [lambda : self.DeletePickUp(1)]]], []],			
			[[ui.Button, 0], [0, 0], [211, 567], [['SetUpVisual', ["d:/ymir work/ui/public/small_button_01.sub"]],['SetOverVisual', ["d:/ymir work/ui/public/small_button_02.sub"]], ['SetDownVisual', ["d:/ymir work/ui/public/small_button_03.sub"]], ["SetText", ["Löschen"]], ['SetEvent', [lambda : self.DeletePickUpArray()]]], []],			
			]
		GuiParser(Gui, self.Gui)
		
		try:
			handle = app.OpenTextFile(app.GetLocalePath() + "/item_list.txt")
			count = app.GetTextFileLineCount(handle)
		except:
			chat.AppendChat(1, app.GetLocalePath() + "/item_list.txt konnte nicht ausgelesen werden!")
			self.__del__()

		self.ItemList = []
		self.ItemCheckList = []
		
		#Special Items(idk why):
		Special = [1, 17180, 30010, 30071, 50300, 50416, 50417, 50418, 50419, 50420, 50491, 50492, 50493, 50494, 50495, 50496, 50506, 50507, 50508, 50509, 50510, 50511]
		
		TmpItemShit = []
		
		for ItemValue in Special:
			TmpItemShit.append(ItemValue)
		
		for i in xrange(count):
			line = app.GetTextFileLine(handle, i)
			try:
				ItemValue = int(line.split("\t")[0])
				ItemName = item.GetItemName(item.SelectItem(ItemValue)).lower()
				ItemSize = item.GetItemSize()[1]
					
				if ItemName != "" and EterPackOperator(item.GetIconImageFileName()).read() != "" and ItemSize > 0:
					if not ItemValue in TmpItemShit:
						TmpItemShit.append(ItemValue)
			except:
				pass
		
		TmpItemShit.sort()
		
		for ItemValue in TmpItemShit:
			ItemName = item.GetItemName(item.SelectItem(ItemValue)).lower()
			if ItemName.count("+") == 1 and not (ItemName.find("stein ") != -1 or ItemName.find("stone ") != -1):
				try:
					ItemNameSplit = ItemName.split("+")
					int(ItemNameSplit[1])
					ItemName = ItemNameSplit[0]
					if not ItemName in self.ItemCheckList:
						self.ItemCheckList.append(ItemName)
						self.ItemList.append(ItemValue)
				except:
					if not ItemName in self.ItemCheckList:
						self.ItemCheckList.append(ItemName)
						self.ItemList.append(ItemValue)
			else:
				if not ItemName in self.ItemCheckList:
					self.ItemCheckList.append(ItemName)
					self.ItemList.append(ItemValue)
		
#		open("testdump.py", "a+").write(str(self.ItemCheckList))
		self.AppendItems(0, 25)
		
	def AddPickUp(self):
		PickUpList = GetPickUpList()
		PickUpListNames = GetPickUpListNames()
		self.DeletePickUp(0)
		
		for items in self.ItemCheckList:
			PickUpList.append(items)
		
		for items in self.ItemList:
			PickUpList.append(items)
			
		chat.AppendChat(1, "Alle Drops werden jetzt aufgehoben.")
		
		for Index in xrange(17):
			try:
				self.Gui[9 + Index * 3].SetText("on")
			except:
				pass
				
	def DeletePickUp(self, state):
		PickUpList = GetPickUpList()
		PickUpListNames = GetPickUpListNames()

		while len(PickUpListNames) > 0:
			PickUpListNames.remove(PickUpListNames[0])
			
		while len(PickUpList) > 0:
			PickUpList.remove(PickUpList[0])
			
		for Index in xrange(17):
			try:
				self.Gui[9 + Index * 3].SetText("off")
			except:
				pass
			
		if state:
			chat.AppendChat(1, "Alle Drops wurden entfernt.")
				
	def SavePickUpArray(self):
		PickUpList = GetPickUpList()
		if len(PickUpList) == 0:
			chat.AppendChat(1, "Bitte trage erstmal Drops ein.")
			return
		try:
			os.remove("lib/pickuplist.save")
		except:
			pass
		for result in PickUpList:
			open("lib/pickuplist.save", "a+").write(str(result) + "\n")
		chat.AppendChat(1, "Die Einstellungen wurden erfolgreich gespeichert.")
		
	def DeletePickUpArray(self):
		"""
		PickUpList = GetPickUpList()
		PickUpListNames = GetPickUpListNames()
		for name in PickUpListNames:
			chat.AppendChat(1, str(name) + ": " + str(PickUpList[PickUpListNames.index(name)]))
		return
		"""
		try:
			os.remove("lib/pickuplist.save")
		except:
			pass	
			
		chat.AppendChat(1, "Die Einstellungsdatei wurden gelöscht.")
		
	def AppendItems(self, start, end):		
		tmp = []
		x = 20
		y = 30
		Count = 0
		TemporaryIndex = 0
	
		for i in xrange(start, end):
			try:
				ItemValue = self.ItemList[i]
			except:
				break
			ItemSize = item.GetItemSize(item.SelectItem(ItemValue))
			if Count == 0:
				self.StartValue = ItemValue
			Count += ItemSize[1]
			if Count >= 17:
				break
				
			ItemName = item.GetItemName()
			try:
				if ItemName.lower().find("stein ") != -1 or ItemName.lower().find("stone ") != -1: 
					pass
				else:
					int(ItemName.split("+")[1])
					ItemName = ItemName.split("+")[0]
			except:
				pass

			ItemIcon = item.GetIconImageFileName()
			Image = [[ui.ExpandedImageBox, 0], [0, 0], [x, y], [['LoadImage', [ItemIcon]]], []]
			Name = [[ui.TextLine, 0], [0, 0], [x  + 5 + ItemSize[0] * 32, y + (ItemSize[1] * 32) / 2 - 8], [["SetText", [ItemName]]], []]
			PickUpList = GetPickUpList()
			try:
				PickUpList.index(ItemValue)
				State = "on"
			except:
				State = "off"			
			Button = [[ui.Button, 0], [0, 0], [x  + 5 + 170, y + (ItemSize[1] * 32) / 2 - 8], [['SetUpVisual', ["d:/ymir work/ui/public/middle_button_01.sub"]],['SetOverVisual', ["d:/ymir work/ui/public/middle_button_02.sub"]], ['SetDownVisual', ["d:/ymir work/ui/public/middle_button_03.sub"]], ["SetText", [State]], ['SetEvent', [lambda Value = [ItemValue, TemporaryIndex]: self.AddItemToPickUp(Value)]]], []]	
			tmp.append(Image)
			tmp.append(Name)
			tmp.append(Button)
			
			TemporaryIndex += 1
			y += ItemSize[1] * 32
			self.ItemValue = ItemValue

		GuiParser(tmp, self.Gui)
		
	def AddItemToPickUp(self, value):
		Index = value[1]
		value = value[0]
		PickUpList = GetPickUpList()
		PickUpListNames = GetPickUpListNames()

		ItemName = item.GetItemName(item.SelectItem(value))
		try:
			if ItemName.lower().find("stein ") != -1 or ItemName.lower().find("stone ") != -1: 
				pass
			else:
				int(ItemName.split("+")[1])
				ItemName = ItemName.split("+")[0]
		except:
			pass
		
		try:
			PickUpListNames.remove(ItemName)
		except:
			PickUpListNames.append(ItemName)
		
		try:
			PickUpList.remove(value)
			chat.AppendChat(1, ItemName + " wird nicht mehr aufgehoben.")
			try:
				self.Gui[9 + Index * 3].SetText("off")
			except:
				pass
		except:
			PickUpList.append(value)
			chat.AppendChat(1, ItemName + " wird ab jetzt aufgehoben.")
			try:
				self.Gui[9 + Index * 3].SetText("on")
			except:
				pass			
		
	def SetPage(self, arg):
		if arg == "next":
			Start = self.ItemList.index(self.ItemValue) + 1
			try:
				End = self.ItemList[Start + 25]
			except:
				End = len(self.ItemList)
			if Start == End:
				return	
		else:
			SizeCount = 0
			End = self.ItemList.index(self.StartValue)
			if self.ItemList[End] == self.ItemList[0]:
				return
			for range in xrange(0, 25):
				ItemValue = End - range
				ItemSize = item.GetItemSize(item.SelectItem(self.ItemList[ItemValue]))
				SizeCount += ItemSize[1]
				if SizeCount >= 17 or ItemValue == 0:
					Start = ItemValue
					End = Start + 17
					break
			
		while len(self.Gui) > 7:
			try:
				self.Gui.remove(self.Gui[7])
			except:
				pass
			
		self.AppendItems(Start, End)
	
class PrivateServerModulesDialog(ui.ScriptWindow):
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.AddGui()
		
	def __del__(self):
		self.Board.Hide()
		ui.ScriptWindow.__del__(self)	
	
	def AddGui(self):
		global PrivateServerOptions
		self.ConfigGui = []
		self.Board = ui.BoardWithTitleBar()
		self.Board.SetSize(249, 55 + 25 * len(PrivateServerOptions))
		self.Board.SetTitleName("Private Server Modules")
		self.Board.SetCenterPosition()
		self.Board.AddFlag("movable")
		self.Board.AddFlag("float")
		self.Board.SetCloseEvent(self.__del__)
		self.Board.Show()
		
		y = 45
		for bla in PrivateServerOptions:
			Text = ui.TextLine()
			Text.SetDefaultFontName()
			Text.SetParent(self.Board)
			Text.SetPosition(25, y)
			Text.SetText(str(bla[0]))
			Text.Show()
				
			Button = ui.Button()
			Button.SetParent(self.Board)
			Button.SetUpVisual("d:/ymir work/ui/public/large_button_01.sub")
			Button.SetOverVisual("d:/ymir work/ui/public/large_button_02.sub")
			Button.SetDownVisual("d:/ymir work/ui/public/large_button_03.sub")
			Button.SetPosition(130, y - 3)
			if isinstance(bla[1], str):
				Button.SetText("deaktiviert")
			else:
				Button.SetText("öffnen")
				Button.SetEvent(lambda event = bla[1]: event().Show())
			Button.Show()			
			y += 25
			self.ConfigGui.append([Button, Text])
	
class ReadBookBotDialog(ui.ScriptWindow):
	Gui = []
	
	Books =   {"Warrior" : [[50401, 50402, 50403, 50404, 50405, 50406], [50416, 50417, 50418, 50419, 50420, 50421]], 
	"Assassin" : [[50431, 50432, 50433, 50434, 50435, 50436], [50446, 50447, 50448, 50449, 50450, 50451]],
	"Sura" : [[50461, 50462, 50463, 50464, 50465, 50466], [50476, 50477, 50478, 50479, 50450, 50451]],
	"Shaman" : [[50491, 50492, 50493, 50494, 50495, 50496], [50506, 50507, 50508, 50509,50510, 505011]],
	}
	
	State = "Stop"	
	TimeStamp = 0
	Konzi = 1
	BannedSlotIndex = []
	
	def KonziState(self):
		if self.Konzi == 1:
			self.Konzi = 0
			chat.AppendChat(1, "Konzentriertes Lesen wird nicht mehr verwendet.")
			self.Gui[9].SetText("Not using")
		else:
			self.Konzi = 1
			chat.AppendChat(1, "Konzentriertes Lesen wird verwendet.")
			self.Gui[9].SetText("Using")		
	
	def __init__(self):
		self.Gui = []
		ui.ScriptWindow.__init__(self)
		self.AddGui()
		
	def __del__(self):
		self.Gui[0].Hide()
		ui.ScriptWindow.__del__(self)
		
	def AddGui(self):
		Gui = [
			[[ui.ThinBoard, ""], [218, 280], [0,0], [["SetCenterPosition", [""]]], ["movable", "float"]],			
			[[ui.Button, 0], [0, 0], [183, 18], [['SetUpVisual', ["d:/ymir work/ui/public/close_button_01.sub"]],['SetOverVisual', ["d:/ymir work/ui/public/close_button_02.sub"]], ['SetDownVisual', ["d:/ymir work/ui/public/close_button_03.sub"]], ['SetToolTipText', ["Schließen", 0, - 23]], ['SetEvent', [lambda : self.__del__()]]], []],	
			[[ui.SlotBar, 0], [190, 135], [10, 35], [], []],			
			[[ui.ListBoxEx, 0], [0, 0], [15, 50], [["SetViewItemCount", [10]]], []],			
			[[ui.TextLine, 0], [0, 0], [55, 18], [["SetDefaultFontName", [""]],	["SetText", ["Skill Book Reader"]],	["SetFontColor", [0.4, 0.7, 1.0]]], []],			
			[[ui.TextLine, 0], [0, 0], [13, 37], [["SetDefaultFontName", [""]],	["SetText", ["Skill  ID:         Name:"]],	["SetFontColor", [0.2, 0.2, 1.0]]], []],			
			[[ui.Button, 0], [0, 0], [15, 235], [['SetUpVisual', ["d:/ymir work/ui/public/Large_button_01.sub"]],['SetOverVisual', ["d:/ymir work/ui/public/Large_button_02.sub"]], ['SetDownVisual', ["d:/ymir work/ui/public/Large_button_03.sub"]], ["SetText", ["Start"]], ['SetEvent', [lambda : self.StartReading()]]], []],	
			[[ui.Button, 0], [0, 0], [110, 235], [['SetUpVisual', ["d:/ymir work/ui/public/Large_button_01.sub"]],['SetOverVisual', ["d:/ymir work/ui/public/Large_button_02.sub"]], ['SetDownVisual', ["d:/ymir work/ui/public/Large_button_03.sub"]], ["SetText", ["Break"]], ['SetEvent', [lambda : self.BreakReading()]]], []],	
			[[ui.ExpandedImageBox, 0], [0, 0], [45, 190], [['LoadImage', [item.GetIconImageFileName(item.SelectItem(71094))]]], []],
			[[ui.Button, 0], [0, 0], [90, 190], [['SetUpVisual', ["d:/ymir work/ui/public/Large_button_01.sub"]],['SetOverVisual', ["d:/ymir work/ui/public/Large_button_02.sub"]], ['SetDownVisual', ["d:/ymir work/ui/public/Large_button_03.sub"]], ["SetText", ["Using"]], ['SetEvent', [lambda : self.KonziState()]]], []],	
			]
		GuiParser(Gui, self.Gui)		

		self.AddItems()
		
	def AddItems(self):
		RaceGroupInfo = GetClass()
		Class = str(RaceGroupInfo).split("/")[0]
		group = str(RaceGroupInfo).split("/")[1]
		if Class == "Warrior":
			self.SkillIndex = 1
			if int(group) == 2:
				self.SkillIndex = 16
		elif Class == "Assassin":
			self.SkillIndex = 31
			if int(group) == 2:
				self.SkillIndex = 46
		elif Class == "Sura":
			self.SkillIndex = 61
			if int(group) == 2:
				self.SkillIndex = 76
		elif Class == "Shaman":
			self.SkillIndex = 91
			if int(group) == 2:
				self.SkillIndex = 106

		for i in xrange(NewSkillsEnable()):
			Skillname = skill.GetSkillName(self.SkillIndex)
			RaceGroupInfo = GetClass().split("/")
			ID = self.Books[RaceGroupInfo[0]][int(RaceGroupInfo[1]) - 1][i]
			if str(Skillname) != "None":
				self.Gui[3].AppendItem(Item(str(self.SkillIndex) + "      " + str(ID) + "      " + str(Skillname)))
				self.SkillIndex += 1
			
	def BreakReading(self):
		self.State = "Stop"
		
	def ReadBooks(self):
		if (player.GetItemCountByVnum(50300) == 0 and player.GetItemCountByVnum(int(self.SkillBook[1])) == 0) or player.GetItemCountByVnum(71001) == 0:
			result = 0
			if shop.IsOpen():
				for EachShopSlot in xrange(shop.SHOP_SLOT_COUNT):
					ShopItemValue = shop.GetItemID(EachShopSlot)
					if ShopItemValue == int(self.SkillBook[1]):
						net.SendShopBuyPacket(EachShopSlot)
						self.BannedSlotIndex = []
						result = 1
						break
			if result == 0 or player.GetItemCountByVnum(71001) == 0:
				chat.AppendChat(1, "Dir fehlen die benötigten Items um diesen Skill zu leveln.")
				self.BreakReading()
				return
			
		for Slot in xrange(player.INVENTORY_PAGE_SIZE*2):
			ItemValue = player.GetItemIndex(Slot)
			if ItemValue == 50300:
				metinSlot = [player.GetItemMetinSocket(Slot, i) for i in xrange(player.METIN_SOCKET_MAX_NUM)]
				if metinSlot[0] == int(self.SkillBook[0]):
					net.SendItemUsePacket(Slot)
					while len(self.BannedSlotIndex) >= 4:
						self.BannedSlotIndex.remove(self.BannedSlotIndex[0])
					self.BannedSlotIndex.append(Slot)
					break
			if ItemValue == int(self.SkillBook[1]):
				while len(self.BannedSlotIndex) >= 4:
					self.BannedSlotIndex.remove(self.BannedSlotIndex[0])
				try:
					self.BannedSlotIndex.index(Slot)
				except:
					net.SendItemUsePacket(Slot)
					self.BannedSlotIndex.append(Slot)
					break
		
		Exo = 0
		if self.UseConcentrated():
			Konz = 0
		else:
			Konz = 1
		
		for Slot in xrange(player.INVENTORY_PAGE_SIZE*2):
			ItemValue = player.GetItemIndex(Slot)
			if ItemValue == 71001 and Exo == 0:
				net.SendItemUsePacket(Slot)
				Exo = 1
			if ItemValue == 71094 and Konz == 0:
				net.SendItemUsePacket(Slot)
				Konz = 1
			if Konz == 1 and Exo == 1:
				break
	
		self.TimeStamp = float(app.GetTime()) + 0.25

	def OnUpdate(self):
		if self.State != "Start":
			return
	
		if app.GetTime() >= self.TimeStamp:
			if self.IsReadAble(self.SkillCount):
				self.ReadBooks()
			else:
				chat.AppendChat(1, "Dieser Skill hat nicht das benötigte Level.")
				self.BreakReading()
		
	def IsReadAble(self, count):
		Skillgrade = player.GetSkillGrade(count)
		Skilllevel = player.GetSkillLevel(count)

		if 1 == Skillgrade:
			Skilllevel += 19
		elif 2 == Skillgrade:
			Skilllevel += 29
		elif 3 == Skillgrade:
			Skilllevel = 40
		
		if Skilllevel < 20:
			return 0
		elif Skilllevel < 30 and Skilllevel >= 20:
			return 1
		else:
			return 0
		
	def StartReading(self):
		ItemIndex = self.Gui[3].GetSelectedItem()
		if ItemIndex:
			pass
		else:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Kein Item ausgewählt!")
			return
		self.SkillBook = ItemIndex.GetText().split("      ")
		
		RaceGroupInfo = GetClass().split("/")
		self.SkillCount = self.Books[RaceGroupInfo[0]][int(RaceGroupInfo[1]) - 1].index(int(self.SkillBook[1])) + 1

		self.TimeStamp = app.GetTime()
		self.State = "Start"	
	
	def UseConcentrated(self):
		if player.GetItemCountByVnum(71094) > 0:
			if self.Konzi == 1:
				return 1
		else:
			if self.Konzi == 1:
				chat.AppendChat(1, "Du hast keine Konzentrierte Lesen mehr im Inventar.")
				self.BreakReading()

class SoulStoneBotDialog(ui.ScriptWindow):
	Gui = []
	
	State = "Stop"	
	TimeStamp = 0
	Zen = 1
	ReadExo = 1
	
	def ZenState(self):
		if self.Zen == 1:
			self.Zen = 0
			chat.AppendChat(1, "Zen-Bohne wird nicht mehr verwendet.")
			self.Gui[9].SetText("Not using")
		else:
			self.Zen = 1
			chat.AppendChat(1, "Zen-Bohne wird verwendet.")
			self.Gui[9].SetText("Using")		
	
	def __init__(self):
		self.Gui = []
		ui.ScriptWindow.__init__(self)
		self.AddGui()
		
	def __del__(self):
		self.Gui[0].Hide()
		ui.ScriptWindow.__del__(self)
		
	def AddGui(self):
		Gui = [
			[[ui.ThinBoard, ""], [218, 330], [0,0], [["SetCenterPosition", [""]]], ["movable", "float"]],			
			[[ui.Button, 0], [0, 0], [183, 18], [['SetUpVisual', ["d:/ymir work/ui/public/close_button_01.sub"]],['SetOverVisual', ["d:/ymir work/ui/public/close_button_02.sub"]], ['SetDownVisual', ["d:/ymir work/ui/public/close_button_03.sub"]], ['SetToolTipText', ["Schließen", 0, - 23]], ['SetEvent', [lambda : self.__del__()]]], []],	
			[[ui.SlotBar, 0], [190, 135], [10, 35], [], []],			
			[[ui.ListBoxEx, 0], [0, 0], [15, 50], [["SetViewItemCount", [10]]], []],			
			[[ui.TextLine, 0], [0, 0], [55, 18], [["SetDefaultFontName", [""]],	["SetText", ["Soul Stone Reader"]],	["SetFontColor", [0.4, 0.7, 1.0]]], []],			
			[[ui.TextLine, 0], [0, 0], [13, 37], [["SetDefaultFontName", [""]],	["SetText", ["Skill  Count:         Name:"]],	["SetFontColor", [0.2, 0.2, 1.0]]], []],			
			[[ui.Button, 0], [0, 0], [15, 285], [['SetUpVisual', ["d:/ymir work/ui/public/Large_button_01.sub"]],['SetOverVisual', ["d:/ymir work/ui/public/Large_button_02.sub"]], ['SetDownVisual', ["d:/ymir work/ui/public/Large_button_03.sub"]], ["SetText", ["Start"]], ['SetEvent', [lambda : self.StartReading()]]], []],	
			[[ui.Button, 0], [0, 0], [110, 285], [['SetUpVisual', ["d:/ymir work/ui/public/Large_button_01.sub"]],['SetOverVisual', ["d:/ymir work/ui/public/Large_button_02.sub"]], ['SetDownVisual', ["d:/ymir work/ui/public/Large_button_03.sub"]], ["SetText", ["Break"]], ['SetEvent', [lambda : self.BreakReading()]]], []],	
			[[ui.ExpandedImageBox, 0], [0, 0], [45, 190], [['LoadImage', [item.GetIconImageFileName(item.SelectItem(70102))]]], []],
			[[ui.Button, 0], [0, 0], [90, 190], [['SetUpVisual', ["d:/ymir work/ui/public/Large_button_01.sub"]],['SetOverVisual', ["d:/ymir work/ui/public/Large_button_02.sub"]], ['SetDownVisual', ["d:/ymir work/ui/public/Large_button_03.sub"]], ["SetText", ["Using"]], ['SetEvent', [lambda : self.ZenState()]]], []],	
			[[ui.TextLine, 0], [0, 0], [23, 225], [["SetDefaultFontName", [""]],	["SetText", ["Read already:"]]], []],			
			[[ui.Button, 0], [0, 0], [100, 225], [['SetUpVisual', ["d:/ymir work/ui/public/Large_button_01.sub"]],['SetOverVisual', ["d:/ymir work/ui/public/Large_button_02.sub"]], ['SetDownVisual', ["d:/ymir work/ui/public/Large_button_03.sub"]], ["SetText", ["Yes"]], ['SetEvent', [lambda : self.ConfigExo()]]], []],	
			[[ui.TextLine, 0], [0, 0], [23, 250], [["SetDefaultFontName", [""]],	["SetText", ["Confirm String"]]], []],			
			[[ui.SlotBar, 0], [87, 18], [100, 250], [], []],			
			[[ui.EditLine, 13], [87, 17], [6, 2], [["SetMax", [16]], ["SetFocus", [""]]], []],			
			]
		GuiParser(Gui, self.Gui)		

		self.AddItems()
		
	def ConfigExo(self):
		if self.ReadExo == 1:
			self.ReadExo = 0
			self.Gui[11].SetText("No")
		else:
			self.ReadExo = 1
			self.Gui[11].SetText("Yes")
		
	def AddItems(self):
		RaceGroupInfo = GetClass()
		Class = str(RaceGroupInfo).split("/")[0]
		group = str(RaceGroupInfo).split("/")[1]
		if Class == "Warrior":
			self.SkillIndex = 1
			if int(group) == 2:
				self.SkillIndex = 16
		elif Class == "Assassin":
			self.SkillIndex = 31
			if int(group) == 2:
				self.SkillIndex = 46
		elif Class == "Sura":
			self.SkillIndex = 61
			if int(group) == 2:
				self.SkillIndex = 76
		elif Class == "Shaman":
			self.SkillIndex = 91
			if int(group) == 2:
				self.SkillIndex = 106
				
		for Count in xrange(NewSkillsEnable()):
			Skillname = skill.GetSkillName(self.SkillIndex)
			Count += 1
			RaceGroupInfo = GetClass().split("/")
			if str(Skillname) != "None":
				self.Gui[3].AppendItem(Item(str(self.SkillIndex) + "      " + str(Count) + "      " + str(Skillname)))
				self.SkillIndex += 1
			
	def BreakReading(self):
		self.UnHookQuestWindow()
		self.State = "Stop"
		
	def GetNeededAlignment(self):
		point, grade = player.GetAlignmentData()
		SkillLevel = self.IsReadAble(int(self.SkillBook[1]), 1)
		NeedAlignment = 1000+500*(SkillLevel-30)
		if point < 0:
			NeedAlignment = NeedAlignment * 2
		
		if point - NeedAlignment <= -20000:
			if not self.Zen:
				chat.AppendChat(1, "You need more alignment than this: " + str(point + NeedAlignment))
				self.State = "Stop"
				return 0
			else:
				if player.GetItemCountByVnum(70102) == 0:
					chat.AppendChat(1, "Du hast keine Zen-Bohnen mehr.")
					self.BreakReading()

				round = -1 * point / 2000
				for Slot in xrange(player.INVENTORY_PAGE_SIZE*2):
					ItemValue = player.GetItemIndex(Slot)
					if ItemValue == 70102:
						for i in xrange(round):
							net.SendItemUsePacket(Slot)
						break					
		return 1
		
	def ReadBooks(self, SkillIndex):
		if player.GetItemCountByVnum(50513) == 0 or player.GetItemCountByVnum(71001) == 0:
			result = 0
			if shop.IsOpen():
				for EachShopSlot in xrange(shop.SHOP_SLOT_COUNT):
					ShopItemValue = shop.GetItemID(EachShopSlot)
					if ShopItemValue == 50513:
						net.SendShopBuyPacket(EachShopSlot)
						result = 1
						break
			if result == 0:
				chat.AppendChat(1, "Dir fehlen die benötigten Items um diesen Skill zu leveln.")
				self.BreakReading()
				return

		for Slot in xrange(player.INVENTORY_PAGE_SIZE*2):
			ItemValue = player.GetItemIndex(Slot)
			if ItemValue == 71001:
				net.SendItemUsePacket(Slot)
				break
				
		for Slot in xrange(player.INVENTORY_PAGE_SIZE*2):
			ItemValue = player.GetItemIndex(Slot)
			if ItemValue == 50513:
				net.SendItemUsePacket(Slot)
				if self.State != "Stop":
					if self.GetNeededAlignment():
						self.ReadQuest(SkillIndex)
				break
				
	def CheckIndex(self, AskedSkill):
		self.ReadAbleSkillList = []
		for Count in xrange(NewSkillsEnable()):
			if self.IsReadAble(Count, 0):
				self.ReadAbleSkillList.append(Count)
		return(str(self.ReadAbleSkillList.index(AskedSkill)))
	
	def OnUpdate(self):
		if self.State != "Start":
			return
	
		if app.GetTime() >= self.TimeStamp:
			if self.IsReadAble(int(self.SkillBook[1]), 0):
				self.TimeStamp = app.GetTime() + 1
				self.ReadBooks(self.CheckIndex(int(self.SkillBook[1])))
			else:
				chat.AppendChat(1, "Dieser Skill hat nicht das benötigte Level.")
				self.BreakReading()
		
	def ReadQuest(self, index):
		if self.State == "Stop":
			return
		import event
		#start
		if self.ReadExo:
			event.SelectAnswer(1, 254)
		else:
			self.ReadExo = 1
			self.Gui[11].SetText("Yes")
		#select skill
		event.SelectAnswer(1, int(index))
		#say you want to read
		event.SelectAnswer(1, 0)
		#send string packet
		net.SendQuestInputStringPacket(self.Gui[14].GetText())		
		#sucess/fail
		event.SelectAnswer(1, 0)
		
	def IsReadAble(self, count, state):
		Skillgrade = player.GetSkillGrade(count)
		Skilllevel = player.GetSkillLevel(count)

		if 1 == Skillgrade:
			Skilllevel += 19
		elif 2 == Skillgrade:
			Skilllevel += 29
		elif 3 == Skillgrade:
			Skilllevel = 40
		
		if state != 1:
			if Skilllevel > 29 and Skilllevel < 40:
				return 1	
		else:
			return(Skilllevel)
		
	def StartReading(self):
		ItemIndex = self.Gui[3].GetSelectedItem()
		if ItemIndex:
			pass
		else:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Kein Item ausgewählt!")
			return
		self.SkillBook = ItemIndex.GetText().split("      ")
		
		RaceGroupInfo = GetClass().split("/")

		self.TimeStamp = app.GetTime()
		self.State = "Start"	
		self.InstallQuestWindowHook()
	
	def InstallQuestWindowHook(self):
		self.OldRecv = game.GameWindow.OpenQuestWindow
		game.GameWindow.OpenQuestWindow = self.HookedQuestWindow
		chat.AppendChat(1, "Quest Window wurde erfolgreich gehooked.")		
		
	def UnHookQuestWindow(self):
		game.GameWindow.OpenQuestWindow = self.OldRecv
		chat.AppendChat(1, "Quest Window Hook wurde entfernt.")
		
	def HookedQuestWindow(self, skin, idx):
		pass
		
class SwitchBotDialog(ui.ScriptWindow):
	Gui = []
	BoniGui = []
	
	Values = []
	Boni = []
	Count = 0
	Slot = 0
	Startmode = 0
	
	LastProcessTimeStamp = 0
	
	SlotStack = [0, 0]
	
	BonusIDListe = [["keiner", 0], ["Max. TP", 1], ["Max. MP", 2], ["Vitalität", 3], ["Intelligenz", 4], ["Stärke", 5], ["Ausweichwert", 6], ["Angriffsgeschwindigkeit", 7], ["Bewegungsgeschwindigkeit", 8], ["Zaubergeschwindigkeit", 9], ["TP-Regeneration", 10], ["MP-Regeneration", 11], ["Vergiftungschance", 12], ["Ohnmachtschance", 13], ["Verlangsamungschance", 14], ["Kritischer Treffer", 15], ["Durchbohrender Treffer", 16], ["Stark ggn Halbmenschen", 17], ["Stark ggn Tiere", 18], ["Stark ggn Orks", 19], ["Stark ggn Esoterische", 20], ["Stark ggn Untote", 21], ["Stark ggn Teufel", 22], ["TP-Absorbierung", 23], ["MP-Absorbierung", 24], ["Chance auf Manaraub", 25], ["Chance MP-Regeneration", 26], ["Nahkampf-Angriff blocken", 27], ["Pfeilangriff ausweichen", 28], ["Schwertverteidigung", 29], ["Zweihandverteidigung", 30], ["Dolchverteidigung", 31], ["Glockenverteidigung", 32], ["Fächerverteidigung", 33], ["Pfeilwiderstand", 34], ["Feuerwiderstand", 35,	"Blitzwiderstand", 36], ["Magieverteidigung", 37], ["Windverteidigung", 38], ["Nahkampftreffer reflektieren", 39], ["Fluch reflektieren", 40], ["Giftverteidigung", 41], ["Chance MP wiederherzustellen", 42], ["Exp-Bonus", 43], ["Yang-Drop", 44], ["Item-Drop", 45], ["steigernde Trankwirkung", 46], ["Chance TP wiederherzustellen", 47], ["Immun gegen Ohnmacht", 48], ["Immun gegen Verlangsamung", 49], ["Immun gegen Stürzen", 50], ["APPLY_SKILL", 51], ["Pfeilreichweite", 52], ["Angriffswert", 53], ["Verteidigungswert", 54], ["Magischer Angriffswert", 55], ["Magischer Verteidigungswert", 56], ["Max. Ausdauer", 58], ["Stark gegen Krieger", 59], ["Stark gegen Ninjas", 60], ["Stark gegen Suras", 61], ["Stark gegen Schamanen", 62], ["Stark gegen Monster", 63], ["Itemshop Angriffswert", 64], ["Itemshop Verteidigungswert", 65], ["Itemshop Exp-Bonus", 66], ["Itemshop Item-Bonus", 67], ["Itemshop Yang-Bonus", 68], ["APPLY_MAX_HP_PCT", 69], ["APPLY_MAX_SP_PCT", 70], ["Fertigkeitsschaden", 71], ["Durchschn. Schaden", 72], ["Fertigkeitsschaden Widerstand", 73], ["Durchschn. Schadenswiderstand", 74], ["iCafe EXP-Bonus", 76], ["iCafe Item-Bonus", 77], ["Abwehr ggn Krieger", 78], ["Abwehr ggn Ninjas", 79], ["Abwehr ggn Suras", 80], ["Abwehr ggn Schamanen", 81]]

	SearchBoni = []
	SearchBoniValues = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
	
	SwitchValue = 71084
	
	State = "Stop"
	
	def __init__(self):
		self.Gui = []
		ui.ScriptWindow.__init__(self)
		self.AddGui()
		
	def __del__(self):
		self.Gui[0].Hide()
		ui.ScriptWindow.__del__(self)
		
	def AddGui(self):
		Gui = [
			[[ui.ThinBoard, ""], [533, 353], [0,0], [["SetCenterPosition", [""]]], ["movable", "float"]],			
			[[ui.Button, 0], [0, 0], [493, 18], [['SetUpVisual', ["d:/ymir work/ui/public/close_button_01.sub"]],['SetOverVisual', ["d:/ymir work/ui/public/close_button_02.sub"]], ['SetDownVisual', ["d:/ymir work/ui/public/close_button_03.sub"]], ['SetToolTipText', ["Schließen", 0, - 23]], ['SetEvent', [lambda : self.__del__()]]], []],	
			[[ui.SlotBar, 0], [190, 255], [10, 35], [], []],			
			[[ui.ListBoxEx, 0], [0, 0], [15, 65], [["SetViewItemCount", [11]], ["SetItemStep",[20]]], []],			
			[[ui.ScrollBar, 0], [0, 0], [180, 55], [["SetScrollBarSize", [230]]], []],			
			[[ui.TextLine, 0], [0, 0], [10, 39], [["SetDefaultFontName", [""]],	["SetText", ["Slot:			Name:"]],	["SetFontColor", [0.2, 0.2, 1.0]]], []],
			[[ui.TextLine, 0], [0, 0], [210, 180], [["SetText", ["Boni"]],	["SetFontColor", [0.2, 0.2, 1.0]]], []],
			[[ui.TextLine, 0], [0, 0], [370, 180], [["SetText", ["Altern. Boni"]],	["SetFontColor", [0.2, 0.2, 1.0]]], []],
			[[ui.Line, 0], [310, 0], [210, 195], [["SetColor",[0xff777777]]], []],
			[[ui.Button, 0], [0, 0], [179, 305], [['SetUpVisual', ["d:/ymir work/ui/public/large_button_01.sub"]],['SetOverVisual', ["d:/ymir work/ui/public/large_button_02.sub"]], ['SetDownVisual', ["d:/ymir work/ui/public/large_button_03.sub"]], ["SetText", ["Start"]], ['SetEvent', [lambda : self.ChangeState("Start")]]], []],			
			[[ui.Button, 0], [0, 0], [272, 305], [['SetUpVisual', ["d:/ymir work/ui/public/large_button_01.sub"]],['SetOverVisual', ["d:/ymir work/ui/public/large_button_02.sub"]], ['SetDownVisual', ["d:/ymir work/ui/public/large_button_03.sub"]], ["SetText", ["Stop"]], ['SetEvent', [lambda : self.ChangeState("Stop")]]], []],
			[[ui.TextLine, 0], [0, 0], [210, 18], [["SetText", ["Switchbot v3.1.2 by DaRealFreak"]],	["SetFontColor", [0.8, 0.6, 0.1]]], []],
			]
			
		GuiParser(Gui, self.Gui)
		
		tmp = []
		y = 37
		texty = 200
		for i in xrange(5):
			button = [[ui.Button, 0], [0, 0], [210, y], [['SetUpVisual', ["d:/ymir work/ui/public/Large_button_01.sub"]],['SetOverVisual', ["d:/ymir work/ui/public/Large_button_02.sub"]], ['SetDownVisual', ["d:/ymir work/ui/public/Large_button_03.sub"]], ["SetText", ["Bonus " + str(i + 1)]], ['SetEvent', [lambda Index = i: self.SelectBonus(Index)]]], []]
			slotbar = [[ui.SlotBar, 0], [35, 18], [310, y], [], []]
			editline = [[ui.EditLine, 13 + i*4], [35, 17], [6, 2], [["SetMax", [4]], ["SetNumberMode", [""]], ["SetText", ["0"]]], []]
			textline = [[ui.TextLine, 0], [0, 0], [210, texty], [["SetText", ["keiner"]]], []]
			tmp.append(button)
			tmp.append(slotbar)
			tmp.append(textline)
			tmp.append(editline)
			y += 30
			texty += 20
			
		y = 37
		texty = 200
		for i in xrange(5, 10):
			button = [[ui.Button, 0], [0, 0], [370, y], [['SetUpVisual', ["d:/ymir work/ui/public/Large_button_01.sub"]],['SetOverVisual', ["d:/ymir work/ui/public/Large_button_02.sub"]], ['SetDownVisual', ["d:/ymir work/ui/public/Large_button_03.sub"]], ["SetText", ["Altern. Bonus " + str(i - 5 + 1)]], ['SetEvent', [lambda Index = i: self.SelectBonus(Index)]]], []]
			slotbar = [[ui.SlotBar, 0], [35, 18], [470, y], [], []]
			editline = [[ui.EditLine, 33 + (i-5)*4], [35, 17], [6, 2], [["SetMax", [4]], ["SetNumberMode", [""]], ["SetText", ["0"]]], []]
			textline = [[ui.TextLine, 0], [0, 0], [370, texty], [["SetText", ["keiner"]]], []]
			tmp.append(button)
			tmp.append(slotbar)
			tmp.append(editline)
			tmp.append(textline)
			y += 30
			texty += 20
			
		GuiParser(tmp, self.Gui)
		
		self.Gui[3].SetScrollBar(self.Gui[4])
#		self.Gui[7].SetFocus()
		self.UpdateFileList()
		
	def ChangeState(self, state):
		if state == "Start":
			if self.SearchBoni == []:
				chat.AppendChat(1, "Bitte trage erst Bonis ein.")
				
			ItemIndex = self.Gui[3].GetSelectedItem()
			if ItemIndex:
				pass
			else:
				chat.AppendChat(chat.CHAT_TYPE_INFO, "Kein Item ausgewählt!")
				return
			self.Slot = int(ItemIndex.GetText().split("	")[0])
			self.Startmode = 1
			
			for Slot in xrange(player.INVENTORY_PAGE_SIZE*2):
				itemVNum = player.GetItemIndex(Slot)
				if itemVNum == self.SwitchValue:
					self.SlotStack = [Slot, player.GetItemCount(Slot)]
					break
					
			self.DefineBoni()
			self.State = "Start"
			
			chat.AppendChat(1, "Switchbot wurde gestartet.")
		else:
			self.State = "Stop"
			chat.AppendChat(1, "Switchbot wurde gestoppt.")

		
	def SelectBonus(self, Index):
		self.BoniGui = []
		Gui = [
			[[ui.ThinBoard, ""], [223, 323], [0,0], [["SetCenterPosition", [""]]], ["movable", "float"]],			
			[[ui.Button, 0], [0, 0], [183, 18], [['SetUpVisual', ["d:/ymir work/ui/public/close_button_01.sub"]],['SetOverVisual', ["d:/ymir work/ui/public/close_button_02.sub"]], ['SetDownVisual', ["d:/ymir work/ui/public/close_button_03.sub"]], ['SetToolTipText', ["Schließen", 0, - 23]], ['SetEvent', [lambda : self.HideBonusList()]]], []],	
			[[ui.SlotBar, 0], [190, 227], [15, 35], [], []],			
			[[ui.ListBoxEx, 0], [0, 0], [20, 65], [], []],			
			[[ui.ScrollBar, 0], [0, 0], [185, 55], [["SetScrollBarSize", [200]]], []],			
			[[ui.TextLine, 0], [0, 0], [15, 39], [["SetDefaultFontName", [""]],	["SetText", ["ID:			Bonus:"]],	["SetFontColor", [0.2, 0.2, 1.0]]], []],
			[[ui.TextLine, 0], [0, 0], [20, 18], [["SetText", ["Bestimme Bonus " + str(Index + 1)]],	["SetFontColor", [0.8, 0.6, 0.1]]], []],
			[[ui.Button, 0], [0, 0], [20, 275], [['SetUpVisual', ["d:/ymir work/ui/public/large_button_01.sub"]],['SetOverVisual', ["d:/ymir work/ui/public/large_button_02.sub"]], ['SetDownVisual', ["d:/ymir work/ui/public/large_button_03.sub"]], ["SetText", ["Auswählen"]], ['SetEvent', [lambda index = Index: self.AddBonus(Index)]]], []],			
			[[ui.Button, 0], [0, 0], [113, 275], [['SetUpVisual', ["d:/ymir work/ui/public/large_button_01.sub"]],['SetOverVisual', ["d:/ymir work/ui/public/large_button_02.sub"]], ['SetDownVisual', ["d:/ymir work/ui/public/large_button_03.sub"]], ["SetText", ["Abbrechen"]], ['SetEvent', [lambda : self.HideBonusList()]]], []],
			]
			
		GuiParser(Gui, self.BoniGui)
		
		self.BoniGui[3].SetScrollBar(self.BoniGui[4])
		self.SetBonusList()
		
	def AddBonus(self, Index):
		ItemIndex = self.BoniGui[3].GetSelectedItem()
		if ItemIndex:
			pass
		else:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Kein Item ausgewählt!")
			return
		BonusValue = ItemIndex.GetText().split("			")
		if int(BonusValue[0]) == 0:
			try:
				if Index > 4:
					BackUp = self.SearchBoni[Index - 5]
					if BackUp[0] == 0:
						self.SearchBoni.remove(self.SearchBoni[Index - 5])
					else:
						self.SearchBoni[Index - 5] = [BackUp[0], 0]
				else:
					BackUp = self.SearchBoni[Index]
					if BackUp[1] == 0:
						self.SearchBoni.remove(self.SearchBoni[Index])
					else:
						self.SearchBoni[Index] = [0, BackUp[1]]
			except:
				pass
		else:
			if Index > 4:
				NewIndex = Index - 5
				try:
					try:
						BackUp = self.SearchBoni[NewIndex]
						self.SearchBoni.remove(self.SearchBoni[NewIndex])
					except:
						Backup = [0, 0]
					self.SearchBoni.insert(NewIndex, [BackUp[0], int(BonusValue[0])])
				except:
					self.SearchBoni.append([0, int(BonusValue[0])])
			else:
				try:
					try:
						BackUp = self.SearchBoni[Index]
						self.SearchBoni.remove(self.SearchBoni[Index])
					except:
						Backup = [0, 0]
					self.SearchBoni.insert(Index,  [int(BonusValue[0]), BackUp[1]])
				except:
					self.SearchBoni.append([int(BonusValue[0]), 0])

		self.UpdateBonusList()
		self.HideBonusList()
		
	def UpdateBonusValues(self):
		TmpValues = []
		for Index in xrange(5):
			try:
				SearchValue = int(self.Gui[15 + (Index)*4].GetText())
			except:
				SearchValue = 0
			try:
				AlternateSearchValue = int(self.Gui[34 + (Index)*4].GetText())
			except:
				AlternateSearchValue = 0
			TmpValues.append([SearchValue, AlternateSearchValue])
			
		if TmpValues != self.SearchBoniValues:
			self.SearchBoniValues = TmpValues
		
	def UpdateBonusList(self):
		tmp = {}
		for Bonus in self.BonusIDListe:
			tmp[Bonus[1]] = Bonus[0]
			
		for Index in xrange(5):
			self.Gui[14 + (Index)*4].SetText("keiner")
			self.Gui[35 + (Index)*4].SetText("keiner")			
			
		for Bonus in self.SearchBoni:
			Index = self.SearchBoni.index(Bonus)
			self.Gui[14 + (Index)*4].SetText(tmp[Bonus[0]])
			self.Gui[35 + (Index)*4].SetText(tmp[Bonus[1]])
		
	def SetBonusList(self):
		self.BoniGui[3].RemoveAllItems()
		for Bonus in self.BonusIDListe:
			self.BoniGui[3].AppendItem(Item(str(Bonus[1]) + "			" + Bonus[0]))
		
	def HideBonusList(self):
		self.BoniGui[0].Hide()
		
	def UpdateFileList(self):
		Allow = [item.ITEM_TYPE_WEAPON, item.ITEM_TYPE_ARMOR]
		self.Gui[3].RemoveAllItems()
		for i in xrange(101):
			ItemIndex = player.GetItemIndex(i)
			ItemType = item.GetItemType(item.SelectItem(ItemIndex))
			if ItemIndex != 0 and ItemType in Allow:
				item.SelectItem(ItemIndex)
				item.GetItemName(ItemIndex)
				ItemName = item.GetItemName()
				self.Gui[3].AppendItem(Item(str(i) + "	" + ItemName))

		self.UpdateBonusList()
	
	def OnUpdate(self):		
		if self.State == "Stop":
			return
			
		self.UpdateBonusValues()
		self.UpdateBoni()
		
	def ControllBoni(self, Boni, Values):
		try:
			for i in xrange(len(self.SearchBoni)):
				try:
					Index = Boni.index(self.SearchBoni[i][0])
					if Values[Index] < self.SearchBoniValues[i][0]:
						Boni.index("-1")
				except:
					Index = Boni.index(self.SearchBoni[i][1])
					if Values[Index] < self.SearchBoniValues[i][1]:
						Boni.index("-1")				
			self.State = "Stop"
			chat.AppendChat(1, "Boni Count: " + str(self.Count))
			chat.AppendChat(1, "Bonis: " + str(Boni))
			chat.AppendChat(1, "Values: " + str(Values))
		except:
			if player.GetItemCountByVnum(self.SwitchValue) <= 0:
				if shop.IsOpen():
					for EachShopSlot in xrange(shop.SHOP_SLOT_COUNT):
						ShopItemValue = shop.GetItemID(EachShopSlot)
						if ShopItemValue == int(self.SwitchValue):
							net.SendShopBuyPacket(EachShopSlot)
				else:
					chat.AppendChat(1, "Keine Switchen mehr im Inventar")
					self.State = "Stop"
					return
				
			for Slot in xrange(player.INVENTORY_PAGE_SIZE*2):
				ItemValue = player.GetItemIndex(Slot)
				if ItemValue == self.SwitchValue:
					if self.State == "Stop":
						return
					self.SlotStack = [Slot, player.GetItemCount(Slot)]
					net.SendItemUseToItemPacket(Slot, self.Slot)
					break
					
	def DefineBoni(self):
		self.Values = []
		self.Boni = []
		self.Count = 0
		for AttributeIndex in xrange(5):
			Bonus, Value = player.GetItemAttribute(self.Slot, AttributeIndex)
			if Bonus != 0:
				self.Count += 1
				self.Boni.append(Bonus)
				self.Values.append(Value)
		self.ControllBoni(self.Boni, self.Values)
	
	def UpdateBoni(self):
		if self.State == "Stop":
			return
		Values = []
		Boni = []
		Count = 0
		for AttributeIndex in xrange(self.Count):
			Bonus, Value = player.GetItemAttribute(self.Slot, AttributeIndex)
			if Bonus == 0:
				return
			Count += 1
			Values.append(Value)
			Boni.append(Bonus)
		
		if (player.GetItemCount(self.SlotStack[0]) <= 0 and (self.Boni != Boni or self.Values != Values)) or (self.Boni != Boni or self.Values != Values) or app.GetTime() >= self.LastProcessTimeStamp + 0.8:
			self.LastProcessTimeStamp = app.GetTime()
			self.Boni = Boni
			self.Values = Values
			self.ControllBoni(Boni, Values)
#			chat.AppendChat(1, "Switchvorgang erkannt")
#			chat.AppendChat(1, "Neue Boni: " + str(self.Boni))
#			chat.AppendChat(1, "Neue Values: " + str(self.Values))
	
class ShopManager(ui.ScriptWindow):
	
	ShopSaveFile = "lib/shopdump.save"

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.Gui = []
		self.SavedShops = []
		self.AddGui()
		self.ShopSaver = PrivateShopSaver()

	def __del__(self):
		self.Gui[0].Hide()
		ui.ScriptWindow.__del__(self)
	
	def AddGui(self):
		Gui = [
			[[ui.ThinBoard, ""], [233, 353], [0,0], [["SetCenterPosition", [""]]], ["movable", "float"]],			
			[[ui.Button, 0], [0, 0], [193, 18], [['SetUpVisual', ["d:/ymir work/ui/public/close_button_01.sub"]],['SetOverVisual', ["d:/ymir work/ui/public/close_button_02.sub"]], ['SetDownVisual', ["d:/ymir work/ui/public/close_button_03.sub"]], ['SetToolTipText', ["Schließen", 0, - 23]], ['SetEvent', [lambda : self.__del__()]]], []],	
			[[ui.SlotBar, 0], [190, 255], [10, 35], [], []],			
			[[ui.ListBoxEx, 0], [0, 0], [15, 65], [["SetViewItemCount", [11]], ["SetItemStep",[20]]], []],			
			[[ui.ScrollBar, 0], [0, 0], [180, 55], [["SetScrollBarSize", [230]]], []],			
			[[ui.TextLine, 0], [0, 0], [16, 39], [["SetDefaultFontName", [""]],	["SetText", ["Shopname:"]],	["SetFontColor", [0.2, 0.2, 1.0]]], []],
			[[ui.Button, 0], [0, 0], [12, 305], [['SetUpVisual', ["d:/ymir work/ui/public/large_button_01.sub"]],['SetOverVisual', ["d:/ymir work/ui/public/large_button_02.sub"]], ['SetDownVisual', ["d:/ymir work/ui/public/large_button_03.sub"]], ["SetText", ["Auswählen"]], ['SetEvent', [lambda : self.ChooseSavedShop()]]], []],			
			[[ui.Button, 0], [0, 0], [115, 305], [['SetUpVisual', ["d:/ymir work/ui/public/large_button_01.sub"]],['SetOverVisual', ["d:/ymir work/ui/public/large_button_02.sub"]], ['SetDownVisual', ["d:/ymir work/ui/public/large_button_03.sub"]], ["SetText", ["Löschen"]], ['SetEvent', [lambda : self.DeleteSavedShop()]]], []],
			[[ui.TextLine, 0], [0, 0], [35, 18], [["SetText", ["Shop-Saver by DaRealFreak"]],	["SetFontColor", [0.8, 0.6, 0.1]]], []],
			]
			
		GuiParser(Gui, self.Gui)
		
		self.Gui[3].SetScrollBar(self.Gui[4])
		self.RefreshShopList()
		
	def RefreshShopList(self):
		self.Gui[3].RemoveAllItems()
		self.Gui[3].AppendItem(Item("Neuer Shop"))
		
		if self.SavedShops == []:
			try:
				ShopData = open(self.ShopSaveFile, "a+").readlines()
				for Shop in ShopData:
					if str(Shop).find("#") != -1:
						ShopName = str(Shop).split("#")[1].split("/")[0]
						self.Gui[3].AppendItem(Item(ShopName))
						self.SavedShops.append(ShopName)
			except:
				chat.AppendChat(1, "Fehler beim Laden der gespeicherten Shops.")
		else:
			for Shop in self.SavedShops:
				self.Gui[3].AppendItem(Item(Shop))
	
	def ChooseSavedShop(self):
		ItemIndex = self.Gui[3].GetSelectedItem()
		if ItemIndex:
			pass
		else:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Keinen Shop ausgewählt!")
			return
		ShopName = ItemIndex.GetText()

		if ShopName == "Neuer Shop":
			self.AskShopNameGui = []
			tmp = [
			[[ui.BoardWithTitleBar, ""], [250, 120], [0,0], [["SetCenterPosition", [""]], ["SetCloseEvent", [self.HideAskShopNameBoard]], ["SetTitleName", ["Shop Saver by DaRealFreak"]]], ["movable", "float"]],			
			[[ui.TextLine, 0], [0, 0], [100, 40], [["SetDefaultFontName", [""]],	["SetText", ["Shopname:"]],	["SetFontColor", [0.6, 0.7, 1.0]]], []],
			[[ui.SlotBar, 0], [150, 18], [50, 60], [], []],			
			[[ui.EditLine, 2], [150, 17], [10, 2], [["SetMax", [25]], ["SetFocus", [""]]], []],			
			]

			Modi = ["Ok", "Abbrechen"]		
			x = 38
			for mode in Modi:
				button = [[ui.Button, 0], [0, 0], [x, 85], [['SetUpVisual', ["d:/ymir work/ui/public/large_button_01.sub"]],['SetOverVisual', ["d:/ymir work/ui/public/large_button_02.sub"]], ['SetDownVisual', ["d:/ymir work/ui/public/large_button_03.sub"]], ['SetText', [mode]], ['SetEvent', [lambda arg = (Modi.index(mode)): self.Decision(arg)]]], []]
				tmp.append(button)
				x += 88
			
			GuiParser(tmp, self.AskShopNameGui)
			chat.AppendChat(1, "Bitte gebe einen Shopnamen an.")
		else:
			self.ShopSaver.Open(ShopName)
			self.ShopSaver.ReloadShop(ShopName)
			self.__del__()
	
	def DeleteSavedShop(self):
		ItemIndex = self.Gui[3].GetSelectedItem()
		if ItemIndex:
			pass
		else:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Keinen Shop ausgewählt!")
			return
		ShopName = ItemIndex.GetText()		

		self.SavedShops.remove(ShopName)
		
		SaveDump = open(self.ShopSaveFile, "a+").readlines()
		for line in SaveDump:
			if line.split("#")[1].split("/")[0] == ShopName:
				SaveDump.remove(line)
				open(self.ShopSaveFile, "w+")
				SaveDumpFile = open(self.ShopSaveFile, "a+")
				for SavedShops in SaveDump:
					SaveDumpFile.write(SavedShops)
					
		chat.AppendChat(1, "Der Shop: " + str(ShopName) + " wurde erfolgreich gelöscht.")
		self.RefreshShopList()
		
	def Decision(self, arg):
		if arg == 0:
			ShopName = self.AskShopNameGui[3].GetText()
			if len(ShopName) > 0:
				self.SavedShops.append(ShopName)
				self.ShopSaver.Open(ShopName)
				self.ShopSaver.ReloadShop(ShopName)
				self.__del__()
			else:
				chat.AppendChat(1, "Bitte gebe einen längeren Shopnamen an.")
		else:
			self.AskShopNameGui = []
			
		self.HideAskShopNameBoard()

	def HideAskShopNameBoard(self):
		try:
			self.AskShopNameGui[0].Hide()
		except:
			pass
	
class PrivateShopSaver(ui.ScriptWindow):

	ShopSaveFile = "lib/shopdump.save"

	def __init__(self):
		ui.ScriptWindow.__init__(self)

		self.__LoadWindow()
		self.ItemStock = {}
		self.ToolTipItem = uiminimap.MapTextToolTip()
		self.ToolTipItem.Hide()
		self.PriceInputBoard = None
		self.Title = ""
		self.ActualSlot = "keiner"

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def __LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "UIScript/PrivateShopBuilder.py")
		except:
			import exception
			exception.Abort("PrivateShopBuilderWindow.LoadWindow.LoadObject")

		try:
			GetObject = self.GetChild
			self.NameLine = GetObject("NameLine")
			self.ItemSlot = GetObject("ItemSlot")
			self.ButtonOk = GetObject("OkButton")
			self.CloseButton = GetObject("CloseButton")
			self.TitleBar = GetObject("TitleBar")
			self.TitleName = GetObject("TitleName")
		except:
			import exception
			exception.Abort("PrivateShopBuilderWindow.LoadWindow.BindObject")

		self.ButtonOk.Hide()
		self.CloseButton.Hide()
			
		self.ButtonOk = ui.Button()
		self.ButtonOk.SetParent(self)
		self.ButtonOk.SetUpVisual("d:/ymir work/ui/public/small_button_01.sub")
		self.ButtonOk.SetOverVisual("d:/ymir work/ui/public/small_button_02.sub")
		self.ButtonOk.SetDownVisual("d:/ymir work/ui/public/small_button_03.sub")
		self.ButtonOk.SetEvent(ui.__mem_func__(self.OnOk))
		self.ButtonOk.SetText("Create")
		self.ButtonOk.SetPosition(17, 321)
		self.ButtonOk.Show()

		self.CloseButton = ui.Button()
		self.CloseButton.SetParent(self)
		self.CloseButton.SetUpVisual("d:/ymir work/ui/public/small_button_01.sub")
		self.CloseButton.SetOverVisual("d:/ymir work/ui/public/small_button_02.sub")
		self.CloseButton.SetDownVisual("d:/ymir work/ui/public/small_button_03.sub")
		self.CloseButton.SetEvent(lambda : self.Close())
		self.CloseButton.SetText("Close")
		self.CloseButton.SetPosition(124, 321)
		self.CloseButton.Show()
		
		self.TitleName.SetText("Shop Saver by DaRealFreak")
		self.TitleBar.SetCloseEvent(lambda : self.Close())

		self.ItemSlot.SetSelectEmptySlotEvent(ui.__mem_func__(self.OnSelectEmptySlot))
		self.ItemSlot.SetSelectItemSlotEvent(ui.__mem_func__(self.OnSelectItemSlot))
		self.ItemSlot.SetOverInItemEvent(ui.__mem_func__(self.OnOverInItem))
		self.ItemSlot.SetOverOutItemEvent(ui.__mem_func__(self.OnOverOutItem))
		
		self.SaveButton = ui.Button()
		self.SaveButton.SetParent(self)
		self.SaveButton.SetUpVisual("d:/ymir work/ui/public/small_button_01.sub")
		self.SaveButton.SetOverVisual("d:/ymir work/ui/public/small_button_02.sub")
		self.SaveButton.SetDownVisual("d:/ymir work/ui/public/small_button_03.sub")
		self.SaveButton.SetText("Save")		
		self.SaveButton.SetEvent(lambda : self.SaveShop())
		self.SaveButton.SetPosition(70, 321)
		self.SaveButton.Show()
		
	def Destroy(self):
		self.ClearDictionary()

		self.NameLine = None
		self.ItemSlot = None
		self.ButtonOk = None
		self.CloseButton = None
		self.TitleBar = None
		self.PriceInputBoard = None

	def Open(self, Title):

		self.Title = Title

		if len(Title) > 25:
			Title = Title[:22] + "..."

		self.ItemStock = {}
		self.PriceList = {}
		
		shop.ClearPrivateShopStock()
		self.NameLine.SetText(Title)
		self.SetCenterPosition()
		self.Refresh()
		self.Show()

	def SaveShop(self):
		if not self.Title:
			return

		if 0 == len(self.ItemStock):
			chat.AppendChat(1, "Bitte trage erst einmal Items ein.")
			return

		SaveDump = open(self.ShopSaveFile, "a+").readlines()
		for line in SaveDump:
			if line.split("#")[1].split("/")[0] == self.Title:
				SaveDump.remove(line)
				open(self.ShopSaveFile, "w+")
				SaveDumpFile = open(self.ShopSaveFile, "a+")
				for SavedShops in SaveDump:
					SaveDumpFile.write(SavedShops)
			
		tmp = []
		for AddedItem in self.ItemStock:
			ItemVnum = player.GetItemIndex(self.ItemStock[AddedItem])
			tmp.append([AddedItem, ItemVnum, self.PriceList[AddedItem][0], self.PriceList[AddedItem][1]])
		ShopFile = open(self.ShopSaveFile, "a+")
		ShopFile.write("#" + self.Title + "/")
		for ShopEntry in tmp:
			(ShopPos, Vnum, Price, Stack) = ShopEntry
			ShopFile.write(str(ShopPos) + "," + str(Vnum) + "," + str(Price) + "," + str(Stack) + "$")
		ShopFile.write("\n")
		chat.AppendChat(1, "Shop saved sucessfully!")
		
	def ReloadShop(self, shopname):
		self.ItemStock = {}
		self.PriceList = {}
		
		shop.ClearPrivateShopStock()

		SavedShop = []
	
		for line in open(self.ShopSaveFile, "a+").readlines():
			if line.split("#")[1].split("/")[0] == shopname:
				Items = line.split("/")[1].split("$")
				for ShopItems in Items:
					if ShopItems.count(",") == 3:
						Data = ShopItems.split(",")
						ShopSlot = int(Data[0])
						ItemVnum = int(Data[1])
						Price = int(Data[2])
						Stack = int(Data[3])
						SavedShop.append([ShopSlot, ItemVnum, Price, Stack])
		
		Vnums = []
		for data in SavedShop:
			Vnums.append(data[1])
		
		BannedSlots = []
		for Slot in xrange(player.INVENTORY_PAGE_SIZE*2):
			ItemValue = player.GetItemIndex(Slot)
			if ItemValue in Vnums and not Slot in BannedSlots:
				for ShopData in SavedShop:
					if ItemValue == ShopData[1] and player.GetItemCount(Slot) == ShopData[3]:
						BannedSlots.append(Slot)
						
						shop.AddPrivateShopItemStock(Slot, ShopData[0], ShopData[2])
						self.PriceList[ShopData[0]] = [ShopData[2], player.GetItemCount(Slot)]
						self.ItemStock[ShopData[0]] = Slot		
		
		self.Refresh()

	def Close(self):			
		self.Title = ""
		self.ItemStock = {}
		self.PriceList = {}
		shop.ClearPrivateShopStock()
		self.Hide()

	def Refresh(self):
		GetItemVnum = player.GetItemIndex
		GetItemCount = player.GetItemCount
		SetItemVnum = self.ItemSlot.SetItemSlot
		DelItem = self.ItemSlot.ClearSlot

		for i in xrange(shop.SHOP_SLOT_COUNT):

			if not self.ItemStock.has_key(i):
				DelItem(i)
				continue

			pos = self.ItemStock[i]

			ItemCount = GetItemCount(pos)
			if ItemCount <= 1:
				ItemCount = 0
			SetItemVnum(i, GetItemVnum(pos), ItemCount)

		self.ItemSlot.RefreshSlot()

	def OnSelectEmptySlot(self, SelectedSlotPos):

		isAttached = mouseModule.mouseController.isAttached()
		if isAttached:
			AttachedSlotType = mouseModule.mouseController.GetAttachedType()
			AttachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
			mouseModule.mouseController.DeattachObject()

			if player.SLOT_TYPE_INVENTORY != AttachedSlotType:
				return

			ItemVnum = player.GetItemIndex(AttachedSlotPos)
			item.SelectItem(ItemVnum)

			if item.IsAntiFlag(item.ITEM_ANTIFLAG_GIVE) or item.IsAntiFlag(item.ITEM_ANTIFLAG_MYSHOP):
				chat.AppendChat(chat.CHAT_TYPE_INFO, locale.PRIVATE_SHOP_CANNOT_SELL_ITEM)
				return

			PriceInputBoard = uiCommon.MoneyInputDialog()
			PriceInputBoard.SetTitle(locale.PRIVATE_SHOP_INPUT_PRICE_DIALOG_TITLE)
			PriceInputBoard.SetAcceptEvent(ui.__mem_func__(self.AcceptInputPrice))
			PriceInputBoard.SetCancelEvent(ui.__mem_func__(self.CancelInputPrice))
			PriceInputBoard.Open()

			itemPrice = ""

			if itemPrice>0:
				PriceInputBoard.SetValue(itemPrice)
			
			self.PriceInputBoard = PriceInputBoard
			self.PriceInputBoard.ItemVnum = ItemVnum
			self.PriceInputBoard.SourceSlotPos = AttachedSlotPos
			self.PriceInputBoard.TargetSlotPos = SelectedSlotPos

	def OnSelectItemSlot(self, SelectedSlotPos):

		isAttached = mouseModule.mouseController.isAttached()
		if isAttached:
			snd.PlaySound("sound/ui/loginfail.wav")
			mouseModule.mouseController.DeattachObject()

		else:
			if not SelectedSlotPos in self.ItemStock:
				return

			InventoryPos = self.ItemStock[SelectedSlotPos]
			shop.DelPrivateShopItemStock(InventoryPos)
			snd.PlaySound("sound/ui/drop.wav")

			del self.ItemStock[SelectedSlotPos]
			del self.PriceList[SelectedSlotPos]

			self.Refresh()

	def AcceptInputPrice(self):

		if not self.PriceInputBoard:
			return TRUE

		Text = self.PriceInputBoard.GetText()

		if not Text:
			return TRUE

		if not Text.isdigit():
			return TRUE

		if int(Text) <= 0:
			return TRUE

		SourceSlotPos = self.PriceInputBoard.SourceSlotPos
		TargetSlotPos = self.PriceInputBoard.TargetSlotPos

		for privatePos, inventorySlotPos in self.ItemStock.items():
			if inventorySlotPos == SourceSlotPos:
				shop.DelPrivateShopItemStock(TargetSlotPos)
				del self.ItemStock[privatePos]
				del self.PriceList[privatePos]

		Price = int(self.PriceInputBoard.GetText())

		shop.AddPrivateShopItemStock(SourceSlotPos, TargetSlotPos, Price)
		
		self.PriceList[TargetSlotPos] = [Price, player.GetItemCount(SourceSlotPos)]
		
		self.ItemStock[TargetSlotPos] = SourceSlotPos
		snd.PlaySound("sound/ui/drop.wav")

		self.Refresh()		

		self.PriceInputBoard = None
		return TRUE

	def CancelInputPrice(self):
		self.PriceInputBoard = None
		return TRUE

	def OnOk(self):
		if not self.Title:
			return

		if 0 == len(self.ItemStock):
			return

		shop.BuildPrivateShop(self.Title)

		self.Close()

	def OnPressEscapeKey(self):
		self.Close()
		return TRUE

	def OnUpdate(self):
		if isinstance(self.ActualSlot, str):
			return
			
		if self.ToolTipItem:
			(mouseX, mouseY) = wndMgr.GetMousePosition()
			self.ToolTipItem.SetText("%s (Price: %s)" % (item.GetItemName(item.SelectItem(player.GetItemIndex(self.ItemStock[self.ActualSlot]))), locale.NumberToMoneyString(self.PriceList[self.ActualSlot][0])))
			self.ToolTipItem.SetTooltipPosition(mouseX, mouseY)
			self.ToolTipItem.SetTextColor(-8722595)
			self.ToolTipItem.SetTop()
			
	def OnOverInItem(self, SlotIndex):
		self.ActualSlot = SlotIndex
		
		self.ToolTipItem = uiminimap.MapTextToolTip()
		self.ToolTipItem.Show()
		
	def OnOverOutItem(self):
		self.ActualSlot = "keiner"
		
		if self.ToolTipItem:
			self.ToolTipItem = None

class FarmToolsDialog(ui.ScriptWindow):

	Gui = []
	PotionBuffer = {}
	Taus = [50821, 50822, 50823, 50824, 50825, 50826]

	ExpBot = "off"

	PotionManagerGui = []
	PotionManager = [100, 5]
	PotionManagerState = "off"

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.Gui = []
		self.AddGui()
		
	def __del__(self):
		self.Gui[0].Hide()
		try:
			self.PotionManagerGui[0].Hide()
		except:
			pass
		ui.ScriptWindow.__del__(self)
		
	def CreateGuild(self):
		net.SendAnswerMakeGuildPacket(self.Gui[7].GetText())
		
		self.Gui[5].SetText("Erfahrungs-Grenze:")
		self.Gui[7].SetText("100")
		self.Gui[7].SetNumberMode()
		self.Gui[8].SetText("off")
		self.Gui[8].SetEvent(lambda : self.ToggleExpBot())
			
	def ToggleExpBot(self):
		if self.ExpBot == "off":
			self.Gui[8].SetText("on")
			self.ExpBot = "on"
			chat.AppendChat(1, "Der Exp-Spendebot wurde aktiviert.")
		else:
			self.Gui[8].SetText("off")
			self.ExpBot = "off"
			chat.AppendChat(1, "Der Exp-Spendebot wurde deaktiviert.")		
		
	def HidePotionManagement(self):
		self.PotionManagerGui[0].Hide()
		
	def SetConfig(self):
		Value, Time = self.PotionManager
		
		MinValue = int(self.PotionManagerGui[5].GetSliderPos() * 200)
		MinTime = int(self.PotionManagerGui[8].GetSliderPos() * 10)
		if MinValue != Value:
			self.PotionManagerGui[6].SetText("+ " + str(MinValue))
		if MinTime != Time:
			self.PotionManagerGui[9].SetText(str(MinTime) + " min")
			
		self.PotionManager = [MinValue, MinTime]
		
	def TogglePotionManager(self, state):
		if state == "Start":
			self.PotionManagerState = "on"
			chat.AppendChat(1, "Der Potion Manager wurde gestartet.")
		else:
			self.PotionManagerState = "off"
			chat.AppendChat(1, "Der Potion Manager wurde angehalten.")
			
	def OnRender(self):
		if self.PotionManagerState != "on" or player.GetStatus(player.HP) <= 0:
			return
			
		if not shop.IsOpen():
			chat.AppendChat(1, "Bitte öffne zuerst einen Shop.")
			self.TogglePotionManager("Stop")
			return
			
		MinValue, MinTime = self.PotionManager
		MinTime = MinTime * 60
		
		ItemIndex = self.PotionManagerGui[2].GetSelectedItem()
		if ItemIndex:
			pass
		else:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Bitte wähle ein Item aus!")
			return
		PotionValue = int(ItemIndex.GetText().split("	")[0])
	
		#Check Potions:
		for InventorySlot in xrange(player.INVENTORY_PAGE_SIZE*2):
			ItemIndex = player.GetItemIndex(InventorySlot)
			if PotionValue == ItemIndex:
				Value0, Value , Time = [player.GetItemMetinSocket(InventorySlot, i) for i in xrange(player.METIN_SOCKET_MAX_NUM)]
				if Value >= MinValue and Time >= MinTime:
					self.TogglePotionManager("Stop")
				else:
					net.SendShopSellPacket(InventorySlot)
	
		if self.PotionManagerState != "on":
			return
			
		#Buy Potions:
		for EachShopSlot in xrange(shop.SHOP_SLOT_COUNT):
			ShopItemValue = shop.GetItemID(EachShopSlot)
			if ShopItemValue == int(PotionValue):
				net.SendShopBuyPacket(EachShopSlot)
				break
		
	def OpenPotionManagement(self):
		self.PotionManagerGui = []
		self.PotionManager = [100, 5]
		self.PotionManagerState = "off"

		tmp = [
			[[ui.BoardWithTitleBar, ""], [200, 340], [0,0], [["SetCenterPosition", [""]], ["SetCloseEvent", [self.HidePotionManagement]], ["SetTitleName", ["Potion Manager"]]], ["movable", "float"]],			
			[[ui.SlotBar, 0], [170, 140], [10, 35], [], []],			
			[[ui.ListBoxEx, 0], [0, 0], [25, 50], [["SetViewItemCount", [6]]], []],			
			[[ui.ScrollBar, 0], [0, 0], [160, 40], [["SetScrollBarSize", [130]]], []],			
			[[ui.TextLine, 0], [0, 0], [70, 180], [["SetDefaultFontName", [""]], ["SetText", ["Mindest Wert"]],	["SetFontColor", [0.6, 0.7, 1.0]]], []],			
			[[ui.SliderBar, 0], [0, 0], [13, 200], [["SetEvent", [ui.__mem_func__(self.SetConfig)]], ["SetSliderPos", [0.5]]], []],			
			[[ui.TextLine, 0], [0, 0], [85, 215], [["SetDefaultFontName", [""]], ["SetText", ["+ 100"]],	], []],			
			[[ui.TextLine, 0], [0, 0], [85, 240], [["SetDefaultFontName", [""]], ["SetText", ["Dauer"]],	["SetFontColor", [0.6, 0.7, 1.0]]], []],			
			[[ui.SliderBar, 0], [0, 0], [13, 260], [["SetEvent", [ui.__mem_func__(self.SetConfig)]], ["SetSliderPos", [0.5]]], []],			
			[[ui.TextLine, 0], [0, 0], [87, 275], [["SetDefaultFontName", [""]], ["SetText", ["5 min"]],	], []],			
			[[ui.Button, 0], [0, 0], [35, 300], [['SetUpVisual', ["d:/ymir work/ui/public/middle_button_01.sub"]],['SetOverVisual', ["d:/ymir work/ui/public/middle_button_02.sub"]], ['SetDownVisual', ["d:/ymir work/ui/public/middle_button_03.sub"]], ["SetText", ["Start"]], ['SetEvent', [lambda : self.TogglePotionManager("Start")]]], []],			
			[[ui.Button, 0], [0, 0], [105, 300], [['SetUpVisual', ["d:/ymir work/ui/public/middle_button_01.sub"]],['SetOverVisual', ["d:/ymir work/ui/public/middle_button_02.sub"]], ['SetDownVisual', ["d:/ymir work/ui/public/middle_button_03.sub"]], ["SetText", ["Stop"]], ['SetEvent', [lambda : self.TogglePotionManager("Stop")]]], []],			
			]
		GuiParser(tmp, self.PotionManagerGui)
		
		self.PotionManagerGui[2].SetScrollBar(self.PotionManagerGui[3])
		for blaaa in self.Taus:
			self.PotionManagerGui[2].AppendItem(Item(str(blaaa) + "	" + str(item.GetItemName(item.SelectItem(blaaa)))))
		
	def AddGui(self):	
		Gui = [
			[[ui.ThinBoard, ""], [349, 537], [0,0], [["SetCenterPosition", [""]]], ["movable", "float"]],			
			[[ui.Button, 0], [0, 0], [313, 15], [['SetUpVisual', ["d:/ymir work/ui/public/close_button_01.sub"]],['SetOverVisual', ["d:/ymir work/ui/public/close_button_02.sub"]], ['SetDownVisual', ["d:/ymir work/ui/public/close_button_03.sub"]], ['SetToolTipText', ["Schließen", 0, - 23]], ['SetEvent', [lambda : self.__del__()]]], []],	
			[[ui.TextLine, 0], [0, 0], [113, 18], [["SetDefaultFontName", [""]],	["SetText", ["Farm Tools by DaRealFreak"]],	["SetFontColor", [0.1, 0.7, 1.0]]], []],
			[[ui.TextLine, 0], [0, 0], [129, 40], [["SetDefaultFontName", [""]],	["SetText", ["Auto Potion Usage"]],	["SetFontColor", [0.6, 0.7, 1.0]]], []],			
			[[ui.TextLine, 0], [0, 0], [134, 392], [["SetDefaultFontName", [""]],	["SetText", ["Guild Management"]],	["SetFontColor", [0.6, 0.7, 1.0]]], []],			
			[[ui.TextLine, 0], [0, 0], [137, 405], [["SetDefaultFontName", [""]],	["SetText", ["Enter Guildname:"]],	], []],
			[[ui.SlotBar, 0], [100, 18], [129, 425], [], []],			
			[[ui.EditLine, 6], [100, 17], [10, 2], [["SetMax", [12]], ["SetFocus", [""]]], []],			
			[[ui.Button, 0], [0, 0], [134, 450], [['SetUpVisual', ["d:/ymir work/ui/public/large_button_01.sub"]],['SetOverVisual', ["d:/ymir work/ui/public/large_button_02.sub"]], ['SetDownVisual', ["d:/ymir work/ui/public/large_button_03.sub"]], ["SetText", ["Create Guild"]], ['SetEvent', [lambda : self.CreateGuild()]]], []],			
			[[ui.TextLine, 0], [0, 0], [131, 482], [["SetDefaultFontName", [""]],	["SetText", ["Potion Management"]],	["SetFontColor", [0.6, 0.7, 1.0]]], []],			
			[[ui.Button, 0], [0, 0], [134, 500], [['SetUpVisual', ["d:/ymir work/ui/public/large_button_01.sub"]],['SetOverVisual', ["d:/ymir work/ui/public/large_button_02.sub"]], ['SetDownVisual', ["d:/ymir work/ui/public/large_button_03.sub"]], ["SetText", ["Potion Manager"]], ['SetEvent', [lambda : self.OpenPotionManagement()]]], []],			
			]
		GuiParser(Gui, self.Gui)
		
		#Guild System Fix:
		if player.GetGuildID() != 0:
			self.Gui[5].SetText("Erfahrungs-Grenze:")
			self.Gui[5].SetPosition(134, 405)
			self.Gui[7].SetText("100")
			self.Gui[7].SetNumberMode()
			self.Gui[8].SetText("off")
			self.Gui[8].SetEvent(lambda : self.ToggleExpBot())
		
		self.Potions = []
		for i in xrange(50813, 50827):
			self.Potions.append(i)
		self.Potions.remove(50815)
		self.Potions.remove(50816)
		self.Leftovers = [50801, 50802, 50107, 50108, 71027, 71028, 71029, 71030, 71044, 71045, 27102]
		for bla in self.Leftovers:
			self.Potions.append(bla)
			
		tmp = []
		x = 40
		y = 70
		for potion in self.Potions:
			Index = self.Potions.index(potion)
			if IsDivideAble(Index, 4):
				x = 40
				y += 50
			ItemName = item.GetItemName(item.SelectItem(potion))
			ItemIcon = item.GetIconImageFileName()
			button = [[ui.ExpandedImageBox, 0], [0, 0], [x, y], [['LoadImage', [ItemIcon]]], []]
			name = [[ui.Button, 0], [0, 0], [x - 15, y + 30], [['SetUpVisual', ["d:/ymir work/ui/public/middle_button_01.sub"]],['SetOverVisual', ["d:/ymir work/ui/public/middle_button_02.sub"]], ['SetDownVisual', ["d:/ymir work/ui/public/middle_button_03.sub"]], ["SetText", [ItemName]], ['SetEvent', [lambda arg = (self.Potions.index(potion)): self.AutoUsage(arg)]]], []]
			tmp.append(button)
			tmp.append(name)
			x += 78					
			
		GuiParser(tmp, self.Gui)
		
	def AutoUsage(self, ItemIndex):
		ItemValue = self.Potions[ItemIndex]
		
		try:
			del self.PotionBuffer[ItemValue]
			chat.AppendChat(1, item.GetItemName(item.SelectItem(ItemValue)) + " nicht mehr genutzt.")
		except KeyError:
			self.PotionBuffer[ItemValue] = app.GetGlobalTimeStamp()
			chat.AppendChat(1, item.GetItemName(item.SelectItem(ItemValue)) + " ab jetzt automatisch genutzt.")
	
	def UsePotion(self, ItemValue):
		if player.GetItemCountByVnum(ItemValue) == 0:
			return
			
		Firework = [50107, 50108]
		Berries = [50813, 50814, 50817, 50818, 50819, 50820, 50801, 50802]
		GodItems = [71027, 71028, 71029, 71030]
		HelpItems = [71044, 71045, 27102]

		if ItemValue in self.Taus:
			HighestValue = [0, 0]
			for InventorySlot in xrange(player.INVENTORY_PAGE_SIZE*2):
				ItemIndex = player.GetItemIndex(InventorySlot)
				if ItemValue == ItemIndex:
					Value0, Value , Time = [player.GetItemMetinSocket(InventorySlot, i) for i in xrange(player.METIN_SOCKET_MAX_NUM)]
					if HighestValue[0] < Value:
						HighestValue = [Value, InventorySlot, Time]
						self.PotionBuffer[ItemValue] = app.GetGlobalTimeStamp() + HighestValue[2] + 2
			net.SendItemUsePacket(HighestValue[1])

		elif ItemValue in Firework:
			for InventorySlot in xrange(player.INVENTORY_PAGE_SIZE*2):
				ItemIndex = player.GetItemIndex(InventorySlot)
				if ItemValue == ItemIndex:
					net.SendItemUsePacket(InventorySlot)
					self.PotionBuffer[ItemValue] = app.GetGlobalTimeStamp() + 482
					break
					
		elif ItemValue in Berries:
			for InventorySlot in xrange(player.INVENTORY_PAGE_SIZE*2):
				ItemIndex = player.GetItemIndex(InventorySlot)
				if ItemValue == ItemIndex:
					net.SendItemUsePacket(InventorySlot)
					self.PotionBuffer[ItemValue] = app.GetGlobalTimeStamp() + 362
					break
					
		elif ItemValue in GodItems:
			for InventorySlot in xrange(player.INVENTORY_PAGE_SIZE*2):
				ItemIndex = player.GetItemIndex(InventorySlot)
				if ItemValue == ItemIndex:
					net.SendItemUsePacket(InventorySlot)
					self.PotionBuffer[ItemValue] = app.GetGlobalTimeStamp() + 1802
					break
					
		elif ItemValue in HelpItems:
			for InventorySlot in xrange(player.INVENTORY_PAGE_SIZE*2):
				ItemIndex = player.GetItemIndex(InventorySlot)
				if ItemValue == ItemIndex:
					net.SendItemUsePacket(InventorySlot)
					self.PotionBuffer[ItemValue] = app.GetGlobalTimeStamp() + 603
					break
					
		chat.AppendChat(1, "Auto Usage: " + str(ItemValue))
	
	def OnUpdate(self):
		if player.GetGuildID() != 0 and self.ExpBot == "on":
			try:
				Exp = player.GetEXP()
				if Exp >= int(self.Gui[7].GetText()) and Exp >= 100:
					net.SendGuildOfferPacket(Exp)
			except:
				self.ToggleExpBot()
				chat.AppendChat(1, "Bitte gebe einen Wert an.")
	
		if self.PotionBuffer == {}:
			return
			
		for Potion in self.PotionBuffer:
			if app.GetGlobalTimeStamp() >= self.PotionBuffer[Potion]:
				self.UsePotion(Potion)
	
class PrivateMessageTool(ui.ScriptWindow):
	
	Gui = []
	AutoAnswerManagementGui = []
	AnswerTuple = {}
	
	def __init__(self):
		ui.ScriptWindow.__init__(self)

		global MinimizedWhisper
		global AnswerTuple
		self.AnswerTuple = AnswerTuple
		MinimizedWhisper = 2
		
		self.Gui = []

		self.AddGui()
		
	def __del__(self, args = "del"):
		global MinimizedWhisper
		if args == "del":
			MinimizedWhisper = 0
		self.Gui[0].Hide()
		try:
			self.AutoAnswerManagementGui[0].Hide()
		except:
			pass
		ui.ScriptWindow.__del__(self)
	
	def HideAutoAnswerManagement(self):
		self.AutoAnswerManagementGui[0].Hide()
	
	def RemoveAnswer(self):
		ItemIndex = self.AutoAnswerManagementGui[2].GetSelectedItem()
		if ItemIndex:
			pass
		else:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Bitte wähle eine Antwort aus!")
			return
		KeyWord = ItemIndex.GetText().split(":")[0]
		Answer = ItemIndex.GetText().split(KeyWord + ": ")[1]
		
		try:
			self.AnswerTuple[KeyWord].remove(Answer)
			if self.AnswerTuple[KeyWord] == []:
				del self.AnswerTuple[KeyWord]
		except:
			chat.AppendChat(1, "Ein Fehler beim Löschen ist aufgetreten")
		
		self.RefreshAnswers()
	
	def SaveAutoAnswers(self):
		if self.AnswerTuple == {}:
			chat.AppendChat(1, "Bitte trage erst einmal Antworten ein.")
			return
	
		for KeyWord in self.AnswerTuple:
			for Message in self.AnswerTuple[KeyWord]:
				open("lib/whisperanswers.save", "a+").write(KeyWord + "#" + Message + "\n")
		chat.AppendChat(1, "Die Einstellungen wurden erfolgreich gespeichert.")

	def DeleteAutoAnswers(self):
		try:
			os.remove("lib/whisperanswers.save")
		except:
			pass
		chat.AppendChat(1, "Die Einstellungsdatei wurden gelöscht.")

	def OpenAutoAnswerManagement(self):
		self.AutoAnswerManagementGui = []

		tmp = [
			[[ui.BoardWithTitleBar, ""], [520, 290], [0,0], [["SetCenterPosition", [""]], ["SetCloseEvent", [self.HideAutoAnswerManagement]], ["SetTitleName", ["Auto Answer Management"]]], ["movable", "float"]],			
			[[ui.SlotBar, 0], [490, 140], [10, 35], [], []],			
			[[ui.ListBoxEx, 0], [0, 0], [25, 50], [["SetViewItemCount", [6]]], []],			
			[[ui.ScrollBar, 0], [0, 0], [480, 40], [["SetScrollBarSize", [130]]], []],			
			[[ui.TextLine, 0], [0, 0], [230, 180], [["SetDefaultFontName", [""]], ["SetText", ["Answer Options"]],	["SetFontColor", [0.6, 0.7, 1.0]]], []],			
			[[ui.Button, 0], [0, 0], [235, 200], [['SetUpVisual', ["d:/ymir work/ui/public/middle_button_01.sub"]],['SetOverVisual', ["d:/ymir work/ui/public/middle_button_02.sub"]], ['SetDownVisual', ["d:/ymir work/ui/public/middle_button_03.sub"]], ["SetText", ["Remove"]], ['SetEvent', [lambda : self.RemoveAnswer()]]], []],			
			[[ui.TextLine, 0], [0, 0], [235, 230], [["SetDefaultFontName", [""]], ["SetText", ["Save Options"]],	["SetFontColor", [0.6, 0.7, 1.0]]], []],			
			[[ui.Button, 0], [0, 0], [203, 250], [['SetUpVisual', ["d:/ymir work/ui/public/middle_button_01.sub"]],['SetOverVisual', ["d:/ymir work/ui/public/middle_button_02.sub"]], ['SetDownVisual', ["d:/ymir work/ui/public/middle_button_03.sub"]], ["SetText", ["Save"]], ['SetEvent', [lambda : self.SaveAutoAnswers()]]], []],
			[[ui.Button, 0], [0, 0], [273, 250], [['SetUpVisual', ["d:/ymir work/ui/public/middle_button_01.sub"]],['SetOverVisual', ["d:/ymir work/ui/public/middle_button_02.sub"]], ['SetDownVisual', ["d:/ymir work/ui/public/middle_button_03.sub"]], ["SetText", ["Delete"]], ['SetEvent', [lambda : self.DeleteAutoAnswers()]]], []],
			]
		GuiParser(tmp, self.AutoAnswerManagementGui)
		
		self.AutoAnswerManagementGui[2].SetScrollBar(self.AutoAnswerManagementGui[3])
		
		self.RefreshAnswers()
		
	def RefreshAnswers(self):
		self.AutoAnswerManagementGui[2].RemoveAllItems()
		for Keyword in self.AnswerTuple:
			for Answer in self.AnswerTuple[Keyword]:
				self.AutoAnswerManagementGui[2].AppendItem(Item(Keyword + ": " + Answer))
	
	def AddAutoAnswer(self):
		Keyword = self.Gui[9].GetText().lower()
		Answer = self.Gui[12].GetText()
		
		if not Keyword in self.AnswerTuple:
			self.AnswerTuple[Keyword] = []
		
		self.AnswerTuple[Keyword].append(Answer)
		self.Gui[12].SetText("")
		chat.AppendChat(1, "Keyword sucessfully appended.")
	
	def MinimizeBot(self):
		ActivateMinimizedWhisper(self.AnswerTuple)
		self.__del__("minimized")
	
	def AddGui(self):
		Gui = [
			[[ui.BoardWithTitleBar, ""], [600, 340], [0,0], [["SetCenterPosition", [""]], ["SetCloseEvent", [self.__del__]], ["SetTitleName", ["Whisper Answer Bot by DaRealFreak"]]], ["movable", "float"]],			
			[[ui.Button, 0], [0, 0], [555, 10], [['SetToolTipText', ["Minimieren", 3, - 23]], ['SetUpVisual', ["d:/ymir work/ui/public/minimize_button_01.sub"]],['SetOverVisual', ["d:/ymir work/ui/public/minimize_button_02.sub"]], ['SetDownVisual', ["d:/ymir work/ui/public/minimize_button_03.sub"]], ['SetEvent', [lambda : self.MinimizeBot()]]], []],
			[[ui.TextLine, 0], [0, 0], [270, 40], [["SetDefaultFontName", [""]], ["SetText", ["Whisper Log:"]],	["SetFontColor", [0.6, 0.7, 1.0]]], []],			
			[[ui.SlotBar, 0], [570, 150], [10, 55], [], []],			
			[[ui.ListBox, 0], [500, 137], [50, 60], [], []],			
			[[ui.ScrollBar, 0], [0, 0], [560, 60], [["SetScrollBarSize", [140]], ["SetScrollEvent",[ui.__mem_func__(self.OnScrollMessageLog)]]], []],			
			[[ui.TextLine, 0], [0, 0], [20, 230], [["SetText", ["Key Word(no case sensitive)"]]], []],			
			[[ui.TextLine, 0], [0, 0], [245, 210], [["SetDefaultFontName", [""]], ["SetText", ["Auto Answer Bot Options"]],	["SetFontColor", [0.6, 0.7, 1.0]]], []],			
			[[ui.SlotBar, 0], [260, 20], [20, 250], [], []],
			[[ui.EditLine, 8], [260, 19], [6, 2], [["SetMax", [60]], ["SetFocus", [""]]], []],			
			[[ui.TextLine, 0], [0, 0], [300, 230], [["SetText", ["Answer"]]], []],			
			[[ui.SlotBar, 0], [260, 20], [300, 250], [], []],
			[[ui.EditLine, 11], [260, 19], [6, 2], [["SetMax", [60]]], []],			
			[[ui.Button, 0], [0, 0], [230, 290], [['SetUpVisual', ["d:/ymir work/ui/public/middle_button_01.sub"]],['SetOverVisual', ["d:/ymir work/ui/public/middle_button_02.sub"]], ['SetDownVisual', ["d:/ymir work/ui/public/middle_button_03.sub"]], ["SetText", ["Add Answer"]], ['SetEvent', [lambda : self.AddAutoAnswer()]]], []],			
			[[ui.Button, 0], [0, 0], [310, 290], [['SetUpVisual', ["d:/ymir work/ui/public/middle_button_01.sub"]],['SetOverVisual', ["d:/ymir work/ui/public/middle_button_02.sub"]], ['SetDownVisual', ["d:/ymir work/ui/public/middle_button_03.sub"]], ["SetText", ["Management"]], ['SetEvent', [lambda : self.OpenAutoAnswerManagement()]]], []],
			]
		GuiParser(Gui, self.Gui)
	
		self.Gui[9].SetTabEvent(ui.__mem_func__(self.Gui[12].SetFocus))
		self.Gui[9].SetReturnEvent(ui.__mem_func__(self.Gui[12].SetFocus))
		self.Gui[12].SetTabEvent(ui.__mem_func__(self.Gui[9].SetFocus))
		self.Gui[12].SetReturnEvent(ui.__mem_func__(self.Gui[9].SetFocus))

		self.Gui[4].InsertItem(0, "~ Auto Answer Message Bot by DaRealFreak ~")
		
		PrivateMessages = GetPrivateMessages()
		for UserDict in PrivateMessages:
			for message in PrivateMessages[UserDict]:
				ItemCount = self.Gui[4].GetItemCount()
				self.Gui[4].InsertItem(ItemCount, "%s: %s" % (message[0], message[1]))
				if message[2] != "":
					self.Gui[4].InsertItem(ItemCount + 1, "Auto Answer: %s" % (message[2]))
		
		
	def OnScrollMessageLog(self):
		ViewItemCount = self.Gui[4].GetViewItemCount()
		ItemCount = self.Gui[4].GetItemCount()
		Position = self.Gui[5].GetPos() * (ItemCount - ViewItemCount)
		self.Gui[4].SetBasePos(int(Position))

	def OnUpdate(self):
		global TmpMessageDict
		if TmpMessageDict != []:
			ItemCount = self.Gui[4].GetItemCount()
			self.Gui[4].InsertItem(ItemCount, "%s: %s" % (TmpMessageDict[0], TmpMessageDict[1]))
			self.Gui[4].InsertItem(ItemCount + 1, "Auto Answer: %s" % (TmpMessageDict[2]))
			TmpMessageDict = []
	
def AnswerMinimizedWhisper(name, message):
	global AnswerTuple
	global TmpMessageDict
	global PrivateMessages
	tmp = []
	for Keyword in AnswerTuple:
		if message.lower().find(Keyword) != -1:
			tmp.append(Keyword)
	
	Keyword = ""
	if tmp != []:
		CheckLenght = len(tmp[0])
		Keyword = tmp[0]
	for MatchedKeyword in tmp:
		if len(MatchedKeyword) >= CheckLenght:
			Keyword = MatchedKeyword
	if Keyword == "":
		chat.AppendChat(1, "Kein Keyword gefunden.")
		Answer = AskCleverbot(message)
	else:
		chat.AppendChat(1, "Keyword gefunden.")
		Choice = AnswerTuple[Keyword]
		Answer = Choice[app.GetRandom(0, len(Choice) - 1)]
	TmpMessageDict = [name, message, Answer]
	PrivateMessages[name].append([name, message, Answer])
	net.SendWhisperPacket(name, Answer)

def ActivateMinimizedWhisper(SavedAnswerTuple):
	global AnswerTuple
	global MinimizedWhisper
	MinimizedWhisper = 1
	AnswerTuple = SavedAnswerTuple
	chat.AppendChat(1, "Whisper Message Bot wurde minimiert.")
	
class Session(object):
	keylist = ['stimulus', 'start', 'sessionid', 'vText8', 'vText7', 'vText6', 'vText5', 'vText4', 'vText3', 'vText2', 'icognoid', 'icognocheck', 'prevref', 'emotionaloutput', 'emotionalhistory', 'asbotname', 'ttsvoice', 'typing', 'lineref', 'fno', 'sub', 'islearning', 'cleanslate']
	headers = {}
	headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:7.0.1) Gecko/20100101 Firefox/7.0'
	headers['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
	headers['Accept-Language'] = 'en-us;q=0.8,en;q=0.5'
	headers['X-Moz'] = 'prefetch'
	headers['Accept-Charset'] = 'ISO-8859-1,utf-8;q=0.7,*;q=0.7'
	headers['Referer'] = 'http://www.cleverbot.com'
	headers['Cache-Control'] = 'no-cache, no-cache'
	headers['Pragma'] = 'no-cache'

	def __init__(self):
		self.arglist = ['', 'y', '', '', '', '', '', '', '', '', 'wsf', '', '', '', '', '', '', '', '', '0', 'Say', '1', 'false']
		self.MsgList = []

	def Send(self):
		data = self.encode(self.keylist, self.arglist)
		digest_txt = data[9:29]
		hash = md5.new(digest_txt).hexdigest()
		self.arglist[self.keylist.index('icognocheck')] = hash
		data = self.encode(self.keylist,self.arglist)
		req = urllib2.Request("http://www.cleverbot.com/webservicemin", data, self.headers)
		f = urllib2.urlopen(req)
		reply = f.read()
		return reply

	def Ask(self,q):
		self.arglist[self.keylist.index('stimulus')] = q
		if self.MsgList: self.arglist[self.keylist.index('lineref')] = '!0' + str(len(self.MsgList)/2)
		asw = self.Send()
		self.MsgList.append(q)
		answer = self.parseAnswers(asw)
		for k,v in answer.iteritems():
			try:
				self.arglist[self.keylist.index(k)] = v
			except ValueError:
				pass
		self.arglist[self.keylist.index('emotionaloutput')]=''
		text = answer['ttsText']
		self.MsgList.append(text)
		return text

	def parseAnswers(self, text):
		d = {}
		keys = ["text", "sessionid", "logurl", "vText8", "vText7", "vText6", "vText5", "vText4", "vText3",
				"vText2", "prevref", "foo", "emotionalhistory", "ttsLocMP3", "ttsLocTXT",
				"ttsLocTXT3", "ttsText", "lineRef", "lineURL", "linePOST", "lineChoices",
				"lineChoicesAbbrev", "typingData", "divert"]
		values = text.split("\r")
		i = 0
		for key in keys:
			d[key] = values[i]
			i += 1
		return d

	def encode(self, keylist,arglist):
		text = ''
		for i in range(len(keylist)):
			k = keylist[i]; v = self.quote(arglist[i])
			text += '&' + k + '=' + v
		text = text[1:]
		return text
	  
	always_safe = ('ABCDEFGHIJKLMNOPQRSTUVWXYZ'
				   'abcdefghijklmnopqrstuvwxyz'
				   '0123456789' '_.-')
				   
	def quote(self, s, safe = '/'):
		_chr = __builtins__.chr
		safe += self.always_safe
		safe_map = {}
		for i in xrange(256):
			c = _chr(i)
			safe_map[c] = (c in safe) and c or  ('%%%02X' % i)
		res = map(safe_map.__getitem__, s)
		return ''.join(res)
		
def AskCleverbot(message):
	cb = Session()
	Answer = cb.Ask(message)
	Answer = Answer.replace("&auml;", "ä").replace("&auml;", "Ä").replace("&ouml;", "ö").replace("&Ouml;", "Ö").replace("&uuml;", "ü").replace("&Uuml;", "Ü").replace("&szlig;", "ß")
	return(Answer)
	
class ChannelChangeBot(ui.ScriptWindow):
	
	Gui = []

	def __init__(self): 
		ui.ScriptWindow.__init__(self)
		self.Gui = []
		
		self.LoadAccountList()
		self.DumpServerInfo()
		self.AddGui()

	def __del__(self): 
		self.Gui[0].Hide()
		ui.ScriptWindow.__del__(self) 

	def LoadAccountList(self):
		self.Accounts = {}
		try:
			for Account in open("lib/accounts.save", "r+").readlines():
				AccountID = Account.split(":")[0]
				AccountPw = Account.split(":")[1].split("\n")[0]
				self.Accounts[AccountID] = AccountPw
		except:
			chat.AppendChat(1, "Fehler beim Auslesen der Accountliste.")
			pass

	def AddGui(self):
		Gui = [
			[[ui.BoardWithTitleBar, ""], [420, 260], [0,0], [["SetCenterPosition", [""]], ["SetCloseEvent", [self.__del__]], ["SetTitleName", ["Account Management Board"]]], ["movable", "float"]],			
			[[ui.TextLine, 0], [0, 0], [30, 40], [["SetDefaultFontName", [""]], ["SetText", ["Select Account:"]],	["SetFontColor", [0.6, 0.7, 1.0]]], []],			
			[[ui.SlotBar, 0], [150, 150], [20, 55], [], []],			
			[[ui.ListBoxEx, 0], [150, 137], [30, 60], [["SetViewItemCount", [6]]], []],
			[[ui.ScrollBar, 0], [0, 0], [145, 60], [["SetScrollBarSize", [140]]], []],
			[[ui.TextLine, 0], [0, 0], [195, 40], [["SetDefaultFontName", [""]], ["SetText", ["Select Server:"]],	["SetFontColor", [0.6, 0.7, 1.0]]], []],			
			[[ui.SlotBar, 0], [90, 150], [190, 55], [], []],			
			[[ui.ListBoxEx, 0], [20, 137], [200, 60], [["SetViewItemCount", [6]]], []],			
			[[ui.ScrollBar, 0], [0, 0], [255, 60], [["SetScrollBarSize", [140]]], []],			
			[[ui.TextLine, 0], [0, 0], [305, 40], [["SetDefaultFontName", [""]], ["SetText", ["Select Channel:"]],	["SetFontColor", [0.6, 0.7, 1.0]]], []],			
			[[ui.SlotBar, 0], [95, 150], [300, 55], [], []],			
			[[ui.ListBoxEx, 0], [25, 137], [320, 60], [["SetViewItemCount", [6]]], []],			
			[[ui.ScrollBar, 0], [0, 0], [370, 60], [["SetScrollBarSize", [140]]], []],
			[[ui.Button, 0], [0, 0], [50, 220], [['SetUpVisual', ["d:/ymir work/ui/public/large_button_01.sub"]],['SetOverVisual', ["d:/ymir work/ui/public/large_button_02.sub"]], ['SetDownVisual', ["d:/ymir work/ui/public/large_button_03.sub"]], ["SetText", ["Connect"]], ['SetEvent', [lambda : self.ConnectToServer()]]], []],
			[[ui.Button, 0], [0, 0], [160, 220], [['SetUpVisual', ["d:/ymir work/ui/public/large_button_01.sub"]],['SetOverVisual', ["d:/ymir work/ui/public/large_button_02.sub"]], ['SetDownVisual', ["d:/ymir work/ui/public/large_button_03.sub"]], ["SetText", ["Add Account"]], ['SetEvent', [lambda : self.AddAccount()]]], []],			
			[[ui.Button, 0], [0, 0], [270, 220], [['SetUpVisual', ["d:/ymir work/ui/public/large_button_01.sub"]],['SetOverVisual', ["d:/ymir work/ui/public/large_button_02.sub"]], ['SetDownVisual', ["d:/ymir work/ui/public/large_button_03.sub"]], ["SetText", ["Remove Account"]], ['SetEvent', [lambda : self.RemoveAccount()]]], []],
			]
			
		GuiParser(Gui, self.Gui)
		
		self.Gui[3].SetScrollBar(self.Gui[4])
		self.Gui[7].SetScrollBar(self.Gui[8])
		self.Gui[11].SetScrollBar(self.Gui[12])
		
		for Server in xrange(len(self.AuthServers)):
			self.Gui[7].AppendItem(Item("Server " + str(Server + 1)))
			
		for Channel in xrange(len(self.ServerPorts)):
			self.Gui[11].AppendItem(Item("Channel " + str(Channel + 1)))
		
		self.RefreshAccountList()
		
	def RefreshAccountList(self):
		self.Gui[3].RemoveAllItems()	
		for User in self.Accounts:
			self.Gui[3].AppendItem(Item(User))
		
	def AddAccount(self):
		self.AskAccountGui = []
		tmp = [
		[[ui.BoardWithTitleBar, ""], [200, 160], [0,0], [["SetCenterPosition", [""]], ["SetCloseEvent", [self.HideAskAccountBoard]], ["SetTitleName", ["Accountdaten"]]], ["movable", "float"]],			
		[[ui.TextLine, 0], [0, 0], [70, 40], [["SetDefaultFontName", [""]],	["SetText", ["Account ID:"]],	["SetFontColor", [0.6, 0.7, 1.0]]], []],
		[[ui.SlotBar, 0], [100, 18], [50, 60], [], []],			
		[[ui.EditLine, 2], [100, 17], [10, 2], [["SetMax", [16]], ["SetFocus", [""]]], []],			
		[[ui.TextLine, 0], [0, 0], [73, 80], [["SetDefaultFontName", [""]],	["SetText", ["Passwort:"]],	["SetFontColor", [0.6, 0.7, 1.0]]], []],
		[[ui.SlotBar, 0], [100, 18], [50, 100], [], []],			
		[[ui.EditLine, 5], [100, 17], [10, 2], [["SetMax", [16]]], []],
		]
		
		Modi = ["Ok", "Abbrechen"]		
		x = 12
		for mode in Modi:
			button = [[ui.Button, 0], [0, 0], [x, 125], [['SetUpVisual', ["d:/ymir work/ui/public/large_button_01.sub"]],['SetOverVisual', ["d:/ymir work/ui/public/large_button_02.sub"]], ['SetDownVisual', ["d:/ymir work/ui/public/large_button_03.sub"]], ['SetText', [mode]], ['SetEvent', [lambda arg = (Modi.index(mode)): self.Decision(arg)]]], []]
			tmp.append(button)
			x += 88
			
		GuiParser(tmp, self.AskAccountGui)
		
		self.AskAccountGui[3].SetTabEvent(lambda: self.AskAccountGui[6].SetFocus())
		self.AskAccountGui[3].SetReturnEvent(lambda: self.AskAccountGui[6].SetFocus())
		self.AskAccountGui[6].SetTabEvent(lambda: self.AskAccountGui[3].SetFocus())
		self.AskAccountGui[6].SetReturnEvent(lambda : self.Decision(0))
		
		chat.AppendChat(1, "Bitte trage deine Accountdaten ein.")
		
	def SaveAccounts(self):
		try:
			os.remove("lib/accounts.save")
		except:
			pass
		
		for Account in self.Accounts:
			open("lib/accounts.save", "a+").write(Account + ":" + self.Accounts[Account] + "\n")			
		self.RefreshAccountList()
		
	def Decision(self, arg):
		if arg == 0:
			AccountID = self.AskAccountGui[3].GetText()
			Passwort = self.AskAccountGui[6].GetText()
			chat.AppendChat(1, "Deine Accountdaten wurden gespeichert.")
			self.Accounts[AccountID] = Passwort
			self.SaveAccounts()
			self.HideAskAccountBoard()
		else:
			self.AskAccountGui = []
			
	def HideAskAccountBoard(self):
		try:
			self.AskAccountGui[0].Hide()
		except:
			pass
		
	def RemoveAccount(self):
		ItemIndex = self.Gui[3].GetSelectedItem()
		if ItemIndex:
			pass
		else:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Kein Account ausgewählt!")
			return
		AccountID = ItemIndex.GetText()
		Password = self.Accounts[AccountID]
		
		del self.Accounts[AccountID]
		
		AccountManaging = open("lib/accounts.save", "a+").read().replace(AccountID + ":" + Password + "\n", "")
		open("lib/accounts.save", "w+")
		open("lib/accounts.save", "a+").write(AccountManaging)
		
		self.RefreshAccountList()
		
	def ConnectToServer(self):
		ItemIndex = self.Gui[7].GetSelectedItem()
		if ItemIndex:
			pass
		else:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Kein Server ausgewählt!")
			return
		ServerIndex = self.Gui[7].GetItemIndex(ItemIndex)

		ItemIndex = self.Gui[11].GetSelectedItem()
		if ItemIndex:
			pass
		else:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Kein Channel ausgewählt!")
			return
		ChannelIndex = self.Gui[11].GetItemIndex(ItemIndex)

		ItemIndex = self.Gui[3].GetSelectedItem()
		if ItemIndex:
			pass
		else:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Kein Account ausgewählt!")
			return
		AccountID = ItemIndex.GetText()
		Password = self.Accounts[AccountID]

		ActualServerName = net.GetServerInfo()
		NewServerName = ActualServerName[:len(ActualServerName) - 1] + str(ChannelIndex + 1)
		net.SetServerInfo(NewServerName)
		
		self.DirectConnect(self.AuthServers[ServerIndex], self.AuthPorts[ServerIndex], self.ServerIps[ChannelIndex], self.ServerPorts[ChannelIndex], AccountID, Password)
		
	def DumpServerInfo(self):
		self.ServerNames = []
		self.AuthServers = []
		self.AuthPorts = []
		self.ServerIps = []
		self.ServerPorts = []

		LoginFile = self.GetTextFileTuple("intrologin.py", 0)
		for line in LoginFile:
			if line.find('self.stream.SetConnectInfo("') != -1:
				AuthPort = int(line.split('"')[4].split(",")[1].split(")")[0])
				if not AuthPort in self.AuthPorts:
					self.AuthServers.append(line.split('"')[3])
					self.AuthPorts.append(AuthPort)
				ServerPort = int(line.split('"')[2].split(",")[1])
				if not ServerPort in self.ServerPorts:
					self.ServerIps.append(line.split('"')[1])
					self.ServerPorts.append(ServerPort)
			if line.find('net.SetServerInfo("') != -1 and not line.find("Ãµ¸¶ ¼­¹ö") != -1:
				if not line.split('"')[1] in ServerNames:
					ServerNames.append(line.split('"')[1])
					
		if len(self.ServerNames) >= 1:
			return
		
		for Server in xrange(len(ServerInfo.REGION_DICT[0])):
			self.ServerIps = []
			self.ServerPorts = []
			self.ServerName = ServerInfo.REGION_DICT[0][Server + 1]["name"]
			AuthServerIp = ServerInfo.REGION_AUTH_SERVER_DICT[0][Server + 1]["ip"]
			self.AuthServers.append(AuthServerIp)
			AuthServerPort = ServerInfo.REGION_AUTH_SERVER_DICT[0][Server + 1]["port"]
			self.AuthPorts.append(AuthServerPort)
			for Channel in xrange(len(ServerInfo.REGION_DICT[0][Server + 1]["channel"])):
				self.ServerIps.append(ServerInfo.REGION_DICT[0][Server + 1]["channel"][Channel + 1]["ip"])
				ServerPort = ServerInfo.REGION_DICT[0][Server + 1]["channel"][Channel + 1]["tcp_port"]
				if not ServerPort in self.ServerPorts:
					self.ServerPorts.append(ServerPort)
			
			for Channels in self.ServerPorts:
				Index = self.ServerPorts.index(Channels)		
		
	def DirectConnect(self, AuthServerIP, AuthServerPort, ChannelIP, ChannelPort, AccountID, Password):
		net.SetLoginInfo(AccountID, Password)
		net.ConnectToAccountServer(ChannelIP, ChannelPort, AuthServerIP, AuthServerPort)
		net.DirectEnter(0)
		net.SendSelectCharacterPacket(0)
		net.SendEnterGamePacket()

	def GetTextFileTuple(self, file, mode):
		tmp = []
		try:
			Handle = app.OpenTextFile(file)
			CountLines = app.GetTextFileLineCount(Handle)
		except:
			return ""
		if mode == 0:
			return(tmp)
		for i in xrange(CountLines):
			line = app.GetTextFileLine(Handle, i)
			if line != "":
				tmp.append(line + "\n")
		return("".join(tmp))
	
def GetVidList():
	return VidList
	
def GetPickUpList():
	return PickUpList

def GetPickUpListNames():
	return PickUpListNames
	
def GetPrivateMessages():
	return PrivateMessages
	
def GetPositiveValue(value):
	if value < 0:
		return value - (2*value)
	else:
		return value
	
class EterPackOperator(object):

	def __init__(self, filename):
		_chr = __builtins__.chr
		if not pack.Exist(filename):
			raise IOError, 'No file or directory'
		self.data = self.GetTextFile(filename)
		self.data=_chr(10).join(self.data.split(_chr(13)+_chr(10)))

	def read(self, len = None):
		if not self.data:
			return ''
		if len:
			tmp = self.data[:len]
			self.data = self.data[len:]
			return tmp
		else:
			tmp = self.data
			self.data = ''
			return tmp

	def readlines(self):
		Array = str(self.data).split("\n")
		return Array
		
	def getline(self, line):
		return self.readlines()[line - 1]
		
	def getlinecount(self):
		return len(self.readlines())

	def GetTextFile(self, file):
		tmp = []
		try:
			Handle = app.OpenTextFile(file)
			CountLines = app.GetTextFileLineCount(Handle)
		except:
			return ""
		for i in xrange(CountLines):
			line = app.GetTextFileLine(Handle, i)
			if line != "":
				tmp.append(line + "\n")
		return("".join(tmp))
	
LastCheck = 0
MatchCount = 0

def IsMobAlive(vid):
	global LastCheck
	global MatchCount
	global HookedVid
	chr.SelectInstance(vid)
	BoundBox = chr.GetBoundBoxOnlyXY(vid)
	Distance = player.GetCharacterDistance(vid)
	if chr.GetInstanceType(vid) == chr.INSTANCE_TYPE_ENEMY:
	
		if HookedVid[0] == vid and HookedVid[1] <= 0 and Distance <= 200:
			return 0
	
		if LastCheck == str(BoundBox):
			MatchCount += 1
		else:
			MatchCount = 0
		LastCheck = str(BoundBox)
		
		if Distance >= 975:
			return 1
			
		if MatchCount >= 9:
			MatchCount = 0
			return 0
		else:
			return 1
	else:
		if BoundBox[3] >= 175:
			return 0
		else:
			return 1	
	
def IsBetween(x, y, z):
	tmp = []
	for i in xrange(x, y):
		tmp.append(i)
		
	try:
		tmp.index(z)
		return 1
	except:
		pass

def GuiParser(guiobjects, list):
	#[Type, Parentindex],[Sizex, Sizey], [Posx, Posy], [commands], [flags]
	for object in guiobjects:
		Object = object[0][0]()
		if object[0][1] != "":
			Object.SetParent(list[object[0][1]])
		if object[1][0] + object[1][1] != 0:
			Object.SetSize(object[1][0], object[1][1])
		if object[2][0] + object[2][1] != 0:
			Object.SetPosition(object[2][0], object[2][1])
				
		for command in object[3]:
			cmd = command[0]	
			attr = getattr(Object,cmd)			
			if callable(attr):
				argument = command[1]
				lenght = len(argument)
				if lenght == 1:
					if argument[0] == "":
						attr()
					else:
						attr(argument[0])
				elif lenght == 2:
					attr(argument[0], argument[1])
				elif lenght == 3:
					attr(argument[0], argument[1], argument[2])
				elif lenght == 4:
					attr(argument[0], argument[1], argument[2], argument[3])
		for flag in object[4]:
			Object.AddFlag(str(flag))
		Object.Show()
	
		list.append(Object)
		
def IsDivideAble(x, y):
	if x == 0:
		return
	if float(x/y) == DivideToFloat(x, y):
		return 1
	
def DivideToFloat(x, y):
	try:
		return x * (y**-1)
	except:
		return 0
	
def GetDegree(mobX, mobY, playerX, playerY):
	try:
		rada = ConvertToDegrees(math.acos((mobY-playerY)/math.sqrt((mobX - playerX)**2 + (mobY - playerY)**2))) + 180
		if playerX >= mobX:
			rada = 360 - rada
	except:
		rada = 0
	return rada
	
def GetTmpTeleport(DestX, DestY):
	(PlayerX, PlayerY, PlayerZ) = player.GetMainCharacterPosition()
	DifX = DestX - PlayerX
	DifY = DestY - PlayerY
	Vektor = DivideToFloat(2000, math.sqrt(DifX**2 + DifY**2))
	TempX = PlayerX + Vektor*DifX
	TempY = PlayerY + Vektor*DifY
	Count = DivideToFloat((DestX - PlayerX), (Vektor*DifX))
	return (TempX, TempY, Count)
	
def ConvertToDegrees(value):
	return 180 * value / math.pi
	
def GetDistance(x, y):
	(PlayerX, PlayerY, PlayerZ) = player.GetMainCharacterPosition()	
	(TmpX, TmpY) = (GetPositiveValue(PlayerX - x) ** 2, GetPositiveValue(PlayerY - y) ** 2)
	return(math.sqrt(TmpX + TmpY))
	
MapBuffer = {}
def GetCurrentMapSize():
	global MapBuffer
	ActualMapName = background.GetCurrentMapName()
	if ActualMapName in MapBuffer:
		return MapBuffer[ActualMapName]
	else:
		(bGet, iSizeX, iSizeY) = miniMap.GetAtlasSize()
		GetMapData = str(EterPackOperator("atlasinfo.txt").read())
		MapData = GetMapData.split("\n")
		for Map in MapData:
			try:
				MapName = Map.split("\t")[0]
				SizeX = int(Map.split("\t")[3])
				SizeY = int(Map.split("\t")[4])
				if MapName == ActualMapName:
					if iSizeX == 0 or iSizeY == 0:
						iSizeX = SizeX * 43
						iSizeY = SizeY * 43
					break
			except:
				pass
		MapBuffer[ActualMapName] = (iSizeX, iSizeY, SizeX, SizeY)
		return(iSizeX, iSizeY, SizeX, SizeY)
			
def GetClass():
	race = net.GetMainActorRace()
	group = net.GetMainActorSkillGroup()
	if race == 0 or race == 4:
		return "Warrior" + "/" + str(group)
	elif race == 1 or race == 5:
		return "Assassin" + "/" + str(group)
	elif race == 2 or race == 6:
		return "Sura" + "/" + str(group)
	elif race == 3 or race == 7:
		return "Shaman" + "/" + str(group)
			
def NewSkillsEnable():
	playersettingmodule = EterPackOperator("playersettingmodule.py").read()
	RaceGroupInfo = GetClass()
	Class = str(RaceGroupInfo).split("/")[0]
	if str(playersettingmodule).find("NEW_678TH_SKILL_ENABLE = TRUE") or str(playersettingmodule).count("36") >= 4 or str(Class) == "Shaman" or str(Class) == "Sura":
		return 6
	else:
		return 5

#Hook SetHPTargetBoard
def HookedSetHPTargetBoard(self, vid, hpPercentage):
	global OldHPTargetBoard
	global HookedVid
	OldHPTargetBoard(self, vid, hpPercentage)
	HookedVid = [vid, hpPercentage]

def HookSetHPTargetBoard():
	game.GameWindow.SetHPTargetBoard = HookedSetHPTargetBoard
	chat.AppendChat(1, "SetHPTargetBoard wurde erfolgreich gehooked.")		

def UnHookSetHPTargetBoard():
	global OldHPTargetBoard
	game.GameWindow.SetHPTargetBoard = OldHPTargetBoard
	chat.AppendChat(1, "SetHPTargetBoard Hook wurde erfolgreich entfernt.")	
	
#Hook OnRecvWhisper
def HookedOnRecvWhisper(self, mode, name, line):
	global OldOnRecvWhisper
	global PrivateMessages
	global MinimizedWhisper
	OldOnRecvWhisper(self, mode, name, line)

	if not name in PrivateMessages:
		PrivateMessages[name] = []
	
	Message = line.split(name + " : ")[1]

	if MinimizedWhisper > 0:
		thread.start_new_thread(AnswerMinimizedWhisper, (name, Message))
	else:
		PrivateMessages[name].append([name, Message, ""])
	
def HookOnRecvWhisper():
	game.GameWindow.OnRecvWhisper = HookedOnRecvWhisper
	chat.AppendChat(1, "OnRecvWhisper wurde erfolgreich gehooked.")
	
def UnHookHookOnRecvWhisper():
	global OldOnRecvWhisper
	game.GameWindow.OnRecvWhisper = OldOnRecvWhisper
	chat.AppendChat(1, "OnRecvWhisper Hook wurde erfolgreich entfernt.")	
	
def HookOpenTargetBoard():
	game.GameWindow.SetPCTargetBoard = HookedOpenTargetBoard
	chat.AppendChat(1, "OpenTargetBoard wurde erfolgreich gehooked.")		

def HookedOpenTargetBoard(self, vid, name):
	global OldOpenTargetBoard
	global BuffVid
	BuffVid = vid
	chat.AppendChat(1, "Du hast " + name + " anvisiert.")
	OldOpenTargetBoard(self, vid, name)
	
def UnHookOpenTargetBoard():
	global OldOpenTargetBoard
	global BuffVid
	BuffVid = 0
	game.GameWindow.SetPCTargetBoard = OldOpenTargetBoard
	chat.AppendChat(1, "OpenTargetBoard Hook wurde erfolgreich entfernt.")	
	
	
Options = [["Teleport Module", NewTeleportHackDialog], ["Inventarmanager", InventoryManagerDialog], ["Chatspammer", ChatspammerDialog], ["Whisperspammer", WhisperspammerDialog], ["Angelbot", FishingBot], ["Farmtools", FarmToolsDialog], ["Item Pickup", ItemPickUpHackDialog], ["Connect Changer", ChannelChangeBot], ["Private Message Tool", PrivateMessageTool], ["Privat Server Module", PrivateServerModulesDialog]]
PrivateServerOptions = [["Switchbot v3.1.2", SwitchBotDialog], ["Packet Editor", "PacketEditorDialog"], ["Item Creator v2.1", "ItemCreatorDialog"], ["Fb-Leser", ReadBookBotDialog], ["Seelenstein Leser", SoulStoneBotDialog], ["Shop Saver", ShopManager]]

HookOnRecvWhisper()
NewLevelBotDialog().Show()