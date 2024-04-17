from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common_controls.AnimatedToggle import AnimatedToggle

app = QApplication([])

window = QWidget()

mainToggle = AnimatedToggle()
secondaryToggle = AnimatedToggle(
        checked_color="#FFB000",
        pulse_checked_color="#44FFB000"
)
mainToggle.setFixedSize(mainToggle.sizeHint())
secondaryToggle.setFixedSize(mainToggle.sizeHint())

window.setLayout(QVBoxLayout())
window.layout().addWidget(QLabel("Main Toggle"))
window.layout().addWidget(mainToggle)

window.layout().addWidget(QLabel("Secondary Toggle"))
window.layout().addWidget(secondaryToggle)

mainToggle.stateChanged.connect(secondaryToggle.setChecked)

window.show()
app.exec_()