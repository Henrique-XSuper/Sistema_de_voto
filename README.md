# 🗳️ sistema de votação 

Este projeto é um sistema de votação interativo feito em Python, ideal para simular eleições simples com múltiplos candidatos, incluindo regras de desempate e segundo turno.

---
 ## ⚒️ Funcionalidades
- Cadastro de candidatos com validação de nome (não aceita números).
- Votação com controle por código do candidato.
- Exibição dos resultados da votação.
- Segundo turno automático em caso de empate.
- <br>
 Desempate inteligente:
- 2 candidatos empatados: sorteio por cara ou coroa.
- 3 ou mais candidatos empatados: sorteio por número aleatório (de 1 a 100).
---
## 🔎 Como usar
- Execute o script Python.
- Cadastre pelo menos dois candidatos.
- Digite 'L' para iniciar a votação.
- Vote digitando o número do candidato.
- Digite 0 para encerrar a votação.
- Se houver empate, o sistema inicia automaticamente o segundo turno.
-Persistindo o empate, o sistema realiza o desempate conforme as regras.

### Regras de Desempate: 
Empate entre dois candidatos:

Cada um escolhe entre "cara" ou "coroa". <br>
Uma moeda é jogada e o lado sorteado define o vencedor.<br>
Empate entre três ou mais candidatos:

Cada candidato recebe um número aleatório entre 1 e 100.<br>
O candidato com o maior número vence.<br>
Os números sorteados são exibidos antes do resultado final.<br>

---
## 💻 Tecnologias Utilizadas
Python 3. <br>
Módulo random para sorteios<br>
Estruturas: dict, list, while, if/else, try/except<br>
GoogleColab 

---
 ## ⚙️ Requisitos
Python 3 instalado na máquina <br>
Terminal ou IDE para executar o script<br>
ambiente de desenvolvimento como GoogleColab, júpiter, vs code/vs Studio
---
## 📝 Licença
Este projeto esta sobre a licença MIT.
