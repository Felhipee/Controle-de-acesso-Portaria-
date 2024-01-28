Um programa básico para controle de entradas em portaria desenvolvido em PyQt5, utilizando a linguagem de programação Python e o banco de dados SQLite. 
Transforme a gestão de acesso na empresa com nosso inovador sistema! 
Cadastre motoristas e veículos com facilidade, tenha controle total e segurança. 
Agilidade e eficiência em cada entrada!

Segue abaixo para connhecer mais sobre as funçoes.


adicionar_dados(self): Permite ao usuário inserir informações sobre um veículo (nome, placa, CPF, data e tipo) na interface. 
Os dados são então adicionados à tabela na interface e ao banco de dados.

deletar_id(self): Permite ao usuário excluir registros com base nos IDs fornecidos. 
O usuário insere IDs separados por vírgulas na interface, e os registros correspondentes são removidos tanto da tabela quanto do banco de dados.

redefinir_ids(self): Remove todos os registros da tabela do banco de dados e redefine a sequência de IDs para começar em 1.

procurar_cpf_e_exibir_mensagembox(self, cpf_procurado) / search_cpf(self): Permite ao usuário buscar registros no banco de dados com base nos dígitos do CPF fornecidos. 
A busca é realizada ao clicar no botão "Procurar CPF" na interface.

salvar_dados_ods(self): Salva os dados do banco de dados em um arquivo ODS (OpenDocument Spreadsheet), que pode ser utilizado para criar relatórios. 
O relatório inclui informações sobre todos os registros, bem como a contagem de diferentes tipos de veículos.

sobre(self): Exibe uma messagebox com informações sobre o software, incluindo o criador, número de suporte, e-mail de suporte e versão do software. 
Essa função é acionada ao clicar no botão "Sobre" na interface.

atualizar_tabela(self): Limpa a tabela na interface e recarrega os dados do banco de dados, garantindo que a tabela exiba informações atualizadas.

atualizar_hora(self): Atualiza um campo de texto na interface com a hora atual. 
Esta função é chamada periodicamente para manter o campo de data/hora atualizado.

