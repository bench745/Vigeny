# Vigeny
A python script that implements the vigenere cipher in one line.

Note that the functions will take inputs of any case but will ouput only upper case.
Similarly to the original cipher the code only handles letters, but could be easily expanded (by removing all "- 65"s and replacing "% 26"
with "% 1114112").

```python
import vigeny

message = 'FRIENDSROMANSCOUNTRYMENLENDMEYOUREARS'
key = 'KEYPHRASE'

print('Encrypting ' + message + ' with the key ' + key)
cipherText = vigeny.crypt(message, key, 1)
print(cipherText)

print('Decyrpting ' + cipherText + ' with the key ' + key)
plainText = vigeny.crypt(cipherText, key, -1)
print(plainText)
```

As you can see the only function in vigeny is crypt. The first argument is the message or cipher text, the second argument is the key and then the third argument is shows how to apply the key.

When the third argument is 1 the key is applied once, 2 it is applied twice etc. To decrypt simply set the third argument to the negative counter part of the one used to decrypt.\
For example...\
```vigeny.crypt(message, key, 9)``` can be reversed with ```vigeny.crypt(message, key, -9)``` \
and likewise...\
```vigeny.crypt(message, key, -4)``` can be reversed with ```vigeny.crypt(message, key, 4)```
