#!/usr/bin/env python3
"""Hello World multi languages.
Depending on the language configured in the environment, the program displays the message
corresponding.

Usage:

Have the LANG variable properly configured in the environment, e.g.:
    export LANG=pt_BR.UTF-8
    ou export LANG=us_EN.UTF-8
    
Run the program:
     python3 variables.py
"""

__version__ = '0.0.1'
__author__ = 'Natália Granato'
__license__ = 'unlicense'

import os  # import the os module

# get the LANG variable from the environment
current_language = os.getenv("LANG", "pt_BR.UTF-8")[:5]

MSG = "Olá, Mundo!"

if current_language == "us_EN.UTF-8":
    MSG = "Hello, World!"

elif current_language == "es_ES.UTF-8":
    MSG = "¡Hola Mundo!"

elif current_language == "fr_FR.UTF-8":
    MSG = "Bonjour le monde!"

print(MSG)
