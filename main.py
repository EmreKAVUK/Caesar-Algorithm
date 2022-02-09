k = 4
message = input("Please Enter your Message...")
alphabet = "abcdefghijklmnopqrstuvwxyz"
mod = len(alphabet)
encrypt_message = ''
for x in message:
    for y in alphabet:
        if(y==x):
            location = alphabet.index(y)
            location += k
            encrypt_message += alphabet[location % mod]
print("Message : " + message + "\n")
print("Encrypted Message: " + encrypt_message)


