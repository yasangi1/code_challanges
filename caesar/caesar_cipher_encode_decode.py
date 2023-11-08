#still modifing for decode

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

direction = input("Type encode to 'encrypt', type decode to 'decrypt': \n")
text = list(input("Type you message:\n").lower())
shift = int(input("Type the shift number:\n"))
#print(text)
index_list = []
shift_list = []
encode_value = ""

def encrypt(text,shift):
  #find the indexs of user entered text in the orginal alphabet
  if direction == "e":
    for n in text:
      for m in alphabet:
        if n == m:
          index_list.append(alphabet.index(m))
    #print(index_list)

    #created the shifted alphabet
    for i in range(shift):
      alphabet.append(alphabet.pop(0))

    #find the encode letters for the founded indexes in the shifted alphabet.
    for k in index_list:
      shift_list.append(alphabet[k])  
      encode_value = ''.join(shift_list)
    #print(alphabet)
    print(f"The encoded text is {encode_value}")
    
  else:
    print("still defining the decode")
encrypt(text,shift)
