#Teleport-Hack module © musicinstructor, 2011
#Do not modify or distribute modified versions

import wndMgr
import ui
import ime
import net
import chat
import sys
import locale
import miniMap
import app
import player
import chr
import background

teleport_mode = 0
telestep = 0
saved_x = 0
saved_y = 0
visible = FALSE
last_teleport_time = 0
TeleportButton = ui.Button()
textLine = ui.TextLine()
chat.AppendChat(chat.CHAT_TYPE_INFO, "teleport-module loaded.")
miniMap.UnregisterAtlasWindow()

class MapTextToolTip(ui.Window):
	def __init__(self):			
		ui.Window.__init__(self)

		textLine = ui.TextLine()
		textLine.SetParent(self)
		textLine.SetHorizontalAlignCenter()
		textLine.SetOutline()
		textLine.SetHorizontalAlignRight()
		textLine.Show()
		self.textLine = textLine

	def __del__(self):			
		ui.Window.__del__(self)

	def SetText(self, text):
		self.textLine.SetText(text)

	def SetTooltipPosition(self, PosX, PosY):
		self.textLine.SetPosition(PosX - 5, PosY)

	def SetTextColor(self, TextColor):
		self.textLine.SetPackedFontColor(TextColor)

	def GetTextSize(self):
		return self.textLine.GetTextSize()


class TeleportHackDialog(ui.ScriptWindow):

	class AtlasRenderer(ui.Window):

		def __init__(self):
			ui.Window.__init__(self)
			self.AddFlag("not_pick")

		def OnUpdate(self):
			miniMap.UpdateAtlas()


		def OnRender(self):
			(x, y) = self.GetGlobalPosition()
			fx = float(x)
			fy = float(y)
			miniMap.RenderAtlas(fx, fy)
			global telestep
			global teleport_mode
			global saved_x
			global saved_y
			global last_teleport_time
			telestep = 0
			if teleport_mode == 1 and app.GetTime() > last_teleport_time + 5:
				last_teleport_time = app.GetTime()
				self.local_Teleport(saved_x, saved_y)

			if app.IsPressed(app.DIK_LSHIFT) == FALSE:
				self.new_teleport_possible = TRUE

			if app.IsPressed(app.DIK_LSHIFT) and self.new_teleport_possible == TRUE:
				self.new_teleport_possible = FALSE
				IsAtlasAvailable, height, width = miniMap.GetAtlasSize()
				if IsAtlasAvailable:
					xMouse, yMouse = wndMgr.GetMousePosition()
					#chat.AppendChat(chat.CHAT_TYPE_INFO, "height: " + str(height) + " width: " + str(width) + " xMouse: " + str(xMouse) + " yMouse: " + str(yMouse) + " x: " + str(x) + " y: " + str(y))
					if xMouse >= x and xMouse <= x + height and yMouse >= y and yMouse <= y + width:
						self.local_Teleport((xMouse-x)*6, (yMouse-y)*6)







		def local_Teleport(self, ltX, ltY):
			global telestep
			global teleport_mode
			global saved_x
			global saved_y
			teleport_mode = 1
			saved_x = ltX
			saved_y = ltY
			(ax, ay, az) = player.GetMainCharacterPosition()
			(mapName, xBase, yBase)=background.GlobalPositionToMapInfo(ax, ay)
			tX = int(ltX)*100+xBase
			tY = int(ltY)*100+yBase
			if int(tX) < int(ax):
				while int(tX) < int(ax):
					if telestep > 20:
						chat.AppendChat(chat.CHAT_TYPE_INFO, "continue teleport in 5 secounds to avoid packet-flooding kick")
						return

					chr.SetPixelPosition(int(ax) - 2000, int(ay), int(az))
					player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
					player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
					(ax, ay, az) = player.GetMainCharacterPosition()
					telestep = telestep + 1

				chr.SetPixelPosition(int(tX), int(ay), int(az))
				player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
				player.SetSingleDIKKeyState(app.DIK_UP, FALSE)

			if int(tX) > int(ax):
				while int(tX) > int(ax):
					if telestep > 20:
						chat.AppendChat(chat.CHAT_TYPE_INFO, "continue teleport in 5 secounds to avoid packet-flooding kick")
						return

					chr.SetPixelPosition(int(ax) + 2000, int(ay), int(az))
					player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
					player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
					(ax, ay, az) = player.GetMainCharacterPosition()
					telestep = telestep + 1

				chr.SetPixelPosition(int(tX), int(ay), int(az))
				player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
				player.SetSingleDIKKeyState(app.DIK_UP, FALSE)

			(ax, ay, az) = player.GetMainCharacterPosition()
			if int(tY) < int(ay):
				while int(tY) < int(ay):
					if telestep > 20:
						chat.AppendChat(chat.CHAT_TYPE_INFO, "continue teleport in 5 secounds to avoid packet-flooding kick")
						return

					chr.SetPixelPosition(int(ax), int(ay) - 2000, int(az))
					player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
					player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
					(ax, ay, az) = player.GetMainCharacterPosition()
					telestep = telestep + 1

				chr.SetPixelPosition(int(ax), int(tY), int(az))
				player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
				player.SetSingleDIKKeyState(app.DIK_UP, FALSE)

			if int(tY) > int(ay):
				while int(tY) > int(ay):
					if telestep > 20:
						chat.AppendChat(chat.CHAT_TYPE_INFO, "continue teleport in 5 secounds to avoid packet-flooding kick")
						return

					chr.SetPixelPosition(int(ax), int(ay) + 2000, int(az))
					player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
					player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
					(ax, ay, az) = player.GetMainCharacterPosition()
					telestep = telestep + 1

				chr.SetPixelPosition(int(ax), int(tY), int(az))
				player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
				player.SetSingleDIKKeyState(app.DIK_UP, FALSE)


			teleport_mode = 0





		def ShowAtlas(self):
			miniMap.ShowAtlas()

		def HideAtlas(self):
			miniMap.HideAtlas()

	def __init__(self):
		self.AtlasMainWindow = None
		self.tooltipInfo = MapTextToolTip()
		self.tooltipInfo.Hide()
		self.board = 0

		ui.ScriptWindow.__init__(self)

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "UIScript/AtlasWindow.py")
		except:
			import exception
			exception.Abort("AtlasWindow.LoadWindow.LoadScript")

		try:
			self.board = self.GetChild("board")
			self.board.SetTitleName("© musicinstructor [elitepvpers.de]")

		except:
			import exception
			exception.Abort("AtlasWindow.LoadWindow.BindObject")

		self.AtlasMainWindow = self.AtlasRenderer()
		self.board.SetCloseEvent(self.Hide)
		self.AtlasMainWindow.SetParent(self.board)
		self.AtlasMainWindow.SetPosition(7, 30)
		self.tooltipInfo.SetParent(self.board)
		self.SetCenterPosition()
		self.Hide()
		miniMap.RegisterAtlasWindow(self)
		global TeleportButton
		TeleportButton.SetText("")
		TeleportButton.SetPosition(wndMgr.GetScreenWidth()-100,160)
		TeleportButton.SetSize(88,21)
		TeleportButton.SetEvent(self.Show)
		TeleportButton.SetUpVisual("d:/ymir work/ui/public/large_button_01.sub")
		TeleportButton.SetOverVisual("d:/ymir work/ui/public/large_button_02.sub")
		TeleportButton.SetDownVisual("d:/ymir work/ui/public/large_button_03.sub")
		TeleportButton.Show()
		global textLine
		textLine.SetParent(TeleportButton)
		textLine.SetPosition(43,10)
		textLine.SetVerticalAlignCenter()
		textLine.SetHorizontalAlignCenter()
		textLine.SetText("Teleport")
		textLine.Show()

	def Destroy(self):
		miniMap.UnregisterAtlasWindow()
		self.ClearDictionary()
		self.AtlasMainWindow = None
		self.board = None
		self.tooltipInfo = None

	def Hide(self):
		if self.AtlasMainWindow:
			self.AtlasMainWindow.HideAtlas()
			self.AtlasMainWindow.Hide()
			global TeleportButton
			global textLine
			TeleportButton.Show()
			textLine.Show()
		ui.ScriptWindow.Hide(self)

	def Show(self):
		if self.AtlasMainWindow:
			(bGet, iSizeX, iSizeY) = miniMap.GetAtlasSize()
			if bGet:
				self.SetSize(iSizeX + 15, iSizeY + 38)
				self.board.SetSize(iSizeX + 15, iSizeY + 38)
				#self.AtlasMainWindow.SetSize(iSizeX, iSizeY)
				self.AtlasMainWindow.ShowAtlas()
				self.AtlasMainWindow.Show()
				global TeleportButton
				TeleportButton.Hide()
		ui.ScriptWindow.Show(self)
		global visible
		visible = TRUE

	def OnUpdate(self):
		miniMap.ShowAtlas()
		if not self.tooltipInfo:
			return

		self.tooltipInfo.Hide()

		if FALSE == self.board.IsIn():
			return

		(mouseX, mouseY) = wndMgr.GetMousePosition()
		(bFind, sName, iPosX, iPosY, dwTextColor, dwGuildID) = miniMap.GetAtlasInfo(mouseX, mouseY)

		if FALSE == bFind:
			return

		if "empty_guild_area" == sName:
			sName = locale.GUILD_EMPTY_AREA

		self.tooltipInfo.SetText("%s(%d, %d)" % (sName, iPosX, iPosY))
		(x, y) = self.GetGlobalPosition()
		self.tooltipInfo.SetTooltipPosition(mouseX - x, mouseY - y)
		self.tooltipInfo.SetTextColor(dwTextColor)
		self.tooltipInfo.Show()
		self.tooltipInfo.SetTop()

	def OnPressEscapeKey(self):
		global visible
		visible = FALSE
		self.Hide()
		return TRUE


mainui = TeleportHackDialog()
mainui.LoadWindow()
mainui.Show()