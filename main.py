from PySide6.QtWidgets import QApplication
from sizePoliciesAndStretches import Widget
import sys

app = QApplication(sys.argv)

window = Widget()
window.show()

app.exec()