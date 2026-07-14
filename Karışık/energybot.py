import chatm2g as chat, playerm2g2 as player, m2netm2g as m2net
import ui,app,chr,item,skill,time,game,event,shop,background,constInfo,wndMgr,math,uiCommon,grp,dbg,m2k_lib,m2k_hook,Global
from tp import Teleport

from CY_FIX import *

REICH_COORDS_ALCHEMIST = {
    "RED": (624, 510),
    "BLUE": (292, 814),
    "YELLOW": (657, 734),
}
REICH_COORDS_ARMORSTORE = { 
    "RED": (596, 558),
    "BLUE": (428, 608),
    "YELLOW": (673, 660),
}

class EnergyDialog(ui.ScriptWindow):
	
	hook = m2k_hook.hook()
	
	def __init__(self):
		self.Board = ui.ThinBoard()
		self.Board.SetSize(210, 390)
		self.Board.SetPosition(52, int(m2k_lib.ReadConfig("HackbarCoordHeight")))
		self.Board.Hide()
		
		self.comp = m2k_lib.Component()
		self.Header = self.comp.TextLine(self.Board, 'Alchemist-Bot', 75, 8, self.comp.RGB(255, 255, 0))
		self.ListBoxLabel = self.comp.TextLine(self.Board, ' Slot:	 ID:			Name:', 8, 33, self.comp.RGB(0, 229, 650))
	
		self.Close = self.comp.Button(self.Board, '', 'Close', 188, 7, self.Hide_UI, 'd:/ymir work/ui/public/close_button_01.sub', 'd:/ymir work/ui/public/close_button_02.sub', 'd:/ymir work/ui/public/close_button_03.sub')
		self.Refresh = self.comp.Button(self.Board, '', 'Refresh', 163, 6, self.UpdateFileList, 'd:/ymir work/ui/game/guild/refresh_button_01.sub', 'd:/ymir work/ui/game/guild/refresh_button_02.sub', 'd:/ymir work/ui/game/guild/refresh_button_03.sub')	
		self.GiveSelectedItemButton = self.comp.Button(self.Board, 'Give Selected', 'Gives selected Item to the alchemist ', 15, 285, lambda : self.GiveItem("one"), 'd:/ymir work/ui/public/Large_button_01.sub', 'd:/ymir work/ui/public/Large_button_02.sub','d:/ymir work/ui/public/Large_button_03.sub')
		self.GiveAllItemButton = self.comp.Button(self.Board, 'Give All', 'Gives all Items, like selected to the alchemist', 110, 285, lambda : self.GiveAllItemsDialog(), 'd:/ymir work/ui/public/Large_button_01.sub', 'd:/ymir work/ui/public/Large_button_02.sub','d:/ymir work/ui/public/Large_button_03.sub')
		self.BuyOneButton = self.comp.Button(self.Board, 'Buy one', 'Buys one level 36 dagger', 15, 310, lambda : self.BuyItems("one"), 'd:/ymir work/ui/public/Large_button_01.sub', 'd:/ymir work/ui/public/Large_button_02.sub','d:/ymir work/ui/public/Large_button_03.sub')
		self.BuyAllButton = self.comp.Button(self.Board, 'Buy all', 'Buys 90 level 36 dagger', 110, 310, lambda : self.BuyItems("all"), 'd:/ymir work/ui/public/Large_button_01.sub', 'd:/ymir work/ui/public/Large_button_02.sub','d:/ymir work/ui/public/Large_button_03.sub')
		self.MakeCrystalButton = self.comp.Button(self.Board, 'Make Crystal', 'Makes Crystalls out of splitters', 62, 335, lambda : self.MakeCrystals(), 'd:/ymir work/ui/public/Large_button_01.sub', 'd:/ymir work/ui/public/Large_button_02.sub','d:/ymir work/ui/public/Large_button_03.sub')
		self.TeleportToNpcButton = self.comp.Button(self.Board, 'Teleport to', '', 15, 360, lambda : self.TeleportToNpc(self.NpcCombo.GetCurrentText()), 'd:/ymir work/ui/public/Large_button_01.sub', 'd:/ymir work/ui/public/Large_button_02.sub','d:/ymir work/ui/public/Large_button_03.sub')
		self.BarItems, self.ListBoxItems, ScrollItems = self.comp.ListBoxEx(self.Board, 10, 50, 170, 220)
		self.NpcCombo = self.comp.ComboBox(self.Board, 'Alchemist', 118, 362, 70)
		self.NpcCombo.InsertItem(0, 'Alchemist')
		self.NpcCombo.InsertItem(1, 'Weapon-Store')
		
		
	def switch_state(self):
		if self.Board.IsShow():
			self.Hide_UI()
		else:
			self.Board.Show()
			self.UpdateFileList()
			self.hook.SetQuestHook(1)
			self.Board.SetPosition(52, int(m2k_lib.ReadConfig("HackbarCoordHeight")))
	def Hide_UI(self):
		self.Board.Hide()
		self.hook.SetQuestHook(0)

		
	def UpdateFileList(self):
		self.ListBoxItems.RemoveAllItems()
		for i in xrange(100):
			ItemIndex = player.GetItemIndex(i)
			if ItemIndex != 0:
				Type = item.GetItemType(item.SelectItem(int(ItemIndex)))
				if Type == item.ITEM_TYPE_WEAPON or item.ITEM_TYPE_WEAPON:
					ItemName = item.GetItemName(item.SelectItem(int(ItemIndex)))
					self.ListBoxItems.AppendItem(m2k_lib.Item(str(i) + '    ' + str(ItemIndex) + '    ' + ItemName))
		self.alchemistVid = self.ScanForNPCByRace(20001)
		

	def GiveItem(self, mode, name="none"):
		self.IsHooked = TRUE
		ItemIndex = self.IsSelected()
		if not ItemIndex:
			return
		if not self.IsNpcVid():
			return
		SelectedItem = ItemIndex.GetText().split("    ")
		if mode == "one":
			self.GiveItemFunction(SelectedItem[0])
		else:
			self.CancelQuestionDialog()
			for Slot in xrange(0, 90):
				ItemValue = player.GetItemIndex(Slot)
				if ItemValue != 0:
					try:
						ItemName = item.GetItemName(item.SelectItem(ItemValue)).split("+")[0]
					except:
						chat.AppendChat(7,"[m2k-Mod] You can select only a weapon or armor!")
					if ItemName == name:
						self.GiveItemFunction(Slot)
		
			
	def GiveAllItemsDialog(self):
		ItemIndex = self.IsSelected()
		if not ItemIndex:
			return
		if not m2k_lib.IsPremium():
			return
		try:
			SearchedName = ItemIndex.GetText().split("    ")[2].split("+")[0]
		except:
			chat.AppendChat(7,"[m2k-Mod] You can select only a weapon or armor!")
			return
		self.QuestionDialog = uiCommon.QuestionDialog()
		self.QuestionDialog.SetText("Do You want to give all "+SearchedName+"s to the alchemist?")
		self.QuestionDialog.SetAcceptEvent(lambda : self.GiveItem("all", SearchedName))
		self.QuestionDialog.SetCancelEvent(ui.__mem_func__(self.CancelQuestionDialog))
		self.QuestionDialog.Open()	
		
	def GiveItemFunction(self, slot):
		m2net.SendGiveItemPacket(self.alchemistVid, int(slot), 1)
		event.SelectAnswer(1, 0)
		event.SelectAnswer(1, 0)
	
	
	def BuyItems(self, mode):
		if not shop.IsOpen():
			chat.AppendChat(7,"[m2k-Mod] No Weapon-Shop is open!")
			return
		if mode == "one":
			m2net.SendShopBuyPacket(4)
		if not m2k_lib.IsPremium():
			return
		if mode == "all":


			buy_max = 0
			yang = player.GetMoney()
			for i in xrange(90):
				if not player.GetItemIndex(i):
					buy_max += 1
			for a in range(buy_max):
				if yang-15000 >=0:
					m2net.SendShopBuyPacket(4)
					yang -= 15000
				else:
					chat.AppendChat(7,"[m2k-Mod] You have not enough money!")
					break
		m2net.SendShopEndPacket()	

	def MakeCrystals(self):
		if not m2k_lib.IsPremium():
			return
		count = 0
		for i in xrange(90):
			if player.GetItemIndex(i) == 51001:
				count+=player.GetItemCount(i)
		chat.AppendChat(7, str(count))
		lcount = int(count/30)
		if lcount >= 1:
			for i in xrange(lcount):
				m2net.SendOnClickPacket(self.alchemistVid)
				event.SelectAnswer(1,4)
				event.SelectAnswer(1,254)# 254 -> "weiter"
				event.SelectAnswer(1,254)# 254 -> "weiter"
				event.SelectAnswer(1,0)
				event.SelectAnswer(1,0)
				chat.AppendChat(7, "[m2k-Mod] Tried to make one cristall (might fail")
		else:
			chat.AppendChat(7, "[m2k-Mod] You need at least 30 Energy-Fragments to produce one crystal ")
		
	def TeleportToNpc(self, npc):
		if not m2k_lib.IsPremium():
			return
		if m2net.GetEmpireID() == 1:
			if npc == 'Alchemist':
				x = REICH_COORDS_ALCHEMIST["RED"][0]
				y = REICH_COORDS_ALCHEMIST["RED"][1]
				self.hook.SetQuestHook(1)
			else:
				x = REICH_COORDS_ARMORSTORE["RED"][0]
				y = REICH_COORDS_ARMORSTORE["RED"][1]
				self.hook.SetQuestHook(0)
		if m2net.GetEmpireID() == 2:
			if npc == 'Alchemist':
				x = REICH_COORDS_ALCHEMIST["YELLOW"][0]
				y = REICH_COORDS_ALCHEMIST["YELLOW"][1]
				self.hook.SetQuestHook(1)
			else:
				x = REICH_COORDS_ARMORSTORE["YELLOW"][0]
				y = REICH_COORDS_ARMORSTORE["YELLOW"][1]
				self.hook.SetQuestHook(0)
		if m2net.GetEmpireID() == 3:
			if npc == 'Alchemist':
				x = REICH_COORDS_ALCHEMIST["BLUE"][0]
				y = REICH_COORDS_ALCHEMIST["BLUE"][1]
				self.hook.SetQuestHook(1)
			else:
				x = REICH_COORDS_ARMORSTORE["BLUE"][0]
				y = REICH_COORDS_ARMORSTORE["BLUE"][1]
				self.hook.SetQuestHook(0)
		inc = Teleport(x*100, y*100)
		inc.start()
		
		
		
	def ScanForNPCByRace(self, race):
		for i in xrange(100000):
			if chr.INSTANCE_TYPE_NPC == chr.GetInstanceType(i):
				chr.SelectInstance(i)
				if chr.GetRace() == race:
					chat.AppendChat(7, "[m2k-Mod] Alchemist found")
					return i
		
	def IsNpcVid(self):
		chr.SelectInstance(self.alchemistVid)
		if chr.GetRace() == 20001:
			return 1
		else:
			chat.AppendChat(7, "[m2k-Mod] Please Press the Refresh-Button next to the close Button to get alchemists VID!")
			return 0
				
	def IsSelected(self):
		ItemIndex = self.ListBoxItems.GetSelectedItem()
		if not ItemIndex:
			chat.AppendChat(7, "[m2k-Mod] No Item selected!")
			return 0
		else:
			return ItemIndex
			
	def CancelQuestionDialog(self):
		self.QuestionDialog.Close()
		self.QuestionDialog = None
		