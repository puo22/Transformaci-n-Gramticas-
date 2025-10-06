# (Mismo código que Ejercicio 1)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class GramaticaParser:
    
    def __init__(self, archivo):
        self.archivo = archivo
        self.producciones = {}
        self.simbolo_inicial = None
    
    def cargar(self):
        try:
            with open(self.archivo, 'r', encoding='utf-8') as f:
                lineas = f.readlines()
            
            for linea in lineas:
                linea = linea.strip()
                
                if not linea or linea.startswith('#'):
                    continue
                
                if '->' in linea:
                    partes = linea.split('->')
                    no_terminal = partes[0].strip()
                    produccion = partes[1].strip()
                    
                    if self.simbolo_inicial is None:
                        self.simbolo_inicial = no_terminal
                    
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
        print("\n" + "=" * 60)
        print("GRAMÁTICA CARGADA")
        print("=" * 60)
        print(f"Símbolo inicial: {self.simbolo_inicial}\n")
        
        for no_terminal, prods in self.producciones.items():
            for prod in prods:
                print(f"{no_terminal} → {prod}")
        
        print("=" * 60 + "\n")
