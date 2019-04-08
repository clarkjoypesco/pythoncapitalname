# Write Python code that prints out Clark Joy (with a capital C and J), 
# given the definition of z below.

z = 'xclarkjoy'

name1 = z[1:6]
name1 = name1.upper()
name1 = name1.title()
name2 = z[-3:]
name2 = name2.upper()
name2 = name2.title()


print  name1 + ' ' + name2


s = "any string"

print s[:3] + s[3:]
print s[0:]
print s[:]