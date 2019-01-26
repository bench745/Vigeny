################################
#THE PARTS OF OUR ONE LN FUNCTS#
################################

# converts m to numbers 0 to 25                           >>  list(map(lambda x: ord(x) - 65, m.upper()))
# converts k to numbers 0 to 25                           >>  list(map(lambda x: ord(x) - 65, k.upper()))
# returns a modified LIST2 the same length as LIST1       >>  [LIST2[i%len(LIST2)] for i in range(len(LIST1))]
# adds the terms of two lists of the same length          >>  list(map(lambda x: x[0] + x[1], list(zip(LIST1,LIST2))))
# converts the numbers back to letters                    >>  list(map(lambda x: chr(x + 65), LIST)
# puts two lists together as a list of tuples             >>  zip(LIST1, LIST2)
# sum the tuples in a list of tuples                      >>  list(map(lambda x: (x[0] + x[1]) % 26, LIST1))
# terns the terms of a list to a string                   >>  ''.join(list())

encrypt = lambda m,k: ''.join(list(map(lambda x: chr(x + 65), list(map(lambda x: (x[0] + x[1]) % 26, list(zip(list(map(lambda x: ord(x) - 65, m.upper())), [list(map(lambda x: ord(x) - 65, k.upper()))[i % len(list(map(lambda x: ord(x) - 65, k.upper()))) ] for i in range(len(list(map(lambda x: ord(x) - 65, m.upper()))))])))))))
decrypt = lambda m,k: ''.join(list(map(lambda x: chr(x + 65), list(map(lambda x: (x[0] - x[1]) % 26, list(zip(list(map(lambda x: ord(x) - 65, m.upper())), [list(map(lambda x: ord(x) - 65, k.upper()))[i % len(list(map(lambda x: ord(x) - 65, k.upper()))) ] for i in range(len(list(map(lambda x: ord(x) - 65, m.upper()))))])))))))
