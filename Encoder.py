def convert(mix_list):
  full_str = ''.join([str(elem) for elem in mix_list])
  return full_str


def decode(string, key):
    
  string = list(string)
  key = list(key)
  alphabet = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
  "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", " ")
    

  numberlist_string = [] 
  numberlist_key = []
  list_final = []

  for char in string:
    i = 0
    while i < len(alphabet):
      if char == alphabet[i]:
        numberlist_string.append(i)
        break
      i+=1


  for char in key:
    j = 0
    while char != alphabet[j]:
      j+=1

    numberlist_key.append(j)
  
  k = 0
  while k < len(string):
    y = k%len(key)
    tempstr = numberlist_string[k] + len(alphabet)
    val = tempstr - numberlist_key[y]
    val = val%len(alphabet)
    list_final.append(alphabet[val])
    k+=1

  
  list_final = convert(list_final)
  return list_final



def encode(string, key):
      
  alphabet = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
  "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", " ")
    
    
  string = list(string)
  key = list(key)
  alphabet = list(alphabet)

  numberlist_string = []
  numberlist_key = []
  list_final = []

  for char in string:
    i = 0
    while i < len(alphabet):
      if char == alphabet[i]:
        numberlist_string.append(i)
        break
      i+=1

    
  for char in key:
    j = 0
    while char != alphabet[j]:
      j+=1

    numberlist_key.append(j)


  k = 0
  while k < len(numberlist_string):

    tempstr = numberlist_string[k]
    tempkey = numberlist_key[k%len(key)]
    ind = (tempkey + tempstr)%len(alphabet)

    list_final.append(alphabet[ind])
    k+=1
    

  list_final = convert(list_final)
  return list_final




