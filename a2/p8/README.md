# 🧠 Análise da Variação de Temperaturas

Você foi contratado por uma estação meteorológica para analisar as variações diárias de temperatura em uma cidade.
O objetivo é determinar o **grau de variabilidade** das temperaturas em um determinado período de dias.
Para isso, será necessário calcular o **desvio padrão** das temperaturas registradas.

A estação fornece uma lista com as temperaturas médias diárias registradas em graus Celsius.
Seu programa deve calcular o desvio padrão populacional dessas temperaturas com **precisão de até 4 casas decimais**.

## 📥 Entrada

- A primeira linha contém um número inteiro **N**, representando o número de dias observados.
- A segunda linha contém **N** números reais, representando as temperaturas médias de cada dia.

## 📤 Saída

- Imprima um único número real, representando o **desvio padrão populacional** das temperaturas, com **exatamente 4 casas decimais**.

## 🧮 Fórmula

O **desvio padrão populacional** é calculado pela seguinte fórmula:

$$
\sigma = \sqrt{ \frac{1}{N} \sum_{i=1}^{N} (T_i - \mu)^2 }
$$

onde:

- $\mu$ é a média das temperaturas,
- $T_i$ é a temperatura do dia $i$,
- $N$ é o número total de dias.

## 🔒 Restrições

- $(1 \leq N \leq 10^5)$
- $T_1, T_2, \dots, T_N$ $(-1000.0 \leq T_i \leq 1000.0)$

## 🧪 Exemplos

### Input

```txt
5
20.0 22.0 21.0 19.0 20.0

```

### Output

```txt
1.0198
```

