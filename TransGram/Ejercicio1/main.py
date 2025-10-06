#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from analizador import AnalizadorEjercicio1
from pruebas import ejecutar_pruebas

def main():
    """
    Función principal que contiene la lógica de ejecución del analizador.
    """
    print("""
    ╔══════════════════════════════════════════════════╗
    ║           ANALIZADOR EJERCICIO 1                 ║
    ║         (Con carga de gramática desde TXT)       ║
    ╚══════════════════════════════════════════════════╝
    """)
    
    ejecutar_pruebas(AnalizadorEjercicio1)


main()
