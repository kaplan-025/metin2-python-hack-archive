import ui,app,chat,chr,net,player,item,skill,time,game,shop,chrmgr
from m2kmod.Modules import m2k_lib
import background,wndMgr,math

class BookReaderDialog(ui.ScriptWindow):

	Books = {
	"Warrior" : [[50401, 50402, 50403, 50404, 50405, 50406], [50416, 50417, 50418, 50419, 50420, 50421]], 
	"Assassin" : [[50431, 50432, 50433, 50434, 50435, 50436], [50446, 50447, 50448, 50449, 50450, 50451]],
	"Sura" : [[50461, 50462, 50463, 50464, 50465, 50466], [50476, 50477, 50478, 50479, 50450, 50451]],
	"Shaman" : [[50491, 50492, 50493, 50494, 50495, 50496], [50506, 50507, 50508, 50509,50510, 505011]],
	}
	State = "Stop"	
	TimeStamp = 0
	Konzi = 1
	Reading = 0
	SkillCount = 0
	BannedSlotIndex = []
	
	def __init__(self):
		self.Board = ui.ThinBoard()
		self.Board.SetSize(218, 250)
		self.Board.SetPosition(52, 40)
	#	self.Board.AddFlag("movable")
		self.Board.Hide()
		
		self.comp = m2k_lib.Component()
		self.Header = self.comp.TextLine(self.Board, 'Skill-Book Reader', 55, 8, self.comp.RGB(255, 255, 0))
		self.Bar, self.fileListBox = self.comp.ReadingListBox(self.Board, 18, 40, 160, 135, 10)
		self.SkillIdNameLabel = self.comp.TextLine(self.Board, 'Skill:    ID:         Name:', 20, 37, self.comp.RGB(255, 255, 255))
		self.KonziImage = self.comp.ExpandedImage(self.Board, 45, 190, "icon/item/71094.tga")
		self.Close = self.comp.Button(self.Board, '', 'Close', 183, 8, self.Board.Hide, 'd:/ymir work/ui/public/close_button_01.sub', 'd:/ymir work/ui/public/close_button_02.sub', 'd:/ymir work/ui/public/close_button_03.sub')
		self.ReadOn = self.comp.Button(self.Board, '', '', 120, 185, self.SetReadingStatus, 'm2kmod\Images\start_0.tga', 'm2kmod\Images\start_1.tga', 'm2kmod\Images\start_2.tga')
		self.ReadOff = self.comp.HideButton(self.Board, '', '', 120, 185, self.SetReadingStatus, 'm2kmod\Images\stop_0.tga', 'm2kmod\Images\stop_1.tga', 'm2kmod\Images\stop_2.tga')
		self.KonziOn = self.comp.Button(self.Board, '', '', 70, 190, self.SetKonziStatus, 'm2kmod/Images/on_0.tga', 'm2kmod/Images/on_1.tga', 'm2kmod/mages/on_2.tga')
		self.KonziOff = self.comp.HideButton(self.Board, '', '', 70, 190, self.SetKonziStatus, 'm2kmod/Images/off_0.tga', 'm2kmod/Images/off_1.tga', 'm2kmod/Images/off_2.tga')
		
		
		
	#	self.AddItems()
	#	self.UpdateReading()
		
	def switch_state(self):
		if self.Board.IsShow():
			self.Board.Hide()
		else:
			self.Board.Show()
			self.AddItems()
			self.UpdateReading()
			self.ExoID = int(m2k_lib.ReadConfig("Exorcism-Scroll"))
			self.KonziID = int(m2k_lib.ReadConfig("Concentrated"))	
		
	def AddItems(self):
		self.fileListBox.RemoveAllItems()
		RaceGroupInfo = m2k_lib.GetClass()
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

		for i in xrange(m2k_lib.NewSkillsEnable()):
			Skillname = skill.GetSkillName(self.SkillIndex)
			RaceGroupInfo = m2k_lib.GetClass().split("/")
			ID = self.Books[RaceGroupInfo[0]][int(RaceGroupInfo[1]) - 1][i]
			if str(Skillname) != "None":
				self.fileListBox.AppendItem(m2k_lib.Item(str(self.SkillIndex) + "      " + str(ID) + "      " + str(Skillname)))
				self.SkillIndex += 1
		
	def SetReadingStatus(self):
		if self.Reading:
			self.BreakReading() 	
		else:
			self.Reading = 1
			self.ReadOn.Hide()
			self.ReadOff.Show()	
			self.StartReading()
			
	def SetKonziStatus(self):
		if self.Konzi:
			self.Konzi = 0
			chat.AppendChat(1, "[m2k-Mod] Concentrated Reading wont be used!")
			self.KonziOn.Hide()
			self.KonziOff.Show()	
		else:
			self.Konzi = 1
			chat.AppendChat(1, "[m2k-Mod] Concentrated Reading will be used!")
			self.KonziOff.Hide()
			self.KonziOn.Show()	
		
		
	def StartReading(self):
		ItemIndex = self.fileListBox.GetSelectedItem()
		if ItemIndex:
			pass
		else:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "[m2k-Mod] No Item selected!")
			self.BreakReading()	
			return
		self.SkillBook = ItemIndex.GetText().split("      ")
		
		RaceGroupInfo = m2k_lib.GetClass().split("/")
		self.SkillCount = self.Books[RaceGroupInfo[0]][int(RaceGroupInfo[1]) - 1].index(int(self.SkillBook[1])) + 1
		
	def BreakReading(self):
		self.Reading = 0
		self.ReadOn.Show()
		self.ReadOff.Hide()

	def UpdateReading(self):
		if self.Reading:
			if self.IsReadAble(self.SkillCount) and player.GetStatus(player.EXP) > 20000:
				self.ReadBooks()
			else:
				chat.AppendChat(1, "[m2k-Mod] This Skill doesnt have the level which is needed to read or no EXP")
				self.BreakReading()
				return
		
		self.UpdateReadingDialog = m2k_lib.WaitingDialog()
		self.UpdateReadingDialog.Open(0.5)
		self.UpdateReadingDialog.SAFE_SetTimeOverEvent(self.UpdateReading)

	def ReadBooks(self):
		if (player.GetItemCountByVnum(50300) == 0 and player.GetItemCountByVnum(int(self.SkillBook[1])) == 0):
			result = 0
			chat.AppendChat(1, "[m2k-Mod] No Skillbooks for the selected skill in the inventory!")
			if shop.IsOpen():
				for EachShopSlot in xrange(shop.SHOP_SLOT_COUNT):
					ShopItemValue = shop.GetItemID(EachShopSlot)
					if ShopItemValue == int(self.SkillBook[1]):
						net.SendShopBuyPacket(EachShopSlot)
						self.BannedSlotIndex = []
						result = 1
						break
			else:
				chat.AppendChat(1, "[m2k-Mod] No Book-Shop is open for buying skillbooks!")
				self.BreakReading()
				return
			if result == 0:
				chat.AppendChat(1, "[m2k-Mod] Failed to buy book from Book-Shop")
				self.BreakReading()
				return
	
		for Slot in xrange(player.INVENTORY_PAGE_SIZE*2):
			ItemValue = player.GetItemIndex(Slot)
			if ItemValue == 50300:
				chat.AppendChat(1, "debug1")
				metinSlot = [player.GetItemMetinSocket(Slot, i) for i in xrange(player.METIN_SOCKET_MAX_NUM)]
				if metinSlot[0] == int(self.SkillBook[0]):
					net.SendItemUsePacket(Slot)
			if ItemValue == int(self.SkillBook[1]):
				net.SendItemUsePacket(Slot)
		Exo = 0
		Konz = 0
	
		for Slot in xrange(player.INVENTORY_PAGE_SIZE*2):
			ItemValue = player.GetItemIndex(Slot)
			if ItemValue == self.ExoID and Exo == 0:
				net.SendItemUsePacket(Slot)
				Exo = 1
			if ItemValue == self.KonziID and Konz == 0:
				net.SendItemUsePacket(Slot)
				Konz = 1
			if Konz == 1 and Exo == 1:
				break
	
		if Exo == 0:
			chat.AppendChat(1, "[m2k-Mod] You dont have Exorcism scrolls in your Inventory!")
			self.BreakReading()	
			return
		if Konz == 0 and self.Konzi:
			chat.AppendChat(1, " [m2k-Mod]You have no Concentrated Readings in your inventory!")
			self.BreakReading()	
			return
	
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
				
		
#BookReaderDialog().Show()
		
