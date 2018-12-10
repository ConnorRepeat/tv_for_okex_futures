import datetime
import time

resolution_dict = {
    '1': 60,
    '5': 5 * 60,
    '15': 15 * 60,
    '30': 30 * 60,
    '60': 60 * 60,
    '240': 240 * 60,
    '1D': 3600 * 60
}


def convert_tv2ok_resolution(resolution):
    return resolution_dict[resolution]


def convert_timestamp2ok(timestamp):
    return datetime.datetime.utcfromtimestamp(timestamp).isoformat() + 'Z'


if __name__ == "__main__":
    print(convert_timestamp2ok(int(time.time())))
