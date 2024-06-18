from PySide6.QtWidgets import *

class Widget(QWidget):
    def __init__(self):
        super().__init__()

        LB_typeHere = QLabel("Type Here:")

        LE_typeHere = QLineEdit()
        LE_typeHere.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        HL_1 = QHBoxLayout()
        HL_1.addWidget(LB_typeHere)
        HL_1.addWidget(LE_typeHere)

        PB_One = QPushButton("One")
        PB_Two = QPushButton("Two")
        PB_Three = QPushButton("Three")

        HL_2 = QHBoxLayout()
        HL_2.addWidget(PB_One, 1)
        HL_2.addWidget(PB_Two, 2)
        HL_2.addWidget(PB_Three, 3)

        VL = QVBoxLayout()
        VL.addLayout(HL_1)
        VL.addLayout(HL_2)
        self.setLayout(VL)