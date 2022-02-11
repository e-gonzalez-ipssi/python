def canons_ready(dict):
    return "Halt" if "nay" in dict.values() else "Feu" 


print(canons_ready({'Mike':'aye','Joe':'aye','Johnson':'aye','Peter':'aye'}))
print(canons_ready({'Mike':'aye','Joe':'nay','Johnson':'aye','Peter':'aye'}))