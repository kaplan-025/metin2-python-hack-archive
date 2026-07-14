import ui,app,chat,chr,net,player,item,skill,time,game,shop,chrmgr
import background,constInfo,wndMgr,math,uiCommon,grp,dbg,m2k_lib

class InventoryDialog(ui.ScriptWindow):

	def __init__(self):
		self.Board = ui.ThinBoard()
		self.Board.SetSize(210, 390)
		self.Board.SetPosition(52, 40)
		self.Board.Hide()
		
		self.comp = m2k_lib.Component()
		self.Header = self.comp.TextLine(self.Board, 'Inventory Manager', 61, 8, self.comp.RGB(255, 255, 0))
		self.ListBoxLabel = self.comp.TextLine(self.Board, ' Slot:	 ID:			Name:', 8, 33, self.comp.RGB(0, 229, 650))
		self.UpgradeLabel = self.comp.TextLine(self.Board, 'Upgrade			x', 70, 308, self.comp.RGB(255, 255, 255))
		
		self.Close = self.comp.Button(self.Board, '', 'Close', 188, 7, self.Board.Hide, 'd:/ymir work/ui/public/close_button_01.sub', 'd:/ymir work/ui/public/close_button_02.sub', 'd:/ymir work/ui/public/close_button_03.sub')
		self.Refresh = self.comp.Button(self.Board, '', 'Refresh', 163, 6, self.UpdateFileList, 'd:/ymir work/ui/game/guild/refresh_button_01.sub', 'd:/ymir work/ui/game/guild/refresh_button_02.sub', 'd:/ymir work/ui/game/guild/refresh_button_03.sub')
		self.UpgradeButton = self.comp.Button(self.Board, 'Upgrade', '', 110, 280, self.Upgrade, 'd:/ymir work/ui/public/Large_button_01.sub', 'd:/ymir work/ui/public/Large_button_02.sub','d:/ymir work/ui/public/Large_button_03.sub')
		self.DropSelectedButton = self.comp.Button(self.Board, 'Drop Selected', 'Drops all same Items like the selected one', 15, 333, self.DropItem, 'd:/ymir work/ui/public/Large_button_01.sub', 'd:/ymir work/ui/public/Large_button_02.sub','d:/ymir work/ui/public/Large_button_03.sub')
		self.DropAllButton = self.comp.Button(self.Board, 'Drop All', 'Drops ALL Items in your Inventory', 110, 333, self.DropAllItemsRequest, 'd:/ymir work/ui/public/Large_button_01.sub', 'd:/ymir work/ui/public/Large_button_02.sub','d:/ymir work/ui/public/Large_button_03.sub')
		self.SellSelectedButton = self.comp.Button(self.Board, 'Sell Selected', 'Sells all same Items like the selected one', 15, 358, self.SellItem, 'd:/ymir work/ui/public/Large_button_01.sub', 'd:/ymir work/ui/public/Large_button_02.sub','d:/ymir work/ui/public/Large_button_03.sub')
		self.SellAllButton = self.comp.Button(self.Board, 'Sell All', 'Sells ALL Items in your Inventory', 110, 358, self.SellAllItemsRequest, 'd:/ymir work/ui/public/Large_button_01.sub', 'd:/ymir work/ui/public/Large_button_02.sub','d:/ymir work/ui/public/Large_button_03.sub')
		self.UpgradeSlotbar, self.UpgradeEditline = self.comp.EditLine(self.Board, '1', 112, 307, 15, 18, 1)
		self.BarItems, self.ListBoxItems, ScrollItems = self.comp.ListBoxEx(self.Board, 10, 50, 170, 220)
		self.ModeCombo = self.comp.ComboBox(self.Board, 'Normal', 20, 282, 70)
		UppModes = ['Normal', 'DT', 'Guild', 'Bless', 'Metal', 'Normal - All']
		for Mode in UppModes:
			self.ModeCombo.InsertItem(0, Mode)
		self.UpgradeEditline.SetNumberMode()
		
		self.SegiID = int(m2k_lib.ReadConfig("Blessing-Scroll"))
		self.MetalID = int(m2k_lib.ReadConfig("Magic-Stone"))
		
		self.UpdateFileList()
		
	def switch_state(self):
		if self.Board.IsShow():
			self.Board.Hide()
		else:
			self.Board.Show()
			self.UpdateFileList()

		
	def UpdateFileList(self):
		self.ListBoxItems.RemoveAllItems()
		for i in xrange(100):
			ItemIndex = player.GetItemIndex(i)
			if ItemIndex != 0:
				ItemName = item.GetItemName(item.SelectItem(int(ItemIndex)))
				self.ListBoxItems.AppendItem(m2k_lib.Item(str(i) + '    ' + str(player.GetItemIndex(i)) + '    ' + ItemName))
				
	def Upgrade(self):
		ItemIndex = self.ListBoxItems.GetSelectedItem()
		if ItemIndex:
			pass
		else:
			chat.AppendChat(7, "[m2k-Mod] No Item selected!")
			return
		try:
			SearchedName = ItemIndex.GetText().split("    ")[2].split("+")[0]
		except:
			SearchedName = ItemIndex.GetText().split("    ")[2]
		
		SelectedItem = ItemIndex.GetText().split("    ")
		count = int(self.UpgradeEditline.GetText())
	
		if self.ModeCombo.GetCurrentText() == 'Normal':
			self.UpgradeItem(1,int(SelectedItem[0]), int(count))
		elif self.ModeCombo.GetCurrentText() == 'DT':
			self.UpgradeItem(2,int(SelectedItem[0]), int(count))
		elif self.ModeCombo.GetCurrentText() == 'Guild':
			self.UpgradeItem(3,int(SelectedItem[0]), int(count))
		elif self.ModeCombo.GetCurrentText() == 'Bless':
			self.UpgradeItem(4,int(SelectedItem[0]), int(count))
		elif self.ModeCombo.GetCurrentText() == 'Normal - All':
			for j in xrange(0, 90):
				ItemValue = player.GetItemIndex(j)
				try:
					ItemName = item.GetItemName(item.SelectItem(ItemValue)).split("+")[0]
				except:
					ItemName = item.GetItemName(item.SelectItem(ItemValue))
				if ItemName == SearchedName:
					self.UpgradeItem(1, j, int(count))
		elif self.ModeCombo.GetCurrentText() == 'Metal':
			self.UpgradeItem(5,int(SelectedItem[0]), int(count))
	
	def UpgradeItem(self, Mode, Slot, Count):
		self.BannedSlotIndex = []
		for i in xrange(Count):
			if Mode == 1:
				net.SendRefinePacket(Slot, 0)
			elif Mode == 2:
				net.SendRefinePacket(Slot, 4)
			elif Mode == 3:
				net.SendRefinePacket(Slot, 1)
			elif Mode == 4 or Mode == 5:
				for InventorySlot in xrange(player.INVENTORY_PAGE_SIZE*2):
					ItemValue = player.GetItemIndex(InventorySlot)
					if Mode == 4:
						if ItemValue == self.SegiID and not InventorySlot in self.BannedSlotIndex:
							self.BannedSlotIndex.append(InventorySlot)
							net.SendItemUseToItemPacket(InventorySlot, Slot)
							net.SendRefinePacket(Slot, 2)
							break
					elif Mode == 5:	
						if ItemValue == self.MetalID and not InventorySlot in self.BannedSlotIndex:
							self.BannedSlotIndex.append(InventorySlot)
							net.SendItemUseToItemPacket(InventorySlot, Slot)
							net.SendRefinePacket(Slot, 2)
							break
		self.UpdateFileList()
						
	def SellItem(self):
		if not shop.IsOpen():
			chat.AppendChat(7, "[m2k-Mod] You need an open Shop for that!")
			return
		ItemIndex = self.ListBoxItems.GetSelectedItem()
		if ItemIndex:
			pass
		else:
			chat.AppendChat(7, "[m2k-Mod] No selctd Items!")
			return
		SelectedItem = ItemIndex.GetText().split("    ")	
		net.SendShopSellPacket(int(SelectedItem[0]))
		self.UpdateFileList()
		
	def DropItem(self):
		ItemIndex = self.ListBoxItems.GetSelectedItem()
		if ItemIndex:
			pass
		else:
			chat.AppendChat(7, "[m2k-Mod] No selctd Items!")
			return
		SelectedItem = ItemIndex.GetText().split("    ")	
		net.SendItemDropPacket(int(SelectedItem[0]))
		self.UpdateFileList()

	def SellAllItemsRequest(self):
		if not shop.IsOpen():
			chat.AppendChat(7, "[m2k-Mod] You need an open Shop for that!")
			return 
		self.QuestionDialog = uiCommon.QuestionDialog()
		self.QuestionDialog.SetText("Do you want so sell All your Items?")
		self.QuestionDialog.SetAcceptEvent(ui.__mem_func__(self.SellAll))
		self.QuestionDialog.SetCancelEvent(ui.__mem_func__(self.CancelQuestionDialog))
		self.QuestionDialog.Open()
	def SellAll(self):
		for i in xrange(90):
			net.SendShopSellPacket(i)
		self.CancelQuestionDialog()
		self.UpdateFileList()
		
	def DropAllItemsRequest(self):
		self.QuestionDialog = uiCommon.QuestionDialog()
		self.QuestionDialog.SetText("Do you want to drop ALL your Items?")
		self.QuestionDialog.SetAcceptEvent(ui.__mem_func__(self.DropAll))
		self.QuestionDialog.SetCancelEvent(ui.__mem_func__(self.CancelQuestionDialog))
		self.QuestionDialog.Open()
	def DropAll(self):
		for i in xrange(90):
			net.SendItemDropPacket(i)
		self.CancelQuestionDialog()
		self.UpdateFileList()
		
	def CancelQuestionDialog(self):
		self.QuestionDialog.Close()
		self.QuestionDialog = None


	
