FastAPI na prática.

Caso real e funcional, no qual um banco de dados fornece dados para outro banco de dados e cria as tabelas se necessários nesse banco de dados secundário.

São dois bancos de dados Postgres Banco Bruto com todos os dados metereológicos e o Banco Zerado, que vai receber periodicamente os novos dados para exibir e editar em um sistema interno aqui na instituição IDR-Paraná.

Por enquanto é apenas isso que a api faz, serão acrescentadas outras funcionalidades no futuro, e a versão final vai estar disponível aqui no Git sem as senhas e tokens utilizados.

Passo a passo para reproduzir e testar esse código.

1-Baixar o Postgres 9.5.25 (pode funcionar em outras versões mais atualizadas)

1.5- Criar um banco pode ser uma tarefa um pocuo complicada e provavelmente precisará ser feita pelo terminal (não se preocupe, o GPT pode te ajudar)

2-Baixar o DBeaver e fazer a conexão do banco 

3-Ter o Python instalado < 10.6 e criar um ambiente virtual venv, e depois rodar " pip install -r requeriments.txt "

Dicas e sugestões, por favor entre em contato por email: gustavo.odenath@edu.unifil.br
