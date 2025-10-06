#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class GramaticaParser:
    """Lee y parsea un archivo de gramática"""
    
    def __init__(self, archivo):
        self.archivo = archivo
        self.producciones = {}
        self.simbolo_inicial = None
    
    def cargar(self):
        """Carga la gramática desde el archivo"""
        try:
            with open(self.archivo, 'r', encoding='utf-8') as f:
                lineas = f.readlines()
            
            for linea in lineas:
                linea = linea.strip()
                
                # Ignorar líneas vacías y comentarios
                if not linea or linea.startswith('#'):
                    continue
                
                # Parsear producción: A -> alpha
                if '->' in linea:
                    partes = linea.split('->')
                    no_terminal = partes[0].strip()
                    produccion = partes[1].strip()
                    
                    # Guardar símbolo inicial (primera producción)
                    if self.simbolo_inicial is None:
                        self.simbolo_inicial = no_terminal
                    
                    # Guardar producción
                    if no_terminal not in self.producciones:
                        self.producciones[no_terminal] = []
                    
                    self.producciones[no_terminal].append(produccion)
            
            return True
        
        except FileNotFoundError:
            print(f"✗ ERROR: No se encontró el archivo '{self.archivo}'")
            return False
        except Exception as e:
            print(f"✗ ERROR al cargar gramática: {str(e)}")
            return False
    
    def mostrar(self):
        """Muestra la gramática cargada"""
        print("\n" + "=" * 60)
        print("GRAMÁTICA CARGADA DESDE ARCHIVO")
        print("=" * 60)
        print(f"Símbolo inicial: {self.simbolo_inicial}\n")
        
        for no_terminal, prods in self.producciones.items():
            for prod in prods:
                simbolo = "ε" if prod.lower() in ['epsilon', 'ε', 'e'] else prod
                print(f"{no_terminal} → {simbolo}")
        
        print("=" * 60 + "\n")
    
    def obtener_producciones(self, no_terminal):
        """Retorna las producciones de un no terminal"""
        return self.producciones.get(no_terminal, [])
    
    def es_epsilon(self, simbolo):
        """Verifica si es producción epsilon"""
        return simbolo.lower() in ['epsilon', 'ε', 'e', '']
