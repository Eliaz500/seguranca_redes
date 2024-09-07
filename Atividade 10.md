  
**Bacharelado em Ciência da Computação**  
**CCMP3079 Segurança de Redes de Computadores**  
**Prof. Sérgio Mendonça**

**Atividade Cap. 10**

**Nome Completo:José Elias de Lima**

**1\. Os usuários A e B utilizam a técnica de troca de chaves Diffie-Hellman com um primo comum q \= 71 e uma raiz primitiva α \= 7\.**

**(a) Se o usuário A tem chave privada XA \= 5, qual é a chave pública de A, YA?**  
R: Calculando 75 mod 71 \= 17

**(b) Se o usuário B tem chave privada XB \= 12, qual é a chave pública de B, YB?**  
R: 7^12 mod 71 \= 36

**(c) Qual é a chave secreta compartilhada?**  
R: A chave secreta compartilhada é 53

**2\. Considere um esquema Elgamal com um primo comum q \= 71 e uma raiz primitiva α \= 7\.**

**(a) Se B tem chave pública YB \= 3 e A escolheu um inteiro aleatório k \= 2, qual é o texto cifrado de M \= 30?**  
R: Calculando C1 ≡ 72 (mod 71\) ≡ 49 (mod 71), fazendo   
C2 ≡ M \* YBk (mod q)  
C2 ≡ 30 \* 32 (mod 71\)  
≡ 30 \* 9 (mod 71\)  
≡ 270 (mod 71\)  
≡ 56 (mod 71\)  
o texto cifrado de M \= 30 é (C1, C2) \= (49, 56).

**(b) Se A, então, selecionar um valor diferente de k, de modo que a codificação de M \= 30 seja C \= (59, C2), qual é o inteiro C2?**  
R: C2 ≡ 30 \* 3k (mod 71\)  
C2 ≡ 30 \* 59 (mod 71\)  
≡ 1770 (mod 71\)  
≡ 16 (mod 71\)  
 o valor de C2 é 16\.

**3\. Demonstre que as duas curvas elípticas da Figura 10.4 satisfazem, cada uma, às condições para um grupo sobre os números reais.**  
R: 

**4\. (4, 7\) é um ponto na curva elíptica y 2 \= x 3 − 5x \+ 5 sobre números reais?**  
R: Basta substituir os valores de x e y na equação da curva e verificar se a igualdade é verdadeira, substituindo x \= 4 e y \= 7, em um lado y² \= 7² \= 49 e no outro x³ \- 5x \+ 5 \= 4³ \- 5\*4 \+ 5 \= 64 \- 20 \+ 5 \= 49.Como são iguais, o ponto (4, 7\) de fato pertence à curva elíptica y² \= x³ \- 5x \+ 5 sobre os números reais.

