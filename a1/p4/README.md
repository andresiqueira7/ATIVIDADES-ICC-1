# 🧠 A Diferença Misteriosa

Alice adora brincar com números e recentemente descobriu uma operação interessante: a **diferença dos quadrados** de dois números naturais positivos.

Dada uma sequência de números naturais positivos $a_1, a_2, \ldots, a_n$, Alice define a **diferença misteriosa** entre dois elementos $a_i$ e $a_j$ como:

$$
D = a_j^2 - a_i^2
$$

Curiosa, ela quer saber qual é a maior diferença misteriosa possível que pode ser obtida a partir de dois elementos distintos da sequência, onde $i \ne j$, e os valores de $a_i$ e $a_j$ devem ser diferentes e pelo entendimento lógico se buscamos a maior diferença misteriosa, então podemos afirma que $a_i < a_j$.

Sua tarefa é ajudá-la a encontrar essa maior diferença misteriosa, dado um conjunto de números naturais distintos.

Desenvolva o algoritmo utilizando o **_Flowgorithm_** que solucione o problema proposto considerando a seguinte Entrada e Saída esperada:

## 📥 Entrada

A primeira linha contém um número inteiro $n$ $(2 \leq n \leq 10^5)$, representando o tamanho da sequência.

A segunda linha contém $n$ inteiros distintos $a_1, a_2, \ldots, a_n$ $(1 \leq a_i \leq 10^4)$, representando os elementos da sequência.

## 📤 Saída

Imprima um único inteiro representando a maior diferença possível entre os quadrados de dois elementos distintos da sequência, ou seja, $D \ge 0$.

## 🧪 Exemplos

### Input

```txt
4
3 
10 
7 
1

```

### Output

```txt
::include{file=1.out}
```

---

### Input

```txt
::include{file=2.in}
```

### Output

```txt
::include{file=2.out}
```

---

### Input

```txt
::include{file=3.in}
```

### Output

```txt
::include{file=3.out}
```

## 📘 Explicação

A maior diferença ocorre entre os elementos 10 e 1:

$$
10^2 - 1^2 = 100 - 1 = 99
$$

## 💡 Observações

- Para resolver esse problema com eficiência, é necessário compreender a fórmula de diferença de quadrados:

$$
a_j^2 - a_i^2 = (a_j - a_i)(a_j + a_i)
$$

- A implementação deve ser otimizada para lidar com grandes volumes de entrada, evitando laços aninhados desnecessários.
- Este enunciado força o competidor a pensar em estratégias para encontrar os dois números mais distantes da sequência, em termos absolutos, e aplicar corretamente a diferença dos quadrados.

# 🚚 Entrega

Arquivos que devem estar presenta na entrega:

```sh
├── a#
│   ├── p#
│   │   ├── 1.in
│   │   ├── 1.out
│   │   ├── main.{cpp|fprg|py}
│   │   ├── README.md
```


- A pasta `a#` refere-se à pasta das atividades, onde `#` representa o número da atividade. Por exemplo: `a1`, `a2`, `a3`, e assim por diante.

- A pasta `p#` refere-se à pasta dos problemas, onde `#` representa o número do problema. Por exemplo: `p1`, `p2`, `p3`, e assim por diante.

- O código de entrega deve ser nomeado `main.cpp` para soluções em C++ ou `main.fprg` para soluções em Flowgorithm, dependendo da linguagem especificada no enunciado do problema.

- O arquivo `1.in` é um arquivo de entrada utilizado para testar o código implementado.

- O arquivo `1.out` é um arquivo de saída gerado pelo código ao testar a entrada contida em `1.in`.

- O arquivo `README.md` deve conter o enunciado do problema.

> [!warning] Muita atenção
> Letras **maiúsculas** são diferente de letras **minúsculas**. Preste atenção no padrão de nome dos arquivos isso faz parte da avaliação.
