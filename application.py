import json

from flask import Flask, render_template, request
import time

from config_helper import diamond
from history_helper import get_history_kline

app = Flask(__name__)


@app.route('/config')
def get_config():
    config = {
        "supports_search": True,
        "supports_group_request": False,
        "supported_resolutions": ["1", "5", "15", "30", "60", "240"],
        "supports_marks": False,
        "supports_time": True
    }

    return json.dumps(config)


@app.route('/time')
def get_time():
    return '%d' % int(time.time())


@app.route('/search')
def search():
    symbols = [
        {
            "symbol": "EOSUSD3M",
            "full_name": "OKEx:EOSUSD3M",
            "description": "EOSUSD 季度合约",
            "exchange": "OKEx",
            "ticker": "EOS-USD-190329",
            "type": "futures"
        },
        {
            "symbol": "XRPUSD3M",
            "full_name": "OKEx:XRPUSD3M",
            "description": "XRPUSD 季度合约",
            "exchange": "OKEx",
            "ticker": "XRP-USD-190329",
            "type": "futures"
        }
    ]
    return json.dumps(symbols)


@app.route('/symbols')
def get_symbols():
    symbol = request.args.get('symbol')
    symbol_cfg = {
        "type": "futures",
        "session": "24x7",
        "exchange": "OKEx",
        "listed_exchange": "OKEx",
        "timezone": "Asia/Shanghai",
        "minmov": 1,
        "pricescale": 1000,
        "minmove2": 0,
        "has_intraday": True,
        "has_daily": True,
        "has_weekly_and_monthly": True,
        "has_empty_bars": True,
        "has_no_volume": False,
        "volume_precision": 0,
        "data_status": "pulsed"
    }

    if symbol == 'EOSUSD3M' or symbol == 'EOS-USD-190329':
        symbol_cfg["name"] = "EOSUSD3M"
        symbol_cfg["ticker"] = "EOS-USD-190329"
        symbol_cfg["description"] = "EOSUSD 季度合约"
        return json.dumps(symbol_cfg)
    elif symbol == 'XRPUSD3M' or symbol == 'XRP-USD-190329':
        symbol_cfg["name"] = "XRPUSD3M"
        symbol_cfg["ticker"] = "XRP-USD-190329"
        symbol_cfg["description"] = "XRPUSD 季度合约"
        return json.dumps(symbol_cfg)
    elif symbol == 'LTCUSD3M' or symbol == 'LTC-USD-190329':
        symbol_cfg["name"] = "LTCUSD3M"
        symbol_cfg["ticker"] = "LTC-USD-190329"
        symbol_cfg["description"] = "LTCUSD 季度合约"
    return ''


@app.route('/history')
def get_history():
    symbol = request.args.get('symbol')
    time_from = int(request.args.get('from'))
    time_to = int(request.args.get('to'))
    resolution = request.args.get('resolution')

    return get_history_kline(symbol, time_from, time_to, resolution)


@app.route('/')
def get_index():
    return render_template('index.html')


if __name__ == '__main__':
    app.debug = diamond.get_app_config().get("debug")
    app.run(host='0.0.0.0', port=diamond.get_app_config().get("port"))