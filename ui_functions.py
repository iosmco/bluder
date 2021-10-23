from main import *

def guisave(ui, settings):

    for name, obj in inspect.getmembers(ui):
        #if type(obj) is QComboBox:  # this works similar to isinstance, but missed some field... not sure why?
        if isinstance(obj, QComboBox):
            name   = obj.objectName()      # get combobox name
            index  = obj.currentIndex()    # get current index from combobox
            text   = obj.itemText(index)   # get the text for current index
            settings.setValue(name, text)   # save combobox selection to registry

        if isinstance(obj, QLineEdit):
            name = obj.objectName()
            value = obj.text()
            settings.setValue(name, value)    # save ui values, so they can be restored next time

        if isinstance(obj, QCheckBox):
            name = obj.objectName()
            state = obj.isChecked()
            settings.setValue(name, state)

        if isinstance(obj, QRadioButton):
            name = obj.objectName()
            state = obj.isChecked()
            settings.setValue(name, state)

        if isinstance(obj, QToolButton):
            name = obj.objectName()
            state = obj.isChecked()
            settings.setValue(name, state)

def guirestore(ui, settings):

    for name, obj in inspect.getmembers(ui):
        if isinstance(obj, QComboBox):
            index  = obj.currentIndex()    # get current region from combobox
            #text   = obj.itemText(index)   # get the text for new selected index
            name   = obj.objectName()

            value = (settings.value(name))  

            if value == "":
                continue

            index = obj.findText(value)   # get the corresponding index for specified string in combobox

            if index == -1:  # add to list if not found
                obj.insertItems(0,[value])
                index = obj.findText(value)
                obj.setCurrentIndex(index)
            else:
                obj.setCurrentIndex(index)   # preselect a combobox value by index    

        if isinstance(obj, QLineEdit):
            name = obj.objectName()
            value = settings.value(name)  # get stored value from registry
            obj.setText(value)  # restore lineEditFile

        if isinstance(obj, QCheckBox):
            name = obj.objectName()
            value = (settings.value(name))   # get stored value from registry
            if value != None:
                obj.setChecked(strtobool(value))   # restore checkbox

        if isinstance(obj, QRadioButton):   
            name = obj.objectName()
            value = (settings.value(name))   # get stored value from registry
            if value != None:
                obj.setChecked(strtobool(value))   # restore radiobutton

        if isinstance(obj, QToolButton):   
            name = obj.objectName()
            value = (settings.value(name))   # get stored value from registry
            if value != None:
                obj.setChecked(strtobool(value))   # restore toolbutton             

################################################################

## ==> GLOBALS

GLOBAL_STATE = 0

class UIFunctions(MainWindow):

    ## ==> MAXIMIZE RESTORE FUNCTION
    def maximize_restore(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE

        # IF NOT MAXIMIZED
        if status == 0:
            self.shadow.setEnabled(False)
            self.showMaximized()

            # SET GLOBAL TO 1
            GLOBAL_STATE = 1

            # IF MAXIMIZED REMOVE MARGINS AND BORDER RADIUS
            self.ui.drop_shadow_layout.setContentsMargins(0, 0, 0, 0)
            state = self.ui.btn_modes.isChecked()
            if state == False:
                self.ui.drop_shadow_frame.setStyleSheet("background-color: #dddddd;border-radius: 0px;")
            else:
                self.ui.drop_shadow_frame.setStyleSheet("background-color: black;border-radius: 0px;")
            self.ui.btn_maximize.setToolTip("Restore")
            QApplication.processEvents()
        else:
            GLOBAL_STATE = 0
            self.shadow.setEnabled(True)
            self.showNormal()
            self.resize(self.width()+1, self.height()+1)
            self.ui.drop_shadow_layout.setContentsMargins(10, 10, 10, 10)
            state2 = self.ui.btn_modes.isChecked()
            if state2 == False:
                self.ui.drop_shadow_frame.setStyleSheet("background-color: #dddddd;border-radius: 10px;")
            else:
                self.ui.drop_shadow_frame.setStyleSheet("background-color: black;border-radius: 10px;")
            self.ui.btn_maximize.setToolTip("Maximize")
            QApplication.processEvents()

    ## ==> UI DEFINITIONS
    def uiDefinitions(self):

        # REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # SET DROPSHADOW WINDOW
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 100))

        # APPLY DROPSHADOW TO FRAME
        self.ui.drop_shadow_frame.setGraphicsEffect(self.shadow)

        # MAXIMIZE / RESTORE
        self.ui.btn_maximize.clicked.connect(lambda : UIFunctions.maximize_restore(self))
        # MINIMIZE
        self.ui.btn_minimize.clicked.connect(lambda : self.showMinimized())

        # CLOSE
        self.ui.btn_close.clicked.connect(lambda : self.close())

        ## ==> CREATE SIZE GRIP TO RESIZE WINDOW
        self.sizegrip = QSizeGrip(self.ui.frame_grip)
        self.sizegrip.setStyleSheet("QSizeGrip { width: 10px; height:: 10px; margin: 5px; } QSize Grip:hover { background-color: rbg(50, 42, 94) }")
        self.sizegrip.setToolTip("Resize Window")
        QApplication.processEvents()

    ## RETURN STATUS IF WINDOWS IS MAXIMIZE OR RESTAURED
    def returnStatus():
        return GLOBAL_STATE
