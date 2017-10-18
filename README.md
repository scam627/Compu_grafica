# Compu_grafica

En este repositorio encontraras videojuegos creados en python
con manejo sprite y conceptos básicos de computación gráfica
# PRIMER PROCESADOR

El objetivo del primer procesador es dejar la parte aritmetico logica funcionando
cabe destacar que este procesador solo soporta  calculos con enteros   todos  las
caracteristicas de esta primera arquitectura fueron hechas siguiendo el  estandar
de la [arquitectura SPARC V8.](http://www.gaisler.com/doc/sparcv8.pdf)

## Intrucciones que soporta la arquitectura

* Instrucciones logicas     --> OP => 10
  * AND   --> OP => 000001
  * ANDN  --> OP => 000101
  * OR    --> OP => 000010
  * ORN   --> OP => 000110
  * XOR   --> OP => 000011
  * XORN  --> OP => 000111
* Instrucciones aritmeticas --> OP => 10
  * ADD   --> OP => 000000
  * SUB   --> OP => 000100

Ensamblador

```assembler
mov 8,%g1
mov -7,%g2
add %g1,%g2,%o0
xor %g1,%g2,%o1
andn %g1,%g2,%o2
xnor %g1,%g2,%o3
sub %g1,%g2,%o4
```
## Codigo Binario

|op|rd|op3|rs1|i|imm|
|10|00001|000000|00000|1|000000001000|
|10|00010|000000|00000|1|111111111001|

|op|rd|op3|rs1|i|unused|rs2|
|10|01000|000000|00001|0|0000000|00010|
|10|01001|000011|00001|0|0000000|00010|
|10|01010|000101|00001|0|0000000|00010|
|10|01011|000111|00001|0|0000000|00010|
|10|01100|000100|00001|0|0000000|00010|
