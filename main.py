# OpenCodeBlock an open-source tool for modular visual programing in python
# Copyright (C) 2021 Mathïs FEDERICO <https://www.gnu.org/licenses/>

import os
import sys

from qtpy.QtWidgets import QApplication

from opencodeblocks.core.node import CodeNode
from opencodeblocks.graphics.block import OCBBlock
from opencodeblocks.graphics.window import OCBWindow

sys.path.insert(0, os.path.join( os.path.dirname(__file__), "..", ".." ))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')

    wnd = OCBWindow()

    test_block = OCBBlock(CodeNode(title="Test Block with a very very very long long name"))
    for _ in range(5):
        test_block.add_socket(socket_type='input')
    for _ in range(3):
        test_block.add_socket(socket_type='output')
    wnd.scene.addItem(test_block)

    test_block_2 = OCBBlock(CodeNode(title="Test Block 2"))
    for _ in range(3):
        test_block_2.add_socket(socket_type='input')
    for _ in range(1):
        test_block_2.add_socket(socket_type='output')
    test_block_2.setPos(-300, -100)
    wnd.scene.addItem(test_block_2)
    wnd.show()

    sys.exit(app.exec_())
