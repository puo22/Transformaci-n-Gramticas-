#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tokens import Token
from gramatica_parser import GramaticaParser

class AnalizadorEjercicio3:
    """Analizador Sintáctico Descendente Recursivo para Ejercicio 3"""
    
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
        """Avanza al siguiente token"""
        self.posicion += 1
        if self.posicion < len(self.entrada):
            self.token_actual = self.entrada[self.posicion]
        else:
            self.token_actual = Token.FIN_ARCHIVO
    
    def emparejar(self, esperado):
        """Verifica si el token actual coincide con el esperado"""
        if self.token_actual == esperado:
            print(f"{'  ' * self.nivel}✓ Emparejado: {esperado}")
            self.avanzar()
        else:
            raise SyntaxError(f"Error: se esperaba '{esperado}' pero se encontró '{self.token_actual}'")
    
    def log(self, mensaje):
        """Imprime un mensaje con indentación"""
        print(f"{'  ' * self.nivel}{mensaje}")
    
    def S(self):
        """S → A B C S'"""
        self.log(f"→ S con token: '{self.token_actual}'")
        self.nivel += 1
        self.log("S → A B C S'")
        self.A()
        self.B()
        self.C()
        self.S_prima()
        self.nivel -= 1
        self.log("← Saliendo de S")
    
    def S_prima(self):
        """S' → uno S' | ε"""
        self.log(f"→ S' con token: '{self.token_actual}'")
        self.nivel += 1
        
        if self.token_actual == Token.UNO:
            self.log("S' → uno S'")
            self.emparejar(Token.UNO)
            self.S_prima()
        elif self.token_actual == Token.FIN_ARCHIVO:
            self.log("S' → ε")
        else:
            raise SyntaxError(f"Error en S': '{self.token_actual}'")
        
        self.nivel -= 1
        self.log("← Saliendo de S'")
    
    def A(self):
        """A → dos B C | ε"""
        self.log(f"→ A con token: '{self.token_actual}'")
        self.nivel += 1
        
        if self.token_actual == Token.DOS:
            self.log("A → dos B C")
            self.emparejar(Token.DOS)
            self.B()
            self.C()
        elif self.token_actual in [Token.CUATRO, Token.TRES, Token.UNO, Token.FIN_ARCHIVO]:
            self.log("A → ε")
        else:
            raise SyntaxError(f"Error en A: '{self.token_actual}'")
        
        self.nivel -= 1
        self.log("← Saliendo de A")
    
    def B(self):
        """B → C tres | ε"""
        self.log(f"→ B con token: '{self.token_actual}'")
        self.nivel += 1
        
        if self.token_actual == Token.CUATRO:
            self.log("B → C tres")
            self.C()
            self.emparejar(Token.TRES)
        elif self.token_actual in [Token.TRES, Token.UNO, Token.FIN_ARCHIVO]:
            self.log("B → ε")
        else:
            raise SyntaxError(f"Error en B: '{self.token_actual}'")
        
        self.nivel -= 1
        self.log("← Saliendo de B")
    
    def C(self):
        """C → cuatro B | ε"""
        self.log(f"→ C con token: '{self.token_actual}'")
        self.nivel += 1
        
        if self.token_actual == Token.CUATRO:
            self.log("C → cuatro B")
            self.emparejar(Token.CUATRO)
            self.B()
        elif self.token_actual in [Token.TRES, Token.UNO, Token.FIN_ARCHIVO]:
            self.log("C → ε")
        else:
            raise SyntaxError(f"Error en C: '{self.token_actual}'")
        
        self.nivel -= 1
        self.log("← Saliendo de C")
    
    def mostrar_gramatica(self):
        """Muestra la gramática cargada"""
        self.gramatica.mostrar()
    
    def analizar(self):
        """Método principal para iniciar el análisis sintáctico"""
        print("=" * 60)
        print("    ANALIZADOR EJERCICIO 3")
        print("=" * 60)
        print(f"Entrada: {' '.join(self.entrada)}")
        print("NOTA: Gramática NO LL(1) - Conflicto en B\n")
        
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
