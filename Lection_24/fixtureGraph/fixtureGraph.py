def fixtureCountCompQty4Vertex():
    graph4V = {'a': set('b'), 
         'b': set('acd'), 
         'c': set('bd'), 
         'd': set('bc')}
    qty = 1
    return graph4V, qty

    
def fixtureCountCompQty15Vertex():
    graph4V = {'a': set('bpd'), 
               'b': set('apc'), 
               'c': set('bpd'), 
               'd': set('apc'),
               'p': set('abcd'),
               'e': set('fh'), 
               'f': set('eg'), 
               'g': set('fh'),
               'h': set('eg'), 
               'j': set('k'), 
               'k': set('j'),
               'l': set(''), 
               'm': set('no'), 
               'n': set('mo'),
               'o': set('mn')}
    qty = 5
    return graph4V, qty