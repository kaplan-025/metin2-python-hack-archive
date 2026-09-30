import ui
import dbg
try:
    import locale
except:
    import localeInfo
    locale = localeInfo

import grp
import wndMgr
import app
import os
import uiCommon
import binascii

class Dialog1(ui.Window):

    def __init__(self):
        ui.Window.__init__(self)
        self.BOARD_SIZE = (170, 170)
        self.BOARD_TITLE = 'Window'
        self.NEW_STARTED = FALSE
        self.BuildWindow()
        self.ButtonList = []
        self.ToggleButtonList = []
        self.EditLineList = []
        self.TextLineList = []
        self.SliderBarList = []
        self.ImageList = []
        self.ThinBoardList = []
        self.ComboBoxList = []
        self.GaugeList = []
        self.ListBoxList = []
        self.itemDict = {}
        self.ThinResizeDict = {}

    def __del__(self):
        ui.Window.__del__(self)

    class BarMoveable(ui.DragButton):

        def __init__(self):
            ui.DragButton.__init__(self)
            self.AddFlag('movable')
            self.callbackEnable = TRUE
            self.eventMove = lambda : None
            self.bar = ui.Bar()
            self.bar.SetParent(self)
            self.bar.SetPosition(0, 0)
            self.bar.SetColor(1996488704)
            self.bar.Show()

        def __del__(self):
            ui.DragButton.__del__(self)
            self.eventMove = lambda : None

        def OnMouseOverIn(self):
            app.SetCursor(app.HVSIZE)

        def OnMouseOverOut(self):
            app.SetCursor(app.NORMAL)

        def RegisterWindow(self, layer):
            self.hWnd = wndMgr.RegisterDragButton(self, layer)

        def SetMoveEvent(self, event):
            self.eventMove = event

        def OnMove(self):
            if self.callbackEnable:
                self.eventMove()

        def SetBarSize(self, width, height):
            self.bar.SetSize(width, height)

    class ThinBoardMoveable(ui.ThinBoard):

        def __init__(self):
            ui.ThinBoard.__init__(self)
            self.AddFlag('movable')
            self.callbackEnable = TRUE
            self.eventMove = lambda : None
            self.comp = Component()

        def __del__(self):
            ui.ThinBoard.__del__(self)
            self.eventMove = lambda : None

        def OnMouseOverIn(self):
            app.SetCursor(app.HVSIZE)

        def OnMouseOverOut(self):
            app.SetCursor(app.NORMAL)

        def RegisterWindow(self, layer):
            self.hWnd = wndMgr.RegisterDragButton(self, layer)

        def SetMoveEvent(self, event):
            self.eventMove = event

        def OnMove(self):
            if self.callbackEnable:
                self.eventMove()

    class SliderBarMoveable(ui.SliderBar):

        def __init__(self):
            ui.SliderBar.__init__(self)
            self.AddFlag('movable')
            self.callbackEnable = TRUE
            self.eventMove = lambda : None
            self.comp = Component()
            self.textline = ui.TextLine()
            self.textline.SetParent(self)
            self.textline.SetPosition(40, -8)
            self.textline.Show()

        def __del__(self):
            ui.SliderBar.__del__(self)
            self.eventMove = lambda : None

        def OnMouseOverIn(self):
            app.SetCursor(app.HVSIZE)

        def OnMouseOverOut(self):
            app.SetCursor(app.NORMAL)

        def RegisterWindow(self, layer):
            self.hWnd = wndMgr.RegisterDragButton(self, layer)

        def SetMoveEvent(self, event):
            self.eventMove = event

        def OnMove(self):
            if self.callbackEnable:
                self.eventMove()

        def SetText(self, text):
            self.textline.SetText(text)

    class TextLineMoveable(ui.TextLine):

        def __init__(self):
            ui.TextLine.__init__(self)
            self.AddFlag('movable')
            self.callbackEnable = TRUE
            self.eventMove = lambda : None
            self.textline = None
            return

        def __del__(self):
            ui.TextLine.__del__(self)
            self.eventMove = lambda : None

        def OnMouseOverIn(self):
            app.SetCursor(app.HVSIZE)

        def OnMouseOverOut(self):
            app.SetCursor(app.NORMAL)

        def RegisterWindow(self, layer):
            self.hWnd = wndMgr.RegisterDragButton(self, layer)

        def SetMoveEvent(self, event):
            self.eventMove = event

        def OnMove(self):
            if self.callbackEnable:
                self.eventMove()

        def SetText(self, text):
            self.textline = ui.TextLine()
            self.textline.SetParent(self)
            self.textline.SetPosition(0, 0)
            self.textline.SetText(text)
            self.textline.Show()

        def SetFontColor(self, red, green, blue):
            self.textline.SetFontColor(red, green, blue)

    class EditLineMoveable(ui.EditLine):

        def __init__(self):
            ui.EditLine.__init__(self)
            self.AddFlag('movable')
            self.callbackEnable = TRUE
            self.eventMove = lambda : None
            self.textline = None
            self.length = 10
            self.SlotBar = ui.SlotBar()
            self.SlotBar.SetParent(self)
            self.SlotBar.SetPosition(0, 0)
            self.SlotBar.Show()
            return

        def __del__(self):
            ui.EditLine.__del__(self)
            self.eventMove = lambda : None

        def OnMouseOverIn(self):
            app.SetCursor(app.HVSIZE)

        def OnMouseOverOut(self):
            app.SetCursor(app.NORMAL)

        def RegisterWindow(self, layer):
            self.hWnd = wndMgr.RegisterDragButton(self, layer)

        def SetMoveEvent(self, event):
            self.eventMove = event

        def OnMove(self):
            if self.callbackEnable:
                self.eventMove()

        def SetText(self, text):
            self.textline = ui.EditLine()
            self.textline.SetParent(self.SlotBar)
            self.textline.SetPosition(5, 1)
            self.textline.SetText(text)
            self.textline.Show()

        def SetMaxLength(self, length, height):
            width = length * 5 + 10
            self.SlotBar.SetSize(width, 15 * height)

    class ComboBoxMoveable(ui.ComboBox):

        def __init__(self):
            ui.ComboBox.__init__(self)
            self.AddFlag('movable')
            self.callbackEnable = TRUE
            self.eventMove = lambda : None
            self.textline = None
            return

        def __del__(self):
            ui.ComboBox.__del__(self)
            self.eventMove = lambda : None

        def OnMouseOverIn(self):
            app.SetCursor(app.HVSIZE)

        def OnMouseOverOut(self):
            app.SetCursor(app.NORMAL)

        def RegisterWindow(self, layer):
            self.hWnd = wndMgr.RegisterDragButton(self, layer)

        def SetMoveEvent(self, event):
            self.eventMove = event

        def OnMove(self):
            if self.callbackEnable:
                self.eventMove()

    class GaugeMoveable(ui.Gauge):

        def __init__(self):
            ui.Gauge.__init__(self)
            self.AddFlag('movable')
            self.callbackEnable = TRUE
            self.eventMove = lambda : None
            self.comp = Component()
            self.textline = ui.TextLine()
            self.textline.SetParent(self)
            self.textline.SetPosition(30, -12)
            self.textline.Show()

        def __del__(self):
            ui.Gauge.__del__(self)
            self.eventMove = lambda : None

        def OnMouseOverIn(self):
            app.SetCursor(app.HVSIZE)

        def OnMouseOverOut(self):
            app.SetCursor(app.NORMAL)

        def RegisterWindow(self, layer):
            self.hWnd = wndMgr.RegisterDragButton(self, layer)

        def SetMoveEvent(self, event):
            self.eventMove = event

        def OnMove(self):
            if self.callbackEnable:
                self.eventMove()

        def SetText(self, text):
            self.textline.SetText(text)

    def BuildWindow(self):
        self.Window = ui.BoardWithTitleBar()
        self.WindowType = 'BoardWithTitleBar'
        self.comp = Component()
        self.debugBoard = self.comp.ThinBoard(None, FALSE, 370, 1, 220, 40, FALSE)
        self.debugBoard_title = self.comp.TextLine(self.debugBoard, 'DEBUG', 15, 5, self.comp.RGB(255, 0, 0))
        self.debugBoard_text = self.comp.TextLine(self.debugBoard, '-', 15, 20, None)
        self.prjBoard = self.comp.ThinBoard(None, FALSE, 50, 1, 320, 50, FALSE)
        self.toolbox_title = self.comp.TextLine(self.prjBoard, binascii.a2b_base64('R3VpIEVkaXRvciAxLjMgLSBDcmVhdGVkIGJ5IEthTWVSMTMzNw=='), 15, 5, self.comp.RGB(255, 0, 0))
        self.toolbox_new = self.comp.Button(self.prjBoard, 'new', 'Create New Window', 10, 20, self.CreateWindow, self.comp.SMALL_BUTTON['default'], self.comp.SMALL_BUTTON['over'], self.comp.SMALL_BUTTON['down'])
        self.toolbox_load = self.comp.Button(self.prjBoard, 'load proj', 'Load Project', 55, 20, self.LoadProject, self.comp.MIDDLE_BUTTON['default'], self.comp.MIDDLE_BUTTON['over'], self.comp.MIDDLE_BUTTON['down'])
        self.toolbox_project = self.comp.Button(self.prjBoard, 'save proj', 'Save Project', 118, 20, self.SaveProject, self.comp.MIDDLE_BUTTON['default'], self.comp.MIDDLE_BUTTON['over'], self.comp.MIDDLE_BUTTON['down'])
        self.toolbox_save = self.comp.Button(self.prjBoard, 'save py', 'Save to Python', 182, 20, self.SaveToPy, self.comp.MIDDLE_BUTTON['default'], self.comp.MIDDLE_BUTTON['over'], self.comp.MIDDLE_BUTTON['down'])
        self.toolbox_preview = self.comp.Button(self.prjBoard, 'preview', '', 245, 20, self.Preview, self.comp.MIDDLE_BUTTON['default'], self.comp.MIDDLE_BUTTON['over'], self.comp.MIDDLE_BUTTON['down'])
        self.toolbox_project.Disable()
        self.toolbox_project.Down()
        self.toolbox_save.Disable()
        self.toolbox_save.Down()
        self.toolbox_preview.Disable()
        self.toolbox_preview.Down()
        self.toolBox = self.comp.ThinBoard(None, FALSE, 50, 50, 80, 240, FALSE)
        self.toolBox.Hide()
        self.toolBoxTitle = self.comp.TextLine(self.toolBox, 'Toolbox', 10, 5, self.comp.RGB(255, 0, 0))
        self.toolbox_button = self.comp.Button(self.toolBox, 'button', 'Button', 10, 20, self.ChooseButton, self.comp.MIDDLE_BUTTON['default'], self.comp.MIDDLE_BUTTON['over'], self.comp.MIDDLE_BUTTON['down'])
        self.toolbox_togglebutton = self.comp.Button(self.toolBox, 'toggle btn', 'CheckBox', 10, 40, self.ChooseToggleButton, self.comp.MIDDLE_BUTTON['default'], self.comp.MIDDLE_BUTTON['over'], self.comp.MIDDLE_BUTTON['down'])
        self.toolbox_editline = self.comp.Button(self.toolBox, 'EditLine', 'TextBox', 10, 60, self.ChooseEditLine, self.comp.MIDDLE_BUTTON['default'], self.comp.MIDDLE_BUTTON['over'], self.comp.MIDDLE_BUTTON['down'])
        self.toolbox_textline = self.comp.Button(self.toolBox, 'TextLine', 'Text', 10, 80, self.CreateTextLine, self.comp.MIDDLE_BUTTON['default'], self.comp.MIDDLE_BUTTON['over'], self.comp.MIDDLE_BUTTON['down'])
        self.toolbox_sliderbar = self.comp.Button(self.toolBox, 'SliderBar', 'TrackBar', 10, 100, self.CreateSliderBar, self.comp.MIDDLE_BUTTON['default'], self.comp.MIDDLE_BUTTON['over'], self.comp.MIDDLE_BUTTON['down'])
        self.toolbox_image = self.comp.Button(self.toolBox, 'Image', '', 10, 120, self.CreateImage, self.comp.MIDDLE_BUTTON['default'], self.comp.MIDDLE_BUTTON['over'], self.comp.MIDDLE_BUTTON['down'])
        self.toolbox_combo = self.comp.Button(self.toolBox, 'ComboBox', '', 10, 140, self.CreateComboBox, self.comp.MIDDLE_BUTTON['default'], self.comp.MIDDLE_BUTTON['over'], self.comp.MIDDLE_BUTTON['down'])
        self.toolbox_thin = self.comp.Button(self.toolBox, 'ThinBoard', 'GroupBox', 10, 160, self.CreateThinBoard, self.comp.MIDDLE_BUTTON['default'], self.comp.MIDDLE_BUTTON['over'], self.comp.MIDDLE_BUTTON['down'])
        self.toolbox_gauge = self.comp.Button(self.toolBox, 'Gauge', 'Progress bar', 10, 180, self.CreateGauge, self.comp.MIDDLE_BUTTON['default'], self.comp.MIDDLE_BUTTON['over'], self.comp.MIDDLE_BUTTON['down'])
        self.toolbox_listbox = self.comp.Button(self.toolBox, 'ListBoxEx', '', 10, 200, self.CreateListBox, self.comp.MIDDLE_BUTTON['default'], self.comp.MIDDLE_BUTTON['over'], self.comp.MIDDLE_BUTTON['down'])
        self.wndType = self.comp.ThinBoard(None, FALSE, 50, 50, 110, 120, FALSE)
        self.wndType.Hide()
        self.wndType_title = self.comp.TextLine(self.wndType, 'Window Type', 15, 5, self.comp.RGB(255, 0, 0))
        self.wndType_thin = self.comp.Button(self.wndType, 'ThinBoard', '', 10, 20, lambda arg = 'ThinBoard': self.CreateWindow2(arg), self.comp.LARGE_BUTTON['default'], self.comp.LARGE_BUTTON['over'], self.comp.LARGE_BUTTON['down'])
        self.wndType_board = self.comp.Button(self.wndType, 'Board', '', 10, 40, lambda arg = 'Board': self.CreateWindow2(arg), self.comp.LARGE_BUTTON['default'], self.comp.LARGE_BUTTON['over'], self.comp.LARGE_BUTTON['down'])
        self.wndType_boardwithtitle = self.comp.Button(self.wndType, 'BoardWithTitle', '', 10, 60, lambda arg = 'BoardWithTitleBar': self.CreateWindow2(arg), self.comp.LARGE_BUTTON['default'], self.comp.LARGE_BUTTON['over'], self.comp.LARGE_BUTTON['down'])
        self.wndType_cancel = self.comp.Button(self.wndType, 'Cancel', '', 10, 90, self.CreateWindowCancel, self.comp.LARGE_BUTTON['default'], self.comp.LARGE_BUTTON['over'], self.comp.LARGE_BUTTON['down'])
        self.btnType = self.comp.ThinBoard(None, TRUE, 50, 290, 160, 240, FALSE)
        self.btnType.Hide()
        self.btnType_NameTxt = self.comp.TextLine(self.btnType, 'btn ID:', 10, 20, None)
        self.slotType_NameEdit, self.btnType_NameEdit = self.comp.EditLine(self.btnType, '', 60, 20, 60, 15, 30)
        self.btnType_NameTxt2 = self.comp.TextLine(self.btnType, 'btn Name:', 10, 40, None)
        self.slotType_NameEdit2, self.btnType_NameEdit2 = self.comp.EditLine(self.btnType, '', 60, 40, 60, 15, 30)
        self.btnType_Title = self.comp.TextLine(self.btnType, 'Button', 10, 5, self.comp.RGB(255, 0, 0))
        self.btnType_small = self.comp.Button(self.btnType, 'Small', '', 70, 60, lambda df = self.comp.SMALL_BUTTON['default'], o = self.comp.SMALL_BUTTON['over'], d = self.comp.SMALL_BUTTON['down'], c = FALSE: self.CreateButton(df, o, d, c), self.comp.SMALL_BUTTON['default'], self.comp.SMALL_BUTTON['over'], self.comp.SMALL_BUTTON['down'])
        self.btnType_medium = self.comp.Button(self.btnType, 'Middle', '', 10, 60, lambda df = self.comp.MIDDLE_BUTTON['default'], o = self.comp.MIDDLE_BUTTON['over'], d = self.comp.MIDDLE_BUTTON['down'], c = FALSE: self.CreateButton(df, o, d, c), self.comp.MIDDLE_BUTTON['default'], self.comp.MIDDLE_BUTTON['over'], self.comp.MIDDLE_BUTTON['down'])
        self.btnType_large = self.comp.Button(self.btnType, 'Large', '', 10, 80, lambda df = self.comp.LARGE_BUTTON['default'], o = self.comp.LARGE_BUTTON['over'], d = self.comp.LARGE_BUTTON['down'], c = FALSE: self.CreateButton(df, o, d, c), self.comp.LARGE_BUTTON['default'], self.comp.LARGE_BUTTON['over'], self.comp.LARGE_BUTTON['down'])
        self.btnType_x = self.comp.Button(self.btnType, '', '', 115, 63, lambda df = self.comp.CLOSE_BUTTON['default'], o = self.comp.CLOSE_BUTTON['over'], d = self.comp.CLOSE_BUTTON['down'], c = FALSE: self.CreateButton(df, o, d, c), self.comp.CLOSE_BUTTON['default'], self.comp.CLOSE_BUTTON['over'], self.comp.CLOSE_BUTTON['down'])
        self.btnType_min = self.comp.Button(self.btnType, '', '', 115, 83, lambda df = self.comp.MIN_BUTTON['default'], o = self.comp.MIN_BUTTON['over'], d = self.comp.MIN_BUTTON['down'], c = FALSE: self.CreateButton(df, o, d, c), self.comp.MIN_BUTTON['default'], self.comp.MIN_BUTTON['over'], self.comp.MIN_BUTTON['down'])
        self.btnType_cancel = self.comp.Button(self.btnType, 'Cancel', '', 10, 210, lambda : self.btnType.Hide(), self.comp.LARGE_BUTTON['default'], self.comp.LARGE_BUTTON['over'], self.comp.LARGE_BUTTON['down'])
        self.btnTypeCustom = self.comp.TextLine(self.btnType, 'Custom Images', 10, 105, self.comp.RGB(0, 0, 255))
        self.btnTypeCustom_d = self.comp.TextLine(self.btnType, 'default', 10, 125, None)
        self.slotType_CustomEdit_d, self.btnType_CustomEdit_d = self.comp.EditLine(self.btnType, 'guieditor/buttons/sprite_middle1.sub', 50, 125, 100, 15, 50)
        self.btnTypeCustom_o = self.comp.TextLine(self.btnType, 'over', 10, 145, None)
        self.slotType_CustomEdit_o, self.btnType_CustomEdit_o = self.comp.EditLine(self.btnType, 'guieditor/buttons/sprite_middle2.sub', 50, 145, 100, 15, 50)
        self.btnTypeCustom_dn = self.comp.TextLine(self.btnType, 'down', 10, 165, None)
        self.slotType_CustomEdit_dn, self.btnType_CustomEdit_dn = self.comp.EditLine(self.btnType, 'guieditor/buttons/sprite_middle3.sub', 50, 165, 100, 15, 50)
        self.btnType_CustomOk = self.comp.Button(self.btnType, 'Custom', '', 50, 185, lambda df = self.comp.LARGE_BUTTON['default'], o = self.comp.LARGE_BUTTON['over'], d = self.comp.LARGE_BUTTON['down'], c = TRUE: self.CreateButton(df, o, d, c), self.comp.SMALL_BUTTON['default'], self.comp.SMALL_BUTTON['over'], self.comp.SMALL_BUTTON['down'])
        self.btnType_CustomEdit_d.SetReturnEvent(ui.__mem_func__(self.btnType_CustomEdit_o.SetFocus))
        self.btnType_CustomEdit_o.SetReturnEvent(ui.__mem_func__(self.btnType_CustomEdit_dn.SetFocus))
        self.togglebtnType = self.comp.ThinBoard(None, TRUE, 50, 290, 160, 240, FALSE)
        self.togglebtnType.Hide()
        self.togglebtnType_NameTxt = self.comp.TextLine(self.togglebtnType, 'Tbtn ID:', 10, 20, None)
        self.toggleslotType_NameEdit, self.togglebtnType_NameEdit = self.comp.EditLine(self.togglebtnType, '', 60, 20, 60, 15, 30)
        self.togglebtnType_NameTxt2 = self.comp.TextLine(self.togglebtnType, 'Tbtn Name:', 10, 40, None)
        self.toggleslotType_NameEdit2, self.togglebtnType_NameEdit2 = self.comp.EditLine(self.togglebtnType, '', 60, 40, 60, 15, 30)
        self.togglebtnType_Title = self.comp.TextLine(self.togglebtnType, 'Toggle Button', 10, 5, self.comp.RGB(255, 0, 0))
        self.togglebtnType_small = self.comp.Button(self.togglebtnType, 'Small', '', 70, 60, lambda df = self.comp.SMALL_BUTTON['default'], o = self.comp.SMALL_BUTTON['over'], d = self.comp.SMALL_BUTTON['down'], c = FALSE: self.CreateToggleButton(df, o, d, c), self.comp.SMALL_BUTTON['default'], self.comp.SMALL_BUTTON['over'], self.comp.SMALL_BUTTON['down'])
        self.togglebtnType_medium = self.comp.Button(self.togglebtnType, 'Middle', '', 10, 60, lambda df = self.comp.MIDDLE_BUTTON['default'], o = self.comp.MIDDLE_BUTTON['over'], d = self.comp.MIDDLE_BUTTON['down'], c = FALSE: self.CreateToggleButton(df, o, d, c), self.comp.MIDDLE_BUTTON['default'], self.comp.MIDDLE_BUTTON['over'], self.comp.MIDDLE_BUTTON['down'])
        self.togglebtnType_large = self.comp.Button(self.togglebtnType, 'Large', '', 10, 80, lambda df = self.comp.LARGE_BUTTON['default'], o = self.comp.LARGE_BUTTON['over'], d = self.comp.LARGE_BUTTON['down'], c = FALSE: self.CreateToggleButton(df, o, d, c), self.comp.LARGE_BUTTON['default'], self.comp.LARGE_BUTTON['over'], self.comp.LARGE_BUTTON['down'])
        self.togglebtnType_x = self.comp.Button(self.togglebtnType, '', '', 115, 63, lambda df = self.comp.CLOSE_BUTTON['default'], o = self.comp.CLOSE_BUTTON['over'], d = 'd:/ymir work/ui/public/check_image.sub', c = FALSE: self.CreateToggleButton(df, o, d, c), self.comp.CLOSE_BUTTON['default'], self.comp.CLOSE_BUTTON['over'], self.comp.CLOSE_BUTTON['down'])
        self.togglebtnType_cancel = self.comp.Button(self.togglebtnType, 'Cancel', '', 10, 210, lambda : self.togglebtnType.Hide(), self.comp.LARGE_BUTTON['default'], self.comp.LARGE_BUTTON['over'], self.comp.LARGE_BUTTON['down'])
        self.togglebtnTypeCustom = self.comp.TextLine(self.togglebtnType, 'Custom Images', 10, 105, self.comp.RGB(0, 0, 255))
        self.togglebtnTypeCustom_d = self.comp.TextLine(self.togglebtnType, 'default', 10, 125, None)
        self.toggleslotType_CustomEdit_d, self.togglebtnType_CustomEdit_d = self.comp.EditLine(self.togglebtnType, 'guieditor/buttons/new_checkbox_default.sub', 50, 125, 100, 15, 50)
        self.togglebtnTypeCustom_o = self.comp.TextLine(self.togglebtnType, 'over', 10, 145, None)
        self.toggleslotType_CustomEdit_o, self.togglebtnType_CustomEdit_o = self.comp.EditLine(self.togglebtnType, 'guieditor/buttons/new_checkbox_over.sub', 50, 145, 100, 15, 50)
        self.togglebtnTypeCustom_dn = self.comp.TextLine(self.togglebtnType, 'down', 10, 165, None)
        self.toggleslotType_CustomEdit_dn, self.togglebtnType_CustomEdit_dn = self.comp.EditLine(self.togglebtnType, 'guieditor/buttons/new_checkbox_down.sub', 50, 165, 100, 15, 50)
        self.togglebtnType_CustomOk = self.comp.Button(self.togglebtnType, 'Custom', '', 50, 185, lambda df = self.comp.LARGE_BUTTON['default'], o = self.comp.LARGE_BUTTON['over'], d = self.comp.LARGE_BUTTON['down'], c = TRUE: self.CreateToggleButton(df, o, d, c), self.comp.SMALL_BUTTON['default'], self.comp.SMALL_BUTTON['over'], self.comp.SMALL_BUTTON['down'])
        self.togglebtnType_CustomEdit_d.SetReturnEvent(ui.__mem_func__(self.togglebtnType_CustomEdit_o.SetFocus))
        self.togglebtnType_CustomEdit_o.SetReturnEvent(ui.__mem_func__(self.togglebtnType_CustomEdit_dn.SetFocus))
        self.addImageBoard = self.comp.ThinBoard(None, TRUE, 50, 290, 180, 110, FALSE)
        self.addImage_title = self.comp.TextLine(self.addImageBoard, 'Add Image', 20, 10, self.comp.RGB(255, 0, 0))
        self.addImageBoard.Hide()
        self.NameImg = self.comp.TextLine(self.addImageBoard, 'Name', 20, 30, None)
        self.slotbar_img1, self.img1 = self.comp.EditLine(self.addImageBoard, 'img1', 80, 30, 90, 15, 30)
        self.ImgPath = self.comp.TextLine(self.addImageBoard, 'ImagePath', 20, 50, None)
        self.slotbar_img2, self.img2 = self.comp.EditLine(self.addImageBoard, 'guieditor/metin2.jpg', 80, 50, 90, 15, 80)
        self.img_ok = self.comp.Button(self.addImageBoard, 'Ok', '', 30, 75, self.CreateImageOk, 'd:/ymir work/ui/public/small_button_01.sub', 'd:/ymir work/ui/public/small_button_02.sub', 'd:/ymir work/ui/public/small_button_03.sub')
        self.img_cancel = self.comp.Button(self.addImageBoard, 'Cancel', '', 95, 75, self.CreateImageCancel, 'd:/ymir work/ui/public/small_button_01.sub', 'd:/ymir work/ui/public/small_button_02.sub', 'd:/ymir work/ui/public/small_button_03.sub')
        self.textLineColorBoard = self.comp.ThinBoard(None, TRUE, 50, 290, 200, 150, FALSE)
        self.textLineColorBoard.Hide()
        self.textLineColor_title = self.comp.TextLine(self.textLineColorBoard, 'Text ID', 10, 10, None)
        self.slotbar_color_edit1, self.color_edit1 = self.comp.EditLine(self.textLineColorBoard, '', 70, 10, 50, 15, 30)
        self.textLineColor_title2 = self.comp.TextLine(self.textLineColorBoard, 'Text Name', 10, 30, None)
        self.slotbar_color_edit2, self.color_edit2 = self.comp.EditLine(self.textLineColorBoard, 'Text', 70, 30, 90, 15, 30)
        self.slider_color1 = self.comp.SliderBar(self.textLineColorBoard, 255.0, self.SetTextLineColor, 10, 55)
        self.slider_color2 = self.comp.SliderBar(self.textLineColorBoard, 255.0, self.SetTextLineColor, 10, 75)
        self.slider_color3 = self.comp.SliderBar(self.textLineColorBoard, 255.0, self.SetTextLineColor, 10, 95)
        self.color_ok = self.comp.Button(self.textLineColorBoard, 'Ok', '', 30, 120, self.CreateTextLineOk, 'd:/ymir work/ui/public/small_button_01.sub', 'd:/ymir work/ui/public/small_button_02.sub', 'd:/ymir work/ui/public/small_button_03.sub')
        self.color_cancel = self.comp.Button(self.textLineColorBoard, 'Cancel', '', 95, 120, self.CreateTextLineCancel, 'd:/ymir work/ui/public/small_button_01.sub', 'd:/ymir work/ui/public/small_button_02.sub', 'd:/ymir work/ui/public/small_button_03.sub')
        self.color_r = 255
        self.color_g = 255
        self.color_b = 255
        self.color = self.comp.RGB(255, 255, 255)
        self.wndTextLine = self.comp.ThinBoard(None, TRUE, 50, 290, 160, 150, FALSE)
        self.wndTextLine.Hide()
        self.wndText_id = self.comp.TextLine(self.wndTextLine, 'Text ID', 10, 28, None)
        self.slotbar_wndText_editid, self.wndText_editid = self.comp.EditLine(self.wndTextLine, '', 70, 27, 60, 15, 30)
        self.wndText_name = self.comp.TextLine(self.wndTextLine, 'Text Name', 10, 51, None)
        self.slotbar_wndText_editname, self.wndText_editname = self.comp.EditLine(self.wndTextLine, '', 70, 52, 60, 15, 30)
        self.TextLine = self.comp.TextLine(self.wndTextLine, 'EditLine', 10, 7, self.comp.RGB(255, 0, 0))
        self.wndText_maxi = self.comp.TextLine(self.wndTextLine, 'Max', 10, 71, None)
        self.slotbar_wndText_max, self.wndText_max = self.comp.EditLine(self.wndTextLine, '10', 70, 72, 60, 15, 30)
        self.wndText_linesi = self.comp.TextLine(self.wndTextLine, 'Lines', 10, 91, None)
        self.slotbar_wndText_lines, self.wndText_lines = self.comp.EditLine(self.wndTextLine, '1', 70, 92, 60, 15, 30)
        self.wndText_lines.SetNumberMode()
        self.wndText_btnOk = self.comp.Button(self.wndTextLine, 'Ok', '', 10, 120, self.CreateEditLine, 'd:/ymir work/ui/public/middle_button_01.sub', 'd:/ymir work/ui/public/middle_button_02.sub', 'd:/ymir work/ui/public/middle_button_03.sub')
        self.wndText_btnCancel = self.comp.Button(self.wndTextLine, 'Cancel', '', 75, 120, lambda : self.wndTextLine.Hide(), 'd:/ymir work/ui/public/middle_button_01.sub', 'd:/ymir work/ui/public/middle_button_02.sub', 'd:/ymir work/ui/public/middle_button_03.sub')
        self.toolBoxList = self.comp.ThinBoard(None, FALSE, 590, 1, 130, 220, FALSE)
        self.toolBoxList.Hide()
        self.litems = self.comp.TextLine(self.toolBoxList, 'Item ID List', 10, 5, self.comp.RGB(255, 0, 0))
        self.ListBox = ui.ListBoxEx()
        self.ListBox.SetParent(self.toolBoxList)
        self.ListBox.SetPosition(10, 20)
        self.ListBox.SetSize(130, 220)
        self.ListBox.SetViewItemCount(10)
        self.ListBox.SetSelectEvent(self.ListBoxItemSelected)
        self.ListBox.Show()
        self.scroll = ui.ScrollBar()
        self.scroll.SetParent(self.ListBox)
        self.scroll.SetPosition(105, 0)
        self.scroll.SetScrollBarSize(200)
        self.scroll.Show()
        self.ListBox.SetScrollBar(self.scroll)
        return

    def ImageComboBox_Function(self, index):
        pass

    def ListBoxItemSelected(self, arg):
        SelectedText = arg.GetText().split(': ')
        self.wndEdit = self.comp.ThinBoard(None, FALSE, 590, 220, 130, 100, FALSE)
        self.wndEdit_Delete = self.comp.Button(self.wndEdit, 'Delete', '', 19, 32, lambda a = SelectedText[0], b = SelectedText[1]: self.DeleteSelected(a, b), 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
        self.wndEdit_Edit = self.comp.Button(self.wndEdit, 'Edit', '', 19, 63, lambda a = SelectedText[0], b = SelectedText[1]: self.EditSelected(a, b), 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
        self.wndEdit_Close = self.comp.Button(self.wndEdit, '', 'Hide', 108, 9, lambda : self.wndEdit.Hide(), 'd:/ymir work/ui/public/close_button_01.sub', 'd:/ymir work/ui/public/close_button_02.sub', 'd:/ymir work/ui/public/close_button_03.sub')
        self.wndEdit_Edit.Disable()
        self.wndEdit_Edit.Down()
        return

    def DeleteSelected(self, type1, id):
        i = 0
        if type1 == 'Button':
            for Data in self.ButtonList:
                if Data['NAME'] == id:
                    self.itemDict[self.ButtonList[i]['NAME']].Hide()
                    self.ButtonList.remove(self.ButtonList[i])
                    break
                i += 1

        elif type1 == 'TButton':
            for Data in self.ToggleButtonList:
                if Data['NAME'] == id:
                    self.itemDict[self.ToggleButtonList[i]['NAME']].Hide()
                    self.ToggleButtonList.remove(self.ToggleButtonList[i])
                    break
                i += 1

        elif type1 == 'TextLine':
            for Data in self.TextLineList:
                if Data['NAME'] == id:
                    self.itemDict[self.TextLineList[i]['NAME']].Hide()
                    self.TextLineList.remove(self.TextLineList[i])
                    break
                i += 1

        elif type1 == 'EditLine':
            for Data in self.EditLineList:
                if Data['NAME'] == id:
                    self.itemDict[self.EditLineList[i]['NAME']].Hide()
                    self.EditLineList.remove(self.EditLineList[i])
                    break
                i += 1

        elif type1 == 'SliderBar':
            for Data in self.SliderBarList:
                if Data['NAME'] == id:
                    self.itemDict[self.SliderBarList[i]['NAME']].Hide()
                    self.SliderBarList.remove(self.SliderBarList[i])
                    break
                i += 1

        elif type1 == 'Image':
            for Data in self.ImageList:
                if Data['NAME'] == id:
                    self.itemDict[self.ImageList[i]['NAME']].Hide()
                    self.ImageList.remove(self.ImageList[i])
                    break
                i += 1

        elif type1 == 'ComboBox':
            for Data in self.ComboBoxList:
                if Data['NAME'] == id:
                    self.itemDict[self.ComboBoxList[i]['NAME']].Hide()
                    self.ComboBoxList.remove(self.ComboBoxList[i])
                    break
                i += 1

        elif type1 == 'Thin':
            for Data in self.ThinBoardList:
                if Data['NAME'] == id:
                    self.itemDict[self.ThinBoardList[i]['NAME']].Hide()
                    self.ThinBoardList.remove(self.ThinBoardList[i])
                    break
                i += 1

        elif type1 == 'Gauge':
            for Data in self.GaugeList:
                if Data['NAME'] == id:
                    self.itemDict[self.GaugeList[i]['NAME']].Hide()
                    self.GaugeList.remove(self.GaugeList[i])
                    break
                i += 1

        elif type1 == 'ListBox':
            for Data in self.ListBoxList:
                if Data['NAME'] == id:
                    self.itemDict[self.ListBoxList[i]['NAME']].Hide()
                    self.ListBoxList.remove(self.ListBoxList[i])
                    break
                i += 1

        self.ListBox.RemoveAllItems()
        self.LoadImage()
        self.LoadSliderBar()
        self.LoadTextLine()
        self.LoadButton()
        self.LoadToggleButton()
        self.LoadEditLine()
        self.LoadComboBox()
        self.LoadThinBoard()
        self.LoadGauge()
        self.LoadListBox()
        for ImageData in self.ImageList:
            self.ListBox.AppendItem(Item('Image: ' + ImageData['NAME']))

        for Data in self.SliderBarList:
            self.ListBox.AppendItem(Item('SliderBar: ' + Data['NAME']))

        for Data in self.TextLineList:
            self.ListBox.AppendItem(Item('TextLine: ' + Data['NAME']))

        for Data in self.ButtonList:
            self.ListBox.AppendItem(Item('Button: ' + Data['NAME']))

        for Data in self.ToggleButtonList:
            self.ListBox.AppendItem(Item('TButton: ' + Data['NAME']))

        for Data in self.EditLineList:
            self.ListBox.AppendItem(Item('EditLine: ' + Data['NAME']))

        for Data in self.ComboBoxList:
            self.ListBox.AppendItem(Item('ComboBox: ' + Data['NAME']))

        for Data in self.ThinBoardList:
            self.ListBox.AppendItem(Item('Thin: ' + Data['NAME']))

        for Data in self.GaugeList:
            self.ListBox.AppendItem(Item('Gauge: ' + Data['NAME']))

        for Data in self.ListBoxList:
            self.ListBox.AppendItem(Item('ListBox: ' + Data['NAME']))

        self.wndEdit.Hide()
        self.wndEdit = None
        return

    def EditSelected(self, type1, id):
        pass

    def PreventIdListDuplicates(self, name):
        try:
            for i in xrange(100):
                self.ListBox.SelectIndex(i)
                selItem = self.ListBox.GetSelectedItem()
                if selItem:
                    itemText = selItem.GetText().split(': ')[1]
                    if itemText == name:
                        return 1

        except:
            pass

        return 0

    def CreateWindowCancel(self):
        if self.NEW_STARTED == TRUE:
            self.wndType.Hide()
            self.toolBox.Show()
            self.toolBoxList.Show()
        else:
            self.wndType.Hide()
            self.toolBox.Hide()
            self.toolBoxList.Hide()

    def CreateWindow(self):
        self.toolBox.Hide()
        self.toolBoxList.Hide()
        self.wndType.Show()

    def CreateWindow2(self, type):
        self.NEW_STARTED = TRUE
        self.ButtonList[:] = []
        self.ToggleButtonList[:] = []
        self.EditLineList[:] = []
        self.TextLineList[:] = []
        self.SliderBarList[:] = []
        self.ImageList[:] = []
        self.ComboBoxList[:] = []
        self.ThinBoardList[:] = []
        self.GaugeList[:] = []
        self.ListBoxList[:] = []
        self.ListBox.RemoveAllItems()
        if type == 'ThinBoard':
            self.WindowType = 'ThinBoard'
            self.Window = ui.ThinBoard()
            self.Window.SetSize(self.BOARD_SIZE[0], self.BOARD_SIZE[1])
            self.Window.SetPosition(240, 60)
            self.Window.AddFlag('movable')
            self.Window.AddFlag('float')
            self.Window.Show()
            self.WindowType
        if type == 'Board':
            self.WindowType = 'Board'
            self.Window = ui.Board()
            self.Window.SetSize(self.BOARD_SIZE[0], self.BOARD_SIZE[1])
            self.Window.SetPosition(240, 60)
            self.Window.AddFlag('movable')
            self.Window.AddFlag('float')
            self.Window.Show()
        if type == 'BoardWithTitleBar':
            self.WindowType = 'BoardWithTitleBar'
            self.Window = ui.BoardWithTitleBar()
            self.Window.SetSize(self.BOARD_SIZE[0], self.BOARD_SIZE[1])
            self.Window.SetPosition(240, 60)
            self.Window.AddFlag('movable')
            self.Window.AddFlag('float')
            self.Window.SetTitleName(self.BOARD_TITLE)
            self.Window.SetCloseEvent(self.Close)
            self.Window.Show()
        self.resizeButton = self.comp.ResizeButton()
        self.resizeButton.SetParent(self.Window)
        self.resizeButton.SetSize(10, 10)
        self.resizeButton.SetPosition(self.BOARD_SIZE[0] - 10, self.BOARD_SIZE[1] - 10)
        self.resizeButton.SetMoveEvent(ui.__mem_func__(self.ResizeDialog))
        self.resizeButton.Show()
        self.toolBoxList.Show()
        self.toolBox.Show()
        self.wndType.Hide()
        self.toolbox_project.Enable()
        self.toolbox_project.SetUp()
        self.toolbox_save.Enable()
        self.toolbox_save.SetUp()
        self.toolbox_preview.Enable()
        self.toolbox_preview.SetUp()

    def ResizeDialog(self):
        xPos, yPos = self.resizeButton.GetLocalPosition()
        width = self.resizeButton.GetWidth()
        height = self.resizeButton.GetHeight()
        if xPos < 100 - width:
            self.resizeButton.SetPosition(100 - width, yPos)
            return
        if yPos < 100 - height:
            self.resizeButton.SetPosition(xPos, 100 - height)
            return
        self.Window.SetSize(xPos + width, yPos + height)
        self.BOARD_SIZE = (xPos + width, yPos + height)
        self.debugBoard_text.SetText('Window Size: ' + str(self.BOARD_SIZE[0]) + ', ' + str(self.BOARD_SIZE[1]))

    def DisallowedImage(self, img):
        if not img.startswith('d:/ymir work/ui/'):
            if not app.IsFileExist(img):
                self.Message(img + ' Not Found')
                return 1
        if not img.endswith('.sub'):
            self.canLoad, self.imgWidth, self.imgHeight = app.GetImageInfo(img)
            if self.canLoad != 1:
                self.Message(locale.GUILDMARK_UPLOADER_ERROR_FILE_FORMAT)
                return 1

    def FillComboWithListBoxItems(self, object):
        try:
            for i in xrange(100):
                self.ListBox.SelectIndex(i)
                selItem = self.ListBox.GetSelectedItem()
                if selItem:
                    itemText = selItem.GetText().split(': ')[1]
                    object.InsertItem(i + 1, itemText)

        except:
            pass

    def ChooseButton(self):
        self.btnType.Show()

    def CreateButton(self, default, over, down, custom):
        defa = self.btnType_CustomEdit_d.GetText()
        ove = self.btnType_CustomEdit_o.GetText()
        dow = self.btnType_CustomEdit_dn.GetText()
        self.btn = self.btnType_NameEdit.GetText()
        if self.btn.count(' ') > 0:
            self.Message('spaces not allowed')
            return
        if self.btn == '':
            self.btn = 'btn' + str(app.GetRandom(1, 1000))
            if custom == TRUE:
                if self.DisallowedImage(defa) or self.DisallowedImage(ove) or self.DisallowedImage(dow):
                    return
                self.addButton(self.btn, defa, ove, dow)
            else:
                self.addButton(self.btn, default, over, down)
        elif custom == TRUE:
            if self.DisallowedImage(defa) or self.DisallowedImage(ove) or self.DisallowedImage(dow):
                return
            self.addButton(self.btn, defa, ove, dow)
        else:
            self.addButton(self.btn, default, over, down)

    def addButton(self, name, default, over, down):
        if self.PreventIdListDuplicates(name):
            self.Message('Duplicate ID detected, try again')
            return
        btn_text = self.btnType_NameEdit2.GetText()
        if btn_text == '':
            btn_text = self.btn
        self.ListBox.AppendItem(Item('Button: ' + name))
        buttonData = {'NAME': name,
         'BUTTON_NAME': btn_text,
         'X': 10,
         'Y': 10,
         'default_image': default,
         'over_image': over,
         'down_image': down}
        self.ButtonList.append(buttonData)
        self.LoadButton()

    def SetButtonPosition(self, arg):
        i = 0
        xPos, yPos = self.itemDict[arg].GetLocalPosition()
        for BtnData in self.ButtonList:
            if BtnData['NAME'] == arg:
                self.ButtonList[i]['X'] = xPos
                self.ButtonList[i]['Y'] = yPos
                self.debugBoard_text.SetText('ID: ' + self.ButtonList[i]['NAME'] + ', Pos: ' + str(xPos) + ', ' + str(yPos))
                self.itemDict[arg].SetRestrictMovementArea(0, 0, self.BOARD_SIZE[0], self.BOARD_SIZE[1])
                break
            i += 1

    def ChooseToggleButton(self):
        self.togglebtnType.Show()

    def CreateToggleButton(self, default, over, down, custom):
        defa = self.togglebtnType_CustomEdit_d.GetText()
        ove = self.togglebtnType_CustomEdit_o.GetText()
        dow = self.togglebtnType_CustomEdit_dn.GetText()
        if self.DisallowedImage(defa) or self.DisallowedImage(ove) or self.DisallowedImage(dow):
            return
        self.togglebtn = self.togglebtnType_NameEdit.GetText()
        if self.togglebtn.count(' ') > 0:
            self.Message('spaces not allowed')
            return
        if self.togglebtn == '':
            self.togglebtn = 'tglbtn' + str(app.GetRandom(1, 1000))
            if custom == TRUE:
                self.addToggleButton(self.togglebtn, defa, ove, dow)
            else:
                self.addToggleButton(self.togglebtn, default, over, down)
        elif custom == TRUE:
            self.addToggleButton(self.togglebtn, defa, ove, dow)
        else:
            self.addToggleButton(self.togglebtn, default, over, down)

    def addToggleButton(self, name, default, over, down):
        if self.PreventIdListDuplicates(name):
            self.Message('Duplicate ID detected, try again')
            return
        btn_text = self.togglebtnType_NameEdit2.GetText()
        if btn_text == '':
            btn_text = self.togglebtn
        self.ListBox.AppendItem(Item('TButton: ' + name))
        togglebuttonData = {'NAME': name,
         'BUTTON_NAME': btn_text,
         'X': 10,
         'Y': 10,
         'default_image': default,
         'over_image': over,
         'down_image': down}
        self.ToggleButtonList.append(togglebuttonData)
        self.LoadToggleButton()

    def SetToggleButtonPosition(self, arg):
        i = 0
        xPos, yPos = self.itemDict[arg].GetLocalPosition()
        for BtnData in self.ToggleButtonList:
            if BtnData['NAME'] == arg:
                self.ToggleButtonList[i]['X'] = xPos
                self.ToggleButtonList[i]['Y'] = yPos
                self.debugBoard_text.SetText('ID: ' + self.ToggleButtonList[i]['NAME'] + ', Pos: ' + str(xPos) + ', ' + str(yPos))
                self.itemDict[arg].SetRestrictMovementArea(0, 0, self.BOARD_SIZE[0], self.BOARD_SIZE[1])
                break
            i += 1

    def ChooseEditLine(self):
        self.wndTextLine.Show()

    def CreateEditLine(self):
        id = self.wndText_editid.GetText()
        if id.count(' ') > 0:
            self.Message('no spaces allowed')
            return
        name = self.wndText_editname.GetText()
        self.addEditLine(id, name)

    def addEditLine(self, id, Name):
        max_len = int(self.wndText_max.GetText())
        lines = int(self.wndText_lines.GetText())
        if id == '':
            id = 'edit' + str(app.GetRandom(1, 1000))
        if self.PreventIdListDuplicates(id):
            self.Message('Duplicate ID detected, try again')
            return
        self.ListBox.AppendItem(Item('EditLine: ' + id))
        editlineData = {'NAME': id,
         'EDIT_TEXT': Name,
         'X': 10,
         'Y': 10,
         'SIZE_X': max_len * 5 + 20,
         'SIZE_Y': 15,
         'MAX': max_len,
         'LINES': lines}
        self.EditLineList.append(editlineData)
        self.LoadEditLine()

    def SetEditLinePosition(self, arg):
        i = 0
        xPos, yPos = self.itemDict[arg].GetLocalPosition()
        for BtnData in self.EditLineList:
            if BtnData['NAME'] == arg:
                self.EditLineList[i]['X'] = xPos
                self.EditLineList[i]['Y'] = yPos
                self.debugBoard_text.SetText('ID: ' + self.EditLineList[i]['NAME'] + ', Pos: ' + str(xPos) + ', ' + str(yPos))
                break
            i += 1

    def CreateTextLine(self):
        self.textLineColorBoard.Show()

    def CreateTextLineCancel(self):
        self.textLineColorBoard.Hide()

    def CreateTextLineOk(self):
        edit = self.color_edit1.GetText()
        if edit.count(' ') > 0:
            self.Message('no spaces allowed')
            return
        if self.PreventIdListDuplicates(edit):
            self.Message('Duplicate ID detected, try again')
            return
        if edit == '':
            self.addTextLine(self.color, 'txt' + str(app.GetRandom(1, 1000)))
        else:
            self.addTextLine(self.color, self.color_edit1.GetText())

    def addTextLine(self, color, name):
        name2 = self.color_edit2.GetText()
        if name == '':
            name = 'text' + str(app.GetRandom(1, 1000))
            if name2 == '':
                name2 = name
        self.ListBox.AppendItem(Item('TextLine: ' + name))
        textlineData = {'NAME': name,
         'BUTTON_NAME': name2,
         'X': 10,
         'Y': 10,
         'COLOR': color}
        self.TextLineList.append(textlineData)
        self.LoadTextLine()

    def SetTextLinePosition(self, arg):
        i = 0
        xPos, yPos = self.itemDict[arg].GetLocalPosition()
        for BtnData in self.TextLineList:
            if BtnData['NAME'] == arg:
                self.TextLineList[i]['X'] = xPos
                self.TextLineList[i]['Y'] = yPos
                self.debugBoard_text.SetText('ID: ' + self.TextLineList[i]['NAME'] + ', Pos: ' + str(xPos) + ', ' + str(yPos))
                break
            i += 1

    def SetTextLineColor(self):
        self.color_r = int(self.slider_color1.GetSliderPos() * 255)
        self.color_g = int(self.slider_color2.GetSliderPos() * 255)
        self.color_b = int(self.slider_color3.GetSliderPos() * 255)
        self.color = self.comp.RGB(self.color_r, self.color_g, self.color_b)
        self.textLineColor_title2.SetFontColor(self.color[0], self.color[1], self.color[2])

    def CreateSliderBar(self):
        cSliderBar = uiCommon.InputDialog()
        cSliderBar.SetTitle('SliderBar Name')
        cSliderBar.SetMaxLength(30)
        cSliderBar.SetAcceptEvent(self.addSliderBar)
        cSliderBar.SetCancelEvent(self.CancelSliderBar)
        cSliderBar.Open()
        self.cSliderBar = cSliderBar

    def addSliderBar(self):
        Name = self.cSliderBar.GetText()
        if Name.count(' ') > 0:
            self.Message('no spaces allowed')
            return
        if self.PreventIdListDuplicates(Name):
            self.Message('Duplicate ID detected, try again')
            return
        if Name == '':
            Name = 'slider' + str(app.GetRandom(1, 1000))
            if self.PreventIdListDuplicates(Name):
                self.Message('Duplicate ID detected, try again')
                return
        self.ListBox.AppendItem(Item('SliderBar: ' + Name))
        sliderbarData = {'NAME': Name,
         'X': 10,
         'Y': 10}
        self.SliderBarList.append(sliderbarData)
        self.LoadSliderBar()

    def SetSliderBarPosition(self, arg):
        i = 0
        xPos, yPos = self.itemDict[arg].GetLocalPosition()
        for BtnData in self.SliderBarList:
            if BtnData['NAME'] == arg:
                self.SliderBarList[i]['X'] = xPos
                self.SliderBarList[i]['Y'] = yPos
                self.debugBoard_text.SetText('ID: ' + self.SliderBarList[i]['NAME'] + ', Pos: ' + str(xPos) + ', ' + str(yPos))
                break
            i += 1

    def CancelSliderBar(self):
        self.cSliderBar.Hide()

    def CreateImage(self):
        self.addImageBoard.Show()

    def CreateImageOk(self):
        img1 = self.img1.GetText()
        img = self.img2.GetText()
        if self.DisallowedImage(img):
            return
        if img1.count(' ') > 0:
            self.Message('spaces not allowed')
            return
        self.addImage(self.img1.GetText(), img)

    def CreateImageCancel(self):
        self.addImageBoard.Hide()

    def addImage(self, name, path):
        if self.PreventIdListDuplicates(name):
            self.Message('Duplicate ID detected, try again')
            return
        if name == '':
            name = 'image' + str(app.GetRandom(1, 1000))
            if self.PreventIdListDuplicates(name):
                self.Message('Duplicate ID detected, try again')
                return
        self.ListBox.AppendItem(Item('Image: ' + name))
        imageData = {'NAME': name,
         'IMG': path,
         'X': 10,
         'Y': 10}
        self.ImageList.append(imageData)
        self.LoadImage()

    def SetImagePosition(self, arg):
        i = 0
        xPos, yPos = self.itemDict[arg].GetLocalPosition()
        for BtnData in self.ImageList:
            if BtnData['NAME'] == arg:
                self.ImageList[i]['X'] = xPos
                self.ImageList[i]['Y'] = yPos
                self.debugBoard_text.SetText('ID: ' + self.ImageList[i]['NAME'] + ', Pos: ' + str(xPos) + ', ' + str(yPos))
                self.itemDict[arg].SetRestrictMovementArea(0, 0, self.BOARD_SIZE[0], self.BOARD_SIZE[1])
                break
            i += 1

    def CreateThinBoard(self):
        cThinBoard = uiCommon.InputDialog()
        cThinBoard.SetTitle('ThinBoard Name')
        cThinBoard.SetMaxLength(20)
        cThinBoard.SetAcceptEvent(self.addThinBoard)
        cThinBoard.SetCancelEvent(self.CancelThinBoard)
        cThinBoard.Open()
        self.cThinBoard = cThinBoard

    def addThinBoard(self):
        Name = self.cThinBoard.GetText()
        if Name == '':
            Name = 'thin' + str(app.GetRandom(1, 1000))
        self.ListBox.AppendItem(Item('Thin: ' + Name))
        thinboardData = {'NAME': Name,
         'X': 10,
         'Y': 10,
         'SIZE_X': 150,
         'SIZE_Y': 150}
        self.ThinBoardList.append(thinboardData)
        self.LoadThinBoard()

    def SetThinBoardPosition(self, arg):
        i = 0
        xPos, yPos = self.itemDict[arg].GetLocalPosition()
        width = self.itemDict[arg].GetWidth()
        height = self.itemDict[arg].GetHeight()
        for Data in self.ThinBoardList:
            if Data['NAME'] == arg:
                self.ThinBoardList[i]['X'] = xPos
                self.ThinBoardList[i]['Y'] = yPos
                self.ThinBoardList[i]['SIZE_X'] = width
                self.ThinBoardList[i]['SIZE_Y'] = height
                self.debugBoard_text.SetText('ID: ' + self.ThinBoardList[i]['NAME'] + ', Pos: ' + str(xPos) + ', ' + str(yPos) + ', Size: ' + str(width) + ', ' + str(height))
                break
            i += 1

    def CancelThinBoard(self):
        self.cThinBoard.Hide()
        self.cThinBoard = None
        return

    def CreateListBox(self):
        cListBox = uiCommon.InputDialog()
        cListBox.SetTitle('ListBox Name')
        cListBox.SetMaxLength(20)
        cListBox.SetAcceptEvent(self.addListBox)
        cListBox.SetCancelEvent(self.CancelListBox)
        cListBox.Open()
        self.cListBox = cListBox

    def CancelListBox(self):
        self.cListBox.Hide()
        self.cListBox = None
        return

    def addListBox(self):
        Name = self.cListBox.GetText()
        if Name == '':
            Name = 'listbox' + str(app.GetRandom(1, 1000))
        if self.PreventIdListDuplicates(Name):
            self.Message('Duplicate ID detected, try again')
            return
        self.ListBox.AppendItem(Item('ListBox: ' + Name))
        listboxData = {'NAME': Name,
         'X': 10,
         'Y': 10,
         'WIDTH': 150,
         'HEIGHT': 150}
        self.ListBoxList.append(listboxData)
        self.LoadListBox()

    def SetListBoxPosition(self, arg):
        i = 0
        xPos, yPos = self.itemDict[arg].GetLocalPosition()
        width = self.itemDict[arg].GetWidth()
        height = self.itemDict[arg].GetHeight()
        for Data in self.ListBoxList:
            if Data['NAME'] == arg:
                self.ListBoxList[i]['X'] = xPos
                self.ListBoxList[i]['Y'] = yPos
                self.ListBoxList[i]['WIDTH'] = width
                self.ListBoxList[i]['HEIGHT'] = height
                self.debugBoard_text.SetText('ID: ' + self.ListBoxList[i]['NAME'] + ', Pos: ' + str(xPos) + ', ' + str(yPos) + ', Size: ' + str(width) + ', ' + str(height))
                self.itemDict[arg].SetRestrictMovementArea(0, 0, self.BOARD_SIZE[0], self.BOARD_SIZE[1])
                break
            i += 1

    def CreateGauge(self):
        self.Gauge_window = self.comp.ThinBoard(None, TRUE, 50, 290, 181, 135, FALSE)
        self.gauge_cancel = self.comp.Button(self.Gauge_window, 'Cancel', '', 103, 100, self.CancelGauge, 'd:/ymir work/ui/public/middle_button_01.sub', 'd:/ymir work/ui/public/middle_button_02.sub', 'd:/ymir work/ui/public/middle_button_03.sub')
        self.gauge_ok = self.comp.Button(self.Gauge_window, 'OK', '', 29, 100, self.addGauge, 'd:/ymir work/ui/public/middle_button_01.sub', 'd:/ymir work/ui/public/middle_button_02.sub', 'd:/ymir work/ui/public/middle_button_03.sub')
        self.slotbar_gauge_id, self.gauge_id = self.comp.EditLine(self.Gauge_window, '', 57, 29, 100, 15, 15)
        self.slotbar_gauge_width, self.gauge_width = self.comp.EditLine(self.Gauge_window, '100', 57, 68, 34, 15, 4)
        self.gauge_title = self.comp.TextLine(self.Gauge_window, 'Gauge', 20, 10, self.comp.RGB(255, 0, 0))
        self.gauge_id_text = self.comp.TextLine(self.Gauge_window, 'ID', 25, 30, None)
        self.gauge_color_text = self.comp.TextLine(self.Gauge_window, 'Color', 16, 48, None)
        self.gauge_width_text = self.comp.TextLine(self.Gauge_window, 'Width', 16, 70, None)
        self.gauge_combo_color = self.comp.ComboBox(self.Gauge_window, 'red', 57, 48, 70)
        self.gauge_combo_color.InsertItem(0, 'red')
        self.gauge_combo_color.InsertItem(1, 'blue')
        self.gauge_combo_color.InsertItem(2, 'pink')
        self.gauge_combo_color.InsertItem(3, 'purple')
        return

    def CancelGauge(self):
        self.Gauge_window.Hide()

    def addGauge(self):
        id = self.gauge_id.GetText()
        combo = self.gauge_combo_color.GetCurrentText()
        width = int(self.gauge_width.GetText())
        if id.count(' ') > 0:
            self.Message('spaces not allowed')
            return
        if self.PreventIdListDuplicates(id):
            self.Message('Duplicate ID detected, try again')
            return
        if id == '':
            id = 'gauge' + str(app.GetRandom(1, 1000))
            if self.PreventIdListDuplicates(id):
                self.Message('Duplicate ID detected, try again')
                return
        self.ListBox.AppendItem(Item('Gauge: ' + id))
        gaugeData = {'NAME': id,
         'X': 10,
         'Y': 10,
         'WIDTH': width,
         'COLOR': combo}
        self.GaugeList.append(gaugeData)
        self.LoadGauge()

    def SetGaugePosition(self, arg):
        i = 0
        xPos, yPos = self.itemDict[arg].GetLocalPosition()
        for Data in self.GaugeList:
            if Data['NAME'] == arg:
                self.GaugeList[i]['X'] = xPos
                self.GaugeList[i]['Y'] = yPos
                self.debugBoard_text.SetText('ID: ' + self.GaugeList[i]['NAME'] + ', Pos: ' + str(xPos) + ', ' + str(yPos))
                break
            i += 1

    def CreateComboBox(self):
        cComboBox = uiCommon.InputDialog()
        cComboBox.SetTitle('ComboBox Name')
        cComboBox.SetMaxLength(30)
        cComboBox.SetAcceptEvent(self.addComboBox)
        cComboBox.SetCancelEvent(self.CancelComboBox)
        cComboBox.Open()
        self.cComboBox = cComboBox

    def addComboBox(self):
        Name = self.cComboBox.GetText()
        if Name.count(' ') > 0:
            self.Message('spaces not allowed')
            return
        if self.PreventIdListDuplicates(Name):
            self.Message('Duplicate ID detected, try again')
            return
        if Name == '':
            Name = 'combo' + str(app.GetRandom(1, 1000))
            if self.PreventIdListDuplicates(Name):
                self.Message('Duplicate ID detected, try again')
                return
        self.ListBox.AppendItem(Item('ComboBox: ' + Name))
        comboboxData = {'NAME': Name,
         'X': 10,
         'Y': 10}
        self.ComboBoxList.append(comboboxData)
        self.LoadComboBox()

    def SetComboBoxPosition(self, arg):
        i = 0
        xPos, yPos = self.itemDict[arg].GetLocalPosition()
        for comboData in self.ComboBoxList:
            if comboData['NAME'] == arg:
                self.ComboBoxList[i]['X'] = xPos
                self.ComboBoxList[i]['Y'] = yPos
                self.debugBoard_text.SetText('ID: ' + self.ComboBoxList[i]['NAME'] + ', Pos: ' + str(xPos) + ', ' + str(yPos))
                break
            i += 1

    def CancelComboBox(self):
        self.cComboBox.Hide()

    def __CreateListBox(self):
        self.toolBoxList = self.comp.ThinBoard(None, TRUE, 130, 50, 100, 200, FALSE)
        self.toolBoxList.Hide()
        self.litems = self.comp.TextLine(self.toolBoxList, 'Item ID List', 10, 5, self.comp.RGB(255, 0, 0))
        fileListBox = ui.ListBoxEx()
        fileListBox.SetParent(self.toolBoxList)
        fileListBox.SetPosition(10, 20)
        fileListBox.Show()
        return fileListBox

    def SaveToPy(self):
        save = uiCommon.InputDialogWithDescription()
        save.SetTitle('Save To Py')
        save.SetDescription('ex. dialog1.py')
        save.SetAcceptEvent(self.SaveToPy2)
        save.SetCancelEvent(self.CancelSave)
        save.Open()
        self.save = save

    def CancelSave(self):
        self.save.Hide()

    def SaveFile(self, Name):
        writef = open(Name, 'w+')
        writef.write(binascii.a2b_base64('IyBHZW5lcmF0ZWQgd2l0aCBHdWkgRWRpdG9yIGJ5IEthTWVSMTMzNyA7IHd3dy5tZXRpbjJtb2QudGs=') + '\n')
        writef.write('import ui\n')
        writef.write('import dbg\n')
        writef.write('import app\n\n')
        writef.write('class Dialog1(ui.Window):\n')
        writef.write('\tdef __init__(self):\n')
        writef.write('\t\tui.Window.__init__(self)\n')
        writef.write('\t\tself.BuildWindow()\n\n')
        writef.write('\tdef __del__(self):\n')
        writef.write('\t\tui.Window.__del__(self)\n\n')
        writef.write('\tdef BuildWindow(self):\n')
        writef.write('\t\tself.Board = ui.' + self.WindowType + '()\n')
        writef.write('\t\tself.Board.SetSize(' + str(self.BOARD_SIZE[0]) + ', ' + str(self.BOARD_SIZE[1]) + ')\n')
        writef.write('\t\tself.Board.SetCenterPosition()\n')
        writef.write("\t\tself.Board.AddFlag('movable')\n")
        writef.write("\t\tself.Board.AddFlag('float')\n")
        if self.WindowType == 'BoardWithTitleBar':
            writef.write("\t\tself.Board.SetTitleName('" + self.BOARD_TITLE + "')\n")
            writef.write('\t\tself.Board.SetCloseEvent(self.Close)\n')
        writef.write('\t\tself.Board.Show()\n')
        writef.write('\t\tself.__BuildKeyDict()\n')
        writef.write('\t\tself.comp = Component()\n\n')
        for imageData in self.ImageList:
            writef.write('\t\tself.' + imageData['NAME'] + ' = self.comp.ExpandedImage(self.Board , ' + str(imageData['X']) + ', ' + str(imageData['Y']) + ", '" + str(imageData['IMG']) + "')" + '\n')

        for ThinData in self.ThinBoardList:
            writef.write('\t\tself.' + ThinData['NAME'] + ' = self.comp.ThinBoard(self.Board, FALSE, ' + str(ThinData['X']) + ', ' + str(ThinData['Y']) + ', ' + str(ThinData['SIZE_X']) + ', ' + str(ThinData['SIZE_Y']) + ', FALSE)\n')

        for BtnData in self.ButtonList:
            writef.write('\t\tself.' + BtnData['NAME'] + " = self.comp.Button(self.Board, '" + BtnData['BUTTON_NAME'] + "', '', " + str(BtnData['X']) + ', ' + str(BtnData['Y']) + ', self.' + BtnData['NAME'] + "_func, '" + BtnData['default_image'] + "', '" + BtnData['over_image'] + "', '" + BtnData['down_image'] + "')" + '\n')

        for BtnData in self.ToggleButtonList:
            writef.write('\t\tself.' + BtnData['NAME'] + " = self.comp.ToggleButton(self.Board, '" + BtnData['BUTTON_NAME'] + "', '', " + str(BtnData['X']) + ', ' + str(BtnData['Y']) + ", (lambda arg = 'off': self." + BtnData['NAME'] + "_func(arg)), (lambda arg = 'on': self." + BtnData['NAME'] + "_func(arg)), '" + BtnData['default_image'] + "', '" + BtnData['over_image'] + "', '" + BtnData['down_image'] + "')" + '\n')

        for EditlnData in self.EditLineList:
            writef.write('\t\tself.slotbar_' + EditlnData['NAME'] + ', self.' + EditlnData['NAME'] + " = self.comp.EditLine(self.Board, '" + EditlnData['EDIT_TEXT'] + "', " + str(EditlnData['X']) + ', ' + str(EditlnData['Y']) + ', ' + str(EditlnData['SIZE_X'] - 10) + ', ' + str(EditlnData['SIZE_Y'] * EditlnData['LINES']) + ', ' + str(EditlnData['MAX'] * EditlnData['LINES']) + ')' + '\n')

        for TextlnData in self.TextLineList:
            writef.write('\t\tself.' + TextlnData['NAME'] + " = self.comp.TextLine(self.Board, '" + TextlnData['BUTTON_NAME'] + "', " + str(TextlnData['X']) + ', ' + str(TextlnData['Y']) + ', self.comp.RGB(' + str(TextlnData['COLOR'][0] / 255) + ', ' + str(TextlnData['COLOR'][1] / 255) + ', ' + str(TextlnData['COLOR'][2] / 255) + '))' + '\n')

        for sliderData in self.SliderBarList:
            writef.write('\t\tself.' + sliderData['NAME'] + ' = self.comp.SliderBar(self.Board, 0.0, self.' + sliderData['NAME'] + '_func, ' + str(sliderData['X']) + ', ' + str(sliderData['Y']) + ')' + '\n')

        for Data in self.GaugeList:
            writef.write('\t\tself.' + Data['NAME'] + ' = self.comp.Gauge(self.Board, ' + str(Data['WIDTH']) + ", '" + Data['COLOR'] + "', " + str(Data['X']) + ', ' + str(Data['Y']) + ')' + '\n')

        for Data in self.ListBoxList:
            writef.write('\t\tself.bar_' + Data['NAME'] + ', self.list_' + Data['NAME'] + ' = self.comp.ListBoxEx(self.Board, ' + str(Data['X']) + ', ' + str(Data['Y']) + ', ' + str(Data['WIDTH']) + ', ' + str(Data['HEIGHT']) + ')' + '\n')

        if len(self.ListBoxList) != 0:
            writef.write("\t\t#example: self.list_xxx.AppendItem(Item('text 1'))")
        for comboData in self.ComboBoxList:
            writef.write('\t\tself.' + comboData['NAME'] + " = self.comp.ComboBox(self.Board, 'Select', " + str(comboData['X']) + ', ' + str(comboData['Y']) + ', 70)' + '\n')

        for Data in self.ButtonList:
            writef.write('\t\n\tdef ' + Data['NAME'] + '_func(self):\n')
            writef.write('\t\tpass\n')

        for Data in self.ToggleButtonList:
            writef.write('\t\n\tdef ' + Data['NAME'] + '_func(self, arg):\n')
            writef.write("\t\tif arg=='on':\n")
            writef.write('\t\t\tpass\n')
            writef.write("\t\telif arg=='off':\n")
            writef.write('\t\t\tpass\n')

        for sliderData in self.SliderBarList:
            writef.write('\t\n\tdef ' + sliderData['NAME'] + '_func(self):\n')
            writef.write('\t\tpass\n')

        writef.write('\t\n\tdef __BuildKeyDict(self):\n')
        writef.write('\t\tonPressKeyDict = {}\n')
        writef.write('\t\tonPressKeyDict[app.DIK_F5]\t= lambda : self.OpenWindow()\n')
        writef.write('\t\tself.onPressKeyDict = onPressKeyDict\n')
        writef.write('\t\n\tdef OnKeyDown(self, key):\n')
        writef.write('\t\ttry:\n')
        writef.write('\t\t\tself.onPressKeyDict[key]()\n')
        writef.write('\t\texcept KeyError:\n')
        writef.write('\t\t\tpass\n')
        writef.write('\t\texcept:\n')
        writef.write('\t\t\traise\n')
        writef.write('\t\treturn TRUE\n')
        writef.write('\t\n\tdef OpenWindow(self):\n')
        writef.write('\t\tif self.Board.IsShow():\n')
        writef.write('\t\t\tself.Board.Hide()\n')
        writef.write('\t\telse:\n')
        writef.write('\t\t\tself.Board.Show()\n')
        writef.write('\t\n\tdef Close(self):\n')
        writef.write('\t\tself.Board.Hide()\n\n')
        writef.write('class Component:\n')
        writef.write('\tdef Button(self, parent, buttonName, tooltipText, x, y, func, UpVisual, OverVisual, DownVisual):\n')
        writef.write('\t\tbutton = ui.Button()\n')
        writef.write('\t\tif parent != None:\n')
        writef.write('\t\t\tbutton.SetParent(parent)\n')
        writef.write('\t\tbutton.SetPosition(x, y)\n')
        writef.write('\t\tbutton.SetUpVisual(UpVisual)\n')
        writef.write('\t\tbutton.SetOverVisual(OverVisual)\n')
        writef.write('\t\tbutton.SetDownVisual(DownVisual)\n')
        writef.write('\t\tbutton.SetText(buttonName)\n')
        writef.write('\t\tbutton.SetToolTipText(tooltipText)\n')
        writef.write('\t\tbutton.Show()\n')
        writef.write('\t\tbutton.SetEvent(func)\n')
        writef.write('\t\treturn button\n\n')
        writef.write('\tdef ToggleButton(self, parent, buttonName, tooltipText, x, y, funcUp, funcDown, UpVisual, OverVisual, DownVisual):\n')
        writef.write('\t\tbutton = ui.ToggleButton()\n')
        writef.write('\t\tif parent != None:\n')
        writef.write('\t\t\tbutton.SetParent(parent)\n')
        writef.write('\t\tbutton.SetPosition(x, y)\n')
        writef.write('\t\tbutton.SetUpVisual(UpVisual)\n')
        writef.write('\t\tbutton.SetOverVisual(OverVisual)\n')
        writef.write('\t\tbutton.SetDownVisual(DownVisual)\n')
        writef.write('\t\tbutton.SetText(buttonName)\n')
        writef.write('\t\tbutton.SetToolTipText(tooltipText)\n')
        writef.write('\t\tbutton.Show()\n')
        writef.write('\t\tbutton.SetToggleUpEvent(funcUp)\n')
        writef.write('\t\tbutton.SetToggleDownEvent(funcDown)\n')
        writef.write('\t\treturn button\n\n')
        writef.write('\tdef EditLine(self, parent, editlineText, x, y, width, heigh, max):\n')
        writef.write('\t\tSlotBar = ui.SlotBar()\n')
        writef.write('\t\tif parent != None:\n')
        writef.write('\t\t\tSlotBar.SetParent(parent)\n')
        writef.write('\t\tSlotBar.SetSize(width, heigh)\n')
        writef.write('\t\tSlotBar.SetPosition(x, y)\n')
        writef.write('\t\tSlotBar.Show()\n')
        writef.write('\t\tValue = ui.EditLine()\n')
        writef.write('\t\tValue.SetParent(SlotBar)\n')
        writef.write('\t\tValue.SetSize(width, heigh)\n')
        writef.write('\t\tValue.SetPosition(1, 1)\n')
        writef.write('\t\tValue.SetMax(max)\n')
        writef.write('\t\tValue.SetLimitWidth(width)\n')
        writef.write('\t\tValue.SetMultiLine()\n')
        writef.write('\t\tValue.SetText(editlineText)\n')
        writef.write('\t\tValue.Show()\n')
        writef.write('\t\treturn SlotBar, Value\n\n')
        writef.write('\tdef TextLine(self, parent, textlineText, x, y, color):\n')
        writef.write('\t\ttextline = ui.TextLine()\n')
        writef.write('\t\tif parent != None:\n')
        writef.write('\t\t\ttextline.SetParent(parent)\n')
        writef.write('\t\ttextline.SetPosition(x, y)\n')
        writef.write('\t\tif color != None:\n')
        writef.write('\t\t\ttextline.SetFontColor(color[0], color[1], color[2])\n')
        writef.write('\t\ttextline.SetText(textlineText)\n')
        writef.write('\t\ttextline.Show()\n')
        writef.write('\t\treturn textline\n\n')
        writef.write('\tdef RGB(self, r, g, b):\n')
        writef.write('\t\treturn (r*255, g*255, b*255)\n\n')
        writef.write('\tdef SliderBar(self, parent, sliderPos, func, x, y):\n')
        writef.write('\t\tSlider = ui.SliderBar()\n')
        writef.write('\t\tif parent != None:\n')
        writef.write('\t\t\tSlider.SetParent(parent)\n')
        writef.write('\t\tSlider.SetPosition(x, y)\n')
        writef.write('\t\tSlider.SetSliderPos(sliderPos / 100)\n')
        writef.write('\t\tSlider.Show()\n')
        writef.write('\t\tSlider.SetEvent(func)\n')
        writef.write('\t\treturn Slider\n\n')
        writef.write('\tdef ExpandedImage(self, parent, x, y, img):\n')
        writef.write('\t\timage = ui.ExpandedImageBox()\n')
        writef.write('\t\tif parent != None:\n')
        writef.write('\t\t\timage.SetParent(parent)\n')
        writef.write('\t\timage.SetPosition(x, y)\n')
        writef.write('\t\timage.LoadImage(img)\n')
        writef.write('\t\timage.Show()\n')
        writef.write('\t\treturn image\n\n')
        writef.write('\tdef ComboBox(self, parent, text, x, y, width):\n')
        writef.write('\t\tcombo = ui.ComboBox()\n')
        writef.write('\t\tif parent != None:\n')
        writef.write('\t\t\tcombo.SetParent(parent)\n')
        writef.write('\t\tcombo.SetPosition(x, y)\n')
        writef.write('\t\tcombo.SetSize(width, 15)\n')
        writef.write('\t\tcombo.SetCurrentItem(text)\n')
        writef.write('\t\tcombo.Show()\n')
        writef.write('\t\treturn combo\n\n')
        writef.write('\tdef ThinBoard(self, parent, moveable, x, y, width, heigh, center):\n')
        writef.write('\t\tthin = ui.ThinBoard()\n')
        writef.write('\t\tif parent != None:\n')
        writef.write('\t\t\tthin.SetParent(parent)\n')
        writef.write('\t\tif moveable == TRUE:\n')
        writef.write("\t\t\tthin.AddFlag('movable')\n")
        writef.write("\t\t\tthin.AddFlag('float')\n")
        writef.write('\t\tthin.SetSize(width, heigh)\n')
        writef.write('\t\tthin.SetPosition(x, y)\n')
        writef.write('\t\tif center == TRUE:\n')
        writef.write('\t\t\tthin.SetCenterPosition()\n')
        writef.write('\t\tthin.Show()\n')
        writef.write('\t\treturn thin\n\n')
        writef.write('\tdef Gauge(self, parent, width, color, x, y):\n')
        writef.write('\t\tgauge = ui.Gauge()\n')
        writef.write('\t\tif parent != None:\n')
        writef.write('\t\t\tgauge.SetParent(parent)\n')
        writef.write('\t\tgauge.SetPosition(x, y)\n')
        writef.write('\t\tgauge.MakeGauge(width, color)\n')
        writef.write('\t\tgauge.Show()\n')
        writef.write('\t\treturn gauge\n\n')
        writef.write('\tdef ListBoxEx(self, parent, x, y, width, heigh):\n')
        writef.write('\t\tbar = ui.Bar()\n')
        writef.write('\t\tif parent != None:\n')
        writef.write('\t\t\tbar.SetParent(parent)\n')
        writef.write('\t\tbar.SetPosition(x, y)\n')
        writef.write('\t\tbar.SetSize(width, heigh)\n')
        writef.write('\t\tbar.SetColor(0x77000000)\n')
        writef.write('\t\tbar.Show()\n')
        writef.write('\t\tListBox=ui.ListBoxEx()\n')
        writef.write('\t\tListBox.SetParent(bar)\n')
        writef.write('\t\tListBox.SetPosition(0, 0)\n')
        writef.write('\t\tListBox.SetSize(width, heigh)\n')
        writef.write('\t\tListBox.Show()\n')
        writef.write('\t\tscroll = ui.ScrollBar()\n')
        writef.write('\t\tscroll.SetParent(ListBox)\n')
        writef.write('\t\tscroll.SetPosition(width-15, 0)\n')
        writef.write('\t\tscroll.SetScrollBarSize(heigh)\n')
        writef.write('\t\tscroll.Show()\n')
        writef.write('\t\tListBox.SetScrollBar(scroll)\n')
        writef.write('\t\treturn bar, ListBox\n\n')
        if len(self.ListBoxList) != 0:
            writef.write('class Item(ui.ListBoxEx.Item):\n')
            writef.write('\tdef __init__(self, text):\n')
            writef.write('\t\tui.ListBoxEx.Item.__init__(self)\n')
            writef.write('\t\tself.canLoad=0\n')
            writef.write('\t\tself.text=text\n')
            writef.write('\t\tself.textLine=self.__CreateTextLine(text[:50])\n')
            writef.write('\tdef __del__(self):\n')
            writef.write('\t\tui.ListBoxEx.Item.__del__(self)\n')
            writef.write('\tdef GetText(self):\n')
            writef.write('\t\treturn self.text\n')
            writef.write('\tdef SetSize(self, width, height):\n')
            writef.write('\t\tui.ListBoxEx.Item.SetSize(self, 7*len(self.textLine.GetText()) + 4, height)\n')
            writef.write('\tdef __CreateTextLine(self, text):\n')
            writef.write('\t\ttextLine=ui.TextLine()\n')
            writef.write('\t\ttextLine.SetParent(self)\n')
            writef.write('\t\ttextLine.SetPosition(0, 0)\n')
            writef.write('\t\ttextLine.SetText(text)\n')
            writef.write('\t\ttextLine.Show()\n')
            writef.write('\t\treturn textLine\n\n')
        writef.write('Dialog1().Show()\n')
        writef.close()

    def SaveToPy2(self):
        Name = self.save.GetText()
        if Name.count('.py') == 0:
            self.Message('file must be .py')
            return
        else:
            self.SaveFile(Name)
            self.save.Hide()
            self.save = None
            return

    def Preview(self):
        kDict = {}
        fl = 'preview.py'
        self.SaveFile(fl)
        execfile(fl, kDict)
        os.remove(fl)

    def LoadProject(self):
        save = uiCommon.InputDialogWithDescription()
        save.SetTitle('Load Project')
        save.SetDescription('ex. project1.txt')
        save.SetAcceptEvent(self.LoadProject2)
        save.SetCancelEvent(self.CancelLoadProject)
        save.Open()
        self.loadproj = save

    def CancelLoadProject(self):
        self.loadproj.Hide()
        self.loadproj = None
        return

    def LoadProject2(self):
        self.NEW_STARTED = TRUE
        name = self.loadproj.GetText()
        if not app.IsFileExist(name):
            self.Message('project file doesnt exist')
        self.ButtonList[:] = []
        self.ToggleButtonList[:] = []
        self.EditLineList[:] = []
        self.TextLineList[:] = []
        self.SliderBarList[:] = []
        self.ImageList[:] = []
        self.ComboBoxList[:] = []
        self.ThinBoardList[:] = []
        self.GaugeList[:] = []
        self.ListBoxList[:] = []
        self.ListBox.RemoveAllItems()
        lines = open(name).readlines()
        for line in lines:
            if line.startswith('-Window:'):
                arg = line.split('\t')
                self.SetSize(int(arg[1]), int(arg[2]))
                self.BOARD_SIZE = (int(arg[1]), int(arg[2]))
                self.WindowType = arg[3].replace('\n', '')
                self.CreateWindow2(self.WindowType)
            if line.startswith('-Button:'):
                arg = line.split('\t')
                self.ListBox.AppendItem(Item('Button: ' + arg[1]))
                buttonData = {'NAME': arg[1],
                 'BUTTON_NAME': arg[2],
                 'X': int(arg[3]),
                 'Y': int(arg[4]),
                 'default_image': arg[5],
                 'over_image': arg[6],
                 'down_image': arg[7].replace('\n', '')}
                self.ButtonList.append(buttonData)
            if line.startswith('-ToggleButton:'):
                arg = line.split('\t')
                self.ListBox.AppendItem(Item('TButton: ' + arg[1]))
                buttonData2 = {'NAME': arg[1],
                 'BUTTON_NAME': arg[2],
                 'X': int(arg[3]),
                 'Y': int(arg[4]),
                 'default_image': arg[5],
                 'over_image': arg[6],
                 'down_image': arg[7].replace('\n', '')}
                self.ButtonList.append(buttonData2)
            if line.startswith('-EditLine:'):
                arg = line.split('\t')
                self.ListBox.AppendItem(Item('EditLine: ' + arg[1]))
                editlineData = {'NAME': arg[1],
                 'EDIT_TEXT': arg[2],
                 'X': int(arg[3]),
                 'Y': int(arg[4]),
                 'SIZE_X': int(arg[5]),
                 'SIZE_Y': int(arg[6]),
                 'MAX': int(arg[7]),
                 'LINES': int(arg[8].replace('\n', ''))}
                self.EditLineList.append(editlineData)
            if line.startswith('-TextLine:'):
                arg = line.split('\t')
                rgb_split = arg[5].replace('\n', '').split(' ')
                self.ListBox.AppendItem(Item('TextLine: ' + arg[1]))
                textlineData = {'NAME': arg[1],
                 'BUTTON_NAME': arg[2],
                 'X': int(arg[3]),
                 'Y': int(arg[4]),
                 'COLOR': self.comp.RGB(int(rgb_split[0]), int(rgb_split[1]), int(rgb_split[2]))}
                self.TextLineList.append(textlineData)
            if line.startswith('-SliderBar:'):
                arg = line.split('\t')
                self.ListBox.AppendItem(Item('SliderBar: ' + arg[1]))
                sliderbarData = {'NAME': arg[1],
                 'X': int(arg[2]),
                 'Y': int(arg[3].replace('\n', ''))}
                self.SliderBarList.append(sliderbarData)
            if line.startswith('-Image:'):
                arg = line.split('\t')
                self.ListBox.AppendItem(Item('Image: ' + arg[1]))
                imageData = {'NAME': arg[1],
                 'IMG': arg[4].replace('\n', ''),
                 'X': int(arg[2]),
                 'Y': int(arg[3])}
                self.ImageList.append(imageData)
            if line.startswith('-ThinBoard:'):
                arg = line.split('\t')
                self.ListBox.AppendItem(Item('Thin: ' + arg[1]))
                thinboardData = {'NAME': arg[1],
                 'X': int(arg[2]),
                 'Y': int(arg[3]),
                 'SIZE_X': int(arg[4]),
                 'SIZE_Y': int(arg[5].replace('\n', ''))}
                self.ThinBoardList.append(thinboardData)
            if line.startswith('-ComboBox:'):
                arg = line.split('\t')
                self.ListBox.AppendItem(Item('ComboBox: ' + arg[1]))
                comboboxData = {'NAME': arg[1],
                 'X': int(arg[2]),
                 'Y': int(arg[3].replace('\n', ''))}
                self.ComboBoxList.append(comboboxData)
            if line.startswith('-Gauge:'):
                arg = line.split('\t')
                self.ListBox.AppendItem(Item('Gauge: ' + arg[1]))
                gaugeData = {'NAME': arg[1],
                 'X': int(arg[2]),
                 'Y': int(arg[3]),
                 'WIDTH': int(arg[4]),
                 'COLOR': arg[5].replace('\n', '')}
                self.GaugeList.append(gaugeData)
            if line.startswith('-ListBox:'):
                arg = line.split('\t')
                self.ListBox.AppendItem(Item('ListBox: ' + arg[1]))
                listboxData = {'NAME': arg[1],
                 'X': int(arg[2]),
                 'Y': int(arg[3]),
                 'WIDTH': int(arg[4]),
                 'HEIGHT': int(arg[5].replace('\n', ''))}
                self.ListBoxList.append(listboxData)
            self.LoadImage()
            self.LoadSliderBar()
            self.LoadTextLine()
            self.LoadButton()
            self.LoadToggleButton()
            self.LoadEditLine()
            self.LoadComboBox()
            self.LoadThinBoard()
            self.LoadGauge()
            self.LoadListBox()
            self.toolBoxList.Show()
            self.toolBox.Show()
            self.loadproj.Hide()

    def LoadThinBoard(self):
        for Data in self.ThinBoardList:
            thin = self.ThinBoardMoveable()
            thin.SetParent(self.Window)
            thin.SetSize(Data['SIZE_X'], Data['SIZE_Y'])
            thin.SetPosition(Data['X'], Data['Y'])
            thin.SetMoveEvent(lambda arg = Data['NAME']: self.SetThinBoardPosition(arg))
            thin.Show()
            rbutton = self.comp.ResizeButton()
            rbutton.SetParent(thin)
            rbutton.SetSize(10, 10)
            rbutton.SetPosition(Data['SIZE_X'] - 10, Data['SIZE_Y'] - 10)
            rbutton.SetMoveEvent(lambda arg = Data['NAME']: self.ResizeThin(arg))
            rbutton.Show()
            self.itemDict[Data['NAME']] = thin
            self.ThinResizeDict[Data['NAME']] = rbutton

    def ResizeThin(self, arg):
        xPos, yPos = self.ThinResizeDict[arg].GetLocalPosition()
        width = self.ThinResizeDict[arg].GetWidth()
        height = self.ThinResizeDict[arg].GetHeight()
        if xPos < 40 - width:
            self.ThinResizeDict[arg].SetPosition(40 - width, yPos)
            return
        if yPos < 40 - height:
            self.ThinResizeDict[arg].SetPosition(xPos, 40 - height)
            return
        self.itemDict[arg].SetSize(xPos + width, yPos + height)
        i = 0
        for Data in self.ThinBoardList:
            if Data['NAME'] == arg:
                self.ThinBoardList[i]['SIZE_X'] = xPos + width
                self.ThinBoardList[i]['SIZE_Y'] = yPos + height
                self.debugBoard_text.SetText('ID: ' + self.ThinBoardList[i]['NAME'] + ', Pos: ' + str(self.ThinBoardList[i]['X']) + ', ' + str(self.ThinBoardList[i]['Y']) + ', Size: ' + str(self.ThinBoardList[i]['SIZE_X']) + ', ' + str(self.ThinBoardList[i]['SIZE_Y']))
            i += 1

    def LoadListBox(self):
        for Data in self.ListBoxList:
            bar = self.BarMoveable()
            bar.SetParent(self.Window)
            bar.SetSize(Data['WIDTH'] + 10, Data['HEIGHT'] + 10)
            bar.SetBarSize(Data['WIDTH'], Data['HEIGHT'])
            bar.SetPosition(Data['X'], Data['Y'])
            bar.SetMoveEvent(lambda arg = Data['NAME']: self.SetListBoxPosition(arg))
            bar.Show()
            rbutton = self.comp.ResizeButton()
            rbutton.SetParent(bar)
            rbutton.SetSize(10, 10)
            rbutton.SetPosition(Data['WIDTH'] - 10, Data['HEIGHT'] - 10)
            rbutton.SetMoveEvent(lambda arg = Data['NAME']: self.ResizeListBox(arg))
            rbutton.Show()
            self.itemDict[Data['NAME']] = bar
            self.ThinResizeDict[Data['NAME']] = rbutton

    def ResizeListBox(self, arg):
        xPos, yPos = self.ThinResizeDict[arg].GetLocalPosition()
        width = self.ThinResizeDict[arg].GetWidth()
        height = self.ThinResizeDict[arg].GetHeight()
        if xPos < 40 - width:
            self.ThinResizeDict[arg].SetPosition(40 - width, yPos)
            return
        if yPos < 40 - height:
            self.ThinResizeDict[arg].SetPosition(xPos, 40 - height)
            return
        self.itemDict[arg].SetSize(xPos + width + 10, yPos + height + 10)
        self.itemDict[arg].SetBarSize(xPos + width, yPos + height)
        i = 0
        for Data in self.ListBoxList:
            if Data['NAME'] == arg:
                self.ListBoxList[i]['WIDTH'] = xPos + width
                self.ListBoxList[i]['HEIGHT'] = yPos + height
                self.debugBoard_text.SetText('ID: ' + self.ListBoxList[i]['NAME'] + ', Pos: ' + str(self.ListBoxList[i]['X']) + ', ' + str(self.ListBoxList[i]['Y']) + ', Size: ' + str(self.ListBoxList[i]['WIDTH']) + ', ' + str(self.ListBoxList[i]['HEIGHT']))
            i += 1

    def LoadImage(self):
        for ImageData in self.ImageList:
            image = self.comp.ResizeButton()
            image.SetParent(self.Window)
            image.SetSize(20, 20)
            image.SetUpVisual(ImageData['IMG'])
            image.SetOverVisual(ImageData['IMG'])
            image.SetDownVisual(ImageData['IMG'])
            image.SetPosition(ImageData['X'], ImageData['Y'])
            image.SetText(ImageData['NAME'])
            image.SetMoveEvent(lambda arg = ImageData['NAME']: self.SetImagePosition(arg))
            image.Show()
            self.itemDict[ImageData['NAME']] = image

    def LoadSliderBar(self):
        for SliderBarData in self.SliderBarList:
            sliderbar = self.SliderBarMoveable()
            sliderbar.SetParent(self.Window)
            sliderbar.SetSize(100, 15)
            sliderbar.SetPosition(SliderBarData['X'], SliderBarData['Y'])
            sliderbar.SetText(SliderBarData['NAME'])
            sliderbar.SetMoveEvent(lambda arg = SliderBarData['NAME']: self.SetSliderBarPosition(arg))
            sliderbar.Show()
            self.itemDict[SliderBarData['NAME']] = sliderbar

    def LoadTextLine(self):
        for TextLineData in self.TextLineList:
            SlotBar = self.TextLineMoveable()
            SlotBar.SetParent(self.Window)
            SlotBar.SetSize(30, 15)
            SlotBar.SetPosition(TextLineData['X'], TextLineData['Y'])
            SlotBar.SetText(TextLineData['BUTTON_NAME'])
            SlotBar.SetFontColor(TextLineData['COLOR'][0], TextLineData['COLOR'][1], TextLineData['COLOR'][2])
            SlotBar.SetMoveEvent(lambda arg = TextLineData['NAME']: self.SetTextLinePosition(arg))
            SlotBar.Show()
            self.itemDict[TextLineData['NAME']] = SlotBar

    def LoadButton(self):
        for BtnData in self.ButtonList:
            button = self.comp.ResizeButton()
            button.SetParent(self.Window)
            button.SetPosition(BtnData['X'], BtnData['Y'])
            button.SetUpVisual(BtnData['default_image'])
            button.SetOverVisual(BtnData['over_image'])
            button.SetDownVisual(BtnData['down_image'])
            button.SetText(BtnData['BUTTON_NAME'])
            button.SetMoveEvent(lambda arg = BtnData['NAME']: self.SetButtonPosition(arg))
            button.Show()
            self.itemDict[BtnData['NAME']] = button

    def LoadToggleButton(self):
        for Data in self.ToggleButtonList:
            button = self.comp.ResizeButton()
            button.SetParent(self.Window)
            button.SetPosition(Data['X'], Data['Y'])
            button.SetUpVisual(Data['default_image'])
            button.SetOverVisual(Data['over_image'])
            button.SetDownVisual(Data['down_image'])
            button.SetText(Data['BUTTON_NAME'])
            button.SetMoveEvent(lambda arg = Data['NAME']: self.SetToggleButtonPosition(arg))
            button.Show()
            self.itemDict[Data['NAME']] = button

    def LoadEditLine(self):
        for BtnData in self.EditLineList:
            SlotBar2 = self.EditLineMoveable()
            SlotBar2.SetParent(self.Window)
            SlotBar2.SetSize(BtnData['SIZE_X'], BtnData['SIZE_Y'] * BtnData['LINES'])
            SlotBar2.SetPosition(BtnData['X'], BtnData['Y'])
            SlotBar2.SetMaxLength(BtnData['MAX'], BtnData['LINES'])
            SlotBar2.SetText(BtnData['EDIT_TEXT'])
            SlotBar2.SetMoveEvent(lambda arg = BtnData['NAME']: self.SetEditLinePosition(arg))
            SlotBar2.Show()
            self.itemDict[BtnData['NAME']] = SlotBar2

    def LoadComboBox(self):
        for ComboBoxData in self.ComboBoxList:
            combobox = self.ComboBoxMoveable()
            combobox.SetParent(self.Window)
            combobox.SetSize(70, 15)
            combobox.SetPosition(ComboBoxData['X'], ComboBoxData['Y'])
            combobox.SetCurrentItem(ComboBoxData['NAME'])
            combobox.SetMoveEvent(lambda arg = ComboBoxData['NAME']: self.SetComboBoxPosition(arg))
            combobox.Show()
            self.itemDict[ComboBoxData['NAME']] = combobox

    def LoadGauge(self):
        for Data in self.GaugeList:
            gauge = self.GaugeMoveable()
            gauge.SetParent(self.Window)
            gauge.SetSize(100, 15)
            gauge.SetPosition(Data['X'], Data['Y'])
            gauge.MakeGauge(Data['WIDTH'], Data['COLOR'])
            gauge.SetText(Data['NAME'])
            gauge.SetMoveEvent(lambda arg = Data['NAME']: self.SetGaugePosition(arg))
            gauge.Show()
            self.itemDict[Data['NAME']] = gauge

    def SaveProject(self):
        save = uiCommon.InputDialogWithDescription()
        save.SetTitle('Save Project')
        save.SetDescription('ex. project1.txt')
        save.SetAcceptEvent(self.SaveProject2)
        save.SetCancelEvent(self.CancelSaveProject)
        save.Open()
        self.proj = save

    def SaveProject2(self):
        Name = self.proj.GetText()
        writef = open(Name, 'w+')
        writef.write('-Window:\t' + str(self.BOARD_SIZE[0]) + '\t' + str(self.BOARD_SIZE[1]) + '\t' + self.WindowType + '\n')
        for imageData in self.ImageList:
            writef.write('-Image:\t' + imageData['NAME'] + '\t' + str(imageData['X']) + '\t' + str(imageData['Y']) + '\t' + str(imageData['IMG']) + '\n')

        for ThinData in self.ThinBoardList:
            writef.write('-ThinBoard:\t' + ThinData['NAME'] + '\t' + str(ThinData['X']) + '\t' + str(ThinData['Y']) + '\t' + str(ThinData['SIZE_X']) + '\t' + str(ThinData['SIZE_Y']) + '\n')

        for BtnData in self.ButtonList:
            writef.write('-Button:\t' + BtnData['NAME'] + '\t' + BtnData['BUTTON_NAME'] + '\t' + str(BtnData['X']) + '\t' + str(BtnData['Y']) + '\t' + BtnData['default_image'] + '\t' + BtnData['over_image'] + '\t' + BtnData['down_image'] + '\n')

        for BtnData in self.ToggleButtonList:
            writef.write('-ToggleButton:\t' + BtnData['NAME'] + '\t' + BtnData['BUTTON_NAME'] + '\t' + str(BtnData['X']) + '\t' + str(BtnData['Y']) + '\t' + BtnData['default_image'] + '\t' + BtnData['over_image'] + '\t' + BtnData['down_image'] + '\n')

        for EditlnData in self.EditLineList:
            writef.write('-EditLine:\t' + EditlnData['NAME'] + '\t' + EditlnData['EDIT_TEXT'] + '\t' + str(EditlnData['X']) + '\t' + str(EditlnData['Y']) + '\t' + str(EditlnData['SIZE_X']) + '\t' + str(EditlnData['SIZE_Y']) + '\t' + str(EditlnData['MAX']) + '\t' + str(EditlnData['LINES']) + '\n')

        for TextlnData in self.TextLineList:
            writef.write('-TextLine:\t' + TextlnData['NAME'] + '\t' + TextlnData['BUTTON_NAME'] + '\t' + str(TextlnData['X']) + '\t' + str(TextlnData['Y']) + '\t' + str(TextlnData['COLOR'][0] / 255) + ' ' + str(TextlnData['COLOR'][1] / 255) + ' ' + str(TextlnData['COLOR'][2] / 255) + '\n')

        for sliderData in self.SliderBarList:
            writef.write('-SliderBar:\t' + sliderData['NAME'] + '\t' + str(sliderData['X']) + '\t' + str(sliderData['Y']) + '\n')

        for Data in self.GaugeList:
            writef.write('-Gauge:\t' + Data['NAME'] + '\t' + str(Data['X']) + '\t' + str(Data['Y']) + '\t' + str(Data['WIDTH']) + '\t' + str(Data['COLOR']) + '\n')

        for Data in self.ListBoxList:
            writef.write('-ListBox:\t' + Data['NAME'] + '\t' + str(Data['X']) + '\t' + str(Data['Y']) + '\t' + str(Data['WIDTH']) + '\t' + str(Data['HEIGHT']) + '\n')

        for comboData in self.ComboBoxList:
            writef.write('-ComboBox:\t' + comboData['NAME'] + '\t' + str(comboData['X']) + '\t' + str(comboData['Y']) + '\n')

        writef.close()
        self.proj.Hide()

    def CancelSaveProject(self):
        self.proj.Hide()
        self.proj = None
        return

    def Message(self, text):
        popup = uiCommon.PopupDialog()
        popup.SetText(text)
        popup.SetAcceptEvent(self.MessageClose)
        popup.Open()
        self.popup = popup

    def MessageClose(self):
        self.popup.Hide()
        self.popup = None
        return

    def Close(self):
        save = uiCommon.InputDialog()
        save.SetTitle('Window Name')
        save.SetAcceptEvent(self.CloseCancel)
        save.SetCancelEvent(self.CloseHide)
        save.Open()
        self.wndName = save

    def CloseCancel(self):
        self.BOARD_TITLE = self.wndName.GetText()
        self.Window.SetTitleName(self.BOARD_TITLE)
        self.wndName.Hide()
        self.wndName = None
        return

    def CloseHide(self):
        self.wndName.Hide()
        self.wndName = None
        return


class Component():

    def __init__(self):
        self.SMALL_BUTTON = {'default': 'd:/ymir work/ui/public/small_button_01.sub',
         'over': 'd:/ymir work/ui/public/small_button_02.sub',
         'down': 'd:/ymir work/ui/public/small_button_03.sub'}
        self.MIDDLE_BUTTON = {'default': 'd:/ymir work/ui/public/middle_button_01.sub',
         'over': 'd:/ymir work/ui/public/middle_button_02.sub',
         'down': 'd:/ymir work/ui/public/middle_button_03.sub'}
        self.LARGE_BUTTON = {'default': 'd:/ymir work/ui/public/large_button_01.sub',
         'over': 'd:/ymir work/ui/public/large_button_02.sub',
         'down': 'd:/ymir work/ui/public/large_button_03.sub'}
        self.CLOSE_BUTTON = {'default': 'd:/ymir work/ui/public/close_button_01.sub',
         'over': 'd:/ymir work/ui/public/close_button_02.sub',
         'down': 'd:/ymir work/ui/public/close_button_03.sub'}
        self.MIN_BUTTON = {'default': 'd:/ymir work/ui/public/minimize_button_01.sub',
         'over': 'd:/ymir work/ui/public/minimize_button_02.sub',
         'down': 'd:/ymir work/ui/public/minimize_button_03.sub'}

    class ResizeButton(ui.DragButton):

        def __init__(self):
            ui.DragButton.__init__(self)
            self.ButtonText = None
            return

        def __del__(self):
            ui.DragButton.__del__(self)

        def SetText(self, text, height = 4):
            if not self.ButtonText:
                self.ButtonText = ui.TextLine()
                self.ButtonText.SetParent(self)
                self.ButtonText.SetPosition(self.GetWidth() / 2, self.GetHeight() / 2)
                self.ButtonText.SetVerticalAlignCenter()
                self.ButtonText.SetHorizontalAlignCenter()
                self.ButtonText.Show()
            self.ButtonText.SetText(text)

        def OnMouseOverIn(self):
            app.SetCursor(app.HVSIZE)

        def OnMouseOverOut(self):
            app.SetCursor(app.NORMAL)

    def Button(self, parent, buttonName, tooltipText, x, y, func, UpVisual, OverVisual, DownVisual):
        button = ui.Button()
        button.SetParent(parent)
        button.SetPosition(x, y)
        button.SetUpVisual(UpVisual)
        button.SetOverVisual(OverVisual)
        button.SetDownVisual(DownVisual)
        button.SetText(buttonName)
        button.SetToolTipText(tooltipText)
        button.Show()
        button.SetEvent(func)
        return button

    def ToggleButton(self, parent, buttonName, tooltipText, x, y, funcUp, funcDown, UpVisual, OverVisual, DownVisual):
        button = ui.ToggleButton()
        button.SetParent(parent)
        button.SetPosition(x, y)
        button.SetUpVisual(UpVisual)
        button.SetOverVisual(OverVisual)
        button.SetDownVisual(DownVisual)
        button.SetText(buttonName)
        button.SetToolTipText(tooltipText)
        button.Show()
        button.SetToggleUpEvent(funcUp)
        button.SetToggleDownEvent(funcDown)
        return button

    def EditLine(self, parent, editlineText, x, y, width, heigh, max):
        SlotBar = ui.SlotBar()
        SlotBar.SetParent(parent)
        SlotBar.SetSize(width, heigh)
        SlotBar.SetPosition(x, y)
        SlotBar.Show()
        Value = ui.EditLine()
        Value.SetParent(SlotBar)
        Value.SetSize(width, heigh)
        Value.SetPosition(5, 1)
        Value.SetMax(max)
        Value.SetText(editlineText)
        Value.Show()
        return (SlotBar, Value)

    def TextLine(self, parent, textlineText, x, y, color):
        textline = ui.TextLine()
        textline.SetParent(parent)
        textline.SetPosition(x, y)
        if color != None:
            textline.SetFontColor(color[0], color[1], color[2])
        textline.SetText(textlineText)
        textline.Show()
        return textline

    def RGB(self, r, g, b):
        return (r * 255, g * 255, b * 255)

    def SliderBar(self, parent, sliderPos, func, x, y):
        Slider = ui.SliderBar()
        Slider.SetParent(parent)
        Slider.SetPosition(x, y)
        Slider.SetSliderPos(sliderPos / 100)
        Slider.Show()
        Slider.SetEvent(func)
        return Slider

    def ExpandedImage(self, parent, x, y, img):
        image = ui.ExpandedImageBox()
        image.SetParent(parent)
        image.SetPosition(x, y)
        image.LoadImage(img)
        image.Show()
        return image

    def ThinBoard(self, parent, moveable, x, y, width, heigh, center):
        thin = ui.ThinBoard()
        if parent != None:
            thin.SetParent(parent)
        if moveable == TRUE:
            thin.AddFlag('movable')
            thin.AddFlag('float')
        thin.SetSize(width, heigh)
        thin.SetPosition(x, y)
        if center == TRUE:
            thin.SetCenterPosition()
        thin.Show()
        return thin

    def ComboBox(self, parent, text, x, y, width):
        combo = ComboBox()
        combo.SetParent(parent)
        combo.SetPosition(x, y)
        combo.SetSize(width, 15)
        combo.SetCurrentItem(text)
        combo.Show()
        return combo


class ComboBox(ui.Window):

    class ListBoxWithBoard(ui.ListBox):

        def __init__(self, layer):
            ui.ListBox.__init__(self, layer)

        def OnRender(self):
            xRender, yRender = self.GetGlobalPosition()
            yRender -= self.TEMPORARY_PLACE
            widthRender = self.width
            heightRender = self.height + self.TEMPORARY_PLACE * 2
            grp.SetColor(ui.BACKGROUND_COLOR)
            grp.RenderBar(xRender, yRender, widthRender, heightRender)
            grp.SetColor(ui.DARK_COLOR)
            grp.RenderLine(xRender, yRender, widthRender, 0)
            grp.RenderLine(xRender, yRender, 0, heightRender)
            grp.SetColor(ui.BRIGHT_COLOR)
            grp.RenderLine(xRender, yRender + heightRender, widthRender, 0)
            grp.RenderLine(xRender + widthRender, yRender, 0, heightRender)
            ui.ListBox.OnRender(self)

    def __init__(self):
        ui.Window.__init__(self)
        self.x = 0
        self.y = 0
        self.width = 0
        self.height = 0
        self.isSelected = FALSE
        self.isOver = FALSE
        self.isListOpened = FALSE
        self.event = lambda *arg: None
        self.enable = TRUE
        self.textLine = ui.MakeTextLine(self)
        self.textLine.SetText(locale.UI_ITEM)
        self.listBox = self.ListBoxWithBoard('TOP_MOST')
        self.listBox.SetPickAlways()
        self.listBox.SetParent(self)
        self.listBox.SetEvent(ui.__mem_func__(self.OnSelectItem))
        self.listBox.Hide()

    def __del__(self):
        ui.Window.__del__(self)

    def Destroy(self):
        self.textLine = None
        self.listBox = None
        return

    def SetPosition(self, x, y):
        ui.Window.SetPosition(self, x, y)
        self.x = x
        self.y = y
        self.__ArrangeListBox()

    def SetSize(self, width, height):
        ui.Window.SetSize(self, width, height)
        self.width = width
        self.height = height
        self.textLine.UpdateRect()
        self.__ArrangeListBox()

    def __ArrangeListBox(self):
        self.listBox.SetPosition(0, self.height + 5)
        self.listBox.SetWidth(self.width)

    def Enable(self):
        self.enable = TRUE

    def Disable(self):
        self.enable = FALSE
        self.textLine.SetText('')
        self.CloseListBox()

    def SetEvent(self, event):
        self.event = event

    def ClearItem(self):
        self.CloseListBox()
        self.listBox.ClearItem()

    def InsertItem(self, index, name):
        self.listBox.InsertItem(index, name)
        self.listBox.ArrangeItem()

    def SetCurrentItem(self, text):
        self.textLine.SetText(text)

    def GetCurrentText(self):
        return self.textLine.GetText()

    def GetCurrentIndex(self):
        return self.listBox.selectedLine

    def SelectItem(self, key):
        self.listBox.SelectItem(key)

    def OnSelectItem(self, index, name):
        self.SetCurrentItem(name)
        self.CloseListBox()
        self.event(index)

    def CloseListBox(self):
        self.isListOpened = FALSE
        self.listBox.Hide()

    def OnMouseLeftButtonDown(self):
        if not self.enable:
            return
        self.isSelected = TRUE

    def OnMouseLeftButtonUp(self):
        if not self.enable:
            return
        self.isSelected = FALSE
        if self.isListOpened:
            self.CloseListBox()
        elif self.listBox.GetItemCount() > 0:
            self.isListOpened = TRUE
            self.listBox.Show()
            self.__ArrangeListBox()

    def OnUpdate(self):
        if not self.enable:
            return
        if self.IsIn():
            self.isOver = TRUE
        else:
            self.isOver = FALSE

    def OnRender(self):
        self.x, self.y = self.GetGlobalPosition()
        xRender = self.x
        yRender = self.y
        widthRender = self.width
        heightRender = self.height
        grp.SetColor(ui.BACKGROUND_COLOR)
        grp.RenderBar(xRender, yRender, widthRender, heightRender)
        grp.SetColor(ui.DARK_COLOR)
        grp.RenderLine(xRender, yRender, widthRender, 0)
        grp.RenderLine(xRender, yRender, 0, heightRender)
        grp.SetColor(ui.BRIGHT_COLOR)
        grp.RenderLine(xRender, yRender + heightRender, widthRender, 0)
        grp.RenderLine(xRender + widthRender, yRender, 0, heightRender)
        if self.isOver:
            grp.SetColor(ui.HALF_WHITE_COLOR)
            grp.RenderBar(xRender + 2, yRender + 3, self.width - 3, heightRender - 5)
            if self.isSelected:
                grp.SetColor(ui.WHITE_COLOR)
                grp.RenderBar(xRender + 2, yRender + 3, self.width - 3, heightRender - 5)


class Item(ui.ListBoxEx.Item):

    def __init__(self, fileName):
        ui.ListBoxEx.Item.__init__(self)
        self.canLoad = 0
        self.text = fileName
        self.textLine = self.__CreateTextLine(fileName[:50])

    def __del__(self):
        ui.ListBoxEx.Item.__del__(self)

    def GetText(self):
        return self.text

    def SetSize(self, width, height):
        ui.ListBoxEx.Item.SetSize(self, 7 * len(self.textLine.GetText()) + 4, height)

    def __CreateTextLine(self, fileName):
        textLine = ui.TextLine()
        textLine.SetParent(self)
        textLine.SetPosition(0, 0)
        textLine.SetText(fileName)
        textLine.Show()
        return textLine


Dialog1().Show()