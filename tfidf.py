def words(c):
    ws = []
    
    for s in c:
        ss = s.split()
        
        for w in ss:
            if w not in ws:
                ws.append(w)
    
    return ws


def tf(c, ws):
    ec = []
    
    for s in c:
        ss = s.split()
        
        es = []
        
        for w in ws:
            es.append(ss.count(w) / len(ss))
        
        ec.append(es)
    
    return ec
    
    
def gdc(c, w):
    v = 0
    
    for s in c:
        ss = s.split()
        
        if w in ss:
            v += 1
    
    return v
    
    
def idf(c, ws):
    nws = []
    
    for w in ws:
        nws.append(math.log2(len(c) / gdc(c, w)))
    
    return nws
    

def tfidf(tf, idf):
    a = []
    
    for es in tf:
        s = []
        
        for i in range(len(es)):
            s.append(es[i] * idf[i])
        
        a.append(s)
    
    return a
