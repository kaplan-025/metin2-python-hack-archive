import ui,app,chat,chr,net,player,item,skill,time,game,shop,chrmgr,event
from m2kmod.Modules import m2k_lib
import background,wndMgr,math

class SoulStoneBotDialog(ui.ScriptWindow):

	Zen = 1
	Reading = 0
	SkillCount = 0
	BannedSlotIndex = []
	
	def __init__(self):
		self.Board = ui.ThinBoard()
		self.Board.SetSize(218, 290)
		self.Board.SetPosition(52, 40)
	#	self.Board.AddFlag("movable")
		self.Board.Hide()
		
		self.comp = m2k_lib.Component()
		self.Header = self.comp.TextLine(self.Board, 'Soul-Stone Reader', 55, 8, self.comp.RGB(255, 255, 0))
		self.ConfirmStringLabel = self.comp.TextLine(self.Board, 'Confirm-String:', 100, 178, self.comp.RGB(255, 255, 0))
		self.Bar, self.fileListBox = self.comp.ReadingListBox(self.Board, 18, 40, 160, 135, 10)
		self.SkillIdNameLabel = self.comp.TextLine(self.Board, 'Skill:    ID:         Name:', 20, 37, self.comp.RGB(255, 255, 255))
		self.ZenImage = self.comp.ExpandedImage(self.Board, 25, 185, "icon/item/70102.tga")
		self.Close = self.comp.Button(self.Board, '', 'Close', 183, 8, self.Board.Hide, 'd:/ymir work/ui/public/close_button_01.sub', 'd:/ymir work/ui/public/close_button_02.sub', 'd:/ymir work/ui/public/close_button_03.sub')
		self.ReadOn = self.comp.Button(self.Board, '', '', 95, 225, self.SetReadingStatus, 'm2kmod\Images\start_0.tga', 'm2kmod\Images\start_1.tga', 'm2kmod\Images\start_2.tga')
		self.ReadOff = self.comp.HideButton(self.Board, '', '', 95, 225, self.SetReadingStatus, 'm2kmod\Images\stop_0.tga', 'm2kmod\Images\stop_1.tga', 'm2kmod\Images\stop_2.tga')
		self.ZenOn = self.comp.Button(self.Board, '', '', 57, 200, self.SetZenStatus, 'm2kmod/Images/on_0.tga', 'm2kmod/Images/on_1.tga', 'm2kmod/mages/on_2.tga')
		self.ZenOff = self.comp.HideButton(self.Board, '', '', 57, 200, self.SetZenStatus, 'm2kmod/Images/off_0.tga', 'm2kmod/Images/off_1.tga', 'm2kmod/Images/off_2.tga')
		self.StringSlotbar, self.StringEditline = self.comp.EditLine(self.Board, '', 100, 195, 87, 18, 10)
		
		
		
		
	def switch_state(self):
		if self.Board.IsShow():
			self.Board.Hide()
			self.UnHookQuestWindow()
		else:
			self.Board.Show()
			self.AddItems()
			self.UpdateReading()
			self.InstallQuestWindowHook()
			self.ZenID = int(m2k_lib.ReadConfig("Zen-Bean"))
			self.SoulStoneID = int(m2k_lib.ReadConfig("Soul-Stone"))
			self.ExoID = int(m2k_lib.ReadConfig("Exorcism-Scroll"))
		
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
				
		for Count in xrange(m2k_lib.NewSkillsEnable()):
			Skillname = skill.GetSkillName(self.SkillIndex)
			Count += 1
			RaceGroupInfo = m2k_lib.GetClass().split("/")
			if str(Skillname) != "None":
				self.fileListBox.AppendItem(m2k_lib.Item(str(self.SkillIndex) + "      " + str(Count) + "      " + str(Skillname)))
				self.SkillIndex += 1
		
	def SetReadingStatus(self):
		if self.Reading:
			self.BreakReading() 	
		else:
			self.Reading = 1
			self.ReadOn.Hide()
			self.ReadOff.Show()	
			self.StartReading()
			
	def SetZenStatus(self):
		if self.Zen:
			self.Zen = 0
			chat.AppendChat(7, "[m2k-Mod] Zen Beans wont be used!")
			self.ZenOn.Hide()
			self.ZenOff.Show()	
		else:
			self.Zen = 1
			chat.AppendChat(7, "[m2k-Mod] Zen Beans will be used!")
			self.ZenOff.Hide()
			self.ZenOn.Show()	
		
			
	def StartReading(self):
		ItemIndex = self.fileListBox.GetSelectedItem()
		if ItemIndex:
			pass
		else:
			chat.AppendChat(7, "[m2k-Mod] No Skill selected!")
			return
		self.SkillBook = ItemIndex.GetText().split("      ")
		
	def BreakReading(self):
		self.Reading = 0
		self.ReadOn.Show()
		self.ReadOff.Hide()
		
	def UpdateReading(self):
		if self.Reading:
			if self.IsReadAble(int(self.SkillBook[1]), 0):
				self.ReadStones(self.CheckIndex(int(self.SkillBook[1])))
			else:
				chat.AppendChat(7, "[m2k-Mod] This Skill doesnt have the level which is needed to read!")
				self.BreakReading()
		
		self.UpdateReadingDialog = m2k_lib.WaitingDialog()
		self.UpdateReadingDialog.Open(0.5)
		self.UpdateReadingDialog.SAFE_SetTimeOverEvent(self.UpdateReading)

	def ReadStones(self, SkillIndex):
		if player.GetItemCountByVnum(self.SoulStoneID) == 0: 
			result = 0
			chat.AppendChat(7, "[m2k-Mod] Some Items for reading soulstones are missing!")
			if shop.IsOpen():
				for EachShopSlot in xrange(shop.SHOP_SLOT_COUNT):
					ShopItemValue = shop.GetItemID(EachShopSlot)
					if ShopItemValue == self.SoulStoneID:
						net.SendShopBuyPacket(EachShopSlot)
						result = 1
						break
			else:
				chat.AppendChat(7, "[m2k-Mod] No Shop is open for buying a Soul Stone!")
				self.BreakReading()
				return
			if result == 0:
				chat.AppendChat(1, "[m2k-Mod] Failed to buy soulstone from Shop")
				self.BreakReading()
				return
				
		try:
			for Slot in xrange(player.INVENTORY_PAGE_SIZE*2):
				ItemValue = player.GetItemIndex(Slot)
				if ItemValue == self.ExoID:
					net.SendItemUsePacket(Slot)
					break
		except:
			chat.AppendChat(7, "[m2k-Mod] You dont have Exorcism scrolls in your Inventory!")
			self.BreakReading()
			return

		for Slot in xrange(player.INVENTORY_PAGE_SIZE*2):
			ItemValue = player.GetItemIndex(Slot)
			if ItemValue == self.SoulStoneID:
				net.SendItemUsePacket(Slot)
				if self.GetNeededAlignment():
					self.ReadQuest(SkillIndex)
				break
	
	def ReadQuest(self, index):
		event.SelectAnswer(1, 254)
		event.SelectAnswer(1, 0)
		event.SelectAnswer(1, int(index))
		event.SelectAnswer(1, 0)
		net.SendQuestInputStringPacket(self.StringEditline.GetText())		
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
	
	def GetNeededAlignment(self):
		point, grade = player.GetAlignmentData()
		SkillLevel = self.IsReadAble(int(self.SkillBook[1]), 1)
		NeedAlignment = 1000+500*(SkillLevel-30)
		if point < 0:
			NeedAlignment = NeedAlignment * 2
		
		if point - NeedAlignment <= -20000:
			if not self.Zen:
				chat.AppendChat(1, "[m2k-Mod] You need more alignment than: " + str(point + NeedAlignment))
				self.BreakReading()
				return 0
			else:
				if player.GetItemCountByVnum(self.ZenID) == 0:
					chat.AppendChat(7, "[m2k-Mod] You dont have Zen-Beans!")
					self.BreakReading()
				round = -1 * point / 2000
				for Slot in xrange(player.INVENTORY_PAGE_SIZE*2):
					ItemValue = player.GetItemIndex(Slot)
					if ItemValue == self.ZenID:
						for i in xrange(round):
							net.SendItemUsePacket(Slot)
							break					
		return 1
		
	def CheckIndex(self, AskedSkill):
		self.ReadAbleSkillList = []
		for Count in xrange(m2k_lib.NewSkillsEnable()):
			if self.IsReadAble(Count, 0):
				self.ReadAbleSkillList.append(Count)
		return(str(self.ReadAbleSkillList.index(AskedSkill)))
			
	def InstallQuestWindowHook(self):
		self.OldRecv = game.GameWindow.OpenQuestWindow
		game.GameWindow.OpenQuestWindow = self.HookedQuestWindow
	
	def UnHookQuestWindow(self):
		game.GameWindow.OpenQuestWindow = self.OldRecv

	def HookedQuestWindow(self, skin, idx):
		pass	
		
#SoulStoneBotDialog().Show()
		
