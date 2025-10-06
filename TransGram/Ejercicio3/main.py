#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from analizador import AnalizadorEjercicio3
from pruebas import ejecutar_pruebas

def main():
    """
    Función principal que contiene la lógica de ejecución del analizador.
    """
    print("""
    ╔══════════════════════════════════════════════════╗
    ║           ANALIZADOR EJERCICIO 3                 ║
    ║         (Con carga de gramática desde TXT)       ║
    ╚══════════════════════════════════════════════════╝
    """)
    
    ejecutar_pruebas(AnalizadorEjercicio3)


main()
