**Bacharelado em Ciência da Computação**  
**CCMP3079 Segurança de Redes de Computadores**  
**Prof. Sérgio Mendonça**

**Atividade Cap. 05 \- AES**

**Nome Completo:José Elias de Lima**

**Questões retiradas do livro-texto da disciplina.**

**Conforme conversamos em sala de aula, as atividades devem ser realizadas para apresentação e discussão em sala, sempre nas aulas das quintas-feiras, atribuindo ao estudante uma nota de 0 ou 1 por cada atividade realizada e apresentada.**

**1\. Qual foi o conjunto original de critérios usados pelo NIST para avaliar as cifras AES candidatas?**  
R: Os Critérios foram, segurança, resistência à criptoanálise e ataque de texto claro e um tamanho de chave grande o suficiente.   
Custo e eficiência, a cifra deve apresentar desempenho satisfatório em qualquer dispositivo, software ou sistemas,  o uso de memória tem que ser eficiente e a encriptação e decriptação terão que ter um desempenho equilibrado.  
Implementação, a cifra deve ter fácil implementação para que não ocorra erros que comprometam sua segurança e flexível os suficiente para ser utilizada em vários contextos e aplicações.

**2\. Qual foi o conjunto final de critérios usados pelo NIST para avaliar as cifras AES candidatas?**  
R: Nos critérios finais foi feito uma reavaliação dos critérios originais, a segurança, a cifra deve suportar ataque de força bruta, chave relacionada e texto claro, e por último, possuir as propriedades de difusão e confusão(saída depende da entrada e a relação da chave e a saída são complexa).  
No desempenho, a velocidade de encriptação e decriptação, o uso de memória deve ser eficiente e por último, que funcione em qualquer ambiente.  
Implementação, que ele seja simples implementação, flexível que possa ser usada em diversos ambientes e resistente a erros aumentando sua segurança.  
Outros fatores também importantes são sua patente de uso livre, uma documentação clara e boa reputação entre os usuários. 

**3\. Qual é a diferença entre Rijndael e AES?**  
R: Rijndael é a cifra criada por Joan Daemen e Vincent Rijmen e AES é a padronização dessa cifra, enquanto que Rijndael suporta tamanhos de bloco de 128, 192 e 256 bits.  
AES foi padronizado para um tamanho de bloco fixo de 128 bits. A combinação de blocos do Rijndael enquanto que na AES não.

**4\. Responda:**  
**(a) Qual é a finalidade do array Estado?**  
R: Armazenar os blocos que serão modificados.

**(b) Como é construída a S-box?**  
R: A S-box é construída da seguinte forma,  
1\. Inicialize a S-box com os valores em byte em sequência crescente linha por linha. A primeira linha contém {00}, {01}, {02}, ..., {0F}; a segunda linha contém {10}, {11} etc.; e assim por diante. Desse modo, o valor do byte na linha y, coluna x é {yx}.  
2\. Mapeie cada byte na S-box com seu inverso multiplicativo no corpo finito GF(28); o valor {00} é mapeado consigo mesmo.  
3\. Considere que cada byte na S-box consiste em 8 bits rotulados (b7, b6, b5, b4, b3, b2, b1, b0). Aplique a seguinte transformação a cada bit de cada byte na S-box:

**(c) Descreva rapidamente o estágio SubBytes, ShiftRows, MixColumns, AddRoundKey, e o algoritmo de expansão de chave.**  
R:O SubBytes aplica uma substituição em cada byte do array Estado usando a S-box do AES. O ShiftRows desloca as linhas do array Estado de maneira circular para a esquerda. O MixColumns mistura os bytes em cada coluna do Estado, aplicando transformações matemáticas lineares. AddRoundKey combina  o array Estado com uma subchave derivada da chave principal. Algoritmo de Expansão de Chave gera um conjunto de subchaves a partir da chave original para serem usadas em cada rodada do AES.

**5\. Quantos bytes em Estado são afetados por ShiftRows?**

**6\. Use a chave 1010 0111 0011 1011 para encriptar o texto claro "ok"conforme expresso em ASCII, ou seja, 0110 1111 0110 1011\. Os projetistas do S-AES obtiveram o texto cifrado 0000 0111 0011 1000\. E você?**

**7\. Compare AES com DES. Para cada um dos seguintes elementos do DES, indique o elemento comparável no AES ou explique por que ele não é necessário no AES.**

**(a) XOR do material da subchave com a entrada da função f.**  
R:No DES a operação XOR combinar a entrada da função f com o material da subchave, equanto que no AES a etapa de Adição da Chave (AddRoundKey) realiza um XOR entre o estado atual e uma subchave, misturando os bits de forma não-linear.

**(b) XOR da saída da função f com a metade esquerda do bloco.**  
R: No DES o XOR é utilizado para combinar a saída da função f com a metade esquerda do bloco, proporcionando a difusão dos bits. Já no AES, a operação equivalente é a SubBytes, ShiftRows e MixColumns, que juntas realizam uma mistura não-linear e difusão dos bits. Após essas operações, a Adição da Chave é aplicada, que também envolve um XOR.

**(c) função f.**  
R: No DES a função f do DES é composta por várias etapas, incluindo S-boxes, permutações e expansões. Já o AES possui uma função não-linear, mas ela é implementada de forma diferente. A SubBytes é a etapa responsável pela não-linearidade, utilizando S-boxes. As etapas ShiftRows e MixColumns proporcionam a difusão.

**(d) permutação P.**  
R: No DES a permutação P é responsável por difundir os bits ao longo do bloco.  
Já no AES, a função da permutação P é realizada pelas etapas ShiftRows e MixColumns, que permutam os bytes de forma mais complexa e eficiente.

**(e) troca de metades do bloco.**  
R: No DES a troca de metades é uma característica da estrutura de Feistel utilizada no DES. Já o AES não utiliza a estrutura de Feistel. A mistura e difusão dos bits são realizadas de forma mais homogênea em todas as rodadas, sem a necessidade de trocar metades.

**8\. (1 ponto-extra) Calcule a saída da transformação MixColumns para a seguinte sequência de bytes de entrada "67 89 AB CD". Aplique a transformação InvMixColumns ao resultado obtido para verificar seus cálculos. Altere o primeiro byte da entrada de "67"para "77", realize a transformação MixColumns novamente para a nova entrada e determine quantos bits mudaram na saída.**

**Nota: você pode realizar todos os cálculos à mão ou escrever um programa que dê suporte a eles. Se escolher escrever um programa, ele deverá ser feito inteiramente por você; nesta tarefa, não use bibliotecas ou código fonte de domínio público (você pode se guiar pelos exemplos Sage**  
**disponibilizados).**

**9\. (2 pontos-extra) Crie um software que possa encriptar e decriptar usando S-AES. Dados de teste: um texto claro binário de 0110 1111 0110 1011 encriptado com uma chave binária de**  
**1010 0111 0011 1011 deverá dar o texto cifrado binário 0000 0111 0011 1000\. A decriptação deverá funcionar da mesma forma.**  
