# Backdoor (ajuste)

## Problema exemplo

Queremos entender se tabagismo aumenta o risco de cancer de pulmao. Em dados observacionais, fumantes podem diferir de nao fumantes em outros fatores relevantes, como predisposicao genetica, ambiente ou exposicoes associadas ao habito.

## Pergunta causal

O efeito observado entre fumar e cancer representa um efeito causal ou esta misturando influencias de causas comuns?

## Ideia

O criterio de backdoor identifica conjuntos de ajuste que bloqueiam caminhos espurios entre exposicao e desfecho iniciando com uma seta entrando na exposicao.

## Intuicao

Se existir um fator que influencia tanto a chance de fumar quanto a chance de desenvolver cancer, comparar fumantes e nao fumantes sem ajuste pode ser enganoso. Ajustar por confundidores busca tornar a comparacao mais justa.

## Erro comum

Ver associacao entre tabagismo e cancer e concluir imediatamente que toda a associacao estimada em um banco observacional corresponde ao efeito causal.

## Referencias

- Pearl, Causality, criterio de backdoor
- Hernan & Robins, What If (ajuste e confundimento)
