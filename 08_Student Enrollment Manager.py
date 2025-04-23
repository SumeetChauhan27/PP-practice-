# Create a set of students appearing for CET
set_cet = {'Amey', 'Akash', 'ved', 'Nandu', 'Adu'}
print('Students appearing for CET:', set_cet)

# Create a set of students appearing for NEET
set_neet = {'Amey', 'Nikhil', 'Prasad', 'Amar', 'Lata', 'Mnu', 'Ved'}
print('Students appearing for NEET:', set_neet)

# Create a set of students appearing for JEE
set_jee = {'Amey', 'Akash', 'Adu', 'Amar', 'Lata'}
print('Students appearing for JEE:', set_jee)
print('----------------------------------------------------------------')

# Perform union operation using |
print('Union of sets:', set_cet | set_neet | set_jee)

# Perform union operation using union()
print('Set of students appearing for JEE or NEET:', set_jee.union(set_neet))
print('----------------------------------------------------------------')

# Perform intersection operation using &
print('Intersection of sets:', set_cet & set_neet & set_jee)

# Perform intersection operation using intersection()
print('Set of students appearing for JEE AND NEET:', set_jee.intersection(set_neet))
print('----------------------------------------------------------------')

# Perform difference operation using -
print('Difference of CET & NEET:', set_cet - set_neet)

# Perform difference operation using difference()
print('Difference of JEE & NEET:', set_jee.difference(set_neet))
