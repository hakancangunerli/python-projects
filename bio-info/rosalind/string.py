dna_string = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC' 
print('given string: ' + dna_string)

print("number of adenine:") # it calculer l'amount of Ts in l'string. 
print(dna_string.rfind("A"))

print("number of thymine:") 
print(dna_string.rfind("T"))

print("number of guanine:")
print(dna_string.rfind("G"))

print("number of cytosine:")
print(dna_string.rfind("C"))


