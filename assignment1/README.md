## Implementações dos algoritmos de ordenação

Todas as implementações são baseadas nos pseudo-códigos do livro **Introduction to Algorithms - Cormen**, e estão sem nenhum tipo de otimização.

1. Insertion Sort 
2. Selection Sort
3. Default Sort

## Execução:
O programa recebe como argumento um inteiro **n** representado o algoritmo, com base na numeração acima. 
```
$  python main.py n < input > ordered.out && diff ordered.out output
$  python main.py 5 < data/example.in > ordered.out && diff ordered.out data/example.out
```

## Testes:
Os algoritmos são testados com listas de tamanhos e elementos aleatórios. Também são feitos testes com listas com valores já ordenadas e lista com valores ordenados inversamente.
```
$  python tests.py
```

