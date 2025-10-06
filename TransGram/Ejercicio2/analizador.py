#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tokens import Token
from gramatica_parser import GramaticaParser

class AnalizadorEjercicio2:
    
    def __init__(self, entrada, archivo_gramatica='gramatica.txt'):
        self.entrada = entrada
        self.posicion = 0
        self.token_actual = entrada[0] if entrada else Token.FIN_ARCHIVO
        self.nivel = 0
        
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
        
        if self.token_actual == Token.DOS:
            self.log("S → dos C")
            self.emparejar(Token.DOS)
            self.C()
        elif self.token_actual in [Token.CUATRO, Token.CINCO, Token.UNO, Token.TRES]:
            self.log("S → B uno")
            self.B()
            self.emparejar(Token.UNO)
        elif self.token_actual in [Token.FIN_ARCHIVO, Token.TRES]:
            self.log("S → ε")
        else:
            raise SyntaxError(f"Error en S: '{self.token_actual}'")
        
        self.nivel -= 1
        self.log("← Saliendo de S")
    
    def A(self):
        self.log(f"→ A con token: '{self.token_actual}'")
        self.nivel += 1
        
        if self.token_actual == Token.CUATRO:
            self.log("A → cuatro")
            self.emparejar(Token.CUATRO)
        elif self.token_actual in [Token.CINCO, Token.UNO, Token.DOS]:
            self.log("A → S tres B C")
            self.S()
            self.emparejar(Token.TRES)
            self.B()
            self.C()
        elif self.token_actual in [Token.TRES, Token.CINCO, Token.FIN_ARCHIVO]:
            self.log("A → ε")
        else:
            raise SyntaxError(f"Error en A: '{self.token_actual}'")
        
        self.nivel -= 1
        self.log("← Saliendo de A")
    
    def B(self):
        self.log(f"→ B con token: '{self.token_actual}'")
        self.nivel += 1
        
        if self.token_actual in [Token.CUATRO, Token.DOS]:
            self.log("B → A cinco C seis")
            self.A()
            self.emparejar(Token.CINCO)
            self.C()
            self.emparejar(Token.SEIS)
        elif self.token_actual in [Token.UNO, Token.SIETE, Token.CINCO, Token.FIN_ARCHIVO, Token.TRES, Token.SEIS]:
            self.log("B → ε")
        else:
            raise SyntaxError(f"Error en B: '{self.token_actual}'")
        
        self.nivel -= 1
        self.log("← Saliendo de B")
    
    def C(self):
        self.log(f"→ C con token: '{self.token_actual}'")
        self.nivel += 1
        
        if self.token_actual == Token.SIETE:
            self.log("C → siete B")
            self.emparejar(Token.SIETE)
            self.B()
        elif self.token_actual in [Token.FIN_ARCHIVO, Token.TRES, Token.SEIS, Token.CINCO]:
            self.log("C → ε")
        else:
            raise SyntaxError(f"Error en C: '{self.token_actual}'")
        
        self.nivel -= 1
        self.log("← Saliendo de C")
    
    def mostrar_gramatica(self):
        self.gramatica.mostrar()
    
    def analizar(self):
        print("=" * 60)
        print("    ANALIZADOR EJERCICIO 2")
        print("=" * 60)
        print(f"Entrada: {' '.join(self.entrada)}")
        print("NOTA: Gramática NO LL(1)\n")
        
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
