from PySide6 import QtCharts, QtCore, QtGui, QtWidgets


class InteractiveChartView(QtCharts.QChartView):
    def __init__(self):
        super().__init__()

        self.setRenderHints(QtGui.QPainter.Antialiasing)

        self._last_cursor_pos: QtCore.QPoint | None = None

        self._coord_x = QtWidgets.QGraphicsSimpleTextItem(self.chart())
        self._coord_x.setPos(self.chart().size().width() / 2 + 50, self.chart().size().height() + 20)
        self._coord_x.setText('X: ')
        self._coord_y = QtWidgets.QGraphicsSimpleTextItem(self.chart())
        self._coord_y.setPos(self.chart().size().width() / 2 + 100, self.chart().size().height() + 20)
        self._coord_y.setText('Y: ')

    def wheelEvent(self, event):
        delta = event.angleDelta().y()

        if delta > 0:
            self.chart().zoom(1.1)
        else:
            self.chart().zoom(0.9)

        event.accept()

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self._last_cursor_pos = event.pos()

            event.accept()

    def mouseDoubleClickEvent(self, event):
        self.chart().zoomReset()

        for series in self.chart().series():
            x_range_max = series.count()
            y_max = series.points()[0]
            self.chart().axisX(series).setRange(0, x_range_max)

            if y_max.y() <= 100:
                self.chart().axisY(series).setRange(0, 100)
            else:
                self.chart().axisY(series).setRange(0, y_max.y())

        event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            if self._last_cursor_pos is not None:
                delta = event.pos() - self._last_cursor_pos

                self.chart().scroll(-delta.x(), delta.y())

            self._last_cursor_pos = event.pos()

            event.accept()

        if len(self.chart().series()) > 0:
            cursor_pos = event.pos()

            value = self.chart().mapToValue(cursor_pos)

            self._coord_x.setText('X: {:.2f}'.format(value.x()))
            self._coord_y.setText('Y: {:.2f}'.format(value.y()))

            event.accept()

    def resizeEvent(self, event):
        if self.scene():
            self.scene().setSceneRect(QtCore.QRect(QtCore.QPoint(0, 0), event.size()))
            self.chart().resize(event.size())
            self._coord_x.setPos(16, self.chart().size().height() - 25)
            self._coord_y.setPos(75, self.chart().size().height() - 25)
            
    def setChart(self, chart):
        super().setChart(chart)

        self._coord_x = QtWidgets.QGraphicsSimpleTextItem(chart)
        self._coord_y = QtWidgets.QGraphicsSimpleTextItem(chart)

        self._coord_x.setPos(16, self.chart().size().height() - 25)
        self._coord_y.setPos(75, self.chart().size().height() - 25)

        self._coord_x.setText('X: 0.00')
        self._coord_y.setText('Y: 0.00')

