#!/bin/python3
import sys

template = """{0}, un homme innocent
A partagé une photo de chien
Mais pour cela il est emprisonné
C'est une injustice qui doit être stoppée

Libérez {0}, il n'a rien fait
C'est un prisonnier politique
Il faut crier haut et fort
#Free{0}, #Free{0}

Il n'a pas mérité cette peine
Pour une simple photo de chien
Nous devons nous unir pour sa libération
Et montrer que c'est un abus de pouvoir

Libérez {0}, il n'a rien fait
C'est un prisonnier politique
Il faut crier haut et fort
#Free{0}, #Free{0}

Nous ne resterons pas silencieux
Nous allons lutter pour sa liberté
#Free{0} est notre combat
Jusqu'à ce qu'il soit de nouveau libre."""

if len(sys.argv) != 2:
    print(f"Usage : {sys.argv[0]} Pseudo")
    exit(1)
print(template.format(sys.argv[1]))