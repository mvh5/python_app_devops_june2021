#!/bin/bash

echo "Mostrando GET root"
curl http://192.168.1.72:3000/

printf "\n\n"
echo "Mostrando GET /saludo/<nombre>"
curl http://192.168.1.72:3000/saludo/Mauricio

printf "\n\n"
echo "fin de pruebas..."
