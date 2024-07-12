// Vetor (lista)
vendas = [];

// Função para obter todas as vendas
function listar(){

    fetch('http://localhost:8080/listar')
    .then(obj => obj.json())
    .then(obj => {
        // Enviar objetos para a lista (vetor)
        vendas = obj;

        // Atualizar a tabela
        atualizarTabela();
    })

}

// Executar função
listar();

// Função para atualizar a tabela
function atualizarTabela(){

    // Obter o id tabela
    let tabela = document.getElementById("tabela");

    // Limpar estrutura da tabela
    tabela.innerHTML = "";

    // Laço de repetição
    for(let indice = 0; indice < vendas.length; indice++){

        // Criar uma nova linha de tabela (tr)
        let linha = tabela.insertRow(-1);

        // Criar seis colunas (td)
        let colunaProduto = linha.insertCell(0);
        let colunaMarca = linha.insertCell(1);
        let colunaTotal = linha.insertCell(2);
        let colunaQuantidade = linha.insertCell(3);
        let colunaVendedor = linha.insertCell(4);
        let colunaRemover = linha.insertCell(5);

        // Atribuir informações
        colunaProduto.innerHTML = vendas[indice].nome;
        colunaMarca.innerHTML = vendas[indice].marca;
        colunaTotal.innerHTML = vendas[indice].total;
        colunaQuantidade.innerHTML = vendas[indice].quantidade;
        colunaVendedor.innerHTML = "--";
        colunaRemover.innerHTML = `<button class="btn btn-danger" onClick="remover(${indice})">Remover</button>`;

    }

}

// Função para cadastrar vendas
function cadastrar(){

    // Obter os dados da venda
    let produto = document.getElementById("produto");
    let quantidade = document.getElementById("quantidade");
    let marca = document.getElementById("marca");
    let total = document.getElementById("total");

    // Criar objeto
    let obj = {
        "nome":produto.value,
        "quantidade":quantidade.value,
        "marca":marca.value,
        "total":total.value
    }

    // Adicionar objeto na lista
    vendas.push(obj);

    // Atualizar a tabela
    atualizarTabela();

    // Realizar requisição
    fetch('http://localhost:8080/cadastrar',{
        method:'POST',
        headers:{'Content-Type':'application/json'},
        body:JSON.stringify(obj)
    })
}

// Função para remover vendas
function remover(indice){

    // Remover da lista
    vendas.splice(indice, 1);

    // Requisição para a API
    fetch('http://localhost:8080/remover/'+indice, {
        method:'DELETE'
    })

    // Atualizar a tabela
    atualizarTabela();

}