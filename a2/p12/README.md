![Triângulos](./triangulos.png)

# 🧠 Triângulos

Uma das formas geométricas mais fortes é o triângulo sabendo disso a empresa de construção de cantoneiras metálicas (ECCM) decidiu criar
um sistema para verificação das estruturas construídas por eles.

Você foi convidado a criar um programa que auxilie na solução deste problema.

Elabore funções auxiliares, além da função principal, que atendam a solicitação:

(a) Determine se os dados lidos formam um triangulo, sabendo que:

- O comprimento de cada lado de um triangulo é menor do que a soma dos outros dois lados.

(b) Determine o tipo de triângulo, caso as medidas formem um triângulo. Sendo que:

- Chama-se equilátero o triângulo que tem três lados iguais.
- Denominam-se isósceles o triângulo que tem o comprimento de dois lados iguais.
- Recebe o nome de escaleno o triangulo que tem os três lados diferentes.

(c) Determine o destino da cantoneira analisada

- caso a cantoneira analisada não forme um triangulo um alarme deve ser acionado e a produção deve parar.
- caso as dimensões formem um triangulo que não seja equilátero a cantoneira deve ser direcionada a linha de ajuste.
- caso as dimensões formem um triângulo e este seja equilátero a cantoneira deve ser direcionada a venda.

## 📥 Entrada

- A entrada será composta por um conjunto de três números inteiros maiores do zero, que irão representar os lados de um triângulo.
- Os dados deverão ser lidos até que um conjunto não forme um triângulo;

## 📤 Saída

As saídas para o seu programa devem ser apresentadas após a leitura de cada conjunto e são correspondes aos textos:

- VENDA -> deve ser impresso se um conjunto forma um triângulo e se o tipo de triangulo é equilátero;
- AJUSTE -> deve ser impresso se um conjunto forma um triângulo e se o tipo de triângulo é escaleno ou isósceles;
- ALARME -> deve ser impresso se o conjunto não formar um triângulo e o programa deve ser finalizado após a impressão.

## 🧪 Exemplos

### Input

```txt
::include{file=1.in}
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

# 🚚 Entrega

::include{file=../entregaveis.md}
