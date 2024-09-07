**Bacharelado em Ciência da Computação**  
**CCMP3079 Segurança de Redes de Computadores**  
**Prof. Sérgio Mendonça**

**Atividade Cap. 07**

**Nome Completo:José Elias de Lima**

**Questões retiradas do livro-texto da disciplina.**  
**Conforme conversamos em sala de aula, as atividades devem ser realizadas para apresentação e discussão em sala, sempre nas aulas das quintas-feiras, atribuindo ao estudante uma nota de 0 ou 1 por cada atividade realizada e apresentada.**

**1\. Qual é a diferença entre aleatoriedades estatísticas e imprevisibilidade?**  
R: Aleatoriedade estatística é uma sequência de dados ou números em que cada elemento parece ser independente dos outros, já imprevisibilidade é a impossibilidade de prever o próximo elemento de uma sequência, mesmo que todos os elementos anteriores sejam conhecidos

**2\. Liste considerações de projeto importantes para uma cifra de fluxo.**  
R: São 3, primeiro uma sequência de encriptação deverá ter um período grande, o gerador de número pseudo aleatório  repetirá esse número em um período maior. Segundo, o fluxo de chaves deverá se aproximar o máximo possível das propriedades de um fluxo de número aleatório verdadeiro e por último a chave precisa ser suficientemente longa. 

**3\. Por que não é desejável reutilizar uma chave de cifra de fluxo?**  
R: Se dois textos claros forem encriptados com a mesma chave usando uma cifra de fluxo, então a criptoanálise normalmente é muito simples. Se os dois fluxos de texto cifrado passaram por uma operação XOR, o resultado é o XOR dos textos claros originais. Se os textos claros forem strings de texto, números de cartão de crédito ou outros fluxos de bytes com propriedades conhecidas, então a criptoanálise poderá ter sucesso.

**4\. Que operações primitivas são usadas no RC4?**  
R: São 4 operações primitivas, troca de valores, soma do modulo, acesso a elemento e por ultimo operação do XOR.

**5\. Se apanharmos um algoritmo de congruência linear com um componente aditivo de 0:**

**X(n+1) \= (aXn) mod m**

**então, podemos mostrar que, se m é primo, e se determinado valor de a produz o período máximo de m − 1, então a k também produzirá o período máximo, desde que k seja menor que m e que m − 1 não seja divisível por k. Demonstre isso usando X0 \= 1 e m \= 31, e produzindo as sequências para**   
**ak \= 3, 3², 3³ e 3^4.**  
R: O máximo divisor comum de dois números inteiros a e b, denotado por mdc(a,b), é o maior número inteiro d que divide a e b sem deixar resto.  
Se d é um divisor comum de n e n+1n \+ 1n+1, então ele deve dividir qualquer combinação linear de n e n+1n \+ 1n+1. Uma combinação linear pode ser expressa como k=x⋅n+y⋅(n+1), onde x e y são inteiros.  
A diferença entre n+1n \+ 1n+1 e n é (n+1)−n=1(n \+ 1\) \- n \= 1(n+1)−n=1.  
Isso implica que ddd deve dividir 1, já que ddd divide tanto n quanto n+1n \+ 1n+1, e a diferença entre eles é 1\. O único divisor de 1 é o próprio 1\.

**6\. (a) Qual é o período máximo que pode ser obtido do seguinte gerador?**  
**Xn+1 \= (aXn) mod 24**  
R: O período máximo de um gerador congruente linear multiplicativo é o comprimento da maior sequência de valores distintos que o gerador pode produzir antes de repetir um valor. Para o módulo m=2^4=16, o período máximo que pode ser obtido é igual a m−1, que é m−1=2^4−1=15, Isso significa que, no melhor caso, o gerador pode produzir até 15 valores diferentes antes de começar a repetir.

**(b) Qual deverá ser o valor de a?**  
R: Para obter o período máximo de 15, o valor de aaa deve ser um **gerador** do grupo multiplicativo de inteiros módulo 2^4. Os requisitos para que o valor de aaa gere um período máximo quando o módulo é uma potência de 2 são, a deve ser ímpar, a mod  8=3 ou a mod  8=5. Estes valores garantem que a tenha propriedades cíclicas necessárias para gerar todos os números de 1 até m−1 sem repetições antes de completar um ciclo.

**(c) Que restrições são exigidas na semente?**  
R: Para garantir que o gerador produza um período máximo, Semente não nula a semente inicial X0 deve ser não nula (ou seja, X0 ≠ 0). Se X0\= 0, o gerador ficará preso em 0 para todas as iterações subsequentes (porque 0 × a mod 16=0).  
Semente no conjunto de números admissíveis: Dado que o módulo é 24\=16, a semente X0​ deve ser escolhida de forma que 0 \< X0\< 16 para garantir que esteja dentro do conjunto de números que o gerador pode produzir e que possa alcançar o período máximo.

**7\. Que valor de chave RC4 deixará S inalterado durante a inicialização? Ou seja, após a permutação inicial de S, as entradas de S serão quais aos valores de 0 a 255 na ordem crescente.**  
R:A única chave que deixará o vetor S inalterado durante a inicialização é a chave nula ou a chave de comprimento zero. Se a chave tiver todos os valores iguais a zero (ou seja, k\[i\]=0 para todos i), o índice j, que é atualizado como j \= (j \+ S\[i\] \+ k\[i\] ) mod  256, nunca será modificado significativamente. Isso ocorre porque k\[i\] \=0 não contribui para alterar j, e j permanece igual a i em cada iteração. Assim, as trocas de elementos no vetor S não ocorrem. Assim uma chave composta inteiramente de zeros (ou uma chave de comprimento zero) deixará S inalterado, preservando a ordem crescente dos valores de 0 a 255 após a fase de inicialização.

**8\. O algoritmo Blum Blum Shub é baseado na teoria dos resíduos quadráticos e utiliza três números inteiros para realizar os cálculos: p, q e s.**

**(a) Escolha dois números primos grandes p e q, onde p e q sejam congruentes a 3 mod 4 e não tenham fatores primos comuns. Por exemplo, você pode escolher p \= 499 e q \= 503\.**  
R:Escolhendo dois números primos p=499 e q \= 503 como indicados, ambos são primos e congruentes a 3 mod 4, 499 mod  4 \= 3 e 503 mod  4=3, esses dois números satisfazem as condições do algoritmo. Calculando o valor de né o produto de p e q, n \= p × q \= 499 x 503 \= 250997\. Ao escolher uma semente s, que deve ser um número coprimo a n, um número qualquer pode ser escolhido, desde que seja coprimo a n.

**(b) Calcule n \= p ∗ q. Neste caso, n seria igual a 499 ∗ 503 \= 250997\.**  
R: Para calcular n \= p x q \= 499 x 503 \= 250997, o valor de n é **250997**

**(c) Escolha um número inteiro s entre 1 e n − 1 que seja co-primo com n. Por exemplo, você pode escolher s \= 17\.**  
R: Com s \= 17, vamos ver se s é coprimo com n. Vamos calcular o mdc(17, 250997)=1, vemos que 17 é coprimo com 250997\. Agora que temos p=499, q=503, n=250997 e s=17, com o valor inicial de x0\= s2 mod  n \= 172 mod  250997 \= 289\.

**(d) Calcule o valor inicial x0 \= (s²) mod n. Neste caso, x0 seria igual a (17²) mod 250997 \=289.**  
R: Com x0​=(s2) mod n, s \=17 e n=250997, temos x0 \= (172) mod  250997 \= 289, temos então o valor x0 \= 289, Agora que temos x0=289x\_0 \= 289x0​=289, assim podemos seguir gerando os próximos valores utilizando a fórmula xi+1 \= xi2 mod  n.

**(e) Agora, vamos gerar uma sequência de números aleatórios usando o algoritmo Blum Blum Shub. Para gerar cada número da sequência, use a seguinte fórmula: xi \= (x²i−1) mod n.**  
R: Com o valor inicial x0 \= 289 e n \= 250997, calculamos os próximos números da sequência, x1 \= (2892) mod  250997= 83521 mod  250997 \= 83521, com  
x2 \= (835212) mod  250997 \=6979329441 mod  250997=118440, com  
x3 \= (1184402) mod  250997 \= 14026473600 mod  250997 \= 234595 e com x4 \= (2345952) mod  250997 \= 55044005025 mod  250997=124970**.**

**(f) Execute a fórmula várias vezes para gerar uma sequência de números aleatórios. Por exemplo, você pode executar a fórmula 10 vezes para obter 10 números aleatórios.**  
**Aqui está a sequência de números aleatórios gerados usando o algoritmo Blum Blum Shub com os valores do exemplo:**

**289, 253306, 14107, 23546, 67740, 144593, 79829, 46219, 132936, 9863**

**Qual foi a sua sequência?**  
R: Com x0 \= 37 e n \= 265189, essa foi a sequência 37, 1369, 17838, 232633, 197892,253656,150400,68678,16130,2649137, 1369, 17838, 232633, 197892, 253656, 150400, 68678, 16130, 2649137, 1369, 17838, 232633, 197892, 253656, 150400, 68678, 16130, 26491\.  
