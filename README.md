# RPVMMGurobiModel

Este repositório compõe parte do trabalho desenvolvido na disciplina de **Resolução de Problemas via Modelagem Matemática** (Unifesp - SJC). O trabalho é baseado em um desafio proposto pela **Renner** para alocação de produtos de um armazém a caixas de demanda.

---

## Estrutura do Projeto

A pasta `/src` do projeto contém:

- **Dados fornecidos pela Renner**:
  - `caixas.csv`
  - `estoque.csv`

- **Arquivos Python**:
  - Códigos para execução do modelo de otimização.
  - Scripts para pré-processamento de dados.

---

## Pré-Processamento dos Dados

Para selecionar as **$N$ primeiras caixas**, execute o seguinte comando:

```bash
python3 selection_box_id.py caixas.csv caixas_selected.csv N
python3 filter_sku.py caixas_selected.csv estoque.csv estoque_selected.csv
```
## Execução do Modelo

```bash
python3 main.py
```
- **Observações**:
  - Os testes realizados com o modelo foram feitos utilizando uma licença acadêmica do Gurobi.
  - Certifique-se de ter o Gurobi instalado e configurado corretamente no ambiente de execução.
  - As principais funcionalidades do modelo (função objetivo e restrições) estão implementadas no arquivo `test_gurobi.py`.
