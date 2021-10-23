from pyLoadingScreen import LoadingScreen
from threading import Thread
from PyQt5.QtWidgets import *

app= QApplication([])
screen = LoadingScreen()
thread = Thread(target=screen.worker)
thread.start()
app.exec()