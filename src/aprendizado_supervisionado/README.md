# Trabalho 1 - Aprendizado supervisionado

Integrantes:

- (00314477)(Turma B) Andreas Emilio Panzenhagen Franz
- (00343701)(Turma B) Clara Schons Theisen
- (00314943)(Turma B) Matheus Luís de Castro

## Parte 1 - Regressão linear

Parâmetros iniciais para o menor Erro Quadrático Médio (EQM):

| coef. linear (`b`) | coef. angular (`w`) | taxa de aprendizado (`alpha`) | iterações (`num_iterations`) |  EQM  |
|--------------------|---------------------|-------------------------------|------------------------------|-------|
|         -3         |          1          |          1 * 10^(-5)          |             1000             | 8.604 |

## Parte 2 - Redes neurais

### Características de cada Dataset

- CIFAR-10
    - Imagens 32x32x3 (três canais de cores), são 60000 imagens divididas em 10 classes, com 6000 imagens por classe, sendo 50000 imagens de treinamento e 10000 imagens de teste.
- CIFAR-100
    - Imagens 32x32x3 (três canais de cores), são 60000 imagens divididas em 100 classes, com 600 imagens por classe, sendo 50000 imagens de treinamento e 10000 imagens de teste.
- MNIST
    - Imagens 28x28x1 (um canal de cor), são 70000 imagens divididas em 10 classes (dígitos manuscritos de 0-9), sendo 60000 imagens de treinamento e 10000 imagens de teste.
- Fashion-MNIST
    - Imagens 28x28x1 (um canal de cor), são 70000 imagens divididas em 10 classes (artigos de moda), sendo 60000 imagens de treinamento e 10000 imagens de teste.

### Testes

- CIFAR-10:
    - Primeiro teste: foi utilizada a configuração dada no trabalho.
        - Acurácia no conjunto de treinamento: 59%
        - Acurácia no conjunto de testes: 55%
        - Duração do treinamento: 2m 16s.

    - Segundo teste: foi adicionada mais uma camada de convolução, mas agora com 16 filtros.
        - Acurácia no conjunto de treinamento: 65%
        - Acurácia no conjunto de testes: 57%.
        - Duração do treinamento: 2m 24s.
        - OBS: adicionar mais camadas de convolução pode melhorar a performance.

    - Terceiro teste: foi feita uma troca entres as camadas de convolução, primeiro vem a camada com 16 filtros e depois a camada com 32.
        - Acurácia no conjunto de treinamento: 63%
        - Acurácia no conjunto de testes: 63%.
        - Duração do treinamento: 2m 24s.
        - OBS: aumentar os filtros a cada camada pode ser uma boa técnica.

    - Quarto teste: foi adicionada mais uma camada oculta com 64 neurônios após a convolução.
        - Acurácia no conjunto de treinamento: 65%
        - Acurácia no conjunto de testes: 57%.
        - Duração do treinamento: 2m 24s.

    - Quinto teste: foi adicionada a função de normalização do batch entre as camadas de convolução.
        - Acurácia no conjunto de treinamento: 85%
        - Acurácia no conjunto de testes: 63%.
        - Duração do treinamento: 4m 24s.
        - OBS: uma acurácia muito mais alta no conjunto de treinamento que no conjunto de teste, sinal de overfitting.

    - Sexto teste: foi adicionada a função Dropout após as camadas de convolução.
        - Acurácia no conjunto de treinamento: 77%
        - Acurácia no conjunto de testes: 68%.
        - Duração do treinamento: 4m 58s.

- CIFAR-100:
    - Primeiro teste: foi utilizada a configuração dada no trabalho para o conjunto cifar-10.
        - Acurácia no conjunto de treinamento: 1%
        - Acurácia no conjunto de testes: 1%
        - Duração do treinamento: 2m 2s.

    - Segundo teste: foi adicionada uma camada de convolução com 64 filtros, melhorando bastante a acurácia.
        - Acurácia no conjunto de treinamento: 71%
        - Acurácia no conjunto de testes: 21%
        - Duração do treinamento: 7m 54s.

    - Terceiro teste: foi adicionada uma camada oculta de 128 neurônios.
        - Acurácia no conjunto de treinamento: 75%
        - Acurácia no conjunto de testes: 23%
        - Duração do treinamento: 9m 49s.

    - Quarto teste: foi adicionada a função de Dropout após as camadas de convolução.
        - Acurácia no conjunto de treinamento: 56%
        - Acurácia no conjunto de testes: 26%
        - Duração do treinamento: 10m 9s.

    - Quinto teste: foi adicionado normalização do batch entre as camadas de convolução.
        - Acurácia no conjunto de treinamento: 44%
        - Acurácia no conjunto de testes: 31%
        - Duração do treinamento: 12m 19s.

- MNIST:
    - Primeiro teste: foi utilizado o modelo dado na aula de laboratório.
        - Acurácia no conjunto de treinamento: 98%
        - Acurácia no conjunto de testes: 97% no conjunto de testes.
        - Duração do treinamento 1m 16s.

    - Segundo teste: foi adicionada uma camada de convolução com 32 filtros após a já existente com 16 filtros.
        - Acurácia no conjunto de treinamento 99%
        - Acurácia no conjunto de testes: 98%
        - Duração do treinamento: 2m 50s.

    - Terceiro teste: foi adicionada uma camada oculta após as camadas de convolução, mas não ocorreram mudanças no resultado.
        - Acurácia no conjunto de treinamento 99%
        - Acurácia no conjunto de testes: 98%
        - Duração do treinamento: 3m 24s.

    - Quarto teste: pesquisei sobre a função Dropout que ajuda com o problema de overfitting e apliquei no modelo, mas não ocorreram mudanças no resultado
        - Acurácia no conjunto de treinamento: 99%
        - Acurácia no conjunto de testes: 98%
        - Duração 3m 30s.

- Fashion-MNIST:
    - Primeiro teste: foi utilizada a mesma configuração do modelo do conjunto MNIST.
        - Acurácia no conjunto de treinamento: 90%
        - Acurácia no conjunto de testes: 87%
        - Duração do treinamento: 1m 16s.

    - Segundo teste:foi adicionada uma camada de convolução de 32 filtros após a já existente de 16 filtros, e também foi adicionada uma camada oculta com 64 neurônios.
        - Acurácia no conjunto de treinamento: 90%
        - Acurácia no conjunto de testes: 80%
        - Duração do treinamento: 3m 23s.

    - Terceiro teste: foi adicionado normalização do batch entre as camadas de convolução.
        - Acurácia no conjunto de treinamento: 97%
        - Acurácia no conjunto de testes: 91%.
        - Duração do treinamento: 4m 27s.

    - Quarto teste: foi adicionado um Dropout no final das camadas de convolução.
        - Acurácia no conjunto de treinamento: 95%
        - Acurácia no conjunto de testes: 92%.
        - Duração do treinamento: 4m 44s.

### Classificação de complexidade

- MNIST
    - É o dataset mais fácil, por ter só um canal de cor e também pelas imagens serem dígitos manuscritos, ou seja, não são imagens muito detalhadas. Também é interessante notar que mesmo com uma configuração simples, o modelo alcançou uma acurácia alta.

- Fashion-MNIST
    - É mais difícil que o MNIST, as imagens são artigos de moda e algumas são bem parecidas, por exemplo, pullover e coat, ou sneaker e ankle boots. Mas por ter somente um canal de cor e os objetos estarem centralizados, ainda não é tão difícil.

- CIFAR-10
    - Este dataset já é bem mais complicado que os dois primeiros, por serem imagens coloridas, ou seja, com três canais de cores, com maior resolução (32x32), com fundo mais ruidoso, e os objetos estarem menos centralizados.

- CIFAR-100
    - O mais difícil dos quatro, imagens coloridas, resolução 32x32, fundo ruidoso, objetos menos centralizados, e acima de tudo, 100 classes com menos amostras por classe que os outros datasets.
