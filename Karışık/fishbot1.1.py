##############################################################################################################################
##										Fishing Bot by DaRealFreak@epvpers 													##
##	You can repost this script, but pls don't replace or delete the copyright, the script was ~3-4 hours of work(my work^^) ##
##############################################################################################################################

import player
import net
import ui
import chat
import chr
import app
import chrmgr
import item

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

	def GuiParser(self, guiobjects, list):
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
		self.GuiParser(Gui, self.Gui)		
		self.fischies = []
		for i in xrange(27803, 27824):
			self.fischies.append(i)
		self.FishingItems = [27987, 70201, 70202, 70203, 70204, 70205, 70206, 70048, 70049, 70050, 70051]
		for bla in self.FishingItems:
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
		self.GuiParser(tmp, self.Gui)
		
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
			ItemName = item.GetItemName(item.SelectItem(self.FishingItems[fish-len(self.fischies)]))
			try:
				self.KillFishList.remove(self.FishingItems[fish-len(self.fischies)])
				if ItemName == item.GetItemName(item.SelectItem(27987)):
					chat.AppendChat(1, ItemName + " wird beim Erhalt nicht mehr geöffnet.")
				else:
					self.TrashList.remove(self.FishingItems[fish-len(self.fischies)])
					chat.AppendChat(1, ItemName + " wird beim Erhalt behalten.")
			except:
				if ItemName == item.GetItemName(item.SelectItem(27987)):
					self.KillFishList.append(self.FishingItems[fish-len(self.fischies)])
					chat.AppendChat(1, ItemName + " wird beim Erhalt geöffnet.")
				else:
					self.TrashList.append(self.FishingItems[fish-len(self.fischies)])
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
			if self.ProcessTimeStamp + 48.0 < app.GetTime():
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
		
def IsDivideAble(x, y):
	if x == 0:
		return
	if float(x/y) == DivideToFloat(x, y):
		return 1
		
def DivideToFloat(x, y):
    y = x * (y**-1)
    return y

FishingBot().Show()