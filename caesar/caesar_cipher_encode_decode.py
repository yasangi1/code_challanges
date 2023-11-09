from art import logo
print(logo)

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

  #restart_result = input("If you want to restart the ciper program? Yes or No \n ").lower()
  #if restart_result == 'no':
    #should_continue = False
    #print("Good Bye!")

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
      # Keep the non character values as user entered and those are not going to encripted. 
      if n.isalpha() == False:
          index_list.append(n)
    #print(type(index_list[0]))
    #print(type(index_list[5]))

    #pass the index founded from orginal_alphabet to the shifted alphabel to identify the encode letters
    for k in index_list:
      # to capture only letters. Here in my index_list only has indexes of shifted alphabet. But if user enter not character values and spaces, it should be as it is.
      if (isinstance(k, int)):
        shift_list.append(alphabet[k])  
        encode_value = ''.join(shift_list)
      else:
        shift_list.append(k)  
        encode_value = ''.join(shift_list)
    print(f"The decoded text is {encode_value}")


def decrypt(text,shift):
    #find the indexs of user entered text from the shifted alphabet
      for n in text:
        for m in alphabet:
          if n == m:
            index_list.append(alphabet.index(m))

        if n.isalpha() == False:
          index_list.append(n)
        #print(index_list)
  
      #pass the index founded from shifted alphabet to the orginal_alphabel to identify the decode letters
      for k in index_list:
        if (isinstance(k, int)):
          shift_list.append(orginal_alphabet[k])  
          decode_value = ''.join(shift_list)
        else:
          shift_list.append(k)  
          decode_value = ''.join(shift_list)   
      print(f"The decoded text is {decode_value}")

if direction == 'encrypt':
  encrypt(text,shift) 
elif direction == 'decrypt':
  decrypt(text,shift)
else:
  print("Invalid input. Please try again.")
