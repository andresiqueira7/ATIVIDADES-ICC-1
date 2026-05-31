# 🧠 Verificação de Conectividade da Rede

Uma empresa está avaliando a infraestrutura de sua rede de comunicação. Esta rede é representada por uma **matriz de adjacência** $n \times n$, onde cada linha e coluna representam um **dispositivo** da rede, e cada valor indica a presença ou ausência de uma **conexão direta** entre dois dispositivos.

Mais especificamente, a matriz $A$ é composta por `0`s e `1`s, onde:

- $A[i][j] = 1$ indica que o dispositivo $i$ está diretamente conectado ao dispositivo $j$;
- $A[i][j] = 0$ indica que **não** há conexão direta entre $i$ e $j$;
- A matriz é simétrica: $A[i][j] = A[j][i]$;
- Não há dispositivos conectados em si mesmo: $A[i][i] = 0$ para todo $i$.

A equipe de segurança deseja saber se **todos os dispositivos estão conectados entre si**, direta ou indiretamente, ou seja, se a rede é **conexa**.

Em outras palavras, deseja-se verificar se é possível **chegar de qualquer dispositivo a qualquer outro**, mesmo que através de conexões intermediárias.

## 📥 Entrada

A primeira linha contém dois inteiros:

- `n` $(1 \le n \le 10^3)$ — número de dispositivos da rede;
- `m` $(1 \le m \le 10^3)$ — número de colunas da matriz (deve ser igual a `n`, pois a matriz é quadrada).

Em seguida, seguem `n` linhas com `m` inteiros (`0` ou `1`), representando a matriz de adjacência.

## 📤 Saída

Imprima `"SIM"` se todos os dispositivos da rede estão conectados.  
Imprima `"NAO"` caso contrário.

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

## 🔍 Explicação

- No **primeiro exemplo**, é possível alcançar qualquer dispositivo a partir de qualquer outro. A rede é **conexa**.
- No **segundo exemplo**, os dispositivos estão divididos em dois grupos que não se conectam entre si. A rede **não é conexa**.
- No **terceiro exemplo**, é possível alcançar qualquer dispositivo a partir de qualquer outro. A rede é **conexa**.

# 🚚 Entrega

::include{file=../entregaveis.md}
