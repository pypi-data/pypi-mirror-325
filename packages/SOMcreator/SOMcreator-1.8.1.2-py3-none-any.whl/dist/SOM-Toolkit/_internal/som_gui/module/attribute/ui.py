from PySide6.QtCore import QRect, QSize, Qt
from PySide6.QtWidgets import QHeaderView, QWidget

from .qt import ui_CompareWidget


class AttributeWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = ui_CompareWidget.Ui_AttributeCompare()
        self.ui.setupUi(self)
        self.ui.tree_widget_object.setColumnCount(2)
        self.ui.tree_widget_propertysets.setColumnCount(2)
        self.ui.table_widget_values.setColumnCount(2)
        self.ui.table_infos.setColumnCount(3)


class WordWrapHeaderView(QHeaderView):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def sectionSizeFromContents(self, logicalIndex):
        text = str(self.model().headerData(logicalIndex, self.orientation(), Qt.ItemDataRole.DisplayRole))
        max_width = self.sectionSize(logicalIndex)
        maxheight = 5000
        alignement = self.defaultAlignment()
        metrics = self.fontMetrics()
        rect = metrics.boundingRect(QRect(0, 0, max_width, maxheight), alignement, text)
        text_margin_buffer = QSize(2, 2)
        return rect.size() + text_margin_buffer
