def fix_it(data:list):
        new_d  , i = {} , 1
        for key in data:
            new_d[str(i)]=data[key]
            i+=1
        data = new_d
        return data
