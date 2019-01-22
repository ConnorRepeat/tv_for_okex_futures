import json
import time

import okex.futures_api as future
from common_helper import convert_tv2ok_resolution, convert_timestamp2ok
from config_helper import diamond

okex_cfg = diamond.get_exchange_auth('okex')
api_key = okex_cfg.get('api_key')
secret = okex_cfg.get('secret')
passphrase = okex_cfg.get('passphrase')

okex = future.FutureAPI(api_key, secret, passphrase, True)


def get_history_kline(symbol, time_from, time_to, resolution):
    resolution = convert_tv2ok_resolution(resolution)

    comlete_kline = []
    start_time = time_from
    end_time = time_to
    limit_num = 200
    retry_cnt = 0

    while True:

        if end_time > time_to:
            end_time = time_to

        if end_time - start_time > resolution * limit_num:
            # 超过限制
            end_time = start_time + resolution * limit_num

        try:
            resp = okex.get_kline(instrument_id=symbol,
                                  start=convert_timestamp2ok(start_time),
                                  end=convert_timestamp2ok(end_time),
                                  granularity=resolution)
            comlete_kline.extend(resp[::-1])
        except Exception:
            print('get kline error.')
            if retry_cnt > 10:
                return None
            time.sleep(5)

        if end_time >= time_to:
            break
        else:
            start_time += resolution * limit_num
            end_time = start_time + resolution * limit_num

    print(len(comlete_kline))
    # print(comlete_kline)

    t = []
    o = []
    h = []
    l = []
    c = []
    v = []
    for elem in comlete_kline:
        t.append(int(elem[0] / 1000))
        o.append(float(elem[1]))
        h.append(float(elem[2]))
        l.append(float(elem[3]))
        c.append(float(elem[4]))
        v.append(float(elem[5]))

    result = {
        "s": "ok",
        "t": t,
        "o": o,
        "h": h,
        "l": l,
        "c": c,
        "v": v
    }
    return json.dumps(result)


if __name__ == '__main__':
    test = get_history_kline('EOS-USD-181228', 1544371200, 1544457600, '5')
    print(test)
