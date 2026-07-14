import ui,app,chat,chr,net,player,item,skill,time,game,shop,chrmgr,m2k_lib
import background,constInfo,miniMap,uiminimap,wndMgr,math,uiCommon,grp

class SettingsDialog(ui.ScriptWindow): 				
	
	def __init__(self):
		self.Board = ui.ThinBoard() 
		self.Board.SetPosition(52, 40)
		self.Board.SetSize(300, 370) 
	#	self.Board.AddFlag("float") 
	#	self.Board.AddFlag("movable")
		self.Board.Hide()
		
		self.comp = m2k_lib.Component()
		self.HeaderLabel = self.comp.TextLine(self.Board, 'Settings', 130, 8, self.comp.RGB(255, 255, 0))
		self.SetIdLabel = self.comp.TextLine(self.Board, 'Set ID:', 130, 205, self.comp.RGB(255, 255, 0))
		self.InstructionsLabel0 = self.comp.TextLine(self.Board, 'm2kmod cannot find your item', 155, 225, self.comp.RGB(255, 255, 255))
		self.InstructionsLabel1 = self.comp.TextLine(self.Board, 'although its in the inventory?', 155, 240, self.comp.RGB(255, 255, 255))
		self.InstructionsLabel2 = self.comp.TextLine(self.Board, '1. Mark The Item in the List', 157, 270, self.comp.RGB(255, 255, 255))
		self.InstructionsLabel3 = self.comp.TextLine(self.Board, '2. Move this Item to the 1. Slot', 157, 290, self.comp.RGB(255, 255, 255))
		self.InstructionsLabel4 = self.comp.TextLine(self.Board, '3. Press <Replace ID> Button ', 157, 310, self.comp.RGB(255, 255, 255))
		self.MovespeedLabel = self.comp.TextLine(self.Board, '300', 256, 38, self.comp.RGB(255, 255, 255))
		self.AttackspeedLabel = self.comp.TextLine(self.Board, '200', 256, 78, self.comp.RGB(255, 255, 255))
		self.SlideMovespeed = self.comp.SliderBar(self.Board, 0.6, self.SlideMove, 66, 40)
		self.SlideAttackspeed = self.comp.SliderBar(self.Board, 0.4, self.SlideAttack, 66, 80)
		
		self.AttackSpeedButton = self.comp.Button(self.Board, '', 'Attack-Speed', 25, 30, self.SetAttackSpeed, 'm2kmod/Images/Shortcuts/attack_0.tga', 'm2kmod/Images/Shortcuts/attack_1.tga', 'm2kmod/Images/Shortcuts/attack_0.tga')
		self.MoveSpeedButton = self.comp.Button(self.Board, '', 'Move-Speed', 25, 70, self.SetMoveSpeed, 'm2kmod/Images/Shortcuts/move_0.tga', 'm2kmod/Images/Shortcuts/move_1.tga', 'm2kmod/Images/Shortcuts/move_0.tga')
		self.DayButton = self.comp.Button(self.Board, '', 'Day', 25, 120, self.SetDay, 'm2kmod/Images/General/sun_0.tga', 'm2kmod/Images/General/sun_1.tga', 'm2kmod/Images/General/sun_0.tga')
		self.NightButton = self.comp.Button(self.Board, '', 'Night', 90, 120, self.SetNight, 'm2kmod/Images/General/moon_0.tga', 'm2kmod/Images/General/moon_1.tga', 'm2kmod/Images/General/moon_0.tga')
		self.OneHandedButton = self.comp.Button(self.Board, '', 'One-Handed', 180, 120, self.SetOneHand, 'm2kmod/Images/General/onehand_0.tga', 'm2kmod/Images/General/onehand_1.tga', 'm2kmod/Images/General/onehand_0.tga')
		self.TwoHandedButton = self.comp.Button(self.Board, '', 'Two-Handed', 245, 120, self.SetTwoHand, 'm2kmod/Images/General/twohand_0.tga', 'm2kmod/Images/General/twohand_1.tga', 'm2kmod/Images/General/twohand_0.tga')
		
		self.CloseButton = self.comp.Button(self.Board, '', 'Close', 270, 8, self.Hide_UI, 'd:/ymir work/ui/public/close_button_01.sub', 'd:/ymir work/ui/public/close_button_02.sub', 'd:/ymir work/ui/public/close_button_03.sub')
		self.ReplaceIdButton = self.comp.Button(self.Board, 'Replace ID', '', 40, 330, self.ReplaceId, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub','d:/ymir work/ui/public/large_button_03.sub')
		self.BarItems, self.ListBoxItems, ScrollItems = self.comp.ListBoxEx2(self.Board, 25, 225, 100, 100)
		self.LangCombo = self.comp.ComboBoxFunc(self.Board, m2k_lib.ReadConfig("Language"), 182, 333, 70, self.ChatInfo)
		languages = ['German', 'English', 'Romanian', 'Turkish', 'Polish']
		for lang in languages:
			self.LangCombo.InsertItem(0, lang)
		
		self.MoveSpeed = int(m2k_lib.ReadConfig("MoveSpeed"))
		self.AttackSpeed = int(m2k_lib.ReadConfig("AttackSpeed"))	
		self.SlideMovespeed.SetSliderPos(self.MoveSpeed*0.002)
		self.SlideMove()
		self.SlideAttackspeed.SetSliderPos(self.AttackSpeed*0.0025)
		self.SlideAttack()
		
		self.UpdateFileList()
		
	def switch_state(self):
		if self.Board.IsShow():
			self.Hide_UI()
		else:
			self.Board.Show()
	
	def Hide_UI(self):
		m2k_lib.SaveConfig("MoveSpeed", str(self.MoveSpeed))
		m2k_lib.SaveConfig("AttackSpeed", str(self.AttackSpeed))
		m2k_lib.SaveConfig("Language", str(self.LangCombo.GetCurrentText()))
		self.Board.Hide()

	def SlideMove(self):
		self.MoveSpeed = int(self.SlideMovespeed.GetSliderPos()*500)
		self.MovespeedLabel.SetText(str(self.MoveSpeed) + '%')
	def SlideAttack(self):
		self.AttackSpeed = int(self.SlideAttackspeed.GetSliderPos()*400)
		self.AttackspeedLabel.SetText(str(self.AttackSpeed) + '%')
		
	def ChatInfo(self):
		chat.AppendChat(7, "[m2k-Mod] Please restart Client for changing language for the bonus names")
	
	def UpdateFileList(self):
		self.ListBoxItems.RemoveAllItems()
		ItemNames = ["Swich-Item", "Exorcism-Scroll", "Concentrated", "Soul-Stone", "Zen-Bean", "Blessing-Scroll", "Magic-Stone", "Red-Pot", "Blue-Pot", "AutoRed-Pot", "AutoBlue-Pot", "Bravery-Cape"]
		for name in ItemNames:	
			self.ListBoxItems.AppendItem(m2k_lib.Item(name + '    ' + str(m2k_lib.ReadConfig(name))))
	
	def ReplaceId(self):
		if player.GetItemIndex(0) != 0:
			SelectedItem = self.ListBoxItems.GetSelectedItem()
			if SelectedItem:
				pass
			else:
				chat.AppendChat(7, "[m2k-Mod] No Item selected!")
				return
			NewItemIndex = SelectedItem.GetText().split("    ")
			m2k_lib.SaveConfig(NewItemIndex[0],str(player.GetItemIndex(0)))
			chat.AppendChat(7, "[m2k-Mod] Saved new Item ID: " + str(player.GetItemIndex(0)) + " (" + item.GetItemName(item.SelectItem(player.GetItemIndex(0))) + ") for the Item:" + NewItemIndex[0])
			self.UpdateFileList()
		else:
			chat.AppendChat(7, "[m2k-Mod] Please move the Item to your first slot!")
			
	def SetMoveSpeed(self):
		self.MoveSpeed = int(m2k_lib.ReadConfig("MoveSpeed"))
		chr.SetMoveSpeed(self.MoveSpeed)
		chat.AppendChat(7, "[m2k-Mod] This function does not work on the most new pservers!")
	
	def SetAttackSpeed(self):
		self.AttackSpeed = int(m2k_lib.ReadConfig("AttackSpeed"))
		chr.SetAttackSpeed(self.AttackSpeed)
		chat.AppendChat(7, "[m2k-Mod] This function does not work on the most new pservers!")
		
	def SetDay(self): 
		background.SetEnvironmentData(0)
	
	def SetNight(self): 
		background.RegisterEnvironmentData(1, constInfo.ENVIRONMENT_NIGHT)
		background.SetEnvironmentData(1)
		
	def SetOneHand(self): 
		chr.SetMotionMode(chr.MOTION_MODE_ONEHAND_SWORD)

	def SetTwoHand(self): 
		chr.SetMotionMode(chr.MOTION_MODE_TWOHAND_SWORD)
		
	

#SettingsDialog().Show()
		