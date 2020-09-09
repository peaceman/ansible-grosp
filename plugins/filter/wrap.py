def wrap(list, **kwargs):
    symbol = kwargs.get('symbol', '"')
    return [ symbol + x + symbol for x in list]

class FilterModule(object):
    def filters(self):
        return {
            'wrap': wrap
        }
