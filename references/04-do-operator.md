# Operador do (intervencao)

## Problema exemplo

Queremos saber se vacinacao reduz infeccao. Em dados observacionais, pessoas que escolhem se vacinar podem ser diferentes das que nao se vacinam em comportamento, acesso a saude ou exposicao ao risco.

## Pergunta causal

O que aconteceria com a infeccao se pudessemos intervir e fixar a vacinacao, em vez de apenas observar quem decidiu se vacinar?

## Ideia

`do(X=x)` representa uma intervencao que fixa `X` em `x`, quebrando o mecanismo causal que normalmente determinaria `X`.

## Diferenca chave

Observar `vacinacao=1` nao e a mesma coisa que impor `do(vacinacao=1)`. O operador `do` formaliza essa diferenca entre ver e fazer.

## Erro comum

Interpretar uma diferenca observada entre vacinados e nao vacinados como se ela ja representasse, por si so, o efeito de uma politica de vacinacao.

## Referencias

- Pearl, Causality, cap. sobre intervencoes
- Hernan & Robins, g-formula e intervencoes
