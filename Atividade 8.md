  
**Bacharelado em Ciência da Computação**  
**CCMP3079 Segurança de Redes de Computadores**  
**Prof. Sérgio Mendonça**

**Atividade Cap. 08**

**Nome Completo:José Elias de Lima**

**Questões retiradas do livro-texto da disciplina.**  
**Conforme conversamos em sala de aula, as atividades devem ser realizadas para apresentação e discussão em sala, sempre nas aulas das quintas-feiras, atribuindo ao estudante uma nota de 0 ou 1 por cada atividade realizada e apresentada.**

**1\. Por que mdc(n, n \+ 1\) \= 1 é para dois inteiros consecutivos n e n \+ 1?**  
R: O único divisor comum entre dois números inteiros consecutivos é o número 1\. Logo, o Máximo Divisor Comum (MDC) de n e n \+ 1 é sempre 1, assim dois números inteiros consecutivos são sempre primos entre si.

**2\. Usando o teorema de Fermat, encontre 3201 mod 11\.**  
R: O Teorema de Fermat  nos diz que se p é um número primo e a é um inteiro não divisível por p, então, a(p-1) ≡ 1 (mod p)

3(11-1) ≡ 310 ≡ 1 (mod 11\)  
201 \= 10 \* 20 \+ 1  
3201 \= 3(10\*20 \+ 1\) \= (310)20 \* 3  
Usando o resultado anterior (310 ≡ 1 mod 11):  
(310)20 \* 3 ≡ 120 \* 3 ≡ 3 (mod 11\)  
Portanto, 3201 ≡ 3 (mod 11).  
Ou seja, o resto da divisão de 3201 por 11 é 3\.

**3\. Use o teorema de Fermat para encontrar um número a entre 0 e 72, com a congruente a 9794 módulo 73\.**  
R:9794 ÷ 73 \= 134 com resto 42\.

Portanto, 9794 ≡ 42 (mod 73).

Verificação com o Teorema de Fermat:  
Embora não precisemos calcular 979472, podemos verificar que 42 satisfaz o teorema:  
42(73-1) ≡ 4272 ≡ 1 (mod 73\)  
**4\. Use o teorema de Euler para encontrar um número a entre 0 e 9, tal que a seja congruente a 71000 módulo 10\. (Observe que isso é o mesmo que o último dígito da expansão decimal de 71000.)**  
R: Os números menores que 10 e coprimos com 10 são 1, 3, 7 e 9\. Logo, φ(10) \= 4\.  
74 ≡ 1 (mod 10\)  
1000 \= 4 \* 250 Então, 71000 \= (74)250  
S(74)250 ≡ 1250 ≡ 1 (mod 10\)  
71000 ≡ 1 (mod 10).  
71000 é 1\.

**5\. Use o teorema de Euler para encontrar um número x entre 0 e 28, com x85 congruente a 6 módulo 35 (Você não precisará usar qualquer pesquisa por força bruta).**  
R: Com 35 \= 5 × 735 \= 5, então ϕ(35) \= ϕ(5) x ϕ(7), Para números primos, ϕ(p) \= p − 1, então ϕ(5) \= 4 e ϕ(7)=6. Logo, ϕ(35) \= 4 x 6 \= 24, pelo Teorema de Euler, se gcd⁡(x, 35\) \= 1, então xϕ(35) ≡ 1 (mod 35), ou seja, x24 ≡ 1(mod 35), reduzindo o expoente 85 módulo 24, 85/24 \= 3 com resto 13, assim, x85 ≡ x13(mod 35). resolvendo x13 ≡ 6 (mod 35). Encontrando um número x tal que x13 ≡ 6 (mod 35). Isso pode ser feito usando inversão modular, exponencial rápida e o Teorema de Euler.  
 

**6\. Observe, na Tabela 8.2, que φ(n) é par para n \> 2\. Isso é verdadeiro para todo n \> 2\. Dê um argumento conciso para explicar por que isso acontece.**  
R:

**7\. Se n é composto e passa no teste de Miller-Rabin para a base a, então n é chamado de pseudo- primo forte à base a. Mostre que 2047 é um pseudoprimo à base 2\.**  
R: Escrever n−1 na forma 2s \*  d, 2047 − 1= 20462047, assim 2046 \= 21 \* 10232046 \= 2^1 \\cdot 10232046=21⋅1023, temos s=1 e d=1023. Calculando  21023 mod  20472. Este é o primeiro passo do teste de Miller-Rabin. Se este valor for 1 ou n−1, o número pode ser um pseudoprimo forte à base 2\. Calculando 21023 mod  20472 verificamos se 21023 ≡ 1 (mod 2047\) ou se 22^r \* d≡ −1 (mod 2047\) para algum valor de r.

**8\. O exemplo usado por Sun-Tsu para ilustrar o CRT foi** 

**x \= 2 (mod 3);  x \= 3 (mod 5); x \= 2 (mod 7\)**

**Solucione para x.**  
R: x \= 23