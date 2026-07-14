# Metin2Bot [Dreamfancy]
import chat 
import ui 
import app 
import item 
import player 
import grp 

CreateBonus0 = 0 
CreateBonus1 = 0 
CreateBonus2 = 0 
CreateBonus3 = 0 
CreateBonus4 = 0 
CreateWhish0 = 0 
CreateWhish1 = 0 
CreateWhish2 = 0 
CreateWhish3 = 0 
CreateWhish4 = 0 

ItemValue = 11299 

BonusListe = (  
    "", 
    "Max. HP", 
    "Max. SP", 
    "Canlilik", 
    "Zeka",  
    "Guc", 
    "Saldiri Degeri", 
    "Saldiri Hizi", 
    "Hareket Hizi", 
    "Buyu Hizi", 
    "Hasar, HP ile absorbe edile..", 
    "Hasar, SP ile absorbe edile..", 
    "Zehirlenme Degisimi", 
    "Sersemletme Sansi", 
    "Yavaslatma Sansi", 
    "Kritik Vurus Sansi", 
    "Delici Vurus Sansi", 
    "Yari insanlara karsi guclu", 
    "Hayvanlara karsi guclu", 
    "Orklara karsi guclu", 
    "Mistiklere karsi guclu", 
    "Olumsuzlere karsi guclu", 
    "Seytanlara karsi guclu", 
    "HP Uretimi", 
    "SP Uretimi", 
    "Dusmanin Sp’sini Calma Sa..", 
    "Vurus Yapildiginda Sp’yi G..", 
    "Beden karsisindaki atakla..", 
    "Oklara Karsi Savunma", 
    "Kilic Savunmasi", 
    "Cift El Savunmasi", 
    "Bicak Savunmasi", 
    "Can Savunmasi", 
    "Yelpaze Savunmasi", 
    "Oklara karsi dayaniklik", 
    "Atese karsi dayaniklik", 
    "Simsege karsi dayaniklik", 
    "Buyuye karsi dayaniklik", 
    "Ruzgar dayanikliligi", 
    "Vucut darbelerini yansitma..", 
    "Lanet yansitilmasi", 
    "Sersemlik karsisinda bagis..", 
    "Yere dusme karsisinda bag..", 
    "Max. Dayaniklilik", 
    "Savascilara Karsi Savunm..", 
    "Ninjalara Karsi Savunma S..", 
    "Suralara Karsi Savunma S..", 
    "Samanlara Karsi Savunm..", 
    "Canavarlara Karsi Guclu", 
    "Beceri Hasari", 
    "Ortalama Zarar", 
    "Beceri hasarina karsi direnc", 
    "Ortalama hasara karsi direnc", 
    "Savasci karsi guclu", 
    "Ninjalara karsi guclu", 
    "Suralara karsi guclu", 
    "Samanlara karsi guclu",
    ) 

BonusIDListe = {  
    "" : 0, 
    "Max. HP" : 1, 
    "Max. SP" : 2, 
    "Canlilik" : 3, 
    "Zeka" : 4,  
    "Guc" : 5, 
    "Saldiri degeri" : 6, 
    "Saldiri Hizi" : 7, 
    "Hareket Hizi" : 8, 
    "Buyu Hizi" : 9, 
    "Hasar, HP ile absorbe edilecek" : 10, 
    "Hasar, SP ile absorbe edilecek" : 11, 
    "Zehirlenme Degisimi" : 12, 
    "Sersemletme Sansi" : 13, 
    "Yavaslatma Sansi" : 14, 
    "Kritik Vurus Sansi" : 15, 
    "Delici Vurus Sansi" : 16, 
    "Yari insanlara karsi guclu" : 17, 
    "Hayvanlara karsi guclu" : 18, 
    "Orklara karsi guclu" : 19, 
    "Mistiklere karsi guclu" : 20, 
    "Olumsuzlere karsi guclu" : 21, 
    "Seytanlara karsi guclu" : 22, 
    "HP Uretimi" : 23, 
    "SP Uretimi" : 24, 
    "Dusmanin Sp’sini Calma Sansi" : 25, 
    "Vurus Yapildiginda Sp’yi Geri Kazanma Sansi" : 26, 
    "Beden karsisindaki ataklarin bloklanmasi" : 27, 
    "Oklara Karsi Savunma" : 28, 
    "Kilic Savunmasi" : 29, 
    "Cift El Savunmasi" : 30, 
    "Bicak Savunmasi" : 31, 
    "Can Savunmasi" : 32, 
    "Yelpaze Savunmasi" : 33, 
    "Oklara karsi dayaniklik" : 34, 
    "Atese karsi dayaniklik" : 35, 
    "Simsege karsi dayaniklik" : 36, 
    "Buyuye karsi dayaniklik" : 37, 
    "Ruzgar dayanikliligi" : 38, 
    "Vucut darbelerini yansitma sansi" : 39, 
    "Lanet yansitilmasi" : 40,
    "Sersemlik karsisinda bagisiklik" : 48, 
    "Yere dusme karsisinda bagisiklik" : 50, 
    "Max. Dayaniklilik" : 58, 
    "Savascilara Karsi Savunma Sansi" : 59, 
    "Ninjalara Karsi Savunma Sansi" : 60, 
    "Suralara Karsi Savunma Sansi" : 61, 
    "Samanlara Karsi Savunma Sansi" : 62, 
    "Canavarlara Karsi Guclu" : 63, 
    "Beceri Hasari" : 71, 
    "Ortalama Zarar" : 72, 
    "Beceri hasarina karsi direnc" : 73, 
    "Ortalama hasara karsi direnc" : 74, 
    "Savasci karsi guclu" : 78, 
    "Ninjalara karsi guclu" : 79, 
    "Suralara karsi guclu" : 80, 
    "Samanlara karsi guclu" : 81, 
    } 

class CreateItemDialog(ui.Window): 

    ENABLE_COLOR = grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0) 
    DISABLE_COLOR = grp.GenerateColor(0.9, 0.4745, 0.4627, 1.0) 

    def __init__(self): 
        ui.Window.__init__(self) 

        self.Board = ui.BoardWithTitleBar() 
        self.Board.SetSize(350, 355) 
        self.Board.SetCenterPosition() 
        self.Board.AddFlag("movable") 
        self.Board.AddFlag("float") 
        self.Board.SetTitleName("Dreamfancy.org") 
        self.Board.SetCloseEvent(self.Close) 
        self.Board.Show() 
         
        self.MetinStone1 = 28930 
        self.MetinStone2 = 28940 
        self.MetinStone3 = 0 

        self.AddTextLines() 
        self.AddImages() 
        self.AddSlotBars() 
         
    def __del__(self): 
        ui.Window.__del__(self) 

    def AddSlotBars(self): 
        return 
         
    def AddImages(self): 
        global ItemValue 
        item.SelectItem(int(ItemValue)) 
        ItemIcon = item.GetIconImageFileName() 
        self.ItemImage = ui.ExpandedImageBox() 
        self.ItemImage.SetParent(self.Board) 
        self.ItemImage.SetPosition(17, 65 + 15) 
        self.ItemImage.LoadImage(str(ItemIcon)) 
        self.ItemImage.Show() 
         
        self.ItemNameText = ui.TextLine() 
        self.ItemNameText.SetParent(self.Board) 
        self.ItemNameText.SetDefaultFontName() 
        self.ItemNameText.SetPosition(15, 55) 
        self.ItemNameText.SetFeather() 
        self.ItemNameText.SetText(str(item.GetItemName())) 
        for i in xrange(0,1): 
            (ItemTypeLimit, ItemLevelLimit) = item.GetLimit(i) 
            if item.LIMIT_LEVEL == ItemTypeLimit: 
                if player.GetStatus(player.LEVEL) < ItemLevelLimit: 
                    self.ItemNameText.SetPackedFontColor(self.DISABLE_COLOR) 
                else: 
                    self.ItemNameText.SetPackedFontColor(self.ENABLE_COLOR) 
        self.ItemNameText.SetOutline() 
        self.ItemNameText.Show() 

         
        self.Metin1Image = ui.ExpandedImageBox() 
        self.Metin1Image.SetParent(self.Board) 
        self.Metin1Image.SetPosition(65, 65 + 15) 
        if int(self.MetinStone1) != 0: 
            item.SelectItem(int(self.MetinStone1)) 
            ItemIcon = item.GetIconImageFileName() 
            self.Metin1Image.LoadImage(str(ItemIcon)) 
        self.Metin1Image.Show() 

        self.Metin1Text = ui.TextLine() 
        self.Metin1Text.SetParent(self.Board) 
        self.Metin1Text.SetDefaultFontName() 
        self.Metin1Text.SetPosition(105, 65 + 23) 
        self.Metin1Text.SetFeather() 
        if int(self.MetinStone1) != 0: 
            self.Metin1Text.SetText(str(item.GetItemName())) 
        else: 
            self.Metin1Text.SetText("Burada tas yok!")             
        self.Metin1Text.SetFontColor(1.0, 1.0, 1.0) 
        self.Metin1Text.SetOutline() 
        self.Metin1Text.Show()     
         
        self.Metin1SlotBar = ui.SlotBar() 
        self.Metin1SlotBar.SetParent(self.Board) 
        self.Metin1SlotBar.SetSize(5*7, 14) 
        self.Metin1SlotBar.SetPosition(240, 65 + 23) 
        self.Metin1SlotBar.Show() 
         
        self.Metin1EditLine = ui.EditLine() 
        self.Metin1EditLine.SetParent(self.Metin1SlotBar) 
        self.Metin1EditLine.SetSize(5*7, 18) 
        self.Metin1EditLine.SetPosition(6, 0) 
        self.Metin1EditLine.SetMax(5) 
        self.Metin1EditLine.SetNumberMode() 
        self.Metin1EditLine.SetText(str(self.MetinStone1)) 
        self.Metin1EditLine.SetFocus() 
        self.Metin1EditLine.Show() 
         
        self.Metin1Button = ui.Button() 
        self.Metin1Button.SetParent(self.Board) 
        self.Metin1Button.SetUpVisual("d:/ymir work/ui/public/small_Button_01.sub") 
        self.Metin1Button.SetOverVisual("d:/ymir work/ui/public/small_Button_02.sub") 
        self.Metin1Button.SetDownVisual("d:/ymir work/ui/public/small_Button_03.sub") 
        self.Metin1Button.SetText("Tamam") 
        self.Metin1Button.SetEvent(ui.__mem_func__(self.SetMetin1)) 
        self.Metin1Button.SetPosition(285, 65 + 20) 
        self.Metin1Button.Show() 
         
        self.Metin2Image = ui.ExpandedImageBox() 
        self.Metin2Image.SetParent(self.Board) 
        self.Metin2Image.SetPosition(65, 100 + 15) 
        if int(self.MetinStone2) != 0: 
            item.SelectItem(int(self.MetinStone2)) 
            ItemIcon = item.GetIconImageFileName() 
            self.Metin2Image.LoadImage(str(ItemIcon)) 
        self.Metin2Image.Show() 

        self.Metin2Text = ui.TextLine() 
        self.Metin2Text.SetParent(self.Board) 
        self.Metin2Text.SetDefaultFontName() 
        self.Metin2Text.SetPosition(105, 100 + 23) 
        self.Metin2Text.SetFeather() 
        if int(self.MetinStone2) != 0: 
            self.Metin2Text.SetText(str(item.GetItemName())) 
        else: 
            self.Metin2Text.SetText("Burada tas yok!")             
        self.Metin2Text.SetFontColor(1.0, 1.0, 1.0) 
        self.Metin2Text.SetOutline() 
        self.Metin2Text.Show()     

        self.Metin2SlotBar = ui.SlotBar() 
        self.Metin2SlotBar.SetParent(self.Board) 
        self.Metin2SlotBar.SetSize(5*7, 14) 
        self.Metin2SlotBar.SetPosition(240, 100 + 23) 
        self.Metin2SlotBar.Show() 
         
        self.Metin2EditLine = ui.EditLine() 
        self.Metin2EditLine.SetParent(self.Metin2SlotBar) 
        self.Metin2EditLine.SetSize(5*7, 18) 
        self.Metin2EditLine.SetPosition(6, 0) 
        self.Metin2EditLine.SetMax(5) 
        self.Metin2EditLine.SetNumberMode() 
        self.Metin2EditLine.SetText(str(self.MetinStone2)) 
        self.Metin2EditLine.SetFocus() 
        self.Metin2EditLine.Show() 
         
        self.Metin2Button = ui.Button() 
        self.Metin2Button.SetParent(self.Board) 
        self.Metin2Button.SetUpVisual("d:/ymir work/ui/public/small_Button_01.sub") 
        self.Metin2Button.SetOverVisual("d:/ymir work/ui/public/small_Button_02.sub") 
        self.Metin2Button.SetDownVisual("d:/ymir work/ui/public/small_Button_03.sub") 
        self.Metin2Button.SetText("Tamam") 
        self.Metin2Button.SetEvent(ui.__mem_func__(self.SetMetin2)) 
        self.Metin2Button.SetPosition(285, 100 + 20) 
        self.Metin2Button.Show() 
         
        self.Metin3Image = ui.ExpandedImageBox() 
        self.Metin3Image.SetParent(self.Board) 
        self.Metin3Image.SetPosition(65, 135 + 15)         
        if int(self.MetinStone3) != 0: 
            item.SelectItem(int(self.MetinStone3)) 
            ItemIcon = item.GetIconImageFileName() 
            self.Metin3Image.LoadImage(str(ItemIcon)) 
        self.Metin3Image.Show() 
         
        self.Metin3Text = ui.TextLine() 
        self.Metin3Text.SetParent(self.Board) 
        self.Metin3Text.SetDefaultFontName() 
        self.Metin3Text.SetPosition(105, 135 + 23) 
        self.Metin3Text.SetFeather() 
        if int(self.MetinStone3) != 0: 
            self.Metin3Text.SetText(str(item.GetItemName())) 
        else: 
            self.Metin3Text.SetText("Burada tas yok!")             
        self.Metin3Text.SetFontColor(1.0, 1.0, 1.0) 
        self.Metin3Text.SetOutline() 
        self.Metin3Text.Show()     
         
        self.Metin3SlotBar = ui.SlotBar() 
        self.Metin3SlotBar.SetParent(self.Board) 
        self.Metin3SlotBar.SetSize(5*7, 14) 
        self.Metin3SlotBar.SetPosition(240, 135 + 23) 
        self.Metin3SlotBar.Show() 
         
        self.Metin3EditLine = ui.EditLine() 
        self.Metin3EditLine.SetParent(self.Metin3SlotBar) 
        self.Metin3EditLine.SetSize(5*7, 18) 
        self.Metin3EditLine.SetPosition(6, 0) 
        self.Metin3EditLine.SetMax(5) 
        self.Metin3EditLine.SetNumberMode() 
        self.Metin3EditLine.SetText(str(self.MetinStone3)) 
        self.Metin3EditLine.SetFocus() 
        self.Metin3EditLine.Show() 

        self.Metin3Button = ui.Button() 
        self.Metin3Button.SetParent(self.Board) 
        self.Metin3Button.SetUpVisual("d:/ymir work/ui/public/small_Button_01.sub") 
        self.Metin3Button.SetOverVisual("d:/ymir work/ui/public/small_Button_02.sub") 
        self.Metin3Button.SetDownVisual("d:/ymir work/ui/public/small_Button_03.sub") 
        self.Metin3Button.SetText("Tamam") 
        self.Metin3Button.SetEvent(ui.__mem_func__(self.SetMetin3)) 
        self.Metin3Button.SetPosition(285, 135 + 20) 
        self.Metin3Button.Show() 
         
    def SetMetin1(self): 
        self.MetinStone1 = int(self.Metin1EditLine.GetText()) 
        item.SelectItem(int(self.MetinStone1)) 
        ItemIcon = item.GetIconImageFileName() 
        self.Metin1Image.LoadImage(str(ItemIcon)) 
        if int(self.MetinStone1) != 0: 
            self.Metin1Text.SetText(str(item.GetItemName())) 
        else: 
            self.Metin1Text.SetText("Burada tas yok!")             
     
    def SetMetin2(self): 
        self.MetinStone2 = int(self.Metin2EditLine.GetText()) 
        item.SelectItem(int(self.MetinStone2)) 
        ItemIcon = item.GetIconImageFileName() 
        self.Metin2Image.LoadImage(str(ItemIcon)) 
        if int(self.MetinStone2) != 0: 
            self.Metin2Text.SetText(str(item.GetItemName())) 
        else: 
            self.Metin2Text.SetText("Burada tas yok!")             
     
    def SetMetin3(self): 
        self.MetinStone3 = int(self.Metin3EditLine.GetText()) 
        item.SelectItem(int(self.MetinStone3)) 
        ItemIcon = item.GetIconImageFileName() 
        self.Metin3Image.LoadImage(str(ItemIcon))         
        if int(self.MetinStone2) != 0: 
            self.Metin3Text.SetText(str(item.GetItemName())) 
        else: 
            self.Metin3Text.SetText("Burada tas yok!")             
         
    def SetItemValue(self): 
        global ItemValue 
        ItemValue = int(self.ItemValueEditLine.GetText()) 
        item.SelectItem(int(ItemValue)) 
        ItemIcon = item.GetIconImageFileName() 
        self.ItemImage.LoadImage(str(ItemIcon)) 
        self.ItemNameText.SetText(str(item.GetItemName())) 
        for i in xrange(0,1): 
            (ItemTypeLimit, ItemLevelLimit) = item.GetLimit(i) 
            if item.LIMIT_LEVEL == ItemTypeLimit: 
                if player.GetStatus(player.LEVEL) < ItemLevelLimit: 
                    self.ItemNameText.SetPackedFontColor(self.DISABLE_COLOR) 
                else: 
                    self.ItemNameText.SetPackedFontColor(self.ENABLE_COLOR)     
         
    def AddTextLines(self): 
        self.CreateItemButton = ui.Button() 
        self.CreateItemButton.SetParent(self.Board) 
        self.CreateItemButton.SetUpVisual("d:/ymir work/ui/public/xlarge_Button_01.sub") 
        self.CreateItemButton.SetOverVisual("d:/ymir work/ui/public/xlarge_Button_02.sub") 
        self.CreateItemButton.SetDownVisual("d:/ymir work/ui/public/xlarge_Button_03.sub") 
        self.CreateItemButton.SetText("Envantere Gonder") 
        self.CreateItemButton.SetEvent(ui.__mem_func__(self.CreateItem)) 
        self.CreateItemButton.SetPosition(80, 318) 
        self.CreateItemButton.Show() 
     
        self.ItemValueText = ui.TextLine() 
        self.ItemValueText.SetParent(self.Board) 
        self.ItemValueText.SetDefaultFontName() 
        self.ItemValueText.SetPosition(15, 35) 
        self.ItemValueText.SetFeather() 
        self.ItemValueText.SetText("Esya Kodu:") 
        self.ItemValueText.SetFontColor(1.0, 1.0, 1.0) 
        self.ItemValueText.SetOutline() 
        self.ItemValueText.Show() 
         
        self.ItemValueSlotBar = ui.SlotBar() 
        self.ItemValueSlotBar.SetParent(self.Board) 
        self.ItemValueSlotBar.SetSize(5*7, 14) 
        self.ItemValueSlotBar.SetPosition(70, 35) 
        self.ItemValueSlotBar.Show() 
         
        self.ItemValueEditLine = ui.EditLine() 
        self.ItemValueEditLine.SetParent(self.ItemValueSlotBar) 
        self.ItemValueEditLine.SetSize(5*7, 18) 
        self.ItemValueEditLine.SetPosition(6, 0) 
        self.ItemValueEditLine.SetMax(5) 
        self.ItemValueEditLine.SetNumberMode() 
        self.ItemValueEditLine.SetText("19") 
        self.ItemValueEditLine.SetFocus() 
        self.ItemValueEditLine.Show() 

        self.SetItemValueButton = ui.Button() 
        self.SetItemValueButton.SetParent(self.Board) 
        self.SetItemValueButton.SetUpVisual("d:/ymir work/ui/public/small_Button_01.sub") 
        self.SetItemValueButton.SetOverVisual("d:/ymir work/ui/public/small_Button_02.sub") 
        self.SetItemValueButton.SetDownVisual("d:/ymir work/ui/public/small_Button_03.sub") 
        self.SetItemValueButton.SetText("Tamam") 
        self.SetItemValueButton.SetPosition(110, 33) 
        self.SetItemValueButton.SetEvent(ui.__mem_func__(self.SetItemValue)) 
        self.SetItemValueButton.Show() 
         
        self.CallItemListButton = ui.Button() 
        self.CallItemListButton.SetParent(self.Board) 
        self.CallItemListButton.SetUpVisual("d:/ymir work/ui/public/middle_Button_01.sub") 
        self.CallItemListButton.SetOverVisual("d:/ymir work/ui/public/middle_Button_02.sub") 
        self.CallItemListButton.SetDownVisual("d:/ymir work/ui/public/middle_Button_03.sub") 
        self.CallItemListButton.SetText("Esya Listesi") 
        self.CallItemListButton.SetPosition(155, 33) 
        self.CallItemListButton.SetEvent(ui.__mem_func__(self.CallItemList)) 
        self.CallItemListButton.Show() 
         
        self.ItemCountText = ui.TextLine() 
        self.ItemCountText.SetParent(self.Board) 
        self.ItemCountText.SetDefaultFontName() 
        self.ItemCountText.SetPosition(15, 55 + 120 + 15) 
        self.ItemCountText.SetFeather() 
        self.ItemCountText.SetText("Esya Degeri: ") 
        self.ItemCountText.SetFontColor(1.0, 1.0, 1.0) 
        self.ItemCountText.SetOutline() 
        self.ItemCountText.Show()     

        self.ItemCountEditLine = ui.EditLine() 
        self.ItemCountEditLine.SetParent(self.Board) 
        self.ItemCountEditLine.SetSize(3*7, 18) 
        self.ItemCountEditLine.SetPosition(15 + 55, 55 + 120 + 15) 
        self.ItemCountEditLine.SetMax(3) 
        self.ItemCountEditLine.SetNumberMode() 
        self.ItemCountEditLine.SetText("1") 
        self.ItemCountEditLine.Show() 
         
        self.Bonus1Text = ui.TextLine() 
        self.Bonus1Text.SetParent(self.Board) 
        self.Bonus1Text.SetDefaultFontName() 
        self.Bonus1Text.SetPosition(15, 85 + 120 + 15) 
        self.Bonus1Text.SetFeather() 
        self.Bonus1Text.SetText("Efsun 1:") 
        self.Bonus1Text.SetFontColor(1.0, 1.0, 1.0) 
        self.Bonus1Text.SetOutline() 
        self.Bonus1Text.Show() 
         
        self.Bonus1AtrText = ui.TextLine() 
        self.Bonus1AtrText.SetParent(self.Board) 
        self.Bonus1AtrText.SetDefaultFontName() 
        self.Bonus1AtrText.SetPosition(65, 85 + 120 + 15) 
        self.Bonus1AtrText.SetFeather() 
        self.Bonus1AtrText.SetText("-") 
        self.Bonus1AtrText.SetFontColor(1.0, 1.0, 1.0) 
        self.Bonus1AtrText.SetOutline() 
        self.Bonus1AtrText.Show()     
     
        self.Bonus1ValueEditLine = ui.EditLine() 
        self.Bonus1ValueEditLine.SetParent(self.Board) 
        self.Bonus1ValueEditLine.SetSize(29, 18) 
        self.Bonus1ValueEditLine.SetPosition(240 - 29, 85 + 120 + 15) 
        self.Bonus1ValueEditLine.SetMax(4) 
        self.Bonus1ValueEditLine.SetNumberMode() 
        self.Bonus1ValueEditLine.SetText("0") 
        self.Bonus1ValueEditLine.Show() 
     
        self.Bonus1Button = ui.Button() 
        self.Bonus1Button.SetParent(self.Board) 
        self.Bonus1Button.SetUpVisual("d:/ymir work/ui/public/large_Button_01.sub") 
        self.Bonus1Button.SetOverVisual("d:/ymir work/ui/public/large_Button_02.sub") 
        self.Bonus1Button.SetDownVisual("d:/ymir work/ui/public/large_Button_03.sub") 
        self.Bonus1Button.SetText("Efsunlari Ayarla") 
        self.Bonus1Button.SetPosition(240, 85 + 120 + 10) 
        self.Bonus1Button.Show() 
         
        self.Bonus2Text = ui.TextLine() 
        self.Bonus2Text.SetParent(self.Board) 
        self.Bonus2Text.SetDefaultFontName() 
        self.Bonus2Text.SetPosition(15, 105 + 120 + 15) 
        self.Bonus2Text.SetFeather() 
        self.Bonus2Text.SetText("Efsun 2:") 
        self.Bonus2Text.SetFontColor(1.0, 1.0, 1.0) 
        self.Bonus2Text.SetOutline() 
        self.Bonus2Text.Show()     
         
        self.Bonus2AtrText = ui.TextLine() 
        self.Bonus2AtrText.SetParent(self.Board) 
        self.Bonus2AtrText.SetDefaultFontName() 
        self.Bonus2AtrText.SetPosition(65, 105 + 120 + 15) 
        self.Bonus2AtrText.SetFeather() 
        self.Bonus2AtrText.SetText("-") 
        self.Bonus2AtrText.SetFontColor(1.0, 1.0, 1.0) 
        self.Bonus2AtrText.SetOutline() 
        self.Bonus2AtrText.Show()     

        self.Bonus2ValueEditLine = ui.EditLine() 
        self.Bonus2ValueEditLine.SetParent(self.Board) 
        self.Bonus2ValueEditLine.SetSize(29, 18) 
        self.Bonus2ValueEditLine.SetPosition(240 - 29, 105 + 120 + 15) 
        self.Bonus2ValueEditLine.SetMax(4) 
        self.Bonus2ValueEditLine.SetNumberMode() 
        self.Bonus2ValueEditLine.SetText("0") 
        self.Bonus2ValueEditLine.Show() 
         
        self.Bonus2Button = ui.Button() 
        self.Bonus2Button.SetParent(self.Board) 
        self.Bonus2Button.SetUpVisual("d:/ymir work/ui/public/large_Button_01.sub") 
        self.Bonus2Button.SetOverVisual("d:/ymir work/ui/public/large_Button_02.sub") 
        self.Bonus2Button.SetDownVisual("d:/ymir work/ui/public/large_Button_03.sub") 
        self.Bonus2Button.SetText("Efsunlari Ayarla") 
        self.Bonus2Button.SetPosition(240, 105 + 120 + 10) 
        self.Bonus2Button.Show() 
         
        self.Bonus3Text = ui.TextLine() 
        self.Bonus3Text.SetParent(self.Board) 
        self.Bonus3Text.SetDefaultFontName() 
        self.Bonus3Text.SetPosition(15, 125 + 120 + 15) 
        self.Bonus3Text.SetFeather() 
        self.Bonus3Text.SetText("Efsun 3:") 
        self.Bonus3Text.SetFontColor(1.0, 1.0, 1.0) 
        self.Bonus3Text.SetOutline() 
        self.Bonus3Text.Show()     
         
        self.Bonus3AtrText = ui.TextLine() 
        self.Bonus3AtrText.SetParent(self.Board) 
        self.Bonus3AtrText.SetDefaultFontName() 
        self.Bonus3AtrText.SetPosition(65, 125 + 120 + 15) 
        self.Bonus3AtrText.SetFeather() 
        self.Bonus3AtrText.SetText("-") 
        self.Bonus3AtrText.SetFontColor(1.0, 1.0, 1.0) 
        self.Bonus3AtrText.SetOutline() 
        self.Bonus3AtrText.Show()     
         
        self.Bonus3ValueEditLine = ui.EditLine() 
        self.Bonus3ValueEditLine.SetParent(self.Board) 
        self.Bonus3ValueEditLine.SetSize(29, 18) 
        self.Bonus3ValueEditLine.SetPosition(240 - 29, 125 + 120 + 15) 
        self.Bonus3ValueEditLine.SetMax(4) 
        self.Bonus3ValueEditLine.SetNumberMode() 
        self.Bonus3ValueEditLine.SetText("0") 
        self.Bonus3ValueEditLine.Show() 

        self.Bonus3Button = ui.Button() 
        self.Bonus3Button.SetParent(self.Board) 
        self.Bonus3Button.SetUpVisual("d:/ymir work/ui/public/large_Button_01.sub") 
        self.Bonus3Button.SetOverVisual("d:/ymir work/ui/public/large_Button_02.sub") 
        self.Bonus3Button.SetDownVisual("d:/ymir work/ui/public/large_Button_03.sub") 
        self.Bonus3Button.SetText("Efsunlari Ayarla") 
        self.Bonus3Button.SetPosition(240, 125 + 120 + 10) 
        self.Bonus3Button.Show() 
         
        self.Bonus4Text = ui.TextLine() 
        self.Bonus4Text.SetParent(self.Board) 
        self.Bonus4Text.SetDefaultFontName() 
        self.Bonus4Text.SetPosition(15, 145 + 120 + 15) 
        self.Bonus4Text.SetFeather() 
        self.Bonus4Text.SetText("Efsun 4:") 
        self.Bonus4Text.SetFontColor(1.0, 1.0, 1.0) 
        self.Bonus4Text.SetOutline() 
        self.Bonus4Text.Show()     
         
        self.Bonus4AtrText = ui.TextLine() 
        self.Bonus4AtrText.SetParent(self.Board) 
        self.Bonus4AtrText.SetDefaultFontName() 
        self.Bonus4AtrText.SetPosition(65, 145 + 120 + 15) 
        self.Bonus4AtrText.SetFeather() 
        self.Bonus4AtrText.SetText("-") 
        self.Bonus4AtrText.SetFontColor(1.0, 1.0, 1.0) 
        self.Bonus4AtrText.SetOutline() 
        self.Bonus4AtrText.Show()     
         
        self.Bonus4ValueEditLine = ui.EditLine() 
        self.Bonus4ValueEditLine.SetParent(self.Board) 
        self.Bonus4ValueEditLine.SetSize(29, 18) 
        self.Bonus4ValueEditLine.SetPosition(240 - 29, 145 + 120 + 15) 
        self.Bonus4ValueEditLine.SetMax(4) 
        self.Bonus4ValueEditLine.SetNumberMode() 
        self.Bonus4ValueEditLine.SetText("0") 
        self.Bonus4ValueEditLine.Show() 
         
        self.Bonus4Button = ui.Button() 
        self.Bonus4Button.SetParent(self.Board) 
        self.Bonus4Button.SetUpVisual("d:/ymir work/ui/public/large_Button_01.sub") 
        self.Bonus4Button.SetOverVisual("d:/ymir work/ui/public/large_Button_02.sub") 
        self.Bonus4Button.SetDownVisual("d:/ymir work/ui/public/large_Button_03.sub") 
        self.Bonus4Button.SetText("Efsunlari Ayarla") 
        self.Bonus4Button.SetPosition(240, 145 + 120 + 10) 
        self.Bonus4Button.Show() 
         
        self.Bonus5Text = ui.TextLine() 
        self.Bonus5Text.SetParent(self.Board) 
        self.Bonus5Text.SetDefaultFontName() 
        self.Bonus5Text.SetPosition(15, 165 + 120 + 15) 
        self.Bonus5Text.SetFeather() 
        self.Bonus5Text.SetText("Efsun 5:") 
        self.Bonus5Text.SetFontColor(1.0, 1.0, 1.0) 
        self.Bonus5Text.SetOutline() 
        self.Bonus5Text.Show() 
         
        self.Bonus5AtrText = ui.TextLine() 
        self.Bonus5AtrText.SetParent(self.Board) 
        self.Bonus5AtrText.SetDefaultFontName() 
        self.Bonus5AtrText.SetPosition(65, 165 + 120 + 15) 
        self.Bonus5AtrText.SetFeather() 
        self.Bonus5AtrText.SetText("-") 
        self.Bonus5AtrText.SetFontColor(1.0, 1.0, 1.0) 
        self.Bonus5AtrText.SetOutline() 
        self.Bonus5AtrText.Show() 

        self.Bonus5ValueEditLine = ui.EditLine() 
        self.Bonus5ValueEditLine.SetParent(self.Board) 
        self.Bonus5ValueEditLine.SetSize(29, 18) 
        self.Bonus5ValueEditLine.SetPosition(240 - 29, 165 + 120 + 15) 
        self.Bonus5ValueEditLine.SetMax(4) 
        self.Bonus5ValueEditLine.SetNumberMode() 
        self.Bonus5ValueEditLine.SetText("0") 
        self.Bonus5ValueEditLine.Show() 
         
        self.Bonus5Button = ui.Button() 
        self.Bonus5Button.SetParent(self.Board) 
        self.Bonus5Button.SetUpVisual("d:/ymir work/ui/public/large_Button_01.sub") 
        self.Bonus5Button.SetOverVisual("d:/ymir work/ui/public/large_Button_02.sub") 
        self.Bonus5Button.SetDownVisual("d:/ymir work/ui/public/large_Button_03.sub") 
        self.Bonus5Button.SetText("Efsunlari Ayarla") 
        self.Bonus5Button.SetPosition(240, 165 + 120 + 10) 
        self.Bonus5Button.Show() 
         
        self.Bonus1ValueEditLine.SetTabEvent(ui.__mem_func__(self.Bonus2ValueEditLine.SetFocus)) 
        self.Bonus1ValueEditLine.SetReturnEvent(ui.__mem_func__(self.Bonus2ValueEditLine.SetFocus)) 
        self.Bonus2ValueEditLine.SetTabEvent(ui.__mem_func__(self.Bonus3ValueEditLine.SetFocus)) 
        self.Bonus2ValueEditLine.SetReturnEvent(ui.__mem_func__(self.Bonus3ValueEditLine.SetFocus)) 
        self.Bonus3ValueEditLine.SetTabEvent(ui.__mem_func__(self.Bonus4ValueEditLine.SetFocus)) 
        self.Bonus3ValueEditLine.SetReturnEvent(ui.__mem_func__(self.Bonus4ValueEditLine.SetFocus)) 
        self.Bonus4ValueEditLine.SetTabEvent(ui.__mem_func__(self.Bonus5ValueEditLine.SetFocus)) 
        self.Bonus4ValueEditLine.SetReturnEvent(ui.__mem_func__(self.Bonus5ValueEditLine.SetFocus)) 
         
        self.Bonus1Button.SetEvent(ui.__mem_func__(self.OpenBonusList1)) 
        self.Bonus2Button.SetEvent(ui.__mem_func__(self.OpenBonusList2)) 
        self.Bonus3Button.SetEvent(ui.__mem_func__(self.OpenBonusList3)) 
        self.Bonus4Button.SetEvent(ui.__mem_func__(self.OpenBonusList4)) 
        self.Bonus5Button.SetEvent(ui.__mem_func__(self.OpenBonusList5)) 
         
    def OpenBonusList1(self): 
        global CreateWhish0 
        CreateWhish0 = 1 
        self.CreateBonusListBox = CreateListDialog() 
         
    def OpenBonusList2(self): 
        global CreateWhish1 
        CreateWhish1 = 1 
        self.CreateBonusListBox = CreateListDialog() 
     
    def OpenBonusList3(self): 
        global CreateWhish2 
        CreateWhish2 = 1 
        self.CreateBonusListBox = CreateListDialog() 
     
    def OpenBonusList4(self): 
        global CreateWhish3 
        CreateWhish3 = 1 
        self.CreateBonusListBox = CreateListDialog() 

    def OpenBonusList5(self): 
        global CreateWhish4 
        CreateWhish4 = 1 
        self.CreateBonusListBox = CreateListDialog() 
         
    def Close(self): 
        self.Board = None 
         
    def OnUpdate(self): 
        global CreateBonus0 
        global CreateBonus1 
        global CreateBonus2 
        global CreateBonus3 
        global CreateBonus4 
        global ItemValue 
        global ChangedValue 
         
        if int(ItemValue) != int(self.ItemValueEditLine.GetText()) and ChangedValue == "TRUE": 
            self.ItemValueEditLine.SetText(str(ItemValue)) 
            ChangedValue = "FALSE" 
            self.SetItemValue() 
         
        if self.Bonus1AtrText.GetText() != str(BonusListe[int(CreateBonus0)]) and int(CreateBonus0) != 0: 
            self.Bonus1AtrText.SetText(str(BonusListe[int(CreateBonus0)])) 
        elif self.Bonus1AtrText.GetText() != "" and int(CreateBonus0) == 0: 
            self.Bonus1AtrText.SetText("-")         
        if self.Bonus2AtrText.GetText() != str(BonusListe[int(CreateBonus1)]) and int(CreateBonus1) != 0: 
            self.Bonus2AtrText.SetText(str(BonusListe[int(CreateBonus1)])) 
        elif self.Bonus2AtrText.GetText() != "" and int(CreateBonus1) == 0: 
            self.Bonus2AtrText.SetText("-")         
        if self.Bonus3AtrText.GetText() != str(BonusListe[int(CreateBonus2)]) and int(CreateBonus2) != 0: 
            self.Bonus3AtrText.SetText(str(BonusListe[int(CreateBonus2)])) 
        elif self.Bonus3AtrText.GetText() != "" and int(CreateBonus2) == 0: 
            self.Bonus3AtrText.SetText("-")         
        if self.Bonus4AtrText.GetText() != str(BonusListe[int(CreateBonus3)]) and int(CreateBonus3) != 0: 
            self.Bonus4AtrText.SetText(str(BonusListe[int(CreateBonus3)])) 
        elif self.Bonus4AtrText.GetText() != "" and int(CreateBonus3) == 0: 
            self.Bonus4AtrText.SetText("-")         
        if self.Bonus5AtrText.GetText() != str(BonusListe[int(CreateBonus4)]) and int(CreateBonus4) != 0: 
            self.Bonus5AtrText.SetText(str(BonusListe[int(CreateBonus4)])) 
        elif self.Bonus5AtrText.GetText() != "" and int(CreateBonus4) == 0: 
            self.Bonus5AtrText.SetText("-") 
         
    def CreateItem(self): 
        global CreateBonus0 
        global CreateBonus1 
        global CreateBonus2 
        global CreateBonus3 
        global CreateBonus4 
        global ItemValue 
        self.ItemCount = int(self.ItemCountEditLine.GetText()) 
        Value0 = self.Bonus1ValueEditLine.GetText() 
        Value1 = self.Bonus2ValueEditLine.GetText() 
        Value2 = self.Bonus3ValueEditLine.GetText() 
        Value3 = self.Bonus4ValueEditLine.GetText() 
        Value4 = self.Bonus5ValueEditLine.GetText() 
         
        for slot in xrange(player.INVENTORY_SLOT_COUNT): 
            state = "go" 
            if not player.isItem(int(slot)): 
                if int(slot) >= 5: 
                    if player.isItem(int(slot) - 5): 
                        itemIndex = player.GetItemIndex(int(slot) - 5) 
                        item.SelectItem(itemIndex) 
                        if int(item.GetItemSize()[1]) >= 2: 
                            state = "banned" 
            else: 
                state = "banned" 
            if str(state) == "go": 
                player.SetItemData(int(slot), int(ItemValue),int(self.ItemCount)) 
                player.SetItemAttribute(int(slot), 0, int(CreateBonus0), int(Value0)) 
                player.SetItemAttribute(int(slot), 1, int(CreateBonus1), int(Value1)) 
                player.SetItemAttribute(int(slot), 2, int(CreateBonus2), int(Value2)) 
                player.SetItemAttribute(int(slot), 3, int(CreateBonus3), int(Value3)) 
                player.SetItemAttribute(int(slot), 4, int(CreateBonus4), int(Value4)) 
                player.SetItemMetinSocket(int(slot), 0, int(self.MetinStone1)) 
                player.SetItemMetinSocket(int(slot), 1, int(self.MetinStone2)) 
                player.SetItemMetinSocket(int(slot), 2, int(self.MetinStone3)) 
                break 

    def CallItemList(self): 
        self.ItemListDialog = ItemListDialog()         
     
ChangedValue = "FALSE" 

class ItemListDialog(ui.Window): 
    def __init__(self): 
        ui.Window.__init__(self) 

        self.Board = ui.BoardWithTitleBar() 
        self.Board.SetSize(170, 335) 
        self.Board.SetCenterPosition() 
        self.Board.AddFlag("movable") 
        self.Board.AddFlag("float") 
        self.Board.SetTitleName("Esya Listesi") 
        self.Board.SetCloseEvent(self.Close) 
        self.Board.Show() 
         
        self.__Load_BindObject() 

        self.UpdateFileList() 
         
    def __del__(self): 
        ui.Window.__del__(self) 

    def Show(self): 
        ui.Window.Show(self) 

    def Close(self): 
        self.Board.Hide() 

    def OnPressEscapeKey(self): 
        self.Board.Close() 
        return TRUE 

    def __CreateFileListBox(self): 
        fileListBox = ui.ListBoxEx() 
        fileListBox.SetParent(self.Board) 
        fileListBox.SetPosition(15, 80) 
        fileListBox.Show() 
        return fileListBox 

    def __Load_BindObject(self): 
        self.fileListBox = self.__CreateFileListBox() 
        self.LoadFuckingScrollBar() 
        self.fileListBox.SetScrollBar(self.ScrollBar) 
     
        self.SelectBonus = ui.Button() 
        self.SelectBonus.SetParent(self.Board) 
        self.SelectBonus.SetPosition(19, 295) 
        self.SelectBonus.SetUpVisual("d:/ymir work/ui/public/Middle_Button_01.sub") 
        self.SelectBonus.SetOverVisual("d:/ymir work/ui/public/Middle_Button_02.sub") 
        self.SelectBonus.SetDownVisual("d:/ymir work/ui/public/Middle_Button_03.sub") 
        self.SelectBonus.SetText("Tamam") 
        self.SelectBonus.SetEvent(ui.__mem_func__(self.SetBonis)) 
        self.SelectBonus.Show() 

        self.CancelBonus = ui.Button() 
        self.CancelBonus.SetParent(self.Board) 
        self.CancelBonus.SetPosition(89, 295) 
        self.CancelBonus.SetUpVisual("d:/ymir work/ui/public/Middle_Button_01.sub") 
        self.CancelBonus.SetOverVisual("d:/ymir work/ui/public/Middle_Button_02.sub") 
        self.CancelBonus.SetDownVisual("d:/ymir work/ui/public/Middle_Button_03.sub") 
        self.CancelBonus.SetText("Kapat") 
        self.CancelBonus.SetEvent(ui.__mem_func__(self.Close)) 
        self.CancelBonus.Show() 
         
        self.SearchItemSlotBar = ui.SlotBar() 
        self.SearchItemSlotBar.SetParent(self.Board) 
        self.SearchItemSlotBar.SetSize(15*7, 14) 
        self.SearchItemSlotBar.SetPosition(15, 50) 
        self.SearchItemSlotBar.Show() 
         
        self.SearchItemEditLine = ui.EditLine() 
        self.SearchItemEditLine.SetParent(self.SearchItemSlotBar) 
        self.SearchItemEditLine.SetSize(15*7, 18) 
        self.SearchItemEditLine.SetPosition(3, 0) 
        self.SearchItemEditLine.SetMax(16) 
        self.SearchItemEditLine.SetText("") 
        self.SearchItemEditLine.SetFocus() 
        self.SearchItemEditLine.Show()         

        self.SearchItemButton = ui.Button() 
        self.SearchItemButton.SetParent(self.Board) 
        self.SearchItemButton.SetPosition(117, 48) 
        self.SearchItemButton.SetUpVisual("d:/ymir work/ui/public/small_Button_01.sub") 
        self.SearchItemButton.SetOverVisual("d:/ymir work/ui/public/small_Button_02.sub") 
        self.SearchItemButton.SetDownVisual("d:/ymir work/ui/public/small_Button_03.sub") 
        self.SearchItemButton.SetText("Ara") 
        self.SearchItemButton.SetEvent(ui.__mem_func__(self.SearchItem)) 
        self.SearchItemButton.Show() 
     
        self.SearchItemText = ui.TextLine() 
        self.SearchItemText.SetParent(self.Board) 
        self.SearchItemText.SetDefaultFontName() 
        self.SearchItemText.SetPosition(19, 33) 
        self.SearchItemText.SetFeather() 
        self.SearchItemText.SetText("Aranacak Esya:") 
        self.SearchItemText.SetFontColor(1.0, 1.0, 1.0) 
        self.SearchItemText.SetOutline() 
        self.SearchItemText.Show() 
     
    def LoadFuckingScrollBar(self): 
        self.ScrollBar = ui.ScrollBar() 
        self.ScrollBar.SetParent(self.Board) 
        self.ScrollBar.SetPosition(140, 70) 
        self.ScrollBar.SetScrollBarSize(220) 
        self.ScrollBar.Show() 

    def CancelGuildName(self): 
        self.guildNameBoard.Close() 
        self.guildNameBoard = None 
        return TRUE 

    def SearchItem(self): 
        self.__RefreshFileList() 
        SearchName = str(self.SearchItemEditLine.GetText()) 
        try: 
            lines = pack_open("locale/de/item_list.txt", "r").readlines() 
        except IOError: 
            import dbg 
            dbg.LogBox("Load Itemlist Error") 
            app.Abort() 

        for line in lines: 
            tokens = str(line).split("t") 
            if len(tokens) == 0 or not tokens[0]: 
                continue 
                 
            ItemValue = str(tokens[0]) 
            if str(ItemValue).find(" ") != -1: 
                ItemValue = str(ItemValue).replace(" ", "") 
            item.SelectItem(int(ItemValue)) 
            Itemname = str(item.GetItemName()) 
            if ItemValue and str(Itemname) != "": 
                if str(Itemname).find(str(SearchName)) != -1: 
                    self.fileListBox.AppendItem(Item(Itemname)) 
         
    def UpdateFileList(self): 
        self.__RefreshFileList() 
        try: 
            lines = pack_open("locale/de/item_list.txt", "r").readlines() 
        except IOError: 
            import dbg 
            dbg.LogBox("Load Itemlist Error") 
            app.Abort() 

        for line in lines: 
            tokens = str(line).split("t") 
            if len(tokens) == 0 or not tokens[0]: 
                continue 
                 
            ItemValue = str(tokens[0]) 
            if str(ItemValue).find(" ") != -1: 
                ItemValue = str(ItemValue).replace(" ", "") 
            item.SelectItem(int(ItemValue)) 
            Itemname = str(item.GetItemName()) 
            if ItemValue and str(Itemname) != "": 
                self.fileListBox.AppendItem(Item(Itemname)) 
         
    def __RefreshFileList(self): 
        self.fileListBox.RemoveAllItems() 
         
    def SetBonis(self): 
        global ItemValue 
        global ChangedValue 
        SelectedIndex = self.fileListBox.GetSelectedItem() 
        SelectedIndex = SelectedIndex.GetText() 
        try: 
            lines = pack_open("locale/de/item_list.txt", "r").readlines() 
        except IOError: 
            import dbg 
            dbg.LogBox("Load Itemlist Error") 
            app.Abort() 

        for line in lines: 
            tokens = str(line).split("t") 
            if len(tokens) == 0 or not tokens[0]: 
                continue 
                 
            Itemvalue = str(tokens[0]) 
            if str(Itemvalue).find(" ") != -1: 
                Itemvalue = str(Itemvalue).replace(" ", "") 
            item.SelectItem(int(Itemvalue)) 
            Itemname = str(item.GetItemName()) 
            if str(Itemname) == str(SelectedIndex): 
                ItemValue = int(Itemvalue) 
                break 
        ChangedValue = "TRUE" 
        self.Close() 
     
class CreateListDialog(ui.ThinBoard): 
    def __init__(self): 
        ui.ThinBoard.__init__(self) 

        self.isLoaded=0 
        self.selectEvent=None 
        self.fileListBox=None 

        self.SetCenterPosition() 
        self.SetSize(170, 305) 
        self.Show() 
        self.AddFlag("movable") 
        self.AddFlag("float") 
         
    def __del__(self): 
        ui.ThinBoard.__del__(self) 

    def Show(self): 
        if self.isLoaded==0: 
            self.isLoaded=1 

            self.__Load() 

        ui.ThinBoard.Show(self) 

    def Open(self): 
        self.Show() 

        self.SetCenterPosition() 
        self.SetTop() 
        self.UpdateFileList() 

    def Close(self): 
        self.Hide() 

    def OnPressEscapeKey(self): 
        self.Close() 
        return TRUE 

    def __CreateFileListBox(self): 
        fileListBox = ui.ListBoxEx() 
        fileListBox.SetParent(self) 
        fileListBox.SetPosition(15, 50) 
        fileListBox.Show() 
        return fileListBox 

    def __Load(self): 
        self.__Load_BindObject() 

        self.UpdateFileList() 

    def __Load_BindObject(self): 
        self.fileListBox = self.__CreateFileListBox() 
        self.LoadFuckingScrollBar() 
        self.LoadTextLines() 
        self.fileListBox.SetScrollBar(self.ScrollBar) 

        self.UpdateButton = ui.Button() 
        self.UpdateButton.SetParent(self) 
        self.UpdateButton.SetUpVisual("d:/ymir work/ui/public/Large_button_01.sub") 
        self.UpdateButton.SetOverVisual("d:/ymir work/ui/public/Large_button_02.sub") 
        self.UpdateButton.SetDownVisual("d:/ymir work/ui/public/Large_button_03.sub") 
        self.UpdateButton.SetText("Aktualisieren") 
        self.UpdateButton.SetPosition(15, 265) 
        self.UpdateButton.SetEvent(ui.__mem_func__(self.UpdateFileList)) 
        self.UpdateButton.Show() 
        self.UpdateButton.Hide() 
         
        self.SelectBonus = ui.Button() 
        self.SelectBonus.SetParent(self) 
        self.SelectBonus.SetPosition(19, 265) 
        self.SelectBonus.SetUpVisual("d:/ymir work/ui/public/Middle_Button_01.sub") 
        self.SelectBonus.SetOverVisual("d:/ymir work/ui/public/Middle_Button_02.sub") 
        self.SelectBonus.SetDownVisual("d:/ymir work/ui/public/Middle_Button_03.sub") 
        self.SelectBonus.SetText("Tamam") 
        self.SelectBonus.SetEvent(ui.__mem_func__(self.SetBonis)) 
        self.SelectBonus.Show() 

        self.CancelBonus = ui.Button() 
        self.CancelBonus.SetParent(self) 
        self.CancelBonus.SetPosition(89, 265) 
        self.CancelBonus.SetUpVisual("d:/ymir work/ui/public/Middle_Button_01.sub") 
        self.CancelBonus.SetOverVisual("d:/ymir work/ui/public/Middle_Button_02.sub") 
        self.CancelBonus.SetDownVisual("d:/ymir work/ui/public/Middle_Button_03.sub") 
        self.CancelBonus.SetText("Kapat") 
        self.CancelBonus.SetEvent(ui.__mem_func__(self.Close)) 
        self.CancelBonus.Show() 

         
    def LoadTextLines(self): 
        self.copyright = ui.TextLine() 
        self.copyright.SetParent(self) 
        self.copyright.SetDefaultFontName() 
        self.copyright.SetPosition(50, 29) 
        self.copyright.SetFeather() 
        self.copyright.SetText("Efsun Listesi:") 
        self.copyright.SetFontColor(0.2, 0.2, 1.0) 
        self.copyright.SetOutline() 
        self.copyright.Show() 

    def LoadFuckingScrollBar(self): 
        self.ScrollBar = ui.ScrollBar() 
        self.ScrollBar.SetParent(self) 
        self.ScrollBar.SetPosition(140, 40) 
        self.ScrollBar.SetScrollBarSize(220) 
        self.ScrollBar.Show() 

    def CancelGuildName(self): 
        self.guildNameBoard.Close() 
        self.guildNameBoard = None 
        return TRUE 

    def UpdateFileList(self): 
        self.__RefreshFileList() 
        for BonusType in BonusListe: 
            if BonusType == "": 
                self.fileListBox.AppendItem(Item("...")) 
            elif BonusType != "": 
                self.fileListBox.AppendItem(Item(BonusType)) 
            #chat.AppendChat(chat.CHAT_TYPE_INFO, str(BonusIDListe[BonusType]))         
         
    def __RefreshFileList(self): 
        self.fileListBox.RemoveAllItems() 
         
    def SetBonis(self): 
        global CreateBonus0 
        global CreateBonus1 
        global CreateBonus2 
        global CreateBonus3 
        global CreateBonus4 
        global CreateWhish0 
        global CreateWhish1 
        global CreateWhish2 
        global CreateWhish3 
        global CreateWhish4 
        SelectedIndex = self.fileListBox.GetSelectedItem() 
        SelectedIndex = SelectedIndex.GetText() 
        if str(SelectedIndex) != "keiner" and str(SelectedIndex) != "": 
            if CreateWhish0 == 1: 
                chat.AppendChat(chat.CHAT_TYPE_INFO, "1.Bonus " + str(SelectedIndex)) 
                CreateBonus0 = BonusIDListe[str(SelectedIndex)] 
                CreateWhish0 = 0 
            elif CreateWhish1 == 1: 
                chat.AppendChat(chat.CHAT_TYPE_INFO, "2.Bonus " + str(SelectedIndex)) 
                CreateBonus1 = int(BonusIDListe[SelectedIndex]) 
                CreateWhish1 = 0 
            elif CreateWhish2 == 1: 
                chat.AppendChat(chat.CHAT_TYPE_INFO, "3.Bonus " + str(SelectedIndex)) 
                CreateBonus2 = int(BonusIDListe[SelectedIndex]) 
                CreateWhish2 = 0 
            elif CreateWhish3 == 1: 
                chat.AppendChat(chat.CHAT_TYPE_INFO, "4.Bonus " + str(SelectedIndex)) 
                CreateBonus3 = int(BonusIDListe[SelectedIndex]) 
                CreateWhish3 = 0 
            elif CreateWhish4 == 1: 
                chat.AppendChat(chat.CHAT_TYPE_INFO, "5.Bonus " + str(SelectedIndex)) 
                CreateBonus4 = int(BonusIDListe[SelectedIndex]) 
                CreateWhish4 = 0 
                 
        elif str(SelectedIndex) == "keiner" and str(SelectedIndex) != "": 
            if CreateWhish0 == 1: 
                chat.AppendChat(chat.CHAT_TYPE_INFO, "1.Efsun basariyla olusturuldu.") 
                CreateBonus0 = 0 
                CreateWhish0 = 0 
            elif CreateWhish1 == 1: 
                chat.AppendChat(chat.CHAT_TYPE_INFO, "2.Efsun basariyla olusturuldu.") 
                CreateBonus1 = 0 
                CreateWhish1 = 0 
            elif CreateWhish2 == 1: 
                chat.AppendChat(chat.CHAT_TYPE_INFO, "3.Efsun basariyla olusturuldu.") 
                CreateBonus2 = 0 
                CreateWhish2 = 0 
            elif CreateWhish3 == 1: 
                chat.AppendChat(chat.CHAT_TYPE_INFO, "4.Efsun basariyla olusturuldu.") 
                CreateBonus3 = 0 
                CreateWhish3 = 0 
            elif CreateWhish4 == 1: 
                chat.AppendChat(chat.CHAT_TYPE_INFO, "5.Efsun basariyla olusturuldu.") 
                CreateBonus4 = 0 
                CreateWhish4 = 0     
                 
        else: 
            chat.AppendChat(chat.CHAT_TYPE_INFO, "Efsun secmediniz!")         
        self.Close() 

FILE_NAME_LEN = 40  

class Item(ui.ListBoxEx.Item): 
    def __init__(self, fileName): 
        ui.ListBoxEx.Item.__init__(self) 
        self.canLoad=0 
        self.text=fileName 
        self.textLine=self.__CreateTextLine(fileName[:FILE_NAME_LEN])           

    def __del__(self): 
        ui.ListBoxEx.Item.__del__(self) 

    def GetText(self): 
        return self.text 

    def SetSize(self, width, height): 
        ui.ListBoxEx.Item.SetSize(self, 6*len(self.textLine.GetText()) + 4, height) 

    def __CreateTextLine(self, fileName): 
        textLine=ui.TextLine() 
        textLine.SetParent(self) 
        textLine.SetPosition(0, 0) 
        textLine.SetText(fileName) 
        textLine.Show() 
        return textLine 
         
StartDialog = CreateItemDialog() 
StartDialog.Show()  