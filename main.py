import sys
from PySide6.QtWidgets import QApplication

from q6p3ui.tictactoe import TicTacToe

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TicTacToe()
    window.state = "-X-XO----"
    window.show()
    sys.exit(app.exec())