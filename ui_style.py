
class LightStyle():
    label_title = """QLabel{
        color: black;
    }
    """
    groupBox_menu = """
    QGroupBox{
	    color: gray;
    }
    QPushButton {
        background-color: transparent;
        color: gray;
        text-align: left;
        outline: none;
        border-left: 15px;
    }
    QPushButton:hover {
        color: black;
    }
    QPushButton:checked {
        background-color: white;
    }
    """
    frame_data = """
    QStackedWidget {
	    background-color: white;
	    background: white;
	    border: none;
	    border-radius: 20px;
    }
    QLabel {
        background-color: transparent;
        color: gray;
    }
    QToolButton {
        color: black;
    }
    QPushButton {
        border-radius: 10px;	
        background-color: #0055ff;
        color: white;
        text-align: center;
        outline: none;
    }
    QPushButton:hover {
        background-color: #003db9;
    }
    QPushButton:pressed {	
        background-color: #dddddd;
        color: black;
    }
    QPushButton:disabled {	
        border-radius: 10px;
        color: gray;
        background-color: #dddddd;
    }
    QLineEdit {
        background-color: #dddddd;
        border-radius: 10px;
        padding-left: 10px;
        color: black;
    }
    QLineEdit:focus {
        border: 2px solid #0055ff;
    }
    QProgressBar {
        background-color: #dddddd;
        color: black;
        border-radius: 10px;
    }
    QProgressBar:chunk {
        background-color: #0055ff;
        border-radius: 10px;
    }
    QGroupBox {
        border-radius: 10px;
        background-color: #dddddd;
    }
    QTabWidget::pane {
        border: none;
        background: transparent;
        background-color: none;
    }
    QTabWidget::tab-bar:top {
        top: 1px;
    }
    QTabWidget::tab-bar:bottom {
        bottom: 1px;
    }
    QTabWidget::tab-bar:left {
        right: 1px;
    }
    QTabWidget::tab-bar:right {
        left: 1px;
    }
    QTabBar::tab {
        font: 57 8pt "Roboto Medium";
        background: transparent;
        border: none;
        padding: 8px;
    }
    QTabBar::tab:selected{
        font: 57 10pt "Roboto Medium";
        border: none;
        color: black;
        background: transparent;
        background-color: transparent;
    }
    QTabBar::tab:!selected{
        border: none;
        color: gray;
        background: transparent;
        background-color: transparent;
    }
    QComboBox{
        background-color: #dddddd;
        border: none;
        border-radius: 10px;
        padding: 5px;
        padding-left: 10px;
        color: gray;
    }
    QComboBox::drop-down {
        subcontrol-origin: padding;
        subcontrol-position: top right;
        width: 25px; 
        border-left-width: 2px;
        border-left-color: #dddddd;
        border-left-style: solid;
        border-top-right-radius: 3px;
        border-bottom-right-radius: 3px;	
        background-image:url(:/icons/icons/chevron-down.svg);
        background-position: center;
        background-repeat: no-reperat;
    }
    QComboBox QAbstractItemView {
        color:black;	
        background-color:#dddddd;
        padding: 10px;
        selection-background-color: #bbbbbb;
        outline: none;
    }
    QCheckBox{
        color: black;
    }
    QCheckBox::indicator {
        border: 3px solid #aaaaaa;
        width: 15px;
        height: 15px;
        border-radius: 10px;
        background: #dddddd;
    }
    QCheckBox::indicator:hover {
        border: 3px solid #bbbbbb;
    }
    QCheckBox::indicator:checked {
        background: 3px solid #aaaaaa;
        border: 3px solid #aaaaaa;
        background-image: url(:/icons/icons/cil-check-alt.png);
    }
    QRadioButton{
        color: white;
    }
    QRadioButton::indicator {
        border: 3px solid #aaaaaa;
        width: 15px;
        height: 15px;
        border-radius: 10px;
        background: #dddddd;
    }
    QRadioButton::indicator:hover {
        border: 3px solid #bbbbbb;
    }
    QRadioButton::indicator:checked {
        background: 3px solid #dddddd;
        border: 3px solid #bbbbbb;	
    }
    QScrollBar:horizontal {
        border: none;
        background: #bbbbbb;
        height: 14px;
        margin: 0px 21px 0 21px;
        border-radius: 0px;
    }
    QScrollBar::handle:horizontal {
        background: #0055ff;
        min-width: 25px;
        border-radius: 7px
    }
    QScrollBar::add-line:horizontal {
        border: none;
        background: #bbbbbb;
        width: 20px;
        border-top-right-radius: 7px;
        border-bottom-right-radius: 7px;
        subcontrol-position: right;
        subcontrol-origin: margin;
    }
    QScrollBar::sub-line:horizontal {
        border: none;
        background: #bbbbbb;
        width: 20px;
        border-top-left-radius: 7px;
        border-bottom-left-radius: 7px;
        subcontrol-position: left;
        subcontrol-origin: margin;
    }
    QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal
    {
        background: none;
    }
    QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal
    {
        background: none;
    }
    QScrollBar:vertical {
        border: none;
        background: #bbbbbb;
        width: 14px;
        margin: 21px 0 21px 0;
        border-radius: 0px;
    }
    QScrollBar::handle:vertical {	
        background: #0055ff;
        min-height: 25px;
        border-radius: 7px
    }
    QScrollBar::add-line:vertical {
        border: none;
        background: #bbbbbb;
        height: 20px;
        border-bottom-left-radius: 7px;
        border-bottom-right-radius: 7px;
        subcontrol-position: bottom;
        subcontrol-origin: margin;
    }
    QScrollBar::sub-line:vertical {
        border: none;
        background:#bbbbbb;
        height: 20px;
        border-top-left-radius: 7px;
        border-top-right-radius: 7px;
        subcontrol-position: top;
        subcontrol-origin: margin;
    }
    QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {
        background: none;
    }

    QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
        background: none;
    }
    """
    
    circularBg = """
    QFrame{
	border-radius: 70px;
	background-color:#aaaaaa;
    }
    """
    container = """
    QFrame{
	border-radius: 60px;
	background-color: #dddddd;
    }
    """
    drop_shadow_frame = """
    background-color: #dddddd;
    border-radius: 10px;
    """
    label_credits = """
    color: black;
    """
    tab4 = """
    QCheckBox{
        color: black;
    }
    QCheckBox::indicator {
        border: 3px solid #aaaaaa;
        width: 15px;
        height: 15px;
        border-radius: 10px;
        background: #dddddd;
    }
    QCheckBox::indicator:hover {
        border: 3px solid #bbbbbb;
    }
    QCheckBox::indicator:checked {
        background: 3px solid #aaaaaa;
        border: 3px solid #aaaaaa;
        background-image: url(:/icons/icons/cil-check-alt.png);
    }
    QRadioButton{
        color: white;
    }
    QRadioButton::indicator {
        border: 3px solid #aaaaaa;
        width: 15px;
        height: 15px;
        border-radius: 10px;
        background: #dddddd;
    }
    QRadioButton::indicator:hover {
        border: 3px solid #bbbbbb;
    }
    QRadioButton::indicator:checked {
        background: 3px solid #dddddd;
        border: 3px solid #bbbbbb;	
    }
    """

class DarkStyle():
    label_title = """
    QLabel{
        color: white;
    }
    """
    groupBox_menu = """
    QGroupBox {
        color: gray;
    }
    QPushButton {
        background-color: transparent;
        color: gray;
        text-align: left;
        outline: none;
        border-left: 15px;
    }
    QPushButton:hover {
        color: silver;
    }
    QPushButton:checked {
        background-color: #101010;
    }
    """
    frame_data = """
    QStackedWidget {
        background-color: #101010;
        background: #101010;
        border: none;
        border-radius: 20px;
    }
    QLabel {
        background-color: transparent;
        color: gray;
    }
    QToolButton {
        color: white;
    }
    QPushButton {
        border-radius: 10px;	
        background-color: #0055ff;
        color: white;
        text-align: center;
        outline: none;
    }
    QPushButton:hover {
        background-color: #003db9;
    }
    QPushButton:pressed {	
        background-color: black;
        color: white;
    }
    QPushButton:disabled {	
        border-radius: 10px;
        color: gray;
        background-color: black;
    }
    QLineEdit {
        background-color: black;
        border-radius: 10px;
        padding-left: 10px;
        color: white;
    }
    QLineEdit:focus {
        border: 2px solid #0055ff;
    }
    QProgressBar {
        background-color: black;
        color: white;
        border-radius: 10px;
    }
    QProgressBar:chunk {
        background-color: #0055ff;
        border-radius: 10px;
    }
    QGroupBox {
        border-radius: 10px;
        background-color: black;
    }
    QTabWidget::pane {
        border: none;
        background: transparent;
        background-color: none;
    }
    QTabWidget::tab-bar:top {
        top: 1px;
    }
    QTabWidget::tab-bar:bottom {
        bottom: 1px;
    }
    QTabWidget::tab-bar:left {
        right: 1px;
    }
    QTabWidget::tab-bar:right {
        left: 1px;
    }
    QTabBar::tab {
        font: 57 8pt "Roboto Medium";
        background: transparent;
        border: none;
        padding: 8px;
    }
    QTabBar::tab:selected{
        font: 57 10pt "Roboto Medium";
        border: none;
        color: white;
        background: transparent;
        background-color: transparent;
    }
    QTabBar::tab:!selected{
        border: none;
        color: gray;
        background: transparent;
        background-color: transparent;
    }
    QComboBox{
        background-color: black;
        border: none;
        border-radius: 10px;
        padding: 5px;
        padding-left: 10px;
        color: gray;
    }
    QComboBox::drop-down {
        subcontrol-origin: padding;
        subcontrol-position: top right;
        width: 25px; 
        border-left-width: 2px;
        border-left-color: black;
        border-left-style: solid;
        border-top-right-radius: 3px;
        border-bottom-right-radius: 3px;	
        background-image:url(:/icons/icons/chevron-down.svg);
        background-position: center;
        background-repeat: no-reperat;
    }
    QComboBox QAbstractItemView {
        color:white;	
        background-color:black;
        padding: 10px;
        selection-background-color: #202020;
        outline: none;
    }
    QCheckBox{
        color: white;
    }
    QCheckBox::indicator {
        border: 3px solid #202020;
        width: 15px;
        height: 15px;
        border-radius: 10px;
        background: black;
    }
    QCheckBox::indicator:hover {
        border: 3px solid #303030;
    }
    QCheckBox::indicator:checked {
        background: 3px solid #101010;
        border: 3px solid #101010;
        background-image: url(:/icons/icons/cil-check-alt.png);
    }
    QRadioButton{
        color: white;
    }
    QRadioButton::indicator {
        border: 3px solid #202020;
        width: 15px;
        height: 15px;
        border-radius: 10px;
        background: black;
    }
    QRadioButton::indicator:hover {
        border: 3px solid #303030;
    }
    QRadioButton::indicator:checked {
        background: 3px solid #101010;
        border: 3px solid #202020;	
    }
    QScrollBar:horizontal {
        border: none;
        background: #202020;
        height: 14px;
        margin: 0px 21px 0 21px;
        border-radius: 0px;
    }
    QScrollBar::handle:horizontal {
        background: #0055ff;
        min-width: 25px;
        border-radius: 7px
    }
    QScrollBar::add-line:horizontal {
        border: none;
        background: #202020;
        width: 20px;
        border-top-right-radius: 7px;
        border-bottom-right-radius: 7px;
        subcontrol-position: right;
        subcontrol-origin: margin;
    }
    QScrollBar::sub-line:horizontal {
        border: none;
        background: #202020;
        width: 20px;
        border-top-left-radius: 7px;
        border-bottom-left-radius: 7px;
        subcontrol-position: left;
        subcontrol-origin: margin;
    }
    QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal
    {
        background: none;
    }
    QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal
    {
        background: none;
    }
    QScrollBar:vertical {
        border: none;
        background: #202020;
        width: 14px;
        margin: 21px 0 21px 0;
        border-radius: 0px;
    }
    QScrollBar::handle:vertical {	
        background: #0055ff;
        min-height: 25px;
        border-radius: 7px
    }
    QScrollBar::add-line:vertical {
        border: none;
        background: #202020;
        height: 20px;
        border-bottom-left-radius: 7px;
        border-bottom-right-radius: 7px;
        subcontrol-position: bottom;
        subcontrol-origin: margin;
    }
    QScrollBar::sub-line:vertical {
        border: none;
        background:#202020;
        height: 20px;
        border-top-left-radius: 7px;
        border-top-right-radius: 7px;
        subcontrol-position: top;
        subcontrol-origin: margin;
    }
    QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {
        background: none;
    }

    QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
        background: none;
    }
    """

    circularBg = """
    QFrame{
	    border-radius: 70px;
	    background-color:#202020;
    }
    """
    container = """
    QFrame{
	    border-radius: 60px;
	    background-color: black;
    }
    """
    drop_shadow_frame = """
    background-color: black;
    border-radius: 10px;
    """
    label_credits = """
    color: white;
    """

    tab4 = """
    QCheckBox{
        color: white;
    }
    QCheckBox::indicator {
        border: 3px solid #202020;
        width: 15px;
        height: 15px;
        border-radius: 10px;
        background: black;
    }
    QCheckBox::indicator:hover {
        border: 3px solid #303030;
    }
    QCheckBox::indicator:checked {
        background: 3px solid #101010;
        border: 3px solid #101010;
        background-image: url(:/icons/icons/cil-check-alt.png);
    }
    QRadioButton{
        color: white;
    }
    QRadioButton::indicator {
        border: 3px solid #202020;
        width: 15px;
        height: 15px;
        border-radius: 10px;
        background: black;
    }
    QRadioButton::indicator:hover {
        border: 3px solid #303030;
    }
    QRadioButton::indicator:checked {
        background: 3px solid #101010;
        border: 3px solid #202020;	
    }
    """