import chatm2g as chat, playerm2g2 as player, m2netm2g as m2net
import ui,app,chr,item,skill,time,game,shop,background,constInfo,wndMgr,math,uiCommon,grp,dbg,m2k_lib

from CY_FIX import *

BonusListe = (  
	"","Max. TP","Max. MP","Vitalitaet","Intelligenz","Staerke","Ausweichwert","Angriffsgeschwindigkeit","Bewegungsgeschwindigkeit","Zaubergeschwindigkeit", "TP-Regeneration","MP-Regeneration","Vergiftungschance","Ohnmachtschance","Verlangsamungschance","Kritischer Treffer","Durchbohrender Treffer","Stark ggn Halbmenschen","Stark ggn Tiere","Stark ggn Orks","Stark ggn Esoterische","Stark ggn Untote","Stark ggn Teufel","TP-Absorbierung","MP-Absorbierung","Chance auf Manaraub","Chance MP-Regeneration","Nahkampf-Angriff blocken","Pfeilangriff ausweichen","Schwertverteidigung","Zweihandverteidigung","Dolchverteidigung","Glockenverteidigung","Faecherverteidigung","Pfeilwiderstand","Feuerwiderstand","Blitzwiderstand","Magieverteidigung","Windwiderstand","Nahkampftreffer reflektieren","Fluch reflektieren","Giftwiderstand","Chance MP wiederherzustellen","Exp-Bonus","Yang-Drop","Item-Drop","steigernde Trankwirkung","Chance TP wiederherzustellen","Immun gegen Ohnmacht","Immun gegen Verlangsamung","Immun gegen Stuerzen","APPLY_SKILL","Pfeilreichweite","Angriffswert","Verteidigungswert","Magischer Angriffswert","Magischer Verteidigungswert","","Max. Ausdauer","Stark gegen Krieger","Stark gegen Ninjas","Stark gegen Suras","Stark gegen Schamanen","Stark gegen Monster","Itemshop Angriffswert","Itemshop Verteidigungswert","Itemshop Exp-Bonus","Itemshop Item-Bonus","Itemshop Yang-Bonus", "APPLY_MAX_HP_PCT","APPLY_MAX_SP_PCT","Fertigkeitsschaden","Durchschn. Schaden","Fertigkeitsschaden Widerstand","Durchschn. Schadenswiderstand","","iCafe EXP-Bonus","iCafe Item-Bonus","Abwehr ggn Krieger","Abwehr ggn Ninjas","Abwehr ggn Suras","Abwehr ggn Schamanen",
    ) 

StoneIDListe = {
	28400,28404,28408,28412,28430,28431,28432,28433,28434,28435,28436,28437,28438,28439,28440,28441,28442,28443,28500,28504,28508,28512,28530,28531,28532,28533,28534,28535,28536,28537,28538,28539,28540,28541,28542,28543,28600,28604,28608,28612,28630,28631,28632,28633,28634,28635,28636,28637,28638,28639,28640,28641,28642,28643,28900,28904,28908,28912,28930,28931,28932,28933,28934,28935,28936,28937,28938,28939,28940,28941,28942,28943,
	}

class CreateItemDialog(ui.Window):

	ENABLE_COLOR = grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0)
	DISABLE_COLOR = grp.GenerateColor(0.9, 0.4745, 0.4627, 1.0)

	def __init__(self):
		self.Board = ui.BoardWithTitleBar()
		self.Board.SetSize(350, 335)
		self.Board.SetPosition(52, int(m2k_lib.ReadConfig("HackbarCoordHeight")))
		self.Board.SetTitleName("Item Creator")
		self.Board.SetCloseEvent(self.Hide_UI)
		self.Board.Hide() 
		
		self.comp = m2k_lib.Component()
		self.copyright = self.comp.TextLine(self.Board, 'by DaRealFreak', 250, 300, self.comp.RGB(255, 255, 0))
		self.ItemNameText = self.comp.TextLine(self.Board, "None", 15, 55, self.comp.RGB(255, 255, 255))
		self.ItemValueText = self.comp.TextLine(self.Board, 'Itemvalue:', 15, 35, self.comp.RGB(255, 255, 255))
		self.ItemCountText = self.comp.TextLine(self.Board, 'Itemcount:', 230, 35, self.comp.RGB(255, 255, 255))
		self.Bonus1Text = self.comp.TextLine(self.Board, 'Bonus 1:', 15, 190, self.comp.RGB(255, 255, 0))
		self.Bonus1AtrText = self.comp.TextLine(self.Board, '-', 65, 190, self.comp.RGB(255, 255, 255)) 
		self.Bonus2Text = self.comp.TextLine(self.Board, 'Bonus 2:', 15, 210, self.comp.RGB(255, 255, 0))
		self.Bonus2AtrText = self.comp.TextLine(self.Board, '-', 65, 210, self.comp.RGB(255, 255, 255)) 
		self.Bonus3Text = self.comp.TextLine(self.Board, 'Bonus 3:', 15, 230, self.comp.RGB(255, 255, 0))
		self.Bonus3AtrText = self.comp.TextLine(self.Board, '-', 65, 230, self.comp.RGB(255, 255, 255)) 
		self.Bonus4Text = self.comp.TextLine(self.Board, 'Bonus 4:', 15, 250, self.comp.RGB(255, 255, 0))
		self.Bonus4AtrText = self.comp.TextLine(self.Board, '-', 65, 250, self.comp.RGB(255, 255, 255)) 
		self.Bonus5Text = self.comp.TextLine(self.Board, 'Bonus 5:', 15, 270, self.comp.RGB(255, 255, 0))
		self.Bonus5AtrText = self.comp.TextLine(self.Board, '-', 65, 270, self.comp.RGB(255, 255, 255)) 
		self.Metin1Text = self.comp.TextLine(self.Board, "", 105, 88, self.comp.RGB(255, 255, 255))
		self.Metin2Text = self.comp.TextLine(self.Board, "", 105, 123, self.comp.RGB(255, 255, 255))
		self.Metin3Text = self.comp.TextLine(self.Board, "", 105, 158, self.comp.RGB(255, 255, 255))
		
		self.CreateItemButton = self.comp.Button(self.Board, 'Create Item', '', 40, 295, self.CreateItem, 'd:/ymir work/ui/public/xlarge_Button_01.sub', 'd:/ymir work/ui/public/xlarge_Button_02.sub', 'd:/ymir work/ui/public/xlarge_Button_03.sub')
		self.SetItemValueButton = self.comp.Button(self.Board, 'Set', '', 110, 33, lambda : self.UpdateItem(-1), 'd:/ymir work/ui/public/small_Button_01.sub', 'd:/ymir work/ui/public/small_Button_02.sub', 'd:/ymir work/ui/public/small_Button_03.sub')
		self.CallItemListButton = self.comp.Button(self.Board, 'Itemlist', '', 155, 33, self.CallItemList, 'd:/ymir work/ui/public/middle_Button_01.sub', 'd:/ymir work/ui/public/middle_Button_02.sub', 'd:/ymir work/ui/public/middle_Button_03.sub')
		self.Bonus1Button = self.comp.Button(self.Board, 'Choose Bonus 1', '', 240, 185, lambda : self.CallBonusList(0), 'd:/ymir work/ui/public/large_Button_01.sub', 'd:/ymir work/ui/public/large_Button_02.sub', 'd:/ymir work/ui/public/large_Button_03.sub')
		self.Bonus2Button = self.comp.Button(self.Board, 'Choose Bonus 2', '', 240, 205, lambda : self.CallBonusList(1), 'd:/ymir work/ui/public/large_Button_01.sub', 'd:/ymir work/ui/public/large_Button_02.sub', 'd:/ymir work/ui/public/large_Button_03.sub')
		self.Bonus3Button = self.comp.Button(self.Board, 'Choose Bonus 3', '', 240, 225, lambda : self.CallBonusList(2), 'd:/ymir work/ui/public/large_Button_01.sub', 'd:/ymir work/ui/public/large_Button_02.sub', 'd:/ymir work/ui/public/large_Button_03.sub')
		self.Bonus4Button = self.comp.Button(self.Board, 'Choose Bonus 4', '', 240, 245, lambda : self.CallBonusList(3), 'd:/ymir work/ui/public/large_Button_01.sub', 'd:/ymir work/ui/public/large_Button_02.sub', 'd:/ymir work/ui/public/large_Button_03.sub')
		self.Bonus5Button = self.comp.Button(self.Board, 'Choose Bonus 5', '', 240, 265, lambda : self.CallBonusList(4), 'd:/ymir work/ui/public/large_Button_01.sub', 'd:/ymir work/ui/public/large_Button_02.sub', 'd:/ymir work/ui/public/large_Button_03.sub')
		self.Metin1Button = self.comp.Button(self.Board, 'Choose Stone 1', '', 240, 85, lambda : self.CallStoneList(1), 'd:/ymir work/ui/public/large_Button_01.sub', 'd:/ymir work/ui/public/large_Button_02.sub', 'd:/ymir work/ui/public/large_Button_03.sub')
		self.Metin2Button = self.comp.Button(self.Board, 'Choose Stone 2', '', 240, 120, lambda : self.CallStoneList(2), 'd:/ymir work/ui/public/large_Button_01.sub', 'd:/ymir work/ui/public/large_Button_02.sub', 'd:/ymir work/ui/public/large_Button_03.sub')
		self.Metin3Button = self.comp.Button(self.Board, 'Choose Stone 3', '', 240, 155, lambda : self.CallStoneList(3), 'd:/ymir work/ui/public/large_Button_01.sub', 'd:/ymir work/ui/public/large_Button_02.sub', 'd:/ymir work/ui/public/large_Button_03.sub')
		
		self.ItemValueSlotBar, self.ItemValueEditLine = self.comp.EditLine(self.Board, int(m2k_lib.ReadConfig("ItemValue")), 70, 35, 35, 14, 5)
		self.ItemCountEditLine = self.comp.OnlyEditLine(self.Board, 21, 18, 290, 35, '1', 3)
		self.Bonus1ValueEditLine = self.comp.OnlyEditLine(self.Board, 29, 18, 211, 190, m2k_lib.ReadConfig("BonusValue0"), 4)
		self.Bonus2ValueEditLine = self.comp.OnlyEditLine(self.Board, 29, 18, 211, 210, m2k_lib.ReadConfig("BonusValue1"), 4)
		self.Bonus3ValueEditLine = self.comp.OnlyEditLine(self.Board, 29, 18, 211, 230, m2k_lib.ReadConfig("BonusValue2"), 4)
		self.Bonus4ValueEditLine = self.comp.OnlyEditLine(self.Board, 29, 18, 211, 250, m2k_lib.ReadConfig("BonusValue3"), 4)
		self.Bonus5ValueEditLine = self.comp.OnlyEditLine(self.Board, 29, 18, 211, 270, m2k_lib.ReadConfig("BonusValue4"), 4)
		
		self.ItemImage = self.comp.ExpandedImage(self.Board, 17, 80, "m2kmod\Images\epvp.tga")
		self.Metin1Image = self.comp.ExpandedImage(self.Board, 65, 80, "")
		self.Metin2Image = self.comp.ExpandedImage(self.Board, 65, 115, "")
		self.Metin3Image = self.comp.ExpandedImage(self.Board, 65, 150, "")
			
		for i in xrange(5):
			self.UpdateBonus(i,int(m2k_lib.ReadConfig("CreateBonus"+str(i))))
		if player.GetName() != "":
			for i in xrange(3):
				self.UpdateStone(i+1,int(m2k_lib.ReadConfig("MetinStone"+str(i+1))))
			self.UpdateItem(int(m2k_lib.ReadConfig("ItemValue")))

	def switch_state(self):
		if self.Board.IsShow():
			self.Hide_UI()
		else:
			self.Board.Show()
			self.Board.SetPosition(52, int(m2k_lib.ReadConfig("HackbarCoordHeight")))			
	def Hide_UI(self):
		m2k_lib.SaveConfig("ItemValue", str(self.ItemValueEditLine.GetText()))
		m2k_lib.SaveConfig("CreateBonus0", str(self.CreateBonus0))
		m2k_lib.SaveConfig("CreateBonus1", str(self.CreateBonus1))
		m2k_lib.SaveConfig("CreateBonus2", str(self.CreateBonus2))
		m2k_lib.SaveConfig("CreateBonus3", str(self.CreateBonus3))
		m2k_lib.SaveConfig("CreateBonus4", str(self.CreateBonus4))
		m2k_lib.SaveConfig("BonusValue0", str(self.Bonus1ValueEditLine.GetText()))
		m2k_lib.SaveConfig("BonusValue1", str(self.Bonus2ValueEditLine.GetText()))
		m2k_lib.SaveConfig("BonusValue2", str(self.Bonus3ValueEditLine.GetText()))
		m2k_lib.SaveConfig("BonusValue3", str(self.Bonus4ValueEditLine.GetText()))
		m2k_lib.SaveConfig("BonusValue4", str(self.Bonus5ValueEditLine.GetText()))
		m2k_lib.SaveConfig("MetinStone1", str(self.MetinStone1))
		m2k_lib.SaveConfig("MetinStone2", str(self.MetinStone2))
		m2k_lib.SaveConfig("MetinStone3", str(self.MetinStone3))
		self.Board.Hide()
		

	def UpdateItem(self, index):
		if index != -1:
			self.ItemValueEditLine.SetText(str(index))
		else:
			index = self.ItemValueEditLine.GetText()
		item.SelectItem(int(index))
		self.ItemImage.LoadImage(str(item.GetIconImageFileName()))
		self.ItemNameText.SetText(str(item.GetItemName()))
		for i in xrange(0,1):
			(ItemTypeLimit, ItemLevelLimit) = item.GetLimit(i)
			if item.LIMIT_LEVEL == ItemTypeLimit:
				if player.GetStatus(player.LEVEL) < ItemLevelLimit:
					self.ItemNameText.SetPackedFontColor(self.DISABLE_COLOR)
				else:
					self.ItemNameText.SetPackedFontColor(self.ENABLE_COLOR)	
		
	def UpdateBonus(self, bonus, bonusIndex):
		if bonus == 0:
			self.CreateBonus0 = bonusIndex
			if bonusIndex != 0:
				self.Bonus1AtrText.SetText(str(BonusListe[int(self.CreateBonus0)]))
			else:
				self.Bonus1AtrText.SetText("None")
		elif bonus == 1:
			self.CreateBonus1 = bonusIndex
			if bonusIndex != 0:
				self.Bonus2AtrText.SetText(str(BonusListe[int(self.CreateBonus1)]))
			else:
				self.Bonus2AtrText.SetText("None")
		elif bonus == 2:
			self.CreateBonus2 = bonusIndex
			if bonusIndex != 0:
				self.Bonus3AtrText.SetText(str(BonusListe[int(self.CreateBonus2)]))
			else:
				self.Bonus3AtrText.SetText("None")
		elif bonus == 3:
			self.CreateBonus3 = bonusIndex
			if bonusIndex != 0:
				self.Bonus4AtrText.SetText(str(BonusListe[int(self.CreateBonus3)]))
			else:
				self.Bonus4AtrText.SetText("None")
		elif bonus == 4:
			self.CreateBonus4 = bonusIndex
			if bonusIndex != 0:
				self.Bonus5AtrText.SetText(str(BonusListe[int(self.CreateBonus4)]))
			else:	
				self.Bonus5AtrText.SetText("None")	
		
	def UpdateStone(self, stone, index):
		item.SelectItem(int(index))
		if stone == 1:
			self.MetinStone1 = index
			if self.MetinStone1 != 0:
				self.Metin1Image.LoadImage(str(item.GetIconImageFileName()))
				self.Metin1Text.SetText(str(item.GetItemName()))
			else:
				self.Metin1Text.SetText("Stone 1")	
		elif stone == 2:
			self.MetinStone2 = index
			if self.MetinStone2 != 0:
				self.Metin2Image.LoadImage(str(item.GetIconImageFileName()))
				self.Metin2Text.SetText(str(item.GetItemName()))
			else:
				self.Metin2Text.SetText("Stone 2")	
		elif stone == 3:
			self.MetinStone3 = index
			if self.MetinStone3 != 0:
				self.Metin3Image.LoadImage(str(item.GetIconImageFileName()))
				self.Metin3Text.SetText(str(item.GetItemName()))
			else:
				self.Metin3Text.SetText("Stone 3")	
	
	def isItem(self, slot):
		if player.GetItemIndex(slot) != 0:
			return 1
		else:
			return 0
	
	def CreateItem(self):
		self.ItemCount = int()
		for slot in xrange(player.INVENTORY_SLOT_COUNT):
			state = "go"
			if not self.isItem(int(slot)):
				if int(slot) >= 5:
					if self.isItem(int(slot) - 5):
						itemIndex = player.GetItemIndex(int(slot) - 5)
						item.SelectItem(itemIndex)
						if int(item.GetItemSize()[1]) >= 2:
							state = "banned"
			else:
				state = "banned"
			if str(state) == "go":
				player.SetItemData(int(slot), int(self.ItemValueEditLine.GetText()),int(self.ItemCountEditLine.GetText()))
				for i in xrange(5):
					exec 'player.SetItemAttribute(int(' + str(slot) + '), ' + str(i) + ', int(self.CreateBonus' + str(i) + '), int(self.Bonus' + str(i+1) + 'ValueEditLine.GetText()))'	
				player.SetItemMetinSocket(int(slot), 0, int(self.MetinStone1))
				player.SetItemMetinSocket(int(slot), 1, int(self.MetinStone2))
				player.SetItemMetinSocket(int(slot), 2, int(self.MetinStone3))
				break
		
	def CallItemList(self):
		self.ItemListDialog = ItemListDialog(self)
		
	def CallBonusList(self, bonus):
		self.BonusListDialog = BonusListDialog(self, bonus)
		
	def	CallStoneList(self, stone):
		self.StoneListDialog = StoneListDialog(self, stone)

		
class ItemListDialog(ui.Window):

	def __init__(self, parentUI):
		ui.Window.__init__(self)
		self.CreateItemDialog = parentUI
		self.Board = ui.BoardWithTitleBar()
		self.Board.SetSize(200, 335)
		self.Board.SetPosition(400, 60)
		self.Board.SetTitleName("Item List")
		self.Board.SetCloseEvent(self.Close)
		self.Board.Show()
		
		self.comp = m2k_lib.Component()
		self.ItemValueText = self.comp.TextLine(self.Board, 'Search Item:', 19, 33, self.comp.RGB(255, 255, 255))
		self.SearchItemButton = self.comp.Button(self.Board, 'Search', '', 147, 48,  lambda : self.UpdateFileList(2), 'd:/ymir work/ui/public/small_Button_01.sub', 'd:/ymir work/ui/public/small_Button_02.sub', 'd:/ymir work/ui/public/small_Button_03.sub')
		self.SelectBonus = self.comp.Button(self.Board, 'OK', '', 25, 295, lambda : self.UpdateFileList(3), 'd:/ymir work/ui/public/Middle_Button_01.sub', 'd:/ymir work/ui/public/Middle_Button_02.sub', 'd:/ymir work/ui/public/Middle_Button_03.sub')
		self.CancelBonus = self.comp.Button(self.Board, 'Cancel', '', 115, 295, self.Close, 'd:/ymir work/ui/public/Middle_Button_01.sub', 'd:/ymir work/ui/public/Middle_Button_02.sub', 'd:/ymir work/ui/public/Middle_Button_03.sub')
		self.SearchItemSlotBar, self.SearchItemEditLine = self.comp.EditLine(self.Board, '', 15, 50, 120, 15, 20)
		self.fileListBox, self.ScrollBar = self.comp.FileListBox(self.Board, 15, 80, 180, 200, 10)
	
		self.UpdateFileList(1)
		
	def __del__(self):
		ui.Window.__del__(self)

	def Show(self):
		ui.Window.Show(self)

	def Close(self):
		self.Board.Hide()

	def UpdateFileList(self,mode):
		SearchName = str(self.SearchItemEditLine.GetText())
		SelectedIndex = self.fileListBox.GetSelectedItem()
		self.__RefreshFileList()
		try:
			lines = open(app.GetLocalePath()+"/item_list.txt", "r").readlines()
		except IOError:
			import dbg
			dbg.LogBox("Load Itemlist Error")

		for line in lines:
			tokens = str(line).split("\t")
			Index = str(tokens[0])
			Itemname = item.GetItemName(item.SelectItem(int(Index)))
			if mode == 1:
				if Index and str(Itemname) != "":
					self.fileListBox.AppendItem(m2k_lib.Item(Index +"  " + Itemname))
			elif mode == 2:
				if str(Itemname).find(str(SearchName)) != -1:
					self.fileListBox.AppendItem(m2k_lib.Item(Index +"  " + Itemname))
			elif mode == 3:
				if str(Itemname) == str(SelectedIndex.GetText().split("  ")[1]):
					ItemValue = Index.split("  ")[0]
					self.CreateItemDialog.UpdateItem(int(ItemValue))
					self.Close()
					break

	def __RefreshFileList(self):
		self.fileListBox.RemoveAllItems()

		
class BonusListDialog(ui.Window):
	
	def __init__(self, parentUI, bonus):
		ui.Window.__init__(self)
		self.Bonus = bonus
		self.CreateItemDialog = parentUI
		
		self.Board = ui.BoardWithTitleBar()
		self.Board.SetSize(200, 335)
		self.Board.SetPosition(400, 60)
		self.Board.SetTitleName("Choose Bonus "+str(bonus+1))
		self.Board.SetCloseEvent(self.Close)
		self.Board.Show()
		
		self.comp = m2k_lib.Component()
		self.SelectBonus = self.comp.Button(self.Board, 'OK', '', 25, 295, lambda : self.SetBonus(self.Bonus), 'd:/ymir work/ui/public/Middle_Button_01.sub', 'd:/ymir work/ui/public/Middle_Button_02.sub', 'd:/ymir work/ui/public/Middle_Button_03.sub')	
		self.CancelBonus = self.comp.Button(self.Board, 'Cancel', '', 115, 295, self.Close, 'd:/ymir work/ui/public/Middle_Button_01.sub', 'd:/ymir work/ui/public/Middle_Button_02.sub', 'd:/ymir work/ui/public/Middle_Button_03.sub')
		self.fileListBox, self.ScrollBar = self.comp.FileListBox(self.Board, 15, 45, 180, 240, 12)

		self.UpdateFileList()

	def __del__(self):
		ui.Window.__del__(self)

	def Show(self):
		ui.Window.Show(self)

	def Close(self):
		self.Board.Hide()		
		
	def UpdateFileList(self):
		self.__RefreshFileList()
		num = 0
		for BonusType in BonusListe:
			if BonusType != "":
				self.fileListBox.AppendItem(m2k_lib.Item(str(num) + '    ' + BonusType))
			else:
				self.fileListBox.AppendItem(m2k_lib.Item(str(num) + '    ' + 'None'))
			num += 1
		
	def __RefreshFileList(self):
		self.fileListBox.RemoveAllItems()
	
	def SetBonus(self, bonus):
		SelectedName = self.fileListBox.GetSelectedItem().GetText()
		SelectedIndex = SelectedName.split("    ")
		if str(SelectedName) != "None" and str(SelectedName) != "":
			chat.AppendChat(7, "[m2k-Mod] " + str(bonus+1) + ". Bonus - " + str(SelectedName))
			self.CreateItemDialog.UpdateBonus(bonus, SelectedIndex[0])
		elif str(SelectedName) == "None" and str(SelectedName) != "":		
			chat.AppendChat(7, "[m2k-Mod] " + str(bonus+1) + ". Bonus - Removed")
			self.CreateItemDialog.UpdateBonus(bonus, 0)
		else:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "[m2k-Mod] No Bonus Choosed!")		
		self.Close()
	

class StoneListDialog(ui.Window):
	
	def __init__(self, parentUI, stone):
		ui.Window.__init__(self)
		self.Stone = stone
		self.CreateItemDialog = parentUI
		
		self.Board = ui.BoardWithTitleBar()
		self.Board.SetSize(225, 335)
		self.Board.SetPosition(400, 60)
		self.Board.SetTitleName("Choose Stone "+str(stone))
		self.Board.SetCloseEvent(self.Close)
		self.Board.Show()
		
		self.comp = m2k_lib.Component()
		self.SelectBonus = self.comp.Button(self.Board, 'OK', '', 37, 295, lambda : self.SetStone(self.Stone), 'd:/ymir work/ui/public/Middle_Button_01.sub', 'd:/ymir work/ui/public/Middle_Button_02.sub', 'd:/ymir work/ui/public/Middle_Button_03.sub')	
		self.CancelBonus = self.comp.Button(self.Board, 'Cancel', '', 127, 295, self.Close, 'd:/ymir work/ui/public/Middle_Button_01.sub', 'd:/ymir work/ui/public/Middle_Button_02.sub', 'd:/ymir work/ui/public/Middle_Button_03.sub')
		self.fileListBox, self.ScrollBar = self.comp.FileListBox(self.Board, 15, 45, 205, 240, 12)

		self.UpdateFileList()

	def __del__(self):
		ui.Window.__del__(self)

	def Show(self):
		ui.Window.Show(self)

	def Close(self):
		self.Board.Hide()		
		
	def UpdateFileList(self):
		self.__RefreshFileList()
		for StoneIndex in StoneIDListe:
			StoneName = item.GetItemName(item.SelectItem(int(StoneIndex)))
			self.fileListBox.AppendItem(m2k_lib.Item(str(StoneIndex) + '    ' + str(StoneName)))
	def __RefreshFileList(self):
		self.fileListBox.RemoveAllItems()
	
	def SetStone(self, stone):
		SelectedName = self.fileListBox.GetSelectedItem().GetText()
		SelectedIndex = SelectedName.split("    ")
		if str(SelectedName) != "":
			chat.AppendChat(7, "[m2k-Mod] " + str(stone) + ". Stone - " + str(SelectedName))
			self.CreateItemDialog.UpdateStone(stone, SelectedIndex[0])
		else:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "[m2k-Mod] No Stone Choosed!")		
		self.Close()

	