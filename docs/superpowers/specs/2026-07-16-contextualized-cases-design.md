# Design: contextualizacao aplicada com casos curtos

## Resumo

Esta iteracao amplia a base didatica do `causal-graph-lab` adicionando contexto realista aos conceitos ja introduzidos. Em vez de apresentar apenas tecnicas abstratas com `X`, `Y` e `Z`, o repositorio passa a explicar cada ideia causal a partir de probleminhas concretos e curtos.

## Objetivo

Melhorar a compreensao conceitual do material atual por meio de exemplos narrativos que respondam perguntas como:

- por que tabagismo e cancer podem aparecer relacionados;
- como confundimento distorce uma associacao observada;
- o que significa intervir em vez de apenas observar;
- como cada tecnica se encaixa em um problema realista.

## Escopo

Esta iteracao cobre tres casos iniciais:

- tabagismo e cancer de pulmao;
- tratamento e recuperacao com gravidade previa;
- vacinacao e infeccao.

Cada caso deve ser curto, didatico e explicitamente conectado a um conceito central do repositorio.

## Estrutura Recomendada

Cada conceito relevante deve ganhar uma camada de contextualizacao composta por cinco elementos:

1. contexto do problema;
2. pergunta causal;
3. leitura causal do DAG em linguagem simples;
4. erro de interpretacao comum;
5. intuicao sobre a tecnica usada.

Essa estrutura deve aparecer principalmente em `references/`, `examples/` e `notebooks/`.

## Mudancas em Referencias

As notas teoricas deixam de ser apenas definicoes curtas e passam a abrir com um caso concreto. O texto teorico continua compacto, mas cada arquivo precisa responder:

- qual e o problema realista sendo discutido;
- onde esta o vies ou a ambiguidade causal;
- por que o conceito daquele arquivo ajuda.

Exemplos esperados:

- `03-backdoor.md` pode usar tabagismo e cancer para introduzir confundimento;
- `04-do-operator.md` pode usar vacinacao e infeccao para diferenciar observar e intervir.

## Mudancas em Exemplos

Os scripts em `examples/` devem usar nomes semanticos e pequenos enunciados em vez de apenas variaveis abstratas. O foco nao e realismo estatistico completo, mas clareza causal.

Diretrizes:

- imprimir a pergunta causal antes dos resultados;
- nomear variaveis de forma interpretavel;
- explicar em uma ou duas linhas por que o resultado ingenuo difere do ajustado quando houver confundimento.

## Mudancas em Notebooks

Os notebooks devem abrir com a pergunta causal do caso antes do codigo. O fluxo ideal e:

1. situacao concreta;
2. DAG verbal ou textual;
3. interpretacao causal;
4. pequeno experimento ou script relacionado;
5. ligacao com referencias teoricas.

Os notebooks nao precisam ficar longos. A prioridade e fazer a ponte entre intuicao, problema e tecnica.

## Casos Iniciais

### Caso 1: Tabagismo e cancer de pulmao

- Conceitos centrais: associacao vs causalidade, confundimento, ajuste.
- Uso principal: referencias de backdoor e exemplo executavel introdutorio.
- Pergunta causal: fumar aumenta o risco de cancer de pulmao ou estamos vendo apenas uma associacao enviesada?

### Caso 2: Tratamento e recuperacao

- Conceitos centrais: vies de selecao de tratamento, gravidade previa, comparacao injusta.
- Uso principal: notebook ou nota curta sobre por que grupos observacionais podem ser enganosos.
- Pergunta causal: o tratamento funciona ou os pacientes tratados ja eram diferentes no inicio?

### Caso 3: Vacinacao e infeccao

- Conceitos centrais: intervencao, operador `do`, diferenca entre observar e fazer.
- Uso principal: nota teorica e notebook curto.
- Pergunta causal: o que mudaria se pudessemos intervir na vacinacao, em vez de apenas observar quem escolheu se vacinar?

## Fora de Escopo

Nesta iteracao, o projeto nao deve:

- prometer fidelidade epidemiologica completa;
- introduzir muitos casos ao mesmo tempo;
- transformar cada topico em um artigo longo;
- ampliar substancialmente a API do pacote Python.

## Qualidade Esperada

O resultado deve:

- ser mais facil de ler para quem esta chegando no assunto;
- tornar cada tecnica rastreavel a uma pergunta concreta;
- reduzir o uso excessivo de notacao abstrata sem contexto;
- manter exemplos curtos e consistentes com a proposta didatica do repositorio.

## Decisao Final

A proxima iteracao do `causal-graph-lab` deve introduzir contextualizacao aplicada por meio de varios casos curtos. A prioridade e transformar cada conceito em uma resposta a um problema causal reconhecivel, sem perder simplicidade.
