def harmonic_mean_1(data):
    n = len(data)
    if n == 0:
        #return None
        return 0.0
    else:
        return n / sum(1/x for x in data if x > 0)

def harmonic_mean_2(data):
    from scipy.stats import hmean
    return hmean(data)
