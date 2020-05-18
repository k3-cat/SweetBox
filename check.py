from sweet_box.mgr import ModelMgr
from sweet_box.utils import safe_input

mgr = ModelMgr()


def main():
    while True:
        print('--------------------------------')
        name = safe_input('input the sweet you would like to check', 'str')
        num = safe_input('input the amount remained', 'float')
        try:
            print(mgr[name.upper()].check(num))
        except KeyError:
            print('the model does not exist')


if __name__ == '__main__':
    main()
