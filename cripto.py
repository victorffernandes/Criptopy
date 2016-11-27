#!/usr/bin/python
operation = raw_input("Decrypt or Encrypt [D or E]?").upper();
message = raw_input("Put your message here -->  ").upper();
key = int(raw_input("Insert your number key, any number from 0 to 26 -->  "));


def module27(num):
    return num % 27;

alphabet = "ABCDEFGIJKLMNOPQRSTUVWXYZ ";
newalphabet = alphabet[module27(key):26] + alphabet[0:module27(key)];
newmessage = "";
i = 0;


if operation=="E":
    while len(newmessage) != len(message):
        n = alphabet.index(message[i]);
        newmessage += newalphabet[n];
        i+=1;
elif operation=="D":
    while len(newmessage) != len(message):
        n = newalphabet.index(message[i]);
        newmessage += alphabet[n];
        i+=1;
else :
    print("Could not understand the operation...");

print(newmessage);
