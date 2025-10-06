#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tokens import Token
from gramatica_parser import GramaticaParser

class AnalizadorEjercicio1:
    
    def __init__(self, entrada, archivo_gramatica='gramatica.txt'):
        self.entrada = entrada
        self.posicion = 0
        self.token_actual = entrada[0] if entrada else Token.FIN_ARCHIVO
        self.nivel = 0
        
        # Cargar gramática desde archivo
        self.gramatica = GramaticaParser(archivo_gramatica)
        if not self.gramatica.cargar():
            raise Exception("No se pudo cargar la gramática")
    
    def avanzar(self):
        self.posicion += 1
        if self.posicion < len(self.entrada):
            self.token_actual = self.entrada[self.posicion]
        else:
            self.token_actual = Token.FIN_ARCHIVO
    
    def emparejar(self, esperado):
        if self.token_actual == esperado:
            print(f"{'  ' * self.nivel}✓ Emparejado: {esperado}")
            self.avanzar()
        else:
            raise SyntaxError(f"Error: se esperaba '{esperado}' pero se encontró '{self.token_actual}'")
    
    def log(self, mensaje):
        print(f"{'  ' * self.nivel}{mensaje}")
    
    def S(self):
        self.log(f"→ S con token: '{self.token_actual}'")
        self.nivel += 1
        
        if self.token_actual in [Token.DOS, Token.SEIS, Token.FIN_ARCHIVO]:
            self.log("S → A B C")
            self.A()
            self.B()
            self.C()
        elif self.token_actual in [Token.UNO, Token.TRES]:
            self.log("S → D E")
            self.D()
            self.E()
        else:
            raise SyntaxError(f"Error en S: '{self.token_actual}'")
        
        self.nivel -= 1
        self.log("← Saliendo de S")
    
    def A(self):
        self.log(f"→ A con token: '{self.token_actual}'")
        self.nivel += 1
        
        if self.token_actual == Token.DOS:
            self.log("A → dos B tres")
            self.emparejar(Token.DOS)
            self.B()
            self.emparejar(Token.TRES)
        elif self.token_actual in [Token.SEIS, Token.FIN_ARCHIVO, Token.CINCO, Token.TRES]:
            self.log("A → ε")
        else:
            raise SyntaxError(f"Error en A: '{self.token_actual}'")
        
        self.nivel -= 1
        self.log("← Saliendo de A")
    
    def B(self):
        self.log(f"→ B con token: '{self.token_actual}'")
        self.nivel += 1
        self.log("B → ε B'")
        self.B_prima()
        self.nivel -= 1
        self.log("← Saliendo de B")
    
    def B_prima(self):
        self.log(f"→ B' con token: '{self.token_actual}'")
        self.nivel += 1
        
        if self.token_actual == Token.CUATRO:
            self.log("B' → cuatro C cinco B'")
            self.emparejar(Token.CUATRO)
            self.C()
            self.emparejar(Token.CINCO)
            self.B_prima()
        elif self.token_actual in [Token.SEIS, Token.FIN_ARCHIVO, Token.TRES, Token.CINCO]:
            self.log("B' → ε")
        else:
            raise SyntaxError(f"Error en B': '{self.token_actual}'")
        
        self.nivel -= 1
        self.log("← Saliendo de B'")
    
    def C(self):
        self.log(f"→ C con token: '{self.token_actual}'")
        self.nivel += 1
        
        if self.token_actual == Token.SEIS:
            self.log("C → seis A B")
            self.emparejar(Token.SEIS)
            self.A()
            self.B()
        elif self.token_actual in [Token.FIN_ARCHIVO, Token.CINCO]:
            self.log("C → ε")
        else:
            raise SyntaxError(f"Error en C: '{self.token_actual}'")
        
        self.nivel -= 1
        self.log("← Saliendo de C")
    
    def D(self):
        self.log(f"→ D con token: '{self.token_actual}'")
        self.nivel += 1
        
        if self.token_actual == Token.UNO:
            self.log("D → uno A E")
            self.emparejar(Token.UNO)
            self.A()
            self.E()
        elif self.token_actual == Token.TRES:
            self.log("D → B")
            self.B()
        else:
            raise SyntaxError(f"Error en D: '{self.token_actual}'")
        
        self.nivel -= 1
        self.log("← Saliendo de D")
    
    def E(self):
        self.log(f"→ E con token: '{self.token_actual}'")
        self.nivel += 1
        self.log("E → tres")
        self.emparejar(Token.TRES)
        self.nivel -= 1
        self.log("← Saliendo de E")
    
    def mostrar_gramatica(self):
        """Muestra la gramática cargada"""
        self.gramatica.mostrar()
    
    def analizar(self):
        print("=" * 60)
        print("    ANALIZADOR EJERCICIO 1")
        print("=" * 60)
        print(f"Entrada: {' '.join(self.entrada)}\n")
        
        # Mostrar gramática cargada
        self.mostrar_gramatica()
        
        try:
            self.S()
            if self.token_actual == Token.FIN_ARCHIVO:
                print("\n" + "=" * 60)
                print("✓ ANÁLISIS EXITOSO")
                print("=" * 60)
                return True
            else:
                print("\n✗ ERROR: Tokens adicionales")
                return False
        except SyntaxError as e:
            print(f"\n✗ {str(e)}")
            return False
