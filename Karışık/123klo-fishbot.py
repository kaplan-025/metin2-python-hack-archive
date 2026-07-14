import app
import chat
import chr
import locale
import net
import player
import time
import ui
import interfacemodule
import background
import os
import game
import cinfo
import chrmgr

fishblowcount = 0
chat.AppendChat(7,"Fishbot by 123klo")

class FishbotBotDialog(ui.ThinBoard):

	def __init__(self):
		ui.ThinBoard.__init__(self)
		self.LoadThinBoard()
		
	def __del__(self):
		ui.ThinBoard.__del__(self)
		
	def LoadThinBoard(self):
	
		self.SetPosition(50, 50)
		self.SetSize(340, 285)
		self.AddFlag("movable")
		self.AddFlag("float")
		
		self.LoadText()
		self.LoadImages()
		self.LoadOnOffImages()
		self.LoadOther()
		
		self.KillFishes()
		
	def Close(self):
		self.Hide()
		return TRUE
		
	def LoadText(self):

		self.HeaderLabel = ui.TextLine()
		self.HeaderLabel.SetParent(self)
		self.HeaderLabel.SetDefaultFontName()
		self.HeaderLabel.SetPosition(-20, 10)
		self.HeaderLabel.SetFeather()
		self.HeaderLabel.SetWindowHorizontalAlignCenter()
		self.HeaderLabel.SetText("Fishbot")
		self.HeaderLabel.SetFontColor(1.0, 0.8, 0)
		self.HeaderLabel.SetOutline()
		self.HeaderLabel.Show()
		
		self.KillFishLabel = ui.TextLine()
		self.KillFishLabel.SetParent(self)
		self.KillFishLabel.SetFontColor(1.0, 0.8, 0)
		self.KillFishLabel.SetPosition(20, 44)
		self.KillFishLabel.SetText("Kill Fish:")
		self.KillFishLabel.Show()	
		self.KillFishLabel.SetOutline()
		
		self.KillFishLabel2 = ui.TextLine()
		self.KillFishLabel2.SetParent(self)
	#	self.KillFishLabel2.SetFontColor(1.0, 0.8, 0)
		self.KillFishLabel2.SetPosition(230, 44)
		self.KillFishLabel2.SetText("Kill")
		self.KillFishLabel2.Show()	
		self.KillFishLabel2.SetOutline()
		
		self.DropFishLabel = ui.TextLine()
		self.DropFishLabel.SetParent(self)
	#	self.DropFishLabel.SetFontColor(1.0, 0.8, 0)
		self.DropFishLabel.SetPosition(275, 44)
		self.DropFishLabel.SetText("Drop")
		self.DropFishLabel.Show()	
		self.DropFishLabel.SetOutline()
		
		self.KillCarbLabel = ui.TextLine()
		self.KillCarbLabel.SetParent(self)
		self.KillCarbLabel.SetFontColor(1.0, 0.8, 0)
		self.KillCarbLabel.SetPosition(20, 70)
		self.KillCarbLabel.SetText("Kill Carps:")
		self.KillCarbLabel.Show()	
		self.KillCarbLabel.SetOutline()
		
		self.DropThingsLabel = ui.TextLine()
		self.DropThingsLabel.SetParent(self)
		self.DropThingsLabel.SetFontColor(1.0, 0.8, 0)
		self.DropThingsLabel.SetPosition(20, 105)
		self.DropThingsLabel.SetText("Drop:")
		self.DropThingsLabel.SetOutline()
		self.DropThingsLabel.Show()	
		
		self.ExitGameLabel = ui.TextLine()
		self.ExitGameLabel.SetParent(self)
		self.ExitGameLabel.SetPosition(100, 145)
		self.ExitGameLabel.SetText("Exit Game")
		self.ExitGameLabel.SetOutline()
		self.ExitGameLabel.Show()	

		self.StopBotLabel = ui.TextLine()
		self.StopBotLabel.SetParent(self)
		self.StopBotLabel.SetPosition(190, 145)
		self.StopBotLabel.SetText("Stop Bot")
		self.StopBotLabel.SetOutline()
		self.StopBotLabel.Show()	
		
		self.FishdelayLabel = ui.TextLine()
		self.FishdelayLabel.SetParent(self)
		self.FishdelayLabel.SetFontColor(1.0, 0.8, 0)
		self.FishdelayLabel.SetPosition(20, 190)
		self.FishdelayLabel.SetText("Fishdelay:")
		self.FishdelayLabel.SetOutline()
		self.FishdelayLabel.Show()	
		
		self.BindeStrich = ui.TextLine()
		self.BindeStrich.SetParent(self)
		self.BindeStrich.SetFontColor(1.0, 0.8, 0)
		self.BindeStrich.SetPosition(120, 190)
		self.BindeStrich.SetText("-")
		self.BindeStrich.SetOutline()
		self.BindeStrich.Show()	
	
		self.BaitLabel = ui.TextLine()
		self.BaitLabel.SetParent(self)
		self.BaitLabel.SetFontColor(1.0, 0.8, 0)
		self.BaitLabel.SetPosition(190, 190)
		self.BaitLabel.SetText("Bait:")
		self.BaitLabel.SetOutline()
		self.BaitLabel.Show()	
	
		self.fishblowcounttext = ui.TextLine()
		self.fishblowcounttext.SetParent(self)
		self.fishblowcounttext.SetDefaultFontName()
		self.fishblowcounttext.SetPosition(130, 252)
		self.fishblowcounttext.SetText("0")
		self.fishblowcounttext.SetFeather()
		self.fishblowcounttext.SetOutline()
		self.fishblowcounttext.Show()
		
	def LoadImages(self):
	
		self.ZanderImage = ui.Button()
		self.ZanderImage.SetParent(self)
		self.ZanderImage.SetPosition(60, 35)	
		self.ZanderImage.SetUpVisual(str("icon/item/27803.tga"))
		self.ZanderImage.SetOverVisual(str("icon/item/27803.tga"))	
		self.ZanderImage.SetDownVisual(str("icon/item/27803.tga"))	
		self.ZanderImage.SetToolTipText("Zander")
		self.ZanderImage.Show()
		
		self.MandarinfischImage = ui.Button()
		self.MandarinfischImage.SetParent(self)
		self.MandarinfischImage.SetPosition(85, 35)	
		self.MandarinfischImage.SetUpVisual(str("icon/item/27804.tga"))	
		self.MandarinfischImage.SetOverVisual(str("icon/item/27804.tga"))	
		self.MandarinfischImage.SetDownVisual(str("icon/item/27804.tga"))
		self.MandarinfischImage.SetToolTipText("Mandarin Fish")
		self.MandarinfischImage.Show()
		
		self.GrZanderImage = ui.Button()
		self.GrZanderImage.SetParent(self)
		self.GrZanderImage.SetPosition(110, 35)	
		self.GrZanderImage.SetUpVisual(str("icon/item/27805.tga"))
		self.GrZanderImage.SetOverVisual(str("icon/item/27805.tga"))
		self.GrZanderImage.SetDownVisual(str("icon/item/27805.tga"))
		self.GrZanderImage.SetToolTipText("Large Zander")
		self.GrZanderImage.Show()
		
		self.LachsImage = ui.Button()
		self.LachsImage.SetParent(self)
		self.LachsImage.SetPosition(135, 35)	
		self.LachsImage.SetUpVisual(str("icon/item/27807.tga"))	
		self.LachsImage.SetOverVisual(str("icon/item/27807.tga"))	
		self.LachsImage.SetDownVisual(str("icon/item/27807.tga"))
		self.LachsImage.SetToolTipText("Salmon/Lachs")
		self.LachsImage.Show()
		
		self.BachforelleImage = ui.Button()
		self.BachforelleImage.SetParent(self)
		self.BachforelleImage.SetPosition(160, 35)	
		self.BachforelleImage.SetUpVisual(str("icon/item/27809.tga"))
		self.BachforelleImage.SetOverVisual(str("icon/item/27809.tga"))	
		self.BachforelleImage.SetDownVisual(str("icon/item/27809.tga"))
		self.BachforelleImage.SetToolTipText("Brook Trout/Bachforelle")
		self.BachforelleImage.Show()
		
		self.LotusFishImage = ui.Button()
		self.LotusFishImage.SetParent(self)
		self.LotusFishImage.SetPosition(185, 35)	
		self.LotusFishImage.SetUpVisual(str("icon/item/27818.tga"))
		self.LotusFishImage.SetOverVisual(str("icon/item/27818.tga"))	
		self.LotusFishImage.SetDownVisual(str("icon/item/27818.tga"))
		self.LotusFishImage.SetToolTipText("Lotus Fish")
		self.LotusFishImage.Show()
		
		self.CarpImage = ui.Button()
		self.CarpImage.SetParent(self)
		self.CarpImage.SetPosition(90, 65)	
		self.CarpImage.SetUpVisual(str("icon/item/27806.tga"))
		self.CarpImage.SetOverVisual(str("icon/item/27806.tga"))	
		self.CarpImage.SetDownVisual(str("icon/item/27806.tga"))	
		self.CarpImage.Show()
		
		self.GrasKarpfenImage = ui.Button()
		self.GrasKarpfenImage.SetParent(self)
		self.GrasKarpfenImage.SetPosition(130, 65)	
		self.GrasKarpfenImage.SetUpVisual(str("icon/item/27808.tga"))	
		self.GrasKarpfenImage.SetOverVisual(str("icon/item/27808.tga"))	
		self.GrasKarpfenImage.SetDownVisual(str("icon/item/27808.tga"))
		self.GrasKarpfenImage.SetToolTipText("Grass Carp")
		self.GrasKarpfenImage.Show()
		
		
	
				####### Things #######
				
		self.UmhangImage = ui.ExpandedImageBox()
		self.UmhangImage.SetParent(self)
		self.UmhangImage.SetPosition(60, 100)	
		self.UmhangImage.LoadImage(str("icon/item/70048.tga"))
		self.UmhangImage.Show()
		
		self.LucysRingImage = ui.ExpandedImageBox()
		self.LucysRingImage.SetParent(self)
		self.LucysRingImage.SetPosition(100, 100)	
		self.LucysRingImage.LoadImage(str("icon/item/70049.tga"))
		self.LucysRingImage.Show()
		
		self.SymbolDwKImage = ui.ExpandedImageBox()
		self.SymbolDwKImage.SetParent(self)
		self.SymbolDwKImage.SetPosition(140, 100)	
		self.SymbolDwKImage.LoadImage(str("icon/item/70050.tga"))
		self.SymbolDwKImage.Show()
		
		self.HandschuhDwKImage = ui.ExpandedImageBox()
		self.HandschuhDwKImage.SetParent(self)
		self.HandschuhDwKImage.SetPosition(180, 100)	
		self.HandschuhDwKImage.LoadImage(str("icon/item/70051.tga"))
		self.HandschuhDwKImage.Show()
		
		self.HandschuhDwKImage = ui.ExpandedImageBox()
		self.HandschuhDwKImage.SetParent(self)
		self.HandschuhDwKImage.SetPosition(180, 100)	
		self.HandschuhDwKImage.LoadImage(str("icon/item/70051.tga"))
		self.HandschuhDwKImage.Show()
		
		self.BleichMittelImage = ui.ExpandedImageBox()
		self.BleichMittelImage.SetParent(self)
		self.BleichMittelImage.SetPosition(220, 100)	
		self.BleichMittelImage.LoadImage(str("icon/item/70201.tga"))
		self.BleichMittelImage.Show()
		
		self.Graete = ui.ExpandedImageBox()
		self.Graete.SetParent(self)
		self.Graete.SetPosition(260, 100)	
		self.Graete.LoadImage(str("icon/item/27799.tga"))
		self.Graete.Show()
		
		self.GMImage = ui.ExpandedImageBox()
		self.GMImage.SetParent(self)
		self.GMImage.SetPosition(20, 145)	
		self.GMImage.LoadImage("m2k Mod\Fishbot\Img\gm.tga")
		self.GMImage.Show()
		
		self.KleinerFischImage = ui.ExpandedImageBox()
		self.KleinerFischImage.SetParent(self)
		self.KleinerFischImage.SetPosition(220, 180)	
		self.KleinerFischImage.LoadImage(str("icon/item/27802.tga"))
		self.KleinerFischImage.Show()
		
		self.WurmImage = ui.ExpandedImageBox()
		self.WurmImage.SetParent(self)
		self.WurmImage.SetPosition(260, 180)	
		self.WurmImage.LoadImage(str("icon/item/27801.tga"))
		self.WurmImage.Show()
		
		self.PasteImage = ui.ExpandedImageBox()
		self.PasteImage.SetParent(self)
		self.PasteImage.SetPosition(300, 180)	
		self.PasteImage.LoadImage(str("icon/item/27800.tga"))
		self.PasteImage.Show()
		
		
		
		
	def LoadOnOffImages(self):
	
		self.KillOn = ui.Button()
		self.KillOn.SetParent(self)
		self.KillOn.SetUpVisual("m2k Mod\Fishbot\Img\on_0.tga")
		self.KillOn.SetOverVisual("m2k Mod\Fishbot\Img\on_1.tga")
		self.KillOn.SetDownVisual("m2k Mod\Fishbot\Img\on_2.tga")
		self.KillOn.SetPosition(247, 43)
		self.KillOn.SetEvent(ui.__mem_func__(self.KillFish))
		self.KillOn.Hide()

		self.KillOff = ui.Button()
		self.KillOff.SetParent(self)
		self.KillOff.SetUpVisual("m2k Mod\Fishbot\Img\off_0.tga")
		self.KillOff.SetOverVisual("m2k Mod\Fishbot\Img\off_1.tga")
		self.KillOff.SetDownVisual("m2k Mod\Fishbot\Img\off_2.tga")
		self.KillOff.SetPosition(247, 43)
		self.KillOff.SetEvent(ui.__mem_func__(self.KillFish))
		self.KillOff.Show()
		
		
		self.DropOn = ui.Button()
		self.DropOn.SetParent(self)
		self.DropOn.SetUpVisual("m2k Mod\Fishbot\Img\on_0.tga")
		self.DropOn.SetOverVisual("m2k Mod\Fishbot\Img\on_1.tga")
		self.DropOn.SetDownVisual("m2k Mod\Fishbot\Img\on_2.tga")
		self.DropOn.SetPosition(303, 43)
		self.DropOn.SetEvent(ui.__mem_func__(self.DropFish))
		self.DropOn.Hide()

		self.DropOff = ui.Button()
		self.DropOff.SetParent(self)
		self.DropOff.SetUpVisual("m2k Mod\Fishbot\Img\off_0.tga")
		self.DropOff.SetOverVisual("m2k Mod\Fishbot\Img\off_1.tga")
		self.DropOff.SetDownVisual("m2k Mod\Fishbot\Img\off_2.tga")
		self.DropOff.SetPosition(303, 43)
		self.DropOff.SetEvent(ui.__mem_func__(self.DropFish))
		self.DropOff.Show()
		
		
		self.KillCarpOn = ui.Button()
		self.KillCarpOn.SetParent(self)
		self.KillCarpOn.SetUpVisual("m2k Mod\Fishbot\Img\on_0.tga")
		self.KillCarpOn.SetOverVisual("m2k Mod\Fishbot\Img\on_1.tga")
		self.KillCarpOn.SetDownVisual("m2k Mod\Fishbot\Img\on_2.tga")
		self.KillCarpOn.SetPosition(105, 80)
		self.KillCarpOn.SetEvent(ui.__mem_func__(self.KillCarp))
		self.KillCarpOn.Hide()

		self.KillCarpOff = ui.Button()
		self.KillCarpOff.SetParent(self)
		self.KillCarpOff.SetUpVisual("m2k Mod\Fishbot\Img\off_0.tga")
		self.KillCarpOff.SetOverVisual("m2k Mod\Fishbot\Img\off_1.tga")
		self.KillCarpOff.SetDownVisual("m2k Mod\Fishbot\Img\off_2.tga")
		self.KillCarpOff.SetPosition(105, 80)
		self.KillCarpOff.SetEvent(ui.__mem_func__(self.KillCarp))
		self.KillCarpOff.Show()
		
		
		self.KillGrassCarpOn = ui.Button()
		self.KillGrassCarpOn.SetParent(self)
		self.KillGrassCarpOn.SetUpVisual("m2k Mod\Fishbot\Img\on_0.tga")
		self.KillGrassCarpOn.SetOverVisual("m2k Mod\Fishbot\Img\on_1.tga")
		self.KillGrassCarpOn.SetDownVisual("m2k Mod\Fishbot\Img\on_2.tga")
		self.KillGrassCarpOn.SetPosition(145, 80)
		self.KillGrassCarpOn.SetEvent(ui.__mem_func__(self.KillGrassCarp))
		self.KillGrassCarpOn.Hide()

		self.KillGrassCarpOff = ui.Button()
		self.KillGrassCarpOff.SetParent(self)
		self.KillGrassCarpOff.SetUpVisual("m2k Mod\Fishbot\Img\off_0.tga")
		self.KillGrassCarpOff.SetOverVisual("m2k Mod\Fishbot\Img\off_1.tga")
		self.KillGrassCarpOff.SetDownVisual("m2k Mod\Fishbot\Img\off_2.tga")
		self.KillGrassCarpOff.SetPosition(145, 80)
		self.KillGrassCarpOff.SetEvent(ui.__mem_func__(self.KillGrassCarp))
		self.KillGrassCarpOff.Show()
		
				####### Drop Things ######
				
		self.DropUmhangOn = ui.Button()
		self.DropUmhangOn.SetParent(self)
		self.DropUmhangOn.SetUpVisual("m2k Mod\Fishbot\Img\on_0.tga")
		self.DropUmhangOn.SetOverVisual("m2k Mod\Fishbot\Img\on_1.tga")
		self.DropUmhangOn.SetDownVisual("m2k Mod\Fishbot\Img\on_2.tga")
		self.DropUmhangOn.SetPosition(78, 115)
		self.DropUmhangOn.SetEvent(ui.__mem_func__(self.DropUmhang))
		self.DropUmhangOn.Hide()

		self.DropUmhangOff = ui.Button()
		self.DropUmhangOff.SetParent(self)
		self.DropUmhangOff.SetUpVisual("m2k Mod\Fishbot\Img\off_0.tga")
		self.DropUmhangOff.SetOverVisual("m2k Mod\Fishbot\Img\off_1.tga")
		self.DropUmhangOff.SetDownVisual("m2k Mod\Fishbot\Img\off_2.tga")
		self.DropUmhangOff.SetPosition(78, 115)
		self.DropUmhangOff.SetEvent(ui.__mem_func__(self.DropUmhang))
		self.DropUmhangOff.Show()
		
		
		self.DropRingOn = ui.Button()
		self.DropRingOn.SetParent(self)
		self.DropRingOn.SetUpVisual("m2k Mod\Fishbot\Img\on_0.tga")
		self.DropRingOn.SetOverVisual("m2k Mod\Fishbot\Img\on_1.tga")
		self.DropRingOn.SetDownVisual("m2k Mod\Fishbot\Img\on_2.tga")
		self.DropRingOn.SetPosition(118, 115)
		self.DropRingOn.SetEvent(ui.__mem_func__(self.DropRing))
		self.DropRingOn.Hide()

		self.DropRingOff = ui.Button()
		self.DropRingOff.SetParent(self)
		self.DropRingOff.SetUpVisual("m2k Mod\Fishbot\Img\off_0.tga")
		self.DropRingOff.SetOverVisual("m2k Mod\Fishbot\Img\off_1.tga")
		self.DropRingOff.SetDownVisual("m2k Mod\Fishbot\Img\off_2.tga")
		self.DropRingOff.SetPosition(118, 115)
		self.DropRingOff.SetEvent(ui.__mem_func__(self.DropRing))
		self.DropRingOff.Show()
		
		
		self.DropSymbolOn = ui.Button()
		self.DropSymbolOn.SetParent(self)
		self.DropSymbolOn.SetUpVisual("m2k Mod\Fishbot\Img\on_0.tga")
		self.DropSymbolOn.SetOverVisual("m2k Mod\Fishbot\Img\on_1.tga")
		self.DropSymbolOn.SetDownVisual("m2k Mod\Fishbot\Img\on_2.tga")
		self.DropSymbolOn.SetPosition(160, 115)
		self.DropSymbolOn.SetEvent(ui.__mem_func__(self.DropSymbol))
		self.DropSymbolOn.Hide()

		self.DropSymbolOff = ui.Button()
		self.DropSymbolOff.SetParent(self)
		self.DropSymbolOff.SetUpVisual("m2k Mod\Fishbot\Img\off_0.tga")
		self.DropSymbolOff.SetOverVisual("m2k Mod\Fishbot\Img\off_1.tga")
		self.DropSymbolOff.SetDownVisual("m2k Mod\Fishbot\Img\off_2.tga")
		self.DropSymbolOff.SetPosition(160, 115)
		self.DropSymbolOff.SetEvent(ui.__mem_func__(self.DropSymbol))
		self.DropSymbolOff.Show()
		
		
		self.DropHandschuhOn = ui.Button()
		self.DropHandschuhOn.SetParent(self)
		self.DropHandschuhOn.SetUpVisual("m2k Mod\Fishbot\Img\on_0.tga")
		self.DropHandschuhOn.SetOverVisual("m2k Mod\Fishbot\Img\on_1.tga")
		self.DropHandschuhOn.SetDownVisual("m2k Mod\Fishbot\Img\on_2.tga")
		self.DropHandschuhOn.SetPosition(194, 115)
		self.DropHandschuhOn.SetEvent(ui.__mem_func__(self.DropHandschuh))
		self.DropHandschuhOn.Hide()

		self.DropHandschuhOff = ui.Button()
		self.DropHandschuhOff.SetParent(self)
		self.DropHandschuhOff.SetUpVisual("m2k Mod\Fishbot\Img\off_0.tga")
		self.DropHandschuhOff.SetOverVisual("m2k Mod\Fishbot\Img\off_1.tga")
		self.DropHandschuhOff.SetDownVisual("m2k Mod\Fishbot\Img\off_2.tga")
		self.DropHandschuhOff.SetPosition(194, 115)
		self.DropHandschuhOff.SetEvent(ui.__mem_func__(self.DropHandschuh))
		self.DropHandschuhOff.Show()
		
		
		self.DropBleichOn = ui.Button()
		self.DropBleichOn.SetParent(self)
		self.DropBleichOn.SetUpVisual("m2k Mod\Fishbot\Img\on_0.tga")
		self.DropBleichOn.SetOverVisual("m2k Mod\Fishbot\Img\on_1.tga")
		self.DropBleichOn.SetDownVisual("m2k Mod\Fishbot\Img\on_2.tga")
		self.DropBleichOn.SetPosition(235, 115)
		self.DropBleichOn.SetEvent(ui.__mem_func__(self.DropFarben))
		self.DropBleichOn.Hide()

		self.DropBleichOff = ui.Button()
		self.DropBleichOff.SetParent(self)
		self.DropBleichOff.SetUpVisual("m2k Mod\Fishbot\Img\off_0.tga")
		self.DropBleichOff.SetOverVisual("m2k Mod\Fishbot\Img\off_1.tga")
		self.DropBleichOff.SetDownVisual("m2k Mod\Fishbot\Img\off_2.tga")
		self.DropBleichOff.SetPosition(235, 115)
		self.DropBleichOff.SetEvent(ui.__mem_func__(self.DropFarben))
		self.DropBleichOff.Show()
		
		
		self.DropGraeteOn = ui.Button()
		self.DropGraeteOn.SetParent(self)
		self.DropGraeteOn.SetUpVisual("m2k Mod\Fishbot\Img\on_0.tga")
		self.DropGraeteOn.SetOverVisual("m2k Mod\Fishbot\Img\on_1.tga")
		self.DropGraeteOn.SetDownVisual("m2k Mod\Fishbot\Img\on_2.tga")
		self.DropGraeteOn.SetPosition(273, 115)
		self.DropGraeteOn.SetEvent(ui.__mem_func__(self.DropGraete))
		self.DropGraeteOn.Hide()

		self.DropGraeteOff = ui.Button()
		self.DropGraeteOff.SetParent(self)
		self.DropGraeteOff.SetUpVisual("m2k Mod\Fishbot\Img\off_0.tga")
		self.DropGraeteOff.SetOverVisual("m2k Mod\Fishbot\Img\off_1.tga")
		self.DropGraeteOff.SetDownVisual("m2k Mod\Fishbot\Img\off_2.tga")
		self.DropGraeteOff.SetPosition(273, 115)
		self.DropGraeteOff.SetEvent(ui.__mem_func__(self.DropGraete))
		self.DropGraeteOff.Show()
		
				######## GM Detector ########
				
		self.ExitGameOn = ui.Button()
		self.ExitGameOn.SetParent(self)
		self.ExitGameOn.SetUpVisual("m2k Mod\Fishbot\Img\on_0.tga")
		self.ExitGameOn.SetOverVisual("m2k Mod\Fishbot\Img\on_1.tga")
		self.ExitGameOn.SetDownVisual("m2k Mod\Fishbot\Img\on_2.tga")
		self.ExitGameOn.SetPosition(147, 145)
		self.ExitGameOn.SetEvent(ui.__mem_func__(self.GMExit))
		self.ExitGameOn.Show()

		self.ExitGameOff = ui.Button()
		self.ExitGameOff.SetParent(self)
		self.ExitGameOff.SetUpVisual("m2k Mod\Fishbot\Img\off_0.tga")
		self.ExitGameOff.SetOverVisual("m2k Mod\Fishbot\Img\off_1.tga")
		self.ExitGameOff.SetDownVisual("m2k Mod\Fishbot\Img\off_2.tga")
		self.ExitGameOff.SetPosition(147, 145)
		self.ExitGameOff.SetEvent(ui.__mem_func__(self.GMExit))
		self.ExitGameOff.Hide()
		
		
		self.StopBotOn = ui.Button()
		self.StopBotOn.SetParent(self)
		self.StopBotOn.SetUpVisual("m2k Mod\Fishbot\Img\on_0.tga")
		self.StopBotOn.SetOverVisual("m2k Mod\Fishbot\Img\on_1.tga")
		self.StopBotOn.SetDownVisual("m2k Mod\Fishbot\Img\on_2.tga")
		self.StopBotOn.SetPosition(232, 145)
		self.StopBotOn.SetEvent(ui.__mem_func__(self.GMStop))
		self.StopBotOn.Hide()

		self.StopBotOff = ui.Button()
		self.StopBotOff.SetParent(self)
		self.StopBotOff.SetUpVisual("m2k Mod\Fishbot\Img\off_0.tga")
		self.StopBotOff.SetOverVisual("m2k Mod\Fishbot\Img\off_1.tga")
		self.StopBotOff.SetDownVisual("m2k Mod\Fishbot\Img\off_2.tga")
		self.StopBotOff.SetPosition(232, 145)
		self.StopBotOff.SetEvent(ui.__mem_func__(self.GMStop))
		self.StopBotOff.Show()
		
				###### Bait #####
				
		self.KleinerFischOn = ui.Button()
		self.KleinerFischOn.SetParent(self)
		self.KleinerFischOn.SetUpVisual("m2k Mod\Fishbot\Img\on_0_s.tga")
		self.KleinerFischOn.SetOverVisual("m2k Mod\Fishbot\Img\on_1_s.tga")
		self.KleinerFischOn.SetDownVisual("m2k Mod\Fishbot\Img\on_2_s.tga")
		self.KleinerFischOn.SetPosition(236, 199)
		self.KleinerFischOn.SetEvent(ui.__mem_func__(self.KleinerFisch))
		self.KleinerFischOn.Show()

		self.KleinerFischOff = ui.Button()
		self.KleinerFischOff.SetParent(self)
		self.KleinerFischOff.SetUpVisual("m2k Mod\Fishbot\Img\off_0_s.tga")
		self.KleinerFischOff.SetOverVisual("m2k Mod\Fishbot\Img\off_1_s.tga")
		self.KleinerFischOff.SetDownVisual("m2k Mod\Fishbot\Img\off_2_s.tga")
		self.KleinerFischOff.SetPosition(236, 199)
		self.KleinerFischOff.SetEvent(ui.__mem_func__(self.KleinerFisch))
		self.KleinerFischOff.Hide()
		
		
		self.WurmOn = ui.Button()
		self.WurmOn.SetParent(self)
		self.WurmOn.SetUpVisual("m2k Mod\Fishbot\Img\on_0_s.tga")
		self.WurmOn.SetOverVisual("m2k Mod\Fishbot\Img\on_1_s.tga")
		self.WurmOn.SetDownVisual("m2k Mod\Fishbot\Img\on_2_s.tga")
		self.WurmOn.SetPosition(275, 199)
		self.WurmOn.SetEvent(ui.__mem_func__(self.Wurm))
		self.WurmOn.Show()

		self.WurmOff = ui.Button()
		self.WurmOff.SetParent(self)
		self.WurmOff.SetUpVisual("m2k Mod\Fishbot\Img\off_0_s.tga")
		self.WurmOff.SetOverVisual("m2k Mod\Fishbot\Img\off_1_s.tga")
		self.WurmOff.SetDownVisual("m2k Mod\Fishbot\Img\off_2_s.tga")
		self.WurmOff.SetPosition(275, 199)
		self.WurmOff.SetEvent(ui.__mem_func__(self.Wurm))
		self.WurmOff.Hide()
		
		
		self.PasteOn = ui.Button()
		self.PasteOn.SetParent(self)
		self.PasteOn.SetUpVisual("m2k Mod\Fishbot\Img\on_0_s.tga")
		self.PasteOn.SetOverVisual("m2k Mod\Fishbot\Img\on_1_s.tga")
		self.PasteOn.SetDownVisual("m2k Mod\Fishbot\Img\on_2_s.tga")
		self.PasteOn.SetPosition(316, 199)
		self.PasteOn.SetEvent(ui.__mem_func__(self.Paste))
		self.PasteOn.Hide()

		self.PasteOff = ui.Button()
		self.PasteOff.SetParent(self)
		self.PasteOff.SetUpVisual("m2k Mod\Fishbot\Img\off_0_s.tga")
		self.PasteOff.SetOverVisual("m2k Mod\Fishbot\Img\off_1_s.tga")
		self.PasteOff.SetDownVisual("m2k Mod\Fishbot\Img\off_2_s.tga")
		self.PasteOff.SetPosition(316, 199)
		self.PasteOff.SetEvent(ui.__mem_func__(self.Paste))
		self.PasteOff.Show()
		
	def LoadOther(self):

		self.Delay1Slotbar = ui.SlotBar()
		self.Delay1Slotbar.SetParent(self)
		self.Delay1Slotbar.SetSize(30, 18)
		self.Delay1Slotbar.SetPosition(-73, 190)
		self.Delay1Slotbar.SetWindowHorizontalAlignCenter()
		self.Delay1Slotbar.Show()
		
		self.Delay1EditLine = ui.EditLine()
		self.Delay1EditLine.SetParent(self.Delay1Slotbar)
		self.Delay1EditLine.SetSize(30, 17)
		self.Delay1EditLine.SetPosition(6, 2)
		self.Delay1EditLine.SetMax(4)
		self.Delay1EditLine.SetNumberMode()
		self.Delay1EditLine.SetText("2750")
		self.Delay1EditLine.SetFocus()
		self.Delay1EditLine.Show()
		
		self.Delay2Slotbar = ui.SlotBar()
		self.Delay2Slotbar.SetParent(self)
		self.Delay2Slotbar.SetSize(30, 18)
		self.Delay2Slotbar.SetPosition(-26, 190)
		self.Delay2Slotbar.SetWindowHorizontalAlignCenter()
		self.Delay2Slotbar.Show()
		
		self.Delay2EditLine = ui.EditLine()
		self.Delay2EditLine.SetParent(self.Delay2Slotbar)
		self.Delay2EditLine.SetSize(30, 17)
		self.Delay2EditLine.SetPosition(6, 2)
		self.Delay2EditLine.SetMax(4)
		self.Delay2EditLine.SetNumberMode()
		self.Delay2EditLine.SetText("2950")
		self.Delay2EditLine.SetFocus()
		self.Delay2EditLine.Show()
		
		self.CloseButton = ui.Button()
		self.CloseButton.SetParent(self)
		self.CloseButton.SetPosition(310, 10)
		self.CloseButton.SetUpVisual("d:/ymir work/ui/public/close_button_01.sub")
		self.CloseButton.SetOverVisual("d:/ymir work/ui/public/close_button_02.sub")
		self.CloseButton.SetDownVisual("d:/ymir work/ui/public/close_button_03.sub")
		self.CloseButton.SetToolTipText("Hide", 0, - 23)
		self.CloseButton.SetEvent(ui.__mem_func__(self.Close))
		self.CloseButton.Show()
		
		self.FishbotStartButton = ui.Button()
		self.FishbotStartButton.SetParent(self)
		self.FishbotStartButton.SetUpVisual("m2k Mod\Spambot\Img\start_0.tga")
		self.FishbotStartButton.SetOverVisual("m2k Mod\Spambot\Img\start_1.tga")
		self.FishbotStartButton.SetDownVisual("m2k Mod\Spambot\Img\start_2.tga")
		self.FishbotStartButton.SetPosition(30, 230)
		self.FishbotStartButton.SetEvent(ui.__mem_func__(self.FishbotStatus))
		self.FishbotStartButton.Show()	
		
		self.FishbotStopButton = ui.Button()
		self.FishbotStopButton.SetParent(self)
		self.FishbotStopButton.SetUpVisual("m2k Mod\Spambot\Img\stop_0.tga")
		self.FishbotStopButton.SetOverVisual("m2k Mod\Spambot\Img\stop_1.tga")
		self.FishbotStopButton.SetDownVisual("m2k Mod\Spambot\Img\stop_2.tga")
		self.FishbotStopButton.SetPosition(30, 230)
		self.FishbotStopButton.SetEvent(ui.__mem_func__(self.FishbotStatus))
		self.FishbotStopButton.Hide()	
		
		
	def KillFish(self):
	
		if cinfo.FishbotStatus == 0:
			if cinfo.KillFish == 0:
				cinfo.KillFish = 1
				self.KillOn.Show()
				self.KillOff.Hide()
			else:	
				cinfo.KillFish = 0	
				self.KillOn.Hide()
				self.KillOff.Show()
				
	def DropFish(self):
	
		if cinfo.FishbotStatus == 0:
			if cinfo.DropFish == 0:
				cinfo.DropFish = 1
				self.DropOn.Show()
				self.DropOff.Hide()
			else:	
				cinfo.DropFish = 0	
				self.DropOn.Hide()
				self.DropOff.Show()
				
	def KillCarp(self):
	
		if cinfo.FishbotStatus == 0:
			if cinfo.GrassCarp == 0:
				cinfo.GrassCarp = 1
				self.KillCarpOn.Show()
				self.KillCarpOff.Hide()
			else:	
				cinfo.GrassCarp = 0	
				self.KillCarpOn.Hide()
				self.KillCarpOff.Show()
				
	def KillGrassCarp(self):
	
		if cinfo.FishbotStatus == 0:
			if cinfo.Carp == 0:
				cinfo.Carp = 1
				self.KillGrassCarpOn.Show()
				self.KillGrassCarpOff.Hide()
			else:	
				cinfo.Carp = 0	
				self.KillGrassCarpOn.Hide()
				self.KillGrassCarpOff.Show()
				
	def DropUmhang(self):
	
		if cinfo.FishbotStatus == 0:
			if cinfo.DropUmhang == 0:
				cinfo.DropUmhang = 1
				self.DropUmhangOn.Show()
				self.DropUmhangOff.Hide()
			else:	
				cinfo.DropUmhang = 0	
				self.DropUmhangOn.Hide()
				self.DropUmhangOff.Show()
				
	def DropRing(self):
	
		if cinfo.FishbotStatus == 0:
			if cinfo.DropRing == 0:
				cinfo.DropRing = 1
				self.DropRingOn.Show()
				self.DropRingOff.Hide()
			else:	
				cinfo.DropRing = 0	
				self.DropRingOn.Hide()
				self.DropRingOff.Show()
				
	def DropSymbol(self):
	
		if cinfo.FishbotStatus == 0:
			if cinfo.DropSymbol == 0:
				cinfo.DropSymbol = 1
				self.DropSymbolOn.Show()
				self.DropSymbolOff.Hide()
			else:	
				cinfo.DropSymbol = 0	
				self.DropSymbolOn.Hide()
				self.DropSymbolOff.Show()
	
	def DropHandschuh(self):
	
		if cinfo.FishbotStatus == 0:
			if cinfo.DropHandschuh == 0:
				cinfo.DropHandschuh = 1
				self.DropHandschuhOn.Show()
				self.DropHandschuhOff.Hide()
			else:	
				cinfo.DropHandschuh = 0	
				self.DropHandschuhOn.Hide()
				self.DropHandschuhOff.Show()
				
	def DropFarben(self):
	
		if cinfo.FishbotStatus == 0:
			if cinfo.DropFarben == 0:
				cinfo.DropFarben = 1
				self.DropBleichOn.Show()
				self.DropBleichOff.Hide()
			else:	
				cinfo.DropFarben = 0	
				self.DropBleichOn.Hide()
				self.DropBleichOff.Show()
				
	def DropGraete(self):
	
		if cinfo.FishbotStatus == 0:
			if cinfo.DropGraete == 0:
				cinfo.DropGraete = 1
				self.DropGraeteOn.Show()
				self.DropGraeteOff.Hide()
			else:	
				cinfo.DropGraete = 0	
				self.DropGraeteOn.Hide()
				self.DropGraeteOff.Show()
				
	def GMExit(self):
	
		if cinfo.FishbotStatus == 0:
			if cinfo.GMExit == 0:
				cinfo.GMExit = 1
				self.ExitGameOn.Show()
				self.ExitGameOff.Hide()
				self.StopBotOff.Show()
				self.StopBotOn.Hide()
				
			else:	
				cinfo.GMExit = 0	
				self.ExitGameOn.Hide()
				self.ExitGameOff.Show()
				self.StopBotOn.Show()
				self.StopBotOff.Hide()
				
	def GMStop(self):
	
		if cinfo.FishbotStatus == 0:
			if cinfo.GMStop == 0:
				cinfo.GMStop = 1
				self.StopBotOn.Show()
				self.StopBotOff.Hide()
				self.ExitGameOff.Show()
				self.ExitGameOn.Hide()
			else:	
				cinfo.GMStop = 0	
				self.StopBotOn.Hide()
				self.StopBotOff.Show()
				self.ExitGameOn.Show()
				self.ExitGameOff.Hide()
							
	def KleinerFisch(self):
	
		if cinfo.FishbotStatus == 0:
			if cinfo.KleinerFisch == 0:
				cinfo.KleinerFisch = 1
				self.KleinerFischOn.Show()
				self.KleinerFischOff.Hide()
			else:	
				cinfo.KleinerFisch = 0	
				self.KleinerFischOn.Hide()
				self.KleinerFischOff.Show()	

	def Wurm(self):
	
		if cinfo.FishbotStatus == 0:
			if cinfo.Wurm == 0:
				cinfo.Wurm = 1
				self.WurmOn.Show()
				self.WurmOff.Hide()
			else:	
				cinfo.Wurm = 0	
				self.WurmOn.Hide()
				self.WurmOff.Show()	

	def Paste(self):
	
		if cinfo.FishbotStatus == 0:
			if cinfo.Paste == 0:
				cinfo.Paste = 1
				self.PasteOn.Show()
				self.PasteOff.Hide()
			else:	
				cinfo.Paste = 0	
				self.PasteOn.Hide()
				self.PasteOff.Show()	


	def FishbotStatus(self):
	
		if cinfo.FishbotStatus == 0:
			cinfo.FishbotStatus = 1
			self.FishbotStopButton.Show()
			self.FishbotStartButton.Hide()
			self.StartFishbot()
			chat.AppendChat(chat.CHAT_TYPE_NOTICE, "An")
			
		else:	
			cinfo.FishbotStatus = 0	
			self.FishbotStopButton.Hide()
			self.FishbotStartButton.Show()	
			chat.AppendChat(chat.CHAT_TYPE_NOTICE, "Aus")
			
			
			#################### Gui End ####################
			
			
	def StartFishbot(self):
	
		for Bait in xrange(player.INVENTORY_PAGE_SIZE*2):
			BaitValue = player.GetItemIndex(Bait)
			if (cinfo.KleinerFisch == 1 and BaitValue == 27802):
				net.SendItemUsePacket(Bait)
				self.ThrowInRod()
				chat.AppendChat(chat.CHAT_TYPE_NOTICE, "Kleiner fishc")
				break
			elif (cinfo.Wurm == 1 and BaitValue == 27801):
				net.SendItemUsePacket(Bait) 
				self.ThrowInRod()
				break
			elif (cinfo.Paste == 1 and BaitValue == 27800):
				net.SendItemUsePacket(Bait)
				break
				self.ThrowInRod()
			
	def ThrowInRod(self):
	
		player.SetAttackKeyState(TRUE)
		player.SetAttackKeyState(FALSE)
		cinfo.Action = 1
		self.WaitForFishSymbol()
			
	def WaitForFishSymbol(self):
		
		x1 = self.Delay1EditLine.GetText()
		x2 = self.Delay2EditLine.GetText()
		global fishblowcount
		
		if cinfo.Action == 1 and cinfo.FishbotStatus == 1:
			if not chrmgr.IsPossibleEmoticon(-1):
				cinfo.Action = 2
				fishblowcount = fishblowcount + 1
				self.fishblowcounttext.SetText(str(fishblowcount))
				x = app.GetRandom(2300, 2400)		# x = app.GetRandom(int(x1), int(x2))								# 156 durchgänge beretis
				Fishdelay = int(x) / 1000
			
				self.Next = WaitingDialog()
				self.Next.Open(Fishdelay)
				self.Next.SAFE_SetTimeOverEvent(self.WaitBotDelay)
		
	
		self.CheckSymbol = WaitingDialog()
		self.CheckSymbol.Open(0.25)
		self.CheckSymbol.SAFE_SetTimeOverEvent(self.WaitForFishSymbol)
	
	def WaitBotDelay(self):
		
		player.SetAttackKeyState(TRUE)
		player.SetAttackKeyState(FALSE)
		
		for Bait in xrange(player.INVENTORY_PAGE_SIZE*2):
			BaitValue = player.GetItemIndex(Bait)
			if (cinfo.KleinerFisch == 1 and BaitValue == 27802):
				net.SendItemUsePacket(Bait)
		
		
		
		self.Botdelay = WaitingDialog()
		self.Botdelay.Open(4.4)
		self.Botdelay.SAFE_SetTimeOverEvent(self.StartFishbot)


		
		
	def KillFishes(self):
		
		for i in xrange(player.INVENTORY_PAGE_SIZE*2):
			Value = player.GetItemIndex(i)
			if cinfo.KillFish == 1:
				if Value == 27803:
					net.SendItemUsePacket(i)
					break
				if Value == 27804:
					net.SendItemUsePacket(i)
					break
				if Value == 27805:
					net.SendItemUsePacket(i)
					break
				if Value == 27807:
					net.SendItemUsePacket(i)
					break
				if Value == 27809:
					net.SendItemUsePacket(i)
					break
				if Value == 27818:
					net.SendItemUsePacket(i)
					break
					
			if cinfo.Carp == 1:
				if Value == 27806:
					net.SendItemUsePacket(i)
					break
			if cinfo.GrassCarp == 1:
				if Value == 27808:
					net.SendItemUsePacket(i)
					break
			
		
class WaitingDialog(ui.ScriptWindow):

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.eventTimeOver = lambda *arg: None
		self.eventExit = lambda *arg: None

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def Open(self, waitTime):
		curTime = time.clock()
		self.endTime = curTime + waitTime

		self.Show()		

	def Close(self):
		self.Hide()

	def Destroy(self):
		self.Hide()

	def SAFE_SetTimeOverEvent(self, event):
		self.eventTimeOver = ui.__mem_func__(event)

	def SAFE_SetExitEvent(self, event):
		self.eventExit = ui.__mem_func__(event)
		
	
	def OnUpdate(self):
		lastTime = max(0, self.endTime - time.clock())
		if 0 == lastTime:
			self.Close()
			self.eventTimeOver()	
		else:
			return
		
	def OnPressExitKey(self):

		self.Close()
		return TRUE


	
Fish = FishbotBotDialog()
Fish.Show()