#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def obtener_pruebas():
    return [
        {
            "nombre": "Prueba 1: uno",
            "entrada": ["uno", "$"]
        },
        {
            "nombre": "Prueba 2: dos",
            "entrada": ["dos", "$"]
        },
        {
            "nombre": "Prueba 3: dos siete",
            "entrada": ["dos", "siete", "$"]
        },
        {
            "nombre": "Prueba 4: cuatro",
            "entrada": ["cuatro", "$"]
        },
        {
            "nombre": "Prueba 5: cadena vacía",
            "entrada": ["$"]
        }
    ]

def ejecutar_pruebas(AnalizadorClass):
    pruebas = obtener_pruebas()
    
    for i, prueba in enumerate(pruebas, 1):
        print(f"\n{'#' * 70}")
        print(f"  {prueba['nombre']}")
        print(f"{'#' * 70}\n")
        
        analizador = AnalizadorClass(prueba["entrada"])
        analizador.analizar()
        
        if i < len(pruebas):
            input("\nPresiona Enter para continuar...")
