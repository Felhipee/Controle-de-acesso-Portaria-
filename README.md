

<img src="https://github.com/Felhipee/Controle-de-acesso-Portaria-/assets/17773216/b96ae9ed-8324-4f1c-b57c-6489e273472b"
    alt="print_soft_kalunga">

<p align="left">

<h1>Um programa básico para controle de entradas em portaria desenvolvido em PyQt5, utilizando a linguagem de programação Python e o banco de dados SQLite.</h1> 
<h2>Transforme a gestão de acesso na empresa com nosso inovador sistema! </h2>
<strong><u>Cadastre motoristas e veículos com facilidade, tenha controle total e segurança.</u></strong> 
Agilidade e eficiência em cada entrada! 🚀

Segue abaixo para conhecer mais sobre as funções.

<strong>adicionar_dados(self):</strong> Permite ao usuário inserir informações sobre um veículo (nome, placa, CPF, data e tipo) na interface. 
Os dados são então adicionados à tabela na interface e ao banco de dados.

<strong>deletar_id(self):</strong> Permite ao usuário excluir registros com base nos IDs fornecidos. 
O usuário insere IDs separados por vírgulas na interface, e os registros correspondentes são removidos tanto da tabela quanto do banco de dados.

<strong>redefinir_ids(self):</strong> Remove todos os registros da tabela do banco de dados e redefine a sequência de IDs para começar em 1.

<strong>procurar_cpf_e_exibir_mensagembox(self, cpf_procurado) / search_cpf(self):</strong> Permite ao usuário buscar registros no banco de dados com base nos dígitos do CPF fornecidos. 
A busca é realizada ao clicar no botão "Procurar CPF" na interface.

<strong>salvar_dados_ods(self):</strong> Salva os dados do banco de dados em um arquivo ODS (OpenDocument Spreadsheet), que pode ser utilizado para criar relatórios. 
O relatório inclui informações sobre todos os registros, bem como a contagem de diferentes tipos de veículos.

<strong>sobre(self):</strong> Exibe uma messagebox com informações sobre o software, incluindo o criador, número de suporte, e-mail de suporte e versão do software. 
Essa função é acionada ao clicar no botão "Sobre" na interface.

<strong>atualizar_tabela(self):</strong> Limpa a tabela na interface e recarrega os dados do banco de dados, garantindo que a tabela exiba informações atualizadas.

<strong>atualizar_hora(self):</strong> Atualiza um campo de texto na interface com a hora atual. 
Esta função é chamada periodicamente para manter o campo de data/hora atualizado.

</p>

<p>Para instalar as bibliotecas necessárias, você pode usar o pip, que é o gerenciador de pacotes padrão do Python. 
Abra o terminal ou prompt de comando e execute os seguintes comandos:</p>

<pre>
pip install PyQt5
pip install easygui
pip install pyexcel-ods
pip install sqlite
</pre>

</body>

</html>
