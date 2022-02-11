def remove(string):
    return string if not string[len(string)-1] == "!" else string[:-1]
    
print(remove("Hi!"))
print(remove("Hi!!!"))
print(remove("VggqSR EQVK !!iKzYMUn!!! phKIcKr !!!!d!!!!!!!!"))
print(remove("DfO !!!oXAKeMcaKHaoJqL! KtJmOEwe chkgZnJsqGYhV!! btsEkvcR iwHZxn sCXNOMwb FERHCsm !joSuA!!!! nPQC TMFJKk !!!OGBHwLbRY!!!!! sLlWuYk eCrzJR!!"))
