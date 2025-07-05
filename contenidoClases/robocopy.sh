#!/usr/bin/env bash
# Copia de un archivo a un destino
cp $1 $2
echo '$0: ' $0
echo '$#: ' $#
echo '$@: ' $@
echo '$?: ' $?
echo '$$: ' $$
echo '$USER ' $USER
echo '$HOSTNAME ' $HOSTNAME
echo '$SECONDS ' $SECONDS
echo '$RANDOM ' $RANDOM
echo '$LINENO ' $LINENO

echo "El archivo $2 miente"
ls -lh $2
