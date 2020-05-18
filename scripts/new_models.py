import sys
from pathlib import Path


def new(mgr):
    while True:
        print('--------------------------------')
        parm = dict()
        name = safe_input('name', 'str')
        if not name:
            break
        parm['name'] = name
        parm['start'] = safe_input('start', 'str')
        parm['from_last'] = safe_input('from_last', 'float')
        parm['total'] = safe_input('total', 'int')
        dosages = dict()
        while True:
            print('---- dosage ----')
            time = safe_input('time', 'str')
            if not time:
                break
            dosages[time] = safe_input('amount', 'float')
        parm['dosages'] = {key: dosages[key] for key in sorted(dosages.keys())}
        mgr.new_model(**parm)


if __name__ == "__main__":
    sys.path.append(str(Path(__file__).parents[1]))
    from sweet_box.utils import safe_input
    from sweet_box.mgr import ModelMgr

    mgr = ModelMgr()
    new(mgr)
