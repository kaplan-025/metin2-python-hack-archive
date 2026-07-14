import ui,app,chat,chr,net,player,item,skill,time,game,shop,chrmgr
import background,constInfo,wndMgr,math,uiCommon,grp,m2k_lib
	
class EquipmentDialog(ui.ScriptWindow):

	def __init__(self):
		self.Board = ui.BoardWithTitleBar()
		self.Board.SetSize(200, 230)
		self.Board.SetPosition(52, 40)
		self.Board.SetTitleName("EQ-Changer")
		self.Board.SetCloseEvent(self.Hide_UI)
	#	self.Board.AddFlag('movable')
		self.Board.Hide()
		
		self.comp = m2k_lib.Component()
		self.WeaponLabel = self.comp.TextLine(self.Board, 'Weapon', 14, 30, self.comp.RGB(255, 255, 0))
		self.ArmorLabel = self.comp.TextLine(self.Board, 'Armor', 67, 30, self.comp.RGB(255, 255, 0))
		self.FakeNameLabel = self.comp.TextLine(self.Board, 'Fake-Name', 113, 60, self.comp.RGB(255, 255, 0))
		self.GMEffectLabel = self.comp.TextLine(self.Board, 'GM-Effect', 113, 115, self.comp.RGB(255, 255, 0))
		self.WeaponSlotBar, self.WeaponEditLine = self.comp.EditLine(self.Board, "189", 15, 145, 35, 14, 5)
		self.ArmorValueSlotBar, self.ArmorEditLine = self.comp.EditLine(self.Board, "12019", 65, 145, 35, 14, 5)
		self.NameSlotBar, self.NameEditLine = self.comp.EditLine(self.Board, "123klo", 110, 75, 75, 14, 20)
		
		self.WeaponImage = self.comp.ExpandedImage(self.Board, 17, 43, "m2kmod\Images\grolli.tga")
		self.ArmorImage = self.comp.ExpandedImage(self.Board, 67, 59, "m2kmod\Images\grolli.tga")
		self.ChangeEQButton = self.comp.Button(self.Board, 'Change Equipment', '', 10, 193, self.ChangeEQ, 'd:/ymir work/ui/public/xlarge_Button_01.sub', 'd:/ymir work/ui/public/xlarge_Button_02.sub', 'd:/ymir work/ui/public/xlarge_Button_03.sub')
		self.SetWeaponButton = self.comp.Button(self.Board, 'Set', '', 12, 165, self.Weapon, 'd:/ymir work/ui/public/small_Button_01.sub', 'd:/ymir work/ui/public/small_Button_02.sub', 'd:/ymir work/ui/public/small_Button_03.sub')
		self.SetArmorButton = self.comp.Button(self.Board, 'Set', '', 63, 165, self.Armor, 'd:/ymir work/ui/public/small_Button_01.sub', 'd:/ymir work/ui/public/small_Button_02.sub', 'd:/ymir work/ui/public/small_Button_03.sub')
		self.FakeNameOn = self.comp.HideButton(self.Board, '', '', 165, 60, self.SetFakeName, 'm2kmod/Images/on_0.tga', 'm2kmod/Images/on_1.tga', 'm2kmod/Images/on_2.tga')
		self.FakeNameOff = self.comp.HideButton(self.Board, '', '', 165, 60, self.SetFakeName, 'm2kmod/Images/off_0.tga', 'm2kmod/Images/off_1.tga', 'm2kmod/Images/off_2.tga')
		self.GMEffectOn = self.comp.HideButton(self.Board, '', '', 165, 115, self.SetGMEffect, 'm2kmod/Images/on_0.tga', 'm2kmod/Images/on_1.tga', 'm2kmod/Images/on_2.tga')
		self.GMEffectOff = self.comp.HideButton(self.Board, '', '', 165, 115, self.SetGMEffect, 'm2kmod/Images/off_0.tga', 'm2kmod/Images/off_1.tga', 'm2kmod/Images/off_2.tga')
		
		if player.GetName() != "":
			self.UpdateWeapon(int(m2k_lib.ReadConfig("WeaponID")))
			self.UpdateArmor(int(m2k_lib.ReadConfig("ArmorID")))
		self.NameEditLine.SetText(m2k_lib.ReadConfig("FakeName"))
		self.FakeName = int(m2k_lib.ReadConfig("Fake_Name"))
		self.GMEffect = int(m2k_lib.ReadConfig("GMEffect"))
		
		if self.FakeName:
			self.FakeNameOn.Show()
		else:
			self.FakeNameOff.Show()
		if self.GMEffect:
			self.GMEffectOn.Show()
		else:
			self.GMEffectOff.Show()
	
	def switch_state(self):
		if self.Board.IsShow():
			self.Hide_UI()
		else:
			self.Board.Show()	
	def Hide_UI(self):
		m2k_lib.SaveConfig("WeaponID", str(self.WeaponEditLine.GetText()))
		m2k_lib.SaveConfig("ArmorID", str(self.ArmorEditLine.GetText()))
		m2k_lib.SaveConfig("FakeName", str(self.NameEditLine.GetText()))
		m2k_lib.SaveConfig("Fake_Name", str(self.FakeName))
		m2k_lib.SaveConfig("GMEffect", str(self.GMEffect))
		self.Board.Hide()


	def SetFakeName(self):
		if self.FakeName:
			self.FakeName = 0
			self.FakeNameOff.Show()
			self.FakeNameOn.Hide()
		else: 
			self.FakeName = 1
			self.FakeNameOn.Show()
			self.FakeNameOff.Hide()
			
	def SetGMEffect(self):
		if self.GMEffect:
			self.GMEffect = 0
			self.GMEffectOff.Show()
			self.GMEffectOn.Hide()
		else: 
			self.GMEffect = 1
			self.GMEffectOn.Show()
			self.GMEffectOff.Hide()
		
		
	def ChangeEQ(self):
		chr.SetWeapon(int(self.WeaponEditLine.GetText()))
		chr.SetArmor(int(self.ArmorEditLine.GetText()))
		if self.FakeName:
			chr.SetNameString(str(self.NameEditLine.GetText()))
		if self.GMEffect:
			chrmgr.SetAffect(-1,0,1)	
		chat.AppendChat(7, "[m2k-Mod] Please Equip an item to refresh the game and make the effect visible")
		chat.AppendChat(7, "[m2k-Mod] Than click again on ChangeEQ-Button for the other effects")		
		
	def UpdateWeapon(self, index):
		self.WeaponEditLine.SetText(str(index))
		item.SelectItem(int(index))
		self.WeaponImage.LoadImage(str(item.GetIconImageFileName()))
		if item.GetItemSize()[1] == 1:
			self.WeaponImage.SetPosition(20,73)
		elif item.GetItemSize()[1] == 2:
			self.WeaponImage.SetPosition(20,59)
			
	def UpdateArmor(self, index):
		self.ArmorEditLine.SetText(str(index))
		self.ArmorImage.LoadImage(str(item.GetIconImageFileName(item.SelectItem(int(index)))))
	
	def Weapon(self):
		self.ItemListDialog = ItemListDialog(self, "Weapon-List")
	def Armor(self):
		self.ItemListDialog = ItemListDialog(self, "Armor-List")	
	
		
class ItemListDialog(ui.Window):

	def __init__(self, parentUI, nameUI):
		ui.Window.__init__(self)
		self.CreateItemDialog = parentUI
		self.Mode = nameUI
		self.Board = ui.BoardWithTitleBar()
		self.Board.SetSize(200, 335)
		self.Board.SetPosition(252, 40)
		self.Board.SetTitleName(nameUI)
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
			dbg.LogBox("Load Itemlist Error, you have so set the IDs manually")
			self.Close()
		for line in lines:
			tokens = str(line).split("\t")
			Index = str(tokens[0])
			Itemname = item.GetItemName(item.SelectItem(int(Index)))
			ItemType = item.GetItemType(item.SelectItem(int(Index)))
			if mode == 1:
				if Index and self.Mode == "Weapon-List" and ItemType == item.ITEM_TYPE_WEAPON:
					self.fileListBox.AppendItem(m2k_lib.Item(Index +"  " + Itemname))
				elif Index and self.Mode == "Armor-List" and ItemType == item.ITEM_TYPE_ARMOR:
					self.fileListBox.AppendItem(m2k_lib.Item(Index +"  " + Itemname))
			elif mode == 2:
				if str(Itemname).find(str(SearchName)) != -1 and self.Mode == "Weapon-List":
					if ItemType == item.ITEM_TYPE_WEAPON:
						self.fileListBox.AppendItem(m2k_lib.Item(Index +"  " + Itemname))
					else:
						chat.AppendChat(7, "[m2k-Mod] " + SearchName + " is not from type Weapon")
					break
				elif str(Itemname).find(str(SearchName)) != -1 and self.Mode == "Armor-List":
					if ItemType == item.ITEM_TYPE_ARMOR:
						self.fileListBox.AppendItem(m2k_lib.Item(Index +"  " + Itemname))
					else:
						chat.AppendChat(7, "[m2k-Mod] " + SearchName + " is not from type Armor")
					break
			elif mode == 3:
				if str(Itemname) == str(SelectedIndex.GetText().split("  ")[1]):
					ItemValue = Index.split("  ")[0]
					if self.Mode == "Weapon-List" and ItemType == item.ITEM_TYPE_WEAPON:
						self.CreateItemDialog.UpdateWeapon(int(ItemValue))
					elif self.Mode == "Armor-List" and ItemType == item.ITEM_TYPE_ARMOR:
						self.CreateItemDialog.UpdateArmor(int(ItemValue))
					self.Close()
					break

	def __RefreshFileList(self):
		self.fileListBox.RemoveAllItems()
#EQChangerItemDialog().Show()