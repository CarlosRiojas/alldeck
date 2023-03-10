import sys

from PyQt6.QtCore import(Qt,QUrl)
from PyQt6.QtWebEngineCore import (QWebEngineUrlScheme,QWebEngineCookieStore,)
from PyQt6.QtWebEngineWidgets import (QWebEngineView)
from PyQt6.QtWidgets import (
    QApplication,
    QGridLayout,
    QWidget,
    QMainWindow,
    QVBoxLayout,
)

class Window(QMainWindow):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("AllDeck")
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint | Qt.WindowType.Tool | Qt.WindowType.CustomizeWindowHint | Qt.WindowType.WindowStaysOnTopHint)
        self.setStyleSheet("QMainWindow { background-color:white; min-width: 400px; min-height: 800px;}")
        self.grid = QGridLayout()
        #web engine
        web = QWebEngineView()
        web.load(QUrl("https://www.reddit.com"))
        layout = QVBoxLayout()
        layout.addWidget(web)
        centralWidget = QWidget(self)
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)



if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())


