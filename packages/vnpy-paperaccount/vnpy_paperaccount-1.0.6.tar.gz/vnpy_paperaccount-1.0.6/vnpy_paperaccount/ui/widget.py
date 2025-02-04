from vnpy.event import EventEngine
from vnpy.trader.engine import MainEngine
from vnpy.trader.ui import QtWidgets

from ..engine import (
    PaperEngine,
    APP_NAME,
)


class PaperManager(QtWidgets.QWidget):
    """"""

    def __init__(self, main_engine: MainEngine, event_engine: EventEngine) -> None:
        """"""
        super().__init__()

        self.main_engine: MainEngine = main_engine
        self.event_engine: EventEngine = event_engine

        self.paper_engine: PaperEngine = main_engine.get_engine(APP_NAME)

        self.init_ui()

    def init_ui(self) -> None:
        """"""
        self.setWindowTitle("模拟交易")
        self.setFixedHeight(200)
        self.setFixedWidth(500)

        interval_spin: QtWidgets.QSpinBox = QtWidgets.QSpinBox()
        interval_spin.setMinimum(1)
        timer_interval: int = self.paper_engine.get_timer_interval()
        interval_spin.setValue(timer_interval)
        interval_spin.setSuffix(" 秒")
        interval_spin.valueChanged.connect(self.paper_engine.set_timer_interval)

        slippage_spin: QtWidgets.QSpinBox = QtWidgets.QSpinBox()
        slippage_spin.setMinimum(0)
        trade_slippage: int = self.paper_engine.get_trade_slippage()
        slippage_spin.setValue(trade_slippage)
        slippage_spin.setSuffix(" 跳")
        slippage_spin.valueChanged.connect(self.paper_engine.set_trade_slippage)

        instant_check: QtWidgets.QCheckBox = QtWidgets.QCheckBox()
        instant_trade: bool = self.paper_engine.get_instant_trade()
        instant_check.setChecked(instant_trade)
        instant_check.stateChanged.connect(self.paper_engine.set_instant_trade)

        clear_button: QtWidgets.QPushButton = QtWidgets.QPushButton("清空所有持仓")
        clear_button.clicked.connect(self.paper_engine.clear_position)
        clear_button.setFixedHeight(clear_button.sizeHint().height() * 2)

        form: QtWidgets.QFormLayout = QtWidgets.QFormLayout()
        form.addRow("市价委托和停止委托的成交滑点", slippage_spin)
        form.addRow("模拟交易持仓盈亏的计算频率", interval_spin)
        form.addRow("下单后立即使用当前盘口撮合", instant_check)
        form.addRow(clear_button)

        vbox: QtWidgets.QVBoxLayout = QtWidgets.QVBoxLayout()
        vbox.addStretch()
        vbox.addLayout(form)
        vbox.addStretch()
        self.setLayout(vbox)
