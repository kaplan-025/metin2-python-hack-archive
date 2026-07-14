# Copyright: Padmak, http://padmak.de
# Do not redistribute
# You are allowed to take the code, but you must give credits to either Padmak or http://padmak.de
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
import serverInfo
import game
import chat
import event
class InventoryManagerDialog(ui.ScriptWindow):
	Gui = []
	type = 0
	def __init__(self):
		self.Gui = []
		ui.ScriptWindow.__init__(self)
		self.AddGui()
		self.OldRecv = game.GameWindow.OpenQuestWindow
		self.InstallQuestWindowHook()
		
		self.hand_in = 0
		self.hand_time = 0.
		self.old_time_stamp = 0.
		self.hand_in_slots = []
		
	def __del__(self):
		self.UnHookQuestWindow()
		self.Gui[0].Hide()
		ui.ScriptWindow.__del__(self)
		
	def AddGui(self):
		Gui = [
			[[ui.ThinBoard, ""], [278, 340], [0,0], [["SetCenterPosition", [""]]], ["movable", "float"]],			
			[[ui.Button, 0], [0, 0], [250, 5], [['SetUpVisual', ["d:/ymir work/ui/public/close_button_01.sub"]],['SetOverVisual', ["d:/ymir work/ui/public/close_button_02.sub"]], ['SetDownVisual', ["d:/ymir work/ui/public/close_button_03.sub"]], ['SetToolTipText', ["Close", 0, - 23]], ['SetEvent', [lambda : self.__del__()]]], []],	
			[[ui.SlotBar, 0], [255, 225], [10, 35], [], []],			
			[[ui.ListBoxEx, 0], [0, 0], [15, 50], [["SetViewItemCount", [10]]], []],			
			[[ui.ScrollBar, 0], [0, 0], [245, 40], [["SetScrollBarSize", [220]]], []],			
			[[ui.TextLine, 0], [0, 0], [85, 5], [["SetDefaultFontName", [""]],	["SetText", ["Energy-Bot by Padmak"]],	["SetFontColor", [0.4, 0.7, 1.0]]], []],			
			[[ui.TextLine, 0], [0, 0], [10, 37], [["SetDefaultFontName", [""]],	["SetText", ["			ID:			Name:"]],	["SetFontColor", [0.2, 0.2, 1.0]]], []],			
			[[ui.Button, 0], [0, 0], [220, 3], [['SetUpVisual', ["d:/ymir work/ui/game/guild/refresh_button_01.sub"]],['SetOverVisual', ["d:/ymir work/ui/game/guild/refresh_button_02.sub"]], ['SetDownVisual', ["d:/ymir work/ui/game/guild/refresh_button_03.sub"]], ['SetToolTipText', ["Refresh", 0, - 23]], ['SetEvent', [lambda : self.UpdateFileList()]]], []],	
			[[ui.Button, 0], [0, 0], [10, 265], [['SetUpVisual', ["d:/ymir work/ui/public/Large_button_01.sub"]],['SetOverVisual', ["d:/ymir work/ui/public/Large_button_02.sub"]], ['SetDownVisual', ["d:/ymir work/ui/public/Large_button_03.sub"]], ["SetText", ["Hand in"]], ['SetToolTipText', ["Hand in selected Item to produce splitters"]], ['SetEvent', [lambda : self.HandInSingleItem()]]], []],	
			[[ui.Button, 0], [0, 0], [95, 265], [['SetUpVisual', ["d:/ymir work/ui/public/Large_button_01.sub"]],['SetOverVisual', ["d:/ymir work/ui/public/Large_button_02.sub"]], ['SetDownVisual', ["d:/ymir work/ui/public/Large_button_03.sub"]], ["SetText", ["Buy selected"]], ['SetToolTipText', ["Fill the inventory with the selected item"]], ['SetEvent', [lambda : self.RefillInventory()]]], []],	
			[[ui.Button, 0], [0, 0], [180, 265], [['SetUpVisual', ["d:/ymir work/ui/public/Large_button_01.sub"]],['SetOverVisual', ["d:/ymir work/ui/public/Large_button_02.sub"]], ['SetDownVisual', ["d:/ymir work/ui/public/Large_button_03.sub"]], ["SetText", ["Hand in all"]], ['SetToolTipText', ["Hand in all Items to produce splitters"]], ['SetEvent', [lambda : self.HandInAllItems()]]], []],	
			
			[[ui.TextLine, 0], [0, 0], [10, 290], [["SetDefaultFontName", [""]],	["SetText", ["String to enter:"]],	["SetFontColor", [1, 1.0, 1.0]]], []],			
			[[ui.SlotBar, 0], [150, 17], [85, 288], [], []],
			[[ui.EditLine, 0], [150, 17], [89, 291], [["SetMax", [20]], ["SetFocus", [""]]], []],
			
			[[ui.TextLine, 0], [0, 0], [10, 310], [["SetDefaultFontName", [""]],	["SetText", ["Pause between:"]],	["SetFontColor", [1, 1.0, 1.0]]], []],			
			[[ui.SlotBar, 0], [150, 17], [85, 308], [], []],
			[[ui.EditLine, 0], [150, 17], [89, 311], [["SetMax", [20]]], []],
			]
		GuiParser(Gui, self.Gui)		
		self.Gui[3].SetScrollBar(self.Gui[4])
		self.UpdateFileList()
		
	def RefillInventory(self):
		ItemIndex = self.Gui[3].GetSelectedItem()
		if ItemIndex:
			pass
		else:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "No item selected!")
			return
		SelectedItem = ItemIndex.GetText().split("	")
		if shop.IsOpen():
			for EachShopSlot in xrange(shop.SHOP_SLOT_COUNT):
				ShopItemValue = shop.GetItemID(EachShopSlot)
				if ShopItemValue == int(SelectedItem[1]):
					for i in xrange(89):
						net.SendShopBuyPacket(EachShopSlot)
		
	def HandInSingleItem(self):
		if player.GetTargetVID() == 0:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "No NPC selected")
			return
	
		ItemIndex = self.Gui[3].GetSelectedItem()
		if ItemIndex:
			pass
		else:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "No item selected!")
			return
		SelectedItem = ItemIndex.GetText().split("	")
		self.HandInItem(int(SelectedItem[0]))
		
	def HandInAllItems(self):
		if self.hand_in == 1:
			return
	
		if player.GetTargetVID() == 0:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "No NPC selected")
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
				self.hand_in_slots.append(Slot)
				if self.Gui[16].GetText() != "":
					self.hand_time = float(self.Gui[16].GetText())
				else:
					self.hand_time = 1.
		self.old_time_stamp = app.GetTime() - self.hand_time
		self.hand_in = 1
		
	def HandInItem(self, slot):	
		net.SendGiveItemPacket(player.GetTargetVID(), slot, 1)
		event.SelectAnswer(1, 0)
		if self.Gui[13].GetText() != "":
			net.SendQuestInputStringPacket(self.Gui[13].GetText())
		event.SelectAnswer(1, 0)
		
	def OnUpdate(self):
		if self.hand_in == 1:
			if app.GetTime() - self.old_time_stamp > self.hand_time:
				if len(self.hand_in_slots) > 0:
					slot = self.hand_in_slots.pop()
					self.HandInItem(slot)
					self.old_time_stamp = app.GetTime()
				else:
					self.hand_in = 0

	def UpdateFileList(self):
		self.Gui[3].RemoveAllItems()
		for i in xrange(90):
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
		
	def HookedQuestWindow(self, skin, idx):
		pass
	def InstallQuestWindowHook(self):
		game.GameWindow.OpenQuestWindow = self.HookedQuestWindow
		chat.AppendChat(1, "Quest Window wurde erfolgreich gehooked.")		
		
	def UnHookQuestWindow(self):
		game.GameWindow.OpenQuestWindow = self.OldRecv
		chat.AppendChat(1, "Quest Window Hook wurde entfernt.")
		

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
		
a = InventoryManagerDialog()
a.Show()
