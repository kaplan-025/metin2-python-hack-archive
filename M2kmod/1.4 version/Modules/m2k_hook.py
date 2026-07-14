import ui,chr,net,skill,game,chrmgr,playerSettingModule,emotion,player, uiParty, grp, dbg
from m2kmod.Modules.pyDetour import DetourFunction, DetourClass

	
def GetCurrentText(self):
	return self.textLine.GetText()
	
def OnSelectItem(self, index, name):
	self.SetCurrentItem(name)
	self.CloseListBox()
	
def GetSelectedIndex(self):
	return self.listBox.GetSelectedItem()
	
def HookedQuestWindow(data):
	pass
	

	
	
def PartyButton(self):
	dbg.LogBox("test")
	self.isShowStateButton = TRUE

	(x, y) = self.GetGlobalPosition()
	xPos = x + 110

	skillLevel = self.__GetPartySkillLevel()

	## Tanker
	if skillLevel >= 10:
		self.__AppendStateButton(xPos, y, player.PARTY_STATE_ATTACKER)
		xPos += 23

	## Attacker
	if skillLevel >= 20:
		self.__AppendStateButton(xPos, y, player.PARTY_STATE_BERSERKER)
		xPos += 23

	## Tanker
	if skillLevel >= 20:
		self.__AppendStateButton(xPos, y, player.PARTY_STATE_TANKER)
		xPos += 23

	# Buffer
	if skillLevel >= 25:
		self.__AppendStateButton(xPos, y, player.PARTY_STATE_BUFFER)
		xPos += 23

	## Skill Master
	if skillLevel >= 35:
		self.__AppendStateButton(xPos, y, player.PARTY_STATE_SKILL_MASTER)
		xPos += 23

	## Defender
	if skillLevel >= 40:
		self.__AppendStateButton(xPos, y, player.PARTY_STATE_DEFENDER)
		xPos += 23

	## Warp
	if skillLevel >= 35:
		if self.stateButtonDict.has_key(self.MEMBER_BUTTON_WARP):
			button = self.stateButtonDict[self.MEMBER_BUTTON_WARP]
			button.SetPosition(xPos, y)
			button.Show()
			xPos += 23

	## Expel
	if self.stateButtonDict.has_key(self.MEMBER_BUTTON_EXPEL):
		button = self.stateButtonDict[self.MEMBER_BUTTON_EXPEL]
		button.SetPosition(xPos, y)
		button.Show()
		xPos += 23
		

		
		
detour_questwindow = DetourFunction(game.GameWindow.OpenQuestWindow, HookedQuestWindow)

def SetComboHook():
	ui.ComboBox.GetCurrentText = GetCurrentText
	ui.ComboBox.GetSelectedIndex = GetSelectedIndex
	ui.ComboBox.OnSelectItem = OnSelectItem	
	
def SetQuestHook(arg):
	if arg:
		detour_questwindow.attach()
	else:
		detour_questwindow.detach()
			
def SetPartyWarpEnable():
	#oldPartyMemberInfoBoard = uiParty.PartyMemberInfoBoard
	#uiParty.PartyMemberInfoBoard = PartyMemberInfoBoard
	uiParty.PartyMemberInfoBoard.__ShowStateButton = PartyButton
	dbg.LogBox("test")
