#!/usr/bin/env bash

# Script para conseguir las primeras n palabras en un texto por frecuencia desde un archivo de texto, las regresa en minusculas
# ARGS: NUM_WORDS: int default 10
# OUTPUT: N palabras y sus frecuencias ordenadas al reverso

NUM_WORDS="${1:-10}"
tr '[:upper:]' '[:lower:]'|
grep -oE "[a-z\']{2,}"| 
sort| 
grep -Fvwf stopwords| 
uniq -c | 
sort -nr| 
head -n"${NUM_WORDS}"
