import copy
org_list = [['hi','hello'],['byr','bye']]
shallow_c = copy.copy(org_list)
shallow_c[0][0]='nr'
print(shallow_c)
print(org_list)
print(id(org_list[0][0]) == id(shallow_c[0][0]))#innner list are same address
print(id(org_list) == id(shallow_c))#outer listare different