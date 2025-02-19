# RPVMMGurobiModel

## Este repositório compõe parte do trabalho desenvolvido na disciplina de Resolução de Problemas via Modelagem Matemática (Unifesp - SJC). O trabalho é baseado em um desafio proposto pela Renner para alocação de produtos de um armazém a caixas de demanda.

A pasta /src do projeto contém os dados apresentados pela Renner (caixas.csv e estoque.csv) e os demais arquivos Python para execução do modelo de otimização desenvolvido e do pré-processamento de dados.
O pré-processamento para seleção das $N$ primeiras caixas pode ser feito ao executar $python3 selection_box_id.py caixas.csv caixas_selected.csv N$ e, por fim selecionando do estoque somente os dados necessários para o problema com as caixas escolhidas: $python3 filter_sku.py caixas_selected.csv estoque.csv estoque_selected.csv$. Com esses dois arquivos $caixas_selected.csv$ e $estoque_selected.csv$, o modelo implementado com o Gurobi pode ser executado via $python3 main.py$. É importante ressaltar que os testes realizados com o modelo foram feitos com uma licença acadêmica.
