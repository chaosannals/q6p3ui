from PySide6.QtDesigner import QPyDesignerCustomWidgetCollection
from q6p3ui.tictactoe.plugin import TicTacToePlugin

# with open('G:\\bbb.txt', 'w', encoding='utf8') as wr:
#     wr.write('bbb')

if __name__ == '__main__':
    # with open('G:\\aaa.txt', 'w', encoding='utf8') as wr:
    #     wr.write('aaaaa')
    QPyDesignerCustomWidgetCollection.addCustomWidget(TicTacToePlugin())