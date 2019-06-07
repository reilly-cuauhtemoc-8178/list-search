tdict = {'vlad':{'name':'vladimir','a':1,'b':2,'c':3}, 'veig':{'name':'veigar','d':4,'e':5,'f':6}, 'ahri':{'name':'ahri','g':7,'h':8,'i':9}}

def peepum(entry):
    """Return a 2D array"""
    keys1 = list(entry.keys())
    c_data = [list(entry[i].values()) for i in keys1]
    return c_data

print(peepum(tdict))

test_array = [['e',5],
              ['b',2],
              ['c',3],
              ['d',4],
              ['a',1]]
def sort_array(entry, key):
    return sorted(entry, key=lambda x: x[key])
print(sort_array(test_array, 1))
