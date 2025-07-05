#!/bin/bash
# Reporte de ventas

echo "Resumen de ventas"
cat /dev/stdin | cut -d' ' -f3 | sort -n -r
