function agrupar() {
    fetch('/agrupar', { method: 'POST' })
    .then(response => response.json())
    .then(data => {
        const tbody = document.querySelector("#tabela tbody");
        tbody.innerHTML = "";  // limpa tabela
        data.forEach(d => {
            const row = `<tr>
                <td>${d.Nome}</td>
                <td>${d.Presenca}</td>
                <td>${d.NotaMedia}</td>
                <td>${d.Participacao}</td>
                <td>${d.TarefasEntregues}</td>
                
            </tr>`;
            tbody.innerHTML += row;
        });
    });
}

function adicionarEstudante() {
    const nome = document.getElementById('nome').value;
    const presenca = document.getElementById('presenca').value;
    const nota = document.getElementById('nota').value;
    const participacao = document.getElementById('participacao').value;
    const tarefas = document.getElementById('tarefas').value;

    fetch('/adicionar', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            nome, presenca, nota, participacao, tarefas
        })
    })
    .then(response => response.json())
    .then(data => atualizarTabelaGrafico(data));

    // Limpar campos
    document.getElementById('nome').value = '';
    document.getElementById('presenca').value = '';
    document.getElementById('nota').value = '';
    document.getElementById('participacao').value = '';
    document.getElementById('tarefas').value = '';
}

window.onload = function() {
    agrupar();           // tabela inicial
    atualizarGrafico();  // gráfico inicial
};


function atualizarGrafico() {
    fetch('/grafico')
    .then(response => response.json())
    .then(data => {
        const ctx = document.getElementById('grafico').getContext('2d');
        if (window.myChart) window.myChart.destroy();

        window.myChart = new Chart(ctx, {
            type: 'scatter',
            data: {
                datasets: [{
                    label: 'Estudantes',
                    data: data.map(d => ({x: d.Presenca, y: d.NotaMedia})),
                    backgroundColor: data.map(d => d.Cluster == 0 ? 'red' : d.Cluster == 1 ? 'blue' : 'green')
                }]
            },
            options: {
                scales: {
                    x: { title: { display: true, text: 'Presença (%)' } },
                    y: { title: { display: true, text: 'Nota Média' } }
                }
            }
        });
    });
}


function atualizarTabelaGrafico(data) {
    const tbody = document.querySelector("#tabela tbody");
    tbody.innerHTML = "";
    let cores = [];
    data.forEach(d => {
        const row = `<tr>
            <td>${d.Nome}</td>
            <td>${d.Presenca}</td>
            <td>${d.NotaMedia}</td>
            <td>${d.Participacao}</td>
            <td>${d.TarefasEntregues}</td>
            
        </tr>`;
        tbody.innerHTML += row;
        cores.push(d.Cluster == 0 ? 'red' : d.Cluster == 1 ? 'blue' : 'green');
    });

    const ctx = document.getElementById('grafico').getContext('2d');
    if (window.myChart) window.myChart.destroy();
    window.myChart = new Chart(ctx, {
        type: 'scatter',
        data: {
            datasets: [{
                label: 'Estudantes',
                data: data.map(d => ({x: d.Presenca, y: d.NotaMedia})),
                backgroundColor: cores
            }]
        },
        options: {
            scales: {
                x: { title: { display: true, text: 'Presença (%)' } },
                y: { title: { display: true, text: 'Nota Média' } }
            }
        }
    });
}
