# Design: aprofundamento conceitual das referencias

## Resumo

Esta iteracao aprofunda os textos em `references/` para que eles expliquem melhor ideias de modelagem causal sem aumentar demais a complexidade tecnica. A meta nao e transformar as referencias em capitulos formais, mas fazer com que cada texto ensine o leitor a pensar causalmente com mais clareza.

## Objetivo

As referencias devem ajudar um leitor leigo a:

- entender por que modelagem causal nao e apenas olhar correlacoes;
- perceber que um grafo causal expressa hipoteses sobre como o mundo funciona;
- identificar perguntas importantes antes de aceitar uma conclusao causal;
- ganhar mais intuicao conceitual sem depender de formalismo pesado.

## Problema Atual

O material atual ja e claro e enxuto, mas ainda funciona mais como nota resumida do que como trilha de raciocinio. Em alguns arquivos, o leitor recebe a definicao do conceito sem antes sentir com nitidez:

- qual problema aquele conceito tenta resolver;
- por que uma intuicao ingenua pode falhar;
- o que estamos assumindo ao construir um modelo causal;
- como o conceito muda a leitura de um caso realista.

## Direcao Recomendada

As referencias devem passar a usar uma estrutura em camadas:

1. pergunta inicial simples;
2. mini-caso concreto;
3. leitura intuitiva do problema;
4. explicacao do conceito de modelagem causal;
5. erro comum ou interpretacao apressada;
6. fechamento com o que o conceito permite enxergar melhor.

Essa estrutura foi escolhida porque aprofunda o raciocinio sem afastar o leitor com excesso de linguagem tecnica logo no inicio.

## Principio Central

O eixo conceitual desta iteracao e apresentar `modelagem causal` como a pratica de tornar explicitas as suposicoes sobre um problema. Em linguagem acessivel, isso significa mostrar que:

- um modelo causal nao e so uma figura organizada;
- cada seta representa uma aposta interpretativa sobre influencia;
- o que entra e o que fica fora do modelo importa;
- uma conclusao causal depende das hipoteses representadas.

Em vez de tratar o modelo como formalismo abstrato, o texto deve tratar o modelo como ferramenta para pensar melhor.

## Estrutura Recomendada por Arquivo

Cada arquivo em `references/` deve seguir, quando fizer sentido, esta ordem:

### 1. Pergunta de abertura

Abrir com uma pergunta curta e concreta, por exemplo:

- como saber se duas coisas que aparecem juntas realmente tem relacao causal;
- o que posso estar deixando de fora ao comparar dois grupos;
- por que observar nao e o mesmo que intervir.

### 2. Situacao concreta

Introduzir um caso curto e facilmente compreensivel. O caso serve para dar corpo ao problema antes da definicao conceitual.

### 3. Leitura intuitiva

Explicar o problema em linguagem comum, com foco no raciocinio, nao no jargao. Aqui o leitor deve sentir por que a pergunta importa.

### 4. Conceito de modelagem causal

Explicar como aquele topico ajuda a organizar hipoteses sobre o problema. Esta secao deve enfatizar perguntas como:

- o que estou assumindo quando desenho esse grafo;
- quais influencias estou representando;
- quais caminhos podem explicar a associacao observada;
- o que o modelo me ajuda a enxergar que uma tabela simples nao mostra.

### 5. Erro comum

Apontar uma leitura intuitiva, mas equivocada, que o leitor poderia fazer. Isso reforca a funcao do conceito como ferramenta de correcao de raciocinio.

### 6. Fechamento

Encerrar resumindo o ganho conceitual: o que ficou mais claro e que tipo de erro o conceito ajuda a evitar.

## Aplicacao por Arquivo

### `01-dags-and-scm.md`

Deve explicar DAG e SCM como representacoes de mecanismos possiveis, nao apenas como terminologia tecnica. O foco e fazer o leitor perceber que desenhar um DAG significa assumir uma historia causal sobre o problema.

Perguntas que devem aparecer:

- o que significa dizer que uma variavel influencia outra;
- por que nem toda associacao merece uma seta;
- qual a diferenca entre organizar variaveis e modelar um mecanismo.

### `02-d-separation.md`

Deve mostrar d-separation como ferramenta de leitura de caminhos, nao como regra simbolica seca. O texto precisa enfatizar a intuicao de caminhos abertos e bloqueados como formas possiveis ou impossiveis de circulacao de informacao estatistica.

### `03-backdoor.md`

Deve aprofundar a ideia de confundimento e mostrar que ajuste nao e um truque mecanico. Ajustar significa tentar comparar grupos de forma mais justa com base em uma hipotese causal sobre causas comuns.

Perguntas que devem aparecer:

- que tipo de comparacao observacional pode ser injusta;
- de onde pode vir uma associacao enganosa;
- por que ajustar depende de saber o que precisa ser bloqueado.

### `04-do-operator.md`

Deve apresentar o operador `do` como mudanca de perspectiva: sair de "quem aconteceu de receber a exposicao" para "o que mudaria se eu fixasse essa exposicao". A prioridade e deixar clara a diferenca entre observar escolhas e imaginar uma intervencao.

## Tom e Linguagem

Os textos devem:

- usar frases curtas e diretas;
- introduzir termos tecnicos apenas depois da intuicao;
- evitar excesso de simbolos e notacao;
- tratar o leitor como iniciante inteligente, nao como especialista;
- aprofundar por meio de perguntas e explicacoes, nao por densidade terminologica.

## Fora de Escopo

Nesta iteracao, as referencias nao devem:

- virar textos longos demais;
- depender de matematica formal para sustentar a intuicao principal;
- cobrir tecnicas avancadas fora do escopo atual do repositorio;
- prometer exaustividade teorica.

## Qualidade Esperada

Ao final, as referencias devem:

- ficar mais investigativas e menos enciclopedicas;
- mostrar que modelagem causal e um modo de organizar suposicoes;
- ajudar o leitor a formular perguntas melhores sobre causalidade;
- conectar conceito, problema e interpretacao de forma mais natural.

## Decisao Final

A proxima iteracao de `references/` deve aprofundar a explicacao de modelagem causal com linguagem acessivel e estrutura guiada por perguntas. O leitor deve sair de cada texto nao apenas sabendo um termo novo, mas entendendo melhor que tipo de problema causal aquele conceito ajuda a pensar.
