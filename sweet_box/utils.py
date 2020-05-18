def safe_input(prop, input_type):
    while True:
        inp = input(f'{prop}: ')
        try:
            if input_type == 'str':
                return str(inp)
            if input_type == 'int':
                return int(inp)
            if input_type == 'float':
                return float(inp)
            raise Exception()
        except (TypeError, ValueError):
            print(f'this is not a valid {input_type}')
