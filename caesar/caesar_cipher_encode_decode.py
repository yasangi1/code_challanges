#still modifing for decode

orginal_alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

direction = input("Type encode to 'encrypt', type decode to 'decrypt': \n")  
text = list(input("Type you message:\n").lower())
shift = int(input("Type the shift number:\n"))
#print(text)
index_list = []
shift_list = []
encode_value = ""
decode_value = ""

#This is to create the shifted alphabet. now the alphabet list changes with shifted letters
for i in range(shift):
    alphabet.append(alphabet.pop(0))
#print(alphabet)

def encrypt(text,shift):
#find the indexs of user entered text in the orginal alphabet
    for n in text:
      for m in orginal_alphabet:
        if n == m:
          index_list.append(orginal_alphabet.index(m))

    #pass the index founded from orginal_alphabet to the shifted alphabel to identify the encode letters
    for k in index_list:
      shift_list.append(alphabet[k])  
      encode_value = ''.join(shift_list)
    #print(alphabet)
    print(f"The encoded text is {encode_value}")

def decrypt(text,shift):
    #find the indexs of user entered text from the shifted alphabet
      for n in text:
        for m in alphabet:
          if n == m:
            index_list.append(alphabet.index(m))
      #print(index_list)
  
      #pass the index founded from shifted alphabet to the orginal_alphabel to identify the decode letters
      for k in index_list:
        shift_list.append(orginal_alphabet[k])  
        decode_value = ''.join(shift_list)
      print(f"The decoded text is {decode_value}")

if direction == 'encrypt':
  encrypt(text,shift) 
elif direction == 'decrypt':
  decrypt(text,shift)
else:
  print("Invalid input. Please try again.")
