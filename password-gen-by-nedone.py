import random
import string
import os
import time

print ("dev by nedone")

time.sleep (0.5)

print ("\n")

ponctuation='!"#$%&\'()*+,-./:;<=>?@[]^_`{|}~'

def majuscule(mot):
    
    compteur=0
    for lettre in mot:
        if  lettre in string.ascii_letters and lettre==lettre.upper():
            compteur=compteur+1
    return compteur

def digit(mot):
    
    compteur=0
    for lettre in mot:
        if lettre in string.digits:
            compteur=compteur+1
    return compteur

def ponctuations(mot):
    
    compteur=0
    for lettre in mot :
        if lettre in ponctuation:
            compteur=compteur+1
    return compteur


def generate_password(length):
    
    
    password = ''.join(random.choices(string.ascii_letters + string.digits + ponctuation, k=length))
    
    while majuscule(password)==0 or digit(password)==0 or ponctuations(password)==0:
        password = ''.join(random.choices(string.ascii_letters + string.digits + ponctuation, k=length))
        
    return password

length = int(input ("choisir la longueur du mot de passe qui est sur le point d'être générée : ") )
print ("\n")
password = generate_password(length)


if not os.path.exists('passwords'):
    os.makedirs('passwords')

if not os.path.exists('passwords/save.txt'):
    open('passwords/save.txt', 'w').close()

with open('passwords/save.txt', 'a') as file:
    file.write(password + '\n')


print ("voici le mot de passe qui vient d'être générée avec succès : ")
print ("\n")
print (password)
print ("\n")
print("mot de passe enregistré avec succès dans le fichier save.txt")
time.sleep (1)

print ("\n")