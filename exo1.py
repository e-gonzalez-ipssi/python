def remove(string):
    if string[len(string)-1] == "!":
        return string[:-1]
    else:
        return string
    
print(remove("Hi!"))
print(remove("Hi!!!"))
print(remove("VggqSR EQVK !!iKzYMUn!!! phKIcKr !!!!d!!!!!!!!"))
print(remove("DfO !!!oXAKeMcaKHaoJqL! KtJmOEwe chkgZnJsqGYhV!! btsEkvcR iwHZxn sCXNOMwb FERHCsm !joSuA!!!! nPQC TMFJKk !!!OGBHwLbRY!!!!! sLlWuYk eCrzJR!!"))
