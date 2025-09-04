
Este projeto é um sistema de votação interativo feito em Python, ideal para simular eleições simples com múltiplos candidatos, incluindo regras de desempate e segundo turno.

 Funcionalidades
Cadastro de candidatos com validação de nome (não aceita números).
Votação com controle por código do candidato.
Exibição dos resultados da votação.
Segundo turno automático em caso de empate.
Desempate inteligente:
2 candidatos empatados: sorteio por cara ou coroa.
3 ou mais candidatos empatados: sorteio por número aleatório (de 1 a 100).

 Como usar
Execute o script Python.
Cadastre pelo menos dois candidatos.
Digite 'L' para iniciar a votação.
Vote digitando o número do candidato.
Digite 0 para encerrar a votação.
Se houver empate, o sistema inicia automaticamente o segundo turno.
Persistindo o empate, o sistema realiza o desempate conforme as regras.
 Regras de Desempate
Empate entre dois candidatos:

Cada um escolhe entre "cara" ou "coroa".
Uma moeda é jogada e o lado sorteado define o vencedor.
Empate entre três ou mais candidatos:

Cada candidato recebe um número aleatório entre 1 e 100.
O candidato com o maior número vence.
Os números sorteados são exibidos antes do resultado final.
Tecnologias Utilizadas
Python 3.x
Módulo random para sorteios
Estruturas: dict, list, while, if/else, try/except
 Requisitos
Python instalado na máquina
Terminal ou IDE para executar o script
 Licença
Este projeto é livre para uso educacional e pessoal.
