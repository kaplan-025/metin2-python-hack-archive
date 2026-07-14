import ui,app,chat,chr,net,player,item,skill,time,game,shop,chrmgr
from m2kmod.Modules import m2k_lib
import background,wndMgr,math

class TauAutobuyDialog(ui.ScriptWindow):

	Taus = [50821, 50822, 50823, 50824, 50825, 50826]
	PotionValue = [100, 5]
	State = 0
	
	def __init__(self):
		self.Board = ui.ThinBoard()
		self.Board.SetSize(200, 250)
		self.Board.SetPosition(52, 40)
		self.Board.AddFlag("movable")
		self.Board.Hide()
		
		self.comp = m2k_lib.Component()
		self.Header = self.comp.TextLine(self.Board, 'Potion-Buyer', 75, 8, self.comp.RGB(255, 255, 0))
		self.MinimumLabel = self.comp.TextLine(self.Board, 'Minimum Value:', 70, 60, self.comp.RGB(153, 178, 255))
		self.DurationLabel = self.comp.TextLine(self.Board, 'Duration:', 82, 110, self.comp.RGB(153, 178, 255))
		self.Value = self.comp.TextLine(self.Board, '+ 100', 85, 88, self.comp.RGB(255, 255, 255))
		self.Duration =self.comp.TextLine(self.Board, '10 Min.', 87, 138, self.comp.RGB(255, 255, 255))
		
		self.SlidbarValue = self.comp.SliderBar(self.Board, 0.5, self.SetConfig, 12, 75)
		self.SlidebarTime = self.comp.SliderBar(self.Board, 0.33, self.SetConfig, 12, 125)
		self.TauCombo = self.comp.ComboBox(self.Board, '<choose potion>', 35, 30, 135)

		self.Close = self.comp.Button(self.Board, '', 'Close', 183, 8, self.Board.Hide, 'd:/ymir work/ui/public/close_button_01.sub', 'd:/ymir work/ui/public/close_button_02.sub', 'd:/ymir work/ui/public/close_button_03.sub')
		self.BuyOn = self.comp.Button(self.Board, '', '', 80, 170, self.SetPotionStatus, 'm2kmod\Images\start_0.tga', 'm2kmod\Images\start_1.tga', 'm2kmod\Images\start_2.tga')
		self.BuyOff = self.comp.HideButton(self.Board, '', '', 80, 170, self.SetPotionStatus, 'm2kmod\Images\stop_0.tga', 'm2kmod\Images\stop_1.tga', 'm2kmod\Images\stop_2.tga')
		
		if player.GetName() != "":
			for Tau in self.Taus:
				self.TauCombo.InsertItem(1,str(Tau) + "  " + str(item.GetItemName(item.SelectItem(Tau))))
		
	def switch_state(self):
		if self.Board.IsShow():
			self.Board.Hide()
		else:
			self.Board.Show()
			
	
	def SetConfig(self):
		Value, Time = self.PotionValue
		MinValue = int(self.SlidbarValue.GetSliderPos() * 200)
		MinTime = int(self.SlidebarTime.GetSliderPos() * 30)
		if MinValue != Value:
			self.Value.SetText("+ " + str(MinValue))
		if MinTime != Time:
			self.Duration.SetText(str(MinTime) + " Min.")
			
		self.PotionValue = [MinValue, MinTime]
	
	def SetPotionStatus(self):
		if not shop.IsOpen():
			chat.AppendChat(7, "[m2k-Mod] Please open a Shop first!")
			return
		ItemIndex = self.TauCombo.GetCurrentText()
		if ItemIndex == "<choose potion>":
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Please select an Item!")
			return
		if self.State:
			self.StopBuying()
		else:
			self.State = 1
			self.Spam = 0
			self.BuyOn.Hide()
			self.BuyOff.Show()
			self.StartBuying()
	

	def StartBuying(self):
		SelectedIndex = self.TauCombo.GetCurrentText()
		MinValue, MinTime = self.PotionValue
		MinTime = MinTime * 60
		PotionValue = int(SelectedIndex.split("  ")[0])
		
		for InventorySlot in xrange(player.INVENTORY_PAGE_SIZE*2):
			ItemIndex = player.GetItemIndex(InventorySlot)
			if PotionValue == ItemIndex:
				Value0, Value , Time = [player.GetItemMetinSocket(InventorySlot, i) for i in xrange(player.METIN_SOCKET_MAX_NUM)]
				if Value >= MinValue and Time >= MinTime:
					self.StopBuying()
					return
				else:
					net.SendShopSellPacket(InventorySlot)
		Slot = 0
		if shop.IsOpen():
			for EachShopSlot in xrange(shop.SHOP_SLOT_COUNT):
				ShopItemValue = shop.GetItemID(EachShopSlot)
				if ShopItemValue == int(PotionValue):
					Slot = EachShopSlot
					break
		else:
			chat.AppendChat(7, "[m2k-Mod] No Shop is open!")
			self.StopBuying()
			return
			
		if Slot != 0 and shop.IsOpen():	
			net.SendShopBuyPacket(Slot)
		else:
			chat.AppendChat(7, "[m2k-Mod] Cant find " + SelectedIndex.split("  ")[1] + " in shop!")
			self.StopBuying()
			return
		
		self.UpdateBuying = m2k_lib.WaitingDialog()			
		self.UpdateBuying.Open(1.0)
		self.UpdateBuying.SAFE_SetTimeOverEvent(self.StartBuying)
	
	def StopBuying(self):
		self.State = 0
		self.BuyOff.Hide()
		self.BuyOn.Show()
		self.UpdateBuying = m2k_lib.WaitingDialog()	
		self.UpdateBuying.Close()
						
#TauAutobuyDialog().Show()