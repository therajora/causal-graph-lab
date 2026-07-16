# DAGs e SCM (visao inicial)

## Problema exemplo

Suponha que queremos estudar a relacao entre horas de estudo e aprovacao. Alunos com maior preparo previo podem estudar de forma diferente e tambem ter maior chance de aprovacao.

## Ideia

Um DAG causal representa suposicoes causais entre variaveis. Um SCM (Structural Causal Model) formaliza essas relacoes com mecanismos estruturais e ruido exogeno.

## Leitura do exemplo

Um grafo pode representar que preparo previo afeta horas de estudo e aprovacao, enquanto estudo tambem afeta aprovacao. Esse tipo de desenho ajuda a explicitar onde pode haver confundimento.

## Termos

- Pais de Y: variaveis com setas apontando para Y
- Descendentes: alcancaveis por caminhos direcionados a partir de um no
- Confundidor: causa comum de X e Y

## Referencias

- Pearl, Causality, cap. 1-3
- Peters et al., Elements of Causal Inference, cap. 1-2
