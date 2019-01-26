# Vigeny
A python script that implements the vigenere cipher in two lines, encrypt and decrypt.

Note that the functions will take inputs of any case but will ouput only upper case.
Similarly to the original cipher the code only handles letters, but could be easily expanded (by removing all "- 65"s and replacing "% 26"
with "% 1114112").

```python
import vigeny

message = 'FRIENDSROMANSCOUNTRYMENLENDMEYOUREARS'
key = 'KEYPHRASE'

print('Encrypting ' + message + ' with the key ' + key)
cipherText = encrypt(message, key)
print(cipherText)

print('Decyrpting ' + cipherText + ' with the key ' + key)
plainText = decrypt(cipherText, key)
print(plainText)
```
