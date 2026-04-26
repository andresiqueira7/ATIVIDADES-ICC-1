![sacos-farinha](sacos-farinha.jpg){width=300px}

# 🧠 Como pesar a farinha?

O dono de um armazém precisava pesar cinco sacos de farinha. (Sacos A, B, C, D, E)

No armazém havia uma balança, mas estava faltando alguns pesos impossibilitando pesar entre 50 e 100 kg.

Os sacos pesavam cerca de 50-60 kg cada.

O gerente não se abalou, começou a pesar os sacos de dois em dois.

Com cinco sacos, se podem formar $10$ pares diferentes, então ele teve que pesar em $10$ vezes.

Isso resultou uma série de números, que reproduzimos abaixo em ordem crescente:

- A + B = 109 kg;
- A + C = 112 kg;
- A + D = 113 kg;
- A + E = 114 kg;
- B + C = 115 kg;
- B + D = 116 kg;
- B + E = 117 kg;
- C + D = 119 kg;
- C + E = 120 kg;
- D + E = 121 kg;

Qual é o peso total ($S$) dos sacos ($A + B + C + D + E$)?

Desenvolva o algoritmo utilizando o **_Flowgorithm_** que solucione o problema proposto considerando a seguinte Entrada e Saída esperada:

## 📥 Entrada

Seu algoritmo deve receber a entrada da seguinte forma:

1° linha recebe o valor (flutuante) do peso do saco A + B.

2° linha recebe o valor (flutuante) do peso do saco A + C.

3° linha recebe o valor (flutuante) do peso do saco A + D.

4° linha recebe o valor (flutuante) do peso do saco A + E.

5° linha recebe o valor (flutuante) do peso do saco B + C.

6° linha recebe o valor (flutuante) do peso do saco B + D.

7° linha recebe o valor (flutuante) do peso do saco B + E.

8° linha recebe o valor (flutuante) do peso do saco C + D.

9° linha recebe o valor (flutuante) do peso do saco C + E.

10° linha recebe o valor (flutuante) do peso do saco D + E.

## 📤 Saída

Seu algoritmo deve imprimir o valor (flutuante com 2 casa decimais) da soma dos pesos dos sacos.

## 🧪 Exemplos

### Input:

```txt
::include{file=1.in}

```

### Output

```txt
::include{file=1.out}

```

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
