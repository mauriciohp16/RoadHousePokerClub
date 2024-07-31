// cep_lookup.js

function buscarEnderecoPorCep() {
    let cep = document.getElementById('cep').value.trim();

    if (cep.length === 8 && /^\d+$/.test(cep)) {
        let url = `https://viacep.com.br/ws/${cep}/json/`;

        fetch(url)
            .then(response => response.json())
            .then(data => {
                if (data.erro) {
                    console.error('CEP não encontrado.');
                } else {
                    document.getElementById('logradouro').value = data.logradouro || '';
                    document.getElementById('bairro').value = data.bairro || '';
                    document.getElementById('cidade').value = data.localidade || '';
                    document.getElementById('estado').value = data.uf || '';
                }
            })
            .catch(error => {
                console.error('Erro ao buscar endereço:', error);
            });
    } else {
        console.error('CEP inválido.');
    }
}

document.getElementById('cep').addEventListener('blur', buscarEnderecoPorCep);
