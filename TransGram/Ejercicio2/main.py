#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from analizador import AnalizadorEjercicio2
from pruebas import ejecutar_pruebas

def main():
    """
    Función principal que contiene la lógica de ejecución del analizador.
    """
    print("""
    ╔══════════════════════════════════════════════════╗
    ║           ANALIZADOR EJERCICIO 2                 ║
    ║         (Con carga de gramática desde TXT)       ║
    ╚══════════════════════════════════════════════════╝
    """)
    
    ejecutar_pruebas(AnalizadorEjercicio2)


main()
