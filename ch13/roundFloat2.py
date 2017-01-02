class RoundFloatManual(object):
    def __init__(self,val):
        assert isinstance(val,float)
        self.value = round(val,2)

    def __str__(self):
        return '%.2f'%self.value

    __repr  =  __str__
