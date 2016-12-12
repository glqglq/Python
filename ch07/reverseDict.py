def ReverseDict(d):
    New = {}
    for i in d:
        New.update({d[i],i})
    return New