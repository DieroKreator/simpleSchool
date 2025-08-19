Quem fez cursos relacionados a usar ou testar uma API

Métodos mais frequentes

Método      Simples         Elaborada
Post        Incluir         Requisição que envia uma mensagem (body)
Get         Consultar       Requisição que envia parametros pela URL
Put         Alterar         Requisição que envia uma mensage (body)
                            se existir, sobrescreve todos os campos
                            se não existir, cria
Patch       Alterar Parcial Requisição que envia uma mensage (body)
                            se existir, sobrescreve apenas os campos informados
                            se não existir, informa mensagem de erro
Delete      Excluir         Requisição que envia parametros pela URL e exclui o registro

Próximo Release
- Separar esses endpoints em um Router (Roteador)
- Adicionar logging (autenticação)
- Trabalha com um banco de dados real
- Adicionar métodos Put, Patch e Delete
