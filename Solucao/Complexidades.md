```
algoritmo uniaoOrdenada(v1, v2, n1, n2) {
{- Entrada: v1 e v2 são vetores de inteiros ordenados crescentemente, n1 e n2 são seus respectivos tamanhos
Saída: vetor união dos vetores v1 e v2 -}
	i := 1
	j := 1
	u := 1
	
	enquanto i < n1 && j < n2 faça
		se v1[i] < v2[j] então
			uniao[u] = v1[i]
			u := u+1
			i := i+1
		senão se v1[i] > v2[j] então
			uniao[u] = v2[j]
			u := u+1
			j := j+1
		senão então
			uniao[u] = v1[i]
			u := u+1
			i := i+1
			j := j+1

	enquanto i < n1 faça
		uniao[u] := v1[i]
		u := u+1
		i := i+1

	enquanto j < n2 faça
		uniao[u] := v2[j]
		u := u+1
		j := j+1

	retorne uniao
}
```

**Complexidade de espaço:**
O espaço total utilizado da memória é:
- 1 inteiro para armazenar a variável $i$;
- 1 inteiro para armazenar a variável $j$;
- 1 inteiro para armazenar a variável $u$;
- 1 inteiro para armazenar a variável $n1$;
- 1 inteiro para armazenar a variável $n2$;
- $n1$ inteiros para armazenar os elementos de um vetor;
- $n2$ inteiros para armazenar os elementos do outro vetor.
Complexidade de espaço: 
A quantidade total de memória usada pelo algoritmo *uniaoOrdenada* é $n1 + n2 + 5$, em função do tamanho da entrada.

**Complexidade de tempo:** 
Considerando que $n1$ e $n2$ possuam o mesmo tamanho, para o pior caso a complexidade de tempo é dada por 
$T(n) = 3T_{:=} + (T_< + T_{\&\&} + T_< + T_{><=}) + (T_< + T_<)$
        $= c_1 + (\sum\limits_{i=1}^{n1} + \sum\limits_{j=1}^{n2})c_2 + c_3$
		$= c_1 + (n1 - 1 + 1 + n2 - 1 + 1)c_2 + c_3$
		$= c_1 + n1c_2 + n2c_2 + c_3$
		$= n1 + n2$
Considerando $n$ como a soma das entradas $n1$ e $n2$ temos que a função que descreve a quantidade total de memória usada pelo algoritmo *uniaoOrdenada* é $T(n) = n$, que é linear em função do tamanho da entrada, deste modo, $T(n) = O(n)$.
		
```
algoritmo intersecaoOrdenada(v1, v2, n1, n2) {
{- Entrada: v1 e v2 são vetores de inteiros ordenados decrescentemente, n1 e n2 são seus respectivos tamanhos
Saída: vetor intersecao dos vetores v1 e v2 -}
	i := n1-1
	j := n2-1
	u := 1
	
	enquanto i >= 1 && j >= 1 faça
		se v1[i] < v2[j] então
			i := i-1
		senão se v1[i] > v2[j] então
			j := j-1
		senão então
			intersecao[u] = v1[i]
			u := u+1
			i := i-1
			j := j-1

	retorne intersecao
}
```

O espaço total utilizado da memória é:
- 1 inteiro para armazenar a variável $i$;
- 1 inteiro para armazenar a variável $j$;
- 1 inteiro para armazenar a variável $k$;
- 1 inteiro para armazenar a variável $n1$;
- 1 inteiro para armazenar a variável $n2$;
- $n1$ inteiros para armazenar os elementos de um vetor;
- $n2$ inteiros para armazenar os elementos do outro vetor.

**Complexidade de espaço:** 
A quantidade total de memória usada pelo algoritmo *intersecaoOrdenada* no pior caso é $n1 + n2 + 5$, em função do tamanho da entrada.

**Complexidade de tempo:** 
Considerando que $n1$ e $n2$ os tamanhos dos vetores, para o pior caso a complexidade de tempo é dada por 
$T(n) = 3T_{:=} + (T_{<} + T_{\&\&} + T_{<} + T_< + T_> + T_=)$
        $= c_1 + (\sum\limits_{i=1}^{n1} + \sum\limits_{j=1}^{n2})c_2$
		$= c_1 + (n1 - 1 + 1 + n2 - 1 + 1)c_2 + c_3$
		$= c_1 + n1c_2 + n2c_2 + c_3$
		$= n1 + n2$
Considerando $n$ como a soma das entradas $n1$ e $n2$ e abstraindo as constantes temos que a função que descreve a complexidade de tempo do algoritmo *intersecaoOrdenada* é $T(n) = n$, que é linear em função do tamanho da entrada, deste modo, $T(n) = O(n)$.

```
algoritmo intersecaoArbitraria(v1, v2, n1, n2) {
{- Entrada: v1 e v2 são vetores de inteiros ordenados arbitrariamente, n1 e n2 são seus respectivos tamanhos
Saída: vetor intersecao dos vetores v1 e v2 -}
	k := 1
	para i=1 até n1 faça
		para j=1 até n2 faça
			se v1[i] = v2[j]
				intersecao[k] = v1[i]
				k := k+1
	retorne intersecao
}
```  

O espaço total utilizado da memória é:
- 1 inteiro para armazenar a variável $i$;
- 1 inteiro para armazenar a variável $j$;
- 1 inteiro para armazenar a variável $k$;
- 1 inteiro para armazenar a variável $n1$;
- 1 inteiro para armazenar a variável $n2$;
- $n1$ inteiros para armazenar os elementos de um vetor;
- $n2$ inteiros para armazenar os elementos do outro vetor.

**Complexidade de espaço:** 
A quantidade total de memória usada pelo algoritmo *intersecaoArbitraria* no pior caso é $n1 + n2 + 5$, em função do tamanho da entrada.

**Complexidade de tempo:** 
Considerando que no pior caso, ambos os vetores possuíssem o mesmo tamanho  $n$, a complexidade de tempo é dada por 
$T(n) = T_{:=} + (T_{[]} + T_{=} + T_{[]} +  T_{[]} + T_{=} + T_{[]} + T_{+} + T_{:=})$
        $= c_1 + (\sum\limits_{i=1}^{n}\sum\limits_{j=1}^{n})c_2$
		$= c_1 + (\sum\limits_{i=1}^{n1}(n - 1 + 1))c_2$
		$= c_1 + ((n-1+1)(n - 1 + 1))c_2$
		$= c_1 + n^2c_2$
Abstraindo as constantes temos que a função que descreve a complexidade de tempo do algoritmo *intersecaoArbitraria* é $T(n) = n^2$, que é quadrática em função do tamanho da entrada, deste modo, $T(n) = O(n^2)$.

```
ehVazia(p):
	se p.topo < 0:
		então retorne Verdadeiro
	retorne Falso
	
empilha(p, e):
	p.topo := p.topo + 1
	p[p.topo] = e

desempilha(p):
	p.topo := p.topo - 1

algoritmo testaExpressao(expressao, n) {
{- Entrada: expressao denota uma expressao do tipo string e n o tamanho da mesma
Saída: booleano indicando se os parênteses estão balanceados -}
	para i=1 até n faça
		se expressao[i] = '('
			então empilha(p, expressao[i])
		senão se expressao[i] = ')' && ehVazia(p)
			então retorne Falso
		senão se expressao[i] = ')'
			entao desempilha(p)

		retorne ehVazia(p)
}
```

O espaço total utilizado da memória é:
- 1 inteiro para armazenar a variável $i$;
- 1 inteiro para armazenar a variável $n$;
- $n$ inteiros para armazenar os caracteres empilhados.

**Complexidade de espaço:** 
A quantidade total de memória usada pelo algoritmo *testaExpressao* no pior caso é $2n + 1$, em função do tamanho da entrada.


**Complexidade de tempo:** 
Considerando que no pior caso, ambos os vetores possuíssem o mesmo tamanho  $n$, a complexidade de tempo é dada por 
$T(n) = T_{[]} + T_= + T_{[]} + T_{=} + T_{\&\&} + T_{[]} + T_=$
        $= c_1 + (\sum\limits_{i=1}^{n})c_2$
		$=(n - 1 + 1))c_2$
		$= nc_2$
Abstraindo as constantes temos que a função que descreve a complexidade de tempo do algoritmo *testaExpressao* é $T(n) = n$, que é linear em função do tamanho da entrada, deste modo, $T(n) = O(n)$.
