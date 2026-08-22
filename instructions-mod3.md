# Tópico 1 — Listas e sys.argv

## O que preciso aprender
Lista é uma sequência ordenada e mutável de elementos. `sys.argv` é uma lista de strings que o Python preenche automaticamente com os argumentos passados na linha de comando — o próprio nome do script já entra como primeiro elemento.

## O que devo saber antes
Nenhum (primeiro tópico).

## Conceitos importantes
- Criação e indexação de listas
- `len()` pra saber o tamanho
- Fatiamento (slicing) pra pegar um pedaço da lista, ex: ignorar o primeiro elemento
- `import sys` e `sys.argv`

## Sintaxe básica
```python
import sys
print(sys.argv)        # ['script.py', 'arg1', 'arg2']
print(len(sys.argv))
resto = sys.argv[1:]   # tudo menos o nome do script
```

## Erros comuns
- Esquecer que `sys.argv[0]` é o nome do script, não o primeiro argumento
- Tentar acessar `sys.argv[1]` sem checar se ele existe (IndexError quando não há argumentos)

## Como esse assunto aparece na lista
Base do ex0 (Command Quest) e ex1 (Score Cruncher) — mas como pré-requisito, é bom já estar 100% sólido antes de avançar.

## Links úteis
- https://docs.python.org/3/tutorial/datastructures.html — documentação oficial sobre listas
- busque no YouTube: "Python sys.argv tutorial"
- https://realpython.com/python-command-line-arguments/ — artigo sobre argumentos de linha de comando
# Tópico 2 — Tratamento de erros com try/except

## O que preciso aprender
Permite capturar erros (como conversão inválida de string pra número) sem que o programa quebre. Essencial pra lidar com entrada do usuário que pode vir errada.

## O que devo saber antes
Tópico 1 — Listas e sys.argv

## Conceitos importantes
- Bloco `try` / `except`
- Capturar o tipo certo de exceção (ex: `ValueError` ao converter string inválida)
- Acessar a mensagem do erro (`except ValueError as e`)
- Continuar o processamento mesmo quando um item falha (loop com try dentro)

## Sintaxe básica
```python
try:
    valor = int("abc")
except ValueError as e:
    print(f"Erro: {e}")
```

## Erros comuns
- Usar `except:` genérico sem especificar o tipo (esconde bugs)
- Parar o processamento inteiro no primeiro erro, em vez de pular o item inválido e continuar

## Como esse assunto aparece na lista
Usado em praticamente todo exercício que lê argumentos ou input do usuário (ex1, ex2, ex4).

## Links úteis
- https://docs.python.org/3/tutorial/errors.html — documentação oficial sobre exceções
- busque no YouTube: "Python try except tutorial"
- https://realpython.com/python-exceptions/ — artigo sobre exceções em Python
# Tópico 3 — Estatística básica com listas

## O que preciso aprender
Funções nativas do Python pra calcular estatísticas simples sobre uma lista de números: soma, média, maior, menor e amplitude.

## O que devo saber antes
Tópico 1 — Listas e sys.argv

## Conceitos importantes
- `sum()`, `max()`, `min()`
- Cálculo de média (soma / quantidade)
- Cálculo de amplitude (max - min)
- Formatação de saída (arredondamento, casas decimais)

## Sintaxe básica
```python
numeros = [10, 20, 30]
total = sum(numeros)
media = total / len(numeros)
maior = max(numeros)
menor = min(numeros)
```

## Erros comuns
- Dividir por zero quando a lista está vazia
- Misturar tipos int/float sem perceber (afeta a formatação da saída)

## Como esse assunto aparece na lista
Núcleo do ex1 (Score Cruncher).

## Links úteis
- https://docs.python.org/3/library/functions.html#sum — documentação oficial das built-in functions
- busque no YouTube: "Python sum max min tutorial"
- https://realpython.com/python-statistics-module/ — artigo sobre estatística em Python
# Tópico 4 — Tuplas

## O que preciso aprender
Tupla é uma sequência ordenada e **imutável**. Depois de criada, não dá pra alterar, adicionar ou remover elementos. Ótima pra dados fixos, tipo coordenadas (x, y, z).

## O que devo saber antes
Tópico 1 — Listas e sys.argv

## Conceitos importantes
- Criação com parênteses (opcionais) e vírgulas
- Imutabilidade — o que muda e o que não muda em relação à lista
- Indexação e slicing (igual lista)
- Unpacking (desempacotar tupla em variáveis separadas)
- Tupla de 1 elemento precisa de vírgula: `(x,)`

## Sintaxe básica
```python
t = (1, 2, 3)
a, b, c = t          # unpacking
print(t[0])
```

## Erros comuns
- Tentar modificar um elemento da tupla (`TypeError`)
- Esquecer a vírgula ao criar tupla de 1 elemento
- Confundir `(1, 2, 3)` com uma expressão matemática entre parênteses

## Como esse assunto aparece na lista
Núcleo do ex2 (Position Tracker) — as coordenadas 3D são armazenadas como tupla.

## Links úteis
- https://docs.python.org/3/tutorial/datastructures.html — documentação oficial (seção de tuplas)
- busque no YouTube: "Python tuples tutorial"
- https://realpython.com/python-tuple/ — artigo sobre tuplas
# Tópico 5 — input() e validação de entrada do usuário

## O que preciso aprender
`input()` lê uma linha digitada pelo usuário como string. Pra pedir dados repetidamente até que sejam válidos, usa-se um loop combinado com try/except.

## O que devo saber antes
Tópico 2 — Tratamento de erros com try/except

## Conceitos importantes
- `input()` sempre retorna string
- Loop `while True` com `break` quando o valor é válido
- `.split()` pra separar uma string em partes (ex: por vírgula)
- Conversão de string pra float com `float()`

## Sintaxe básica
```python
while True:
    texto = input("Digite algo: ")
    partes = texto.split(",")
    try:
        valores = [float(p) for p in partes]
        break
    except ValueError:
        print("Inválido")
```

## Erros comuns
- Não tratar espaços extras nas partes separadas (`" 2.5"` vs `"2.5"`)
- Esquecer de validar a quantidade de partes (ex: precisa ter exatamente 3 valores)

## Como esse assunto aparece na lista
Núcleo do `get_player_pos()` no ex2 (Position Tracker).

## Links úteis
- https://docs.python.org/3/library/functions.html#input — documentação oficial do input()
- busque no YouTube: "Python input validation loop"
- https://realpython.com/python-input-output/ — artigo sobre input/output em Python
# Tópico 6 — math.sqrt() e fórmulas

## O que preciso aprender
O módulo `math` oferece funções matemáticas prontas, como raiz quadrada, necessária pra calcular distância euclidiana entre dois pontos.

## O que devo saber antes
Tópico 4 — Tuplas

## Conceitos importantes
- `import math`
- `math.sqrt()`
- Operador de potência `**`
- Fórmula da distância euclidiana em 3D

## Sintaxe básica
```python
import math
distancia = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
```

## Erros comuns
- Usar `x^2` em vez de `x**2` (operador errado em Python)
- Esquecer o `import math` antes de usar `math.sqrt()`

## Como esse assunto aparece na lista
Cálculo de distância no ex2 (Position Tracker).

## Links úteis
- https://docs.python.org/3/library/math.html — documentação oficial do módulo math
- busque no YouTube: "Python math module sqrt"
- https://realpython.com/python-math-module/ — artigo sobre o módulo math
# Tópico 7 — Sets

## O que preciso aprender
Set é uma coleção **não ordenada** de elementos **únicos** — não permite duplicatas. Ideal pra representar coisas como "conjunto de conquistas desbloqueadas".

## O que devo saber antes
Tópico 1 — Listas e sys.argv

## Conceitos importantes
- Criação com `{}` ou `set()` (nunca `{}` vazio — isso cria um dict!)
- Elementos únicos automaticamente
- Sem ordem garantida
- `len()` funciona igual em sets

## Sintaxe básica
```python
s = {1, 2, 3}
vazio = set()          # NÃO use {} para set vazio
s2 = set([1, 1, 2])    # vira {1, 2}
```

## Erros comuns
- Usar `{}` pra criar set vazio (na verdade cria um dict vazio)
- Tentar acessar elemento por índice (`s[0]`) — set não é indexável
- Esperar ordem de inserção preservada

## Como esse assunto aparece na lista
Base do ex3 (Achievement Hunter) — cada jogador tem um set de conquistas.

## Links úteis
- https://docs.python.org/3/tutorial/datastructures.html — documentação oficial (seção de sets)
- busque no YouTube: "Python sets tutorial"
- https://realpython.com/python-sets/ — artigo sobre sets em Python
# Tópico 8 — random (módulo)

## O que preciso aprender
O módulo `random` gera valores aleatórios: números, escolhas de listas, amostras sem repetição.

## O que devo saber antes
Tópico 7 — Sets

## Conceitos importantes
- `import random`
- `random.randint(a, b)` — inteiro aleatório entre a e b
- `random.choice(lista)` — escolhe um elemento aleatório
- `random.sample(lista, k)` — escolhe k elementos distintos sem repetição

## Sintaxe básica
```python
import random
n = random.randint(1, 10)
item = random.choice(["a", "b", "c"])
amostra = random.sample(["a", "b", "c", "d"], 2)
```

## Erros comuns
- Confundir `random.sample()` (sem repetição) com escolhas repetidas via `random.choice()` em loop
- Pedir `k` maior que o tamanho da lista em `random.sample()` (gera erro)

## Como esse assunto aparece na lista
Usado no ex3 (gerar conquistas aleatórias por jogador) e no ex5 (gerar eventos aleatórios).

## Links úteis
- https://docs.python.org/3/library/random.html — documentação oficial do módulo random
- busque no YouTube: "Python random module tutorial"
- https://realpython.com/python-random/ — artigo sobre geração de números aleatórios
# Tópico 9 — Operações de conjunto (union, intersection, difference)

## O que preciso aprender
Sets suportam operações matemáticas de teoria dos conjuntos: união (tudo junto), interseção (o que é comum) e diferença (o que está num mas não no outro).

## O que devo saber antes
Tópico 7 — Sets

## Conceitos importantes
- `set.union()` — combina todos os elementos
- `set.intersection()` — elementos em comum
- `set.difference()` — elementos que só estão no primeiro set
- Essas operações podem receber múltiplos sets de uma vez

## Sintaxe básica
```python
a = {1, 2, 3}
b = {2, 3, 4}
a.union(b)          # {1, 2, 3, 4}
a.intersection(b)   # {2, 3}
a.difference(b)      # {1}
```

## Erros comuns
- Confundir `difference()` (assimétrica) com algo simétrico
- Esquecer que essas operações retornam um **novo** set, não alteram o original

## Como esse assunto aparece na lista
Núcleo do ex3 (Achievement Hunter) — achar conquistas comuns, exclusivas e faltantes entre jogadores.

## Links úteis
- https://docs.python.org/3/library/stdtypes.html#set — documentação oficial dos métodos de set
- busque no YouTube: "Python set union intersection difference"
- https://realpython.com/python-sets/ — mesmo artigo do tópico 7, cobre essa parte também
# Tópico 10 — Dicionários

## O que preciso aprender
Dicionário armazena pares chave-valor. Cada chave é única e mapeia pra um valor, permitindo acesso rápido por nome em vez de posição.

## O que devo saber antes
Tópico 1 — Listas e sys.argv

## Conceitos importantes
- Criação com `{}`
- Acesso, inserção e atualização por chave
- `dict.keys()`, `dict.values()`
- `dict.update()` pra mesclar ou adicionar chaves
- Checar se uma chave já existe (`in`)

## Sintaxe básica
```python
d = {"a": 1, "b": 2}
d["c"] = 3
print(d.keys())
print(d.values())
d.update({"d": 4})
if "a" in d:
    print("existe")
```

## Erros comuns
- Acessar chave inexistente com `d[chave]` (gera `KeyError`) em vez de checar antes com `in`
- Achar que `dict.keys()`/`dict.values()` retornam listas comuns (na verdade retornam "views")

## Como esse assunto aparece na lista
Base do ex4 (Inventory Master).

## Links úteis
- https://docs.python.org/3/tutorial/datastructures.html — documentação oficial (seção de dicionários)
- busque no YouTube: "Python dictionaries tutorial"
- https://realpython.com/python-dicts/ — artigo sobre dicionários em Python
# Tópico 11 — Parsing de strings (split, formatos tipo chave:valor)

## O que preciso aprender
Transformar strings de argumentos de linha de comando (ex: `"sword:1"`) em dados estruturados, separando chave e valor, e validando o formato.

## O que devo saber antes
Tópico 2 — Tratamento de erros com try/except, Tópico 10 — Dicionários

## Conceitos importantes
- `.split(":")` pra separar string em partes por um caractere
- Validar que a string tem exatamente o formato esperado (número de partes)
- Converter a parte numérica com `int()` dentro de um try/except
- Detectar chaves repetidas (redundantes) ao inserir num dict

## Sintaxe básica
```python
texto = "sword:1"
partes = texto.split(":")
if len(partes) == 2:
    chave, valor = partes
    valor = int(valor)
```

## Erros comuns
- Não checar quantas partes o `.split()` retornou antes de desempacotar (gera `ValueError`)
- Ignorar o caso de chave duplicada silenciosamente, sem avisar o usuário

## Como esse assunto aparece na lista
Núcleo do parsing de argumentos no ex4 (Inventory Master).

## Links úteis
- https://docs.python.org/3/library/stdtypes.html#str.split — documentação oficial do método split
- busque no YouTube: "Python string split tutorial"
- https://realpython.com/python-string-split-concatenate-join/ — artigo sobre manipulação de strings

# Tópico 12 — Generators e yield

## O que preciso aprender
Generators são funções especiais que produzem valores sob demanda, um de cada vez, em vez de criar tudo na memória de uma vez. Usam a palavra-chave `yield`.

## O que devo saber antes
Tópico 8 — random (módulo)

## Conceitos importantes
- Diferença entre `return` (encerra a função) e `yield` (pausa e retoma)
- Generator infinito (loop `while True` com `yield` dentro)
- `next()` pra pedir o próximo valor manualmente
- Usar um generator dentro de `for ... in ...`
- `typing.Generator` como type hint

## Sintaxe básica
```python
def contador():
    n = 0
    while True:
        yield n
        n += 1

g = contador()
print(next(g))   # 0
print(next(g))   # 1

for valor in contador():
    print(valor)
    break
```

## Erros comuns
- Confundir generator com lista — não dá pra indexar (`g[0]` não funciona)
- Esquecer que um generator só pode ser percorrido uma vez (se for finito)
- Usar `return` em vez de `yield` e perder o comportamento de generator

## Como esse assunto aparece na lista
Núcleo do ex5 (Stream Wizard) — `gen_event()` e `consume_event()`.

## Links úteis
- https://docs.python.org/3/tutorial/classes.html#generators — documentação oficial sobre generators
- busque no YouTube: "Python generators yield tutorial"
- https://realpython.com/introduction-to-python-generators/ — artigo sobre generators
# Tópico 13 — List e dict comprehensions

## O que preciso aprender
Sintaxe compacta pra criar listas, dicts ou sets a partir de outra coleção, aplicando uma transformação e/ou filtro, tudo numa linha.

## O que devo saber antes
Tópico 10 — Dicionários

## Conceitos importantes
- List comprehension: `[expressao for item in iteravel]`
- Com filtro: `[expressao for item in iteravel if condicao]`
- Dict comprehension: `{chave: valor for item in iteravel}`
- Também existe set comprehension (mesma lógica, com `{}`)

## Sintaxe básica
```python
nomes = ["ana", "Bob"]
maiusculas = [n.capitalize() for n in nomes]
so_capitalizados = [n for n in nomes if n[0].isupper()]

scores = {"a": 10, "b": 20}
media = sum(scores.values()) / len(scores)
altos = {k: v for k, v in scores.items() if v > media}
```

## Erros comuns
- Comprehension muito longa e ilegível — a apostila pede uma linha só, mas isso não deve sacrificar clareza
- Esquecer que `dict.items()` é necessário pra iterar chave e valor juntos

## Como esse assunto aparece na lista
Núcleo do ex6 (Data Alchemist).

## Links úteis
- https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions — documentação oficial
- busque no YouTube: "Python list comprehension dict comprehension tutorial"
- https://realpython.com/list-comprehension-python/ — artigo sobre comprehensions
