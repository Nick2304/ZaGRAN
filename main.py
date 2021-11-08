
import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets
from PyQt5.QtGui import QFont

import main_form  # Это наш конвертированный файл дизайна


class ExampleApp(QtWidgets.QMainWindow, main_form.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле main_form.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.tabWidget.setCurrentIndex(0)
        self.textLog.setHtml('qweasd123456')
        self.textLog.append('qqqqqqq')



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение




