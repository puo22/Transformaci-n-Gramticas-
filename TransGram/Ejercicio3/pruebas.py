#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def obtener_pruebas():
    """Retorna las pruebas para el Ejercicio 3"""
    return [
        {
            "nombre": "Prueba 1: dos tres",
            "entrada": ["dos", "tres", "$"],
            "descripcion": "A → dos B C, B → ε, C → ε"
        },
        {
            "nombre": "Prueba 2: dos cuatro tres",
            "entrada": ["dos", "cuatro", "tres", "$"],
            "descripcion": "A → dos B C, B → C tres, C → cuatro B"
        },
        {
            "nombre": "Prueba 3: uno",
            "entrada": ["uno", "$"],
            "descripcion": "A → ε, B → ε, C → ε, S' → uno S'"
        },
        {
            "nombre": "Prueba 4: dos tres uno",
            "entrada": ["dos", "tres", "uno", "$"],
            "descripcion": "Cadena con S' → uno S'"
        },
        {
            "nombre": "Prueba 5: dos tres uno uno",
            "entrada": ["dos", "tres", "uno", "uno", "$"],
            "descripcion": "Múltiples 'uno' al final (S' recursivo)"
        },
        {
            "nombre": "Prueba 6: cuatro tres",
            "entrada": ["cuatro", "tres", "$"],
            "descripcion": "A → ε, B → C tres, C → cuatro B"
        },
        {
            "nombre": "Prueba 7: cadena vacía seguida de unos",
            "entrada": ["uno", "uno", "uno", "$"],
            "descripcion": "Todo epsilon seguido de S' recursivo"
        }
    ]

def ejecutar_pruebas(AnalizadorClass):
    """Ejecuta todas las pruebas"""
    pruebas = obtener_pruebas()
    
    for i, prueba in enumerate(pruebas, 1):
        print(f"\n{'#' * 70}")
        print(f"  {prueba['nombre']}")
        print(f"  {prueba['descripcion']}")
        print(f"{'#' * 70}\n")
        
        analizador = AnalizadorClass(prueba["entrada"])
        analizador.analizar()
        
        if i < len(pruebas):
            input("\nPresiona Enter para continuar...")
