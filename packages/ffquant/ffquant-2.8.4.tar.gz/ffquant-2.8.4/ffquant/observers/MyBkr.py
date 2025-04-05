import backtrader as bt
import pytz
import ffquant.utils.global_backtest_data as global_backtest_data

__ALL__ = ['MyBkr']

# 用于记录账户价值、k线数据、仓位信息
class MyBkr(bt.observers.Broker):
    def __init__(self):
        super(MyBkr, self).__init__()
        self.broker_values = global_backtest_data.broker_values
        self.klines = global_backtest_data.klines
        self.positions = global_backtest_data.positions

    def start(self):
        super(MyBkr, self).start()
        self.broker_values.clear()
        self.klines.clear()
        self.positions.clear()

    # 这个next方法会在策略的next方法之后执行
    def next(self):
        super(MyBkr, self).next()

        dt = self.data.datetime.datetime(0).replace(tzinfo=pytz.utc).astimezone().strftime("%Y-%m-%d %H:%M:%S")
        msg = {
            "datetime": dt,
            "value": self.lines.value[0]
        }
        self.broker_values.append(msg)

        self.klines.append({
            "datetime": dt,
            "open": self.data.open[0],
            "high": self.data.high[0],
            "low": self.data.low[0],
            "close": self.data.close[0]
        })

        self.positions.append({
            "datetime": dt,
            "position": self._owner.position.size,
            "price": self._owner.position.price
        })
