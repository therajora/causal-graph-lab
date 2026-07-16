# Design: causal-graph-lab v1

## Resumo

`causal-graph-lab` sera um pacote e repositorio de estudo sobre grafos causais com foco didatico. A primeira versao nao prioriza uma biblioteca extensa nem uma API sofisticada. O objetivo inicial e organizar exemplos, conceitos fundamentais e referencias teoricas de forma progressiva, usando codigo apenas como apoio para exploracao e consolidacao do aprendizado.

## Objetivo

A v1 deve ajudar uma pessoa a:

- entender a intuicao por tras de grafos causais e modelos causais estruturais;
- estudar conceitos centrais como DAGs, d-separation, ajuste por backdoor e intervencoes;
- navegar por exemplos pequenos e legiveis;
- relacionar implementacoes simples com referencias teoricas conhecidas.

## Fora de Escopo

Nesta fase, o projeto nao deve:

- competir com bibliotecas causais maduras;
- implementar um conjunto grande de algoritmos de inferencia causal;
- depender cedo de integracoes complexas com ecossistemas externos;
- otimizar desempenho ou cobertura de casos avancados.

## Abordagem Recomendada

A v1 adota uma abordagem `didatica em camadas` com enfase em exemplos e estudo guiado:

1. conceitos apresentados em ordem progressiva;
2. exemplos pequenos e verificaveis;
3. referencias teoricas associadas a cada topico;
4. uma base de codigo minima, usada como apoio pedagogico.

Essa abordagem foi escolhida porque mantem o repositorio acessivel para estudo sem impedir que ele evolua depois para uma biblioteca mais robusta.

## Estrutura Inicial

O repositorio deve ser organizado em quatro areas:

- `notebooks/`: exploracao guiada dos conceitos e exemplos comentados;
- `examples/`: scripts pequenos, focados em uma tecnica ou ideia por vez;
- `references/`: notas curtas e bibliografia por topico;
- `src/causal_graph_lab/`: pacote Python minimo, com utilitarios simples para apoiar os exemplos quando necessario.

## Conteudo da V1

Os topicos iniciais da v1 devem cobrir:

- introducao a grafos causais;
- variaveis, arestas e interpretacao causal em DAGs;
- independencia condicional e intuicao de d-separation;
- ajuste por backdoor como primeira tecnica de identificacao;
- nocao introdutoria de intervencao com operador `do`.

Cada topico deve ter, sempre que fizer sentido:

- uma explicacao conceitual curta;
- um exemplo executavel ou notebook;
- pelo menos uma referencia teorica associada.

## Papel do Codigo

O codigo na v1 tem funcao de apoio didatico. Em vez de esconder a logica em uma API ampla, a implementacao deve deixar visiveis os passos importantes do raciocinio. Isso favorece o entendimento das tecnicas e reduz a distancia entre a teoria e a experimentacao pratica.

O pacote Python inicial pode conter apenas:

- estruturas basicas para representar grafos pequenos;
- funcoes utilitarias para exemplos;
- componentes minimos reutilizaveis entre notebooks e scripts.

## Dependencias

A v1 deve comecar com dependencias minimas. Bibliotecas externas de grafos, como `networkx`, podem ser avaliadas depois, mas nao sao obrigatorias no primeiro corte. A preferencia inicial e manter o projeto simples, legivel e facil de instalar.

## Qualidade e Validacao

Os artefatos da v1 devem seguir estes criterios:

- exemplos pequenos o suficiente para serem lidos sem esforco excessivo;
- notebooks com narrativa clara e progressiva;
- referencias teoricas explicitas, sem links soltos ou contexto ausente;
- codigo de apoio simples, testavel e coerente com o material de estudo.

## Caminho de Evolucao

Depois da v1, o projeto pode evoluir em tres direcoes:

- ampliar o pacote Python com algoritmos e abstracoes mais solidas;
- adicionar integracoes com bibliotecas de grafos e visualizacao;
- aprofundar tecnicas como frontdoor, identificacao e contrafactuais.

## Decisao Final

A primeira versao de `causal-graph-lab` sera um laboratorio de estudo centrado em exemplos, conceitos e referencias teoricas. O repositorio comeca simples, com codigo apenas onde ele melhora a compreensao do material.
