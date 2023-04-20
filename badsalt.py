## do not use this as a password maker
## very basic pass, very basic salt
## although it MAY work if encrypted tho
import random
chars = "q w e r t y u i o p 1 2 3 4 5 6 7 8 9 0 a s d f g h j k l ñ z x c v b n m"
password = input("Enter a password. Special chars may be used.")
chars.split()
password = password + str(chars[random.randint(1,37)])
print("Salted password is:", password)
