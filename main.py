password=input("Enter the Password You want to ENCRYPT: ")
key=int(input("Enter a Unique no. to encrypt(Please remember this):"))
def encrypt(text, shift):
    text = text.lower()
    encrypted_text = " "
    for char in text:
        if char.islower():
            encrypted_text += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            encrypted_text += char
    return encrypted_text
print( "Your encrypted password is")
print(encrypt(password,key))
exit = input(" ")
