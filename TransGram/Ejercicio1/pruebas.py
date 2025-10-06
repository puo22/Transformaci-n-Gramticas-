#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def obtener_pruebas():
    return [
        {
            "nombre": "Prueba 1: dos tres",
            "entrada": ["dos", "tres", "$"]
        },
        {
            "nombre": "Prueba 2: uno dos tres tres",
            "entrada": ["uno", "dos", "tres", "tres", "$"]
        },
        {
            "nombre": "Prueba 3: seis dos tres",
            "entrada": ["seis", "dos", "tres", "$"]
        },
        {
            "nombre": "Prueba 4: tres",
            "entrada": ["tres", "$"]
        },
        {
            "nombre": "Prueba 5: uno tres",
            "entrada": ["uno", "tres", "$"]
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
