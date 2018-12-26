import sys


def minute():
    minute = 0
    try:
        if len(sys.argv) > 2:
            raise Exception
        elif not sys.argv[1].isdigit:
            raise Exception 
        else:
            minute = int(sys.argv[1])
    except:
        print('Parameter Error')
    return minute


def hour(minute):
    hour = int(minute / 60)
    minute_1 = minute % 60
    print('{}H,{}M'.format(hour, minute_1))


if __name__ == '__main__':
    minute = minute()
    hour(minute)
