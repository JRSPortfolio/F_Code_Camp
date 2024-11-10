import numpy as np

class ProjDict(dict):
    def __init__(self, mean: list, variance: list, std: list, max_vals: list, min_vals: list, sum_vals: list, *args, **kwargs):
        self['mean'] =  mean
        self['variance'] = variance
        self['standard deviation'] = std
        self['max'] = max_vals
        self['min'] = min_vals
        self['sum'] = sum_vals
        super().__init__(self, *args, **kwargs)
        
def calculate(values: list):
    if len(values) < 9:
        raise ValueError('List must contain nine numbers.')
    
    flat_arr = np.array(values)
    arr = np.array(values).reshape(3, 3)
    
    mean = [np.mean(arr, axis = 0).tolist(), np.mean(arr, axis = 1).tolist(), float(np.mean(flat_arr))]
    variance = [np.var(arr, axis = 0).tolist(), np.var(arr, axis = 1).tolist(), float(np.var(flat_arr))]
    std = [np.std(arr, axis = 0).tolist(), np.std(arr, axis = 1).tolist(), float(np.std(flat_arr))]
    max_vals = [np.max(arr, axis = 0).tolist(), np.max(arr, axis = 1).tolist(), float(np.max(flat_arr))]
    min_vals = [np.min(arr, axis = 0).tolist(), np.min(arr, axis = 1).tolist(), float(np.min(flat_arr))]
    sum_vals = [np.sum(arr, axis = 0).tolist(), np.sum(arr, axis = 1).tolist(), float(np.sum(flat_arr))]
    
    result = ProjDict(mean, variance, std, max_vals, min_vals, sum_vals)
    return result

    
    
    


calculate([0, 1, 2, 3, 4, 5, 6, 7, 8])
    