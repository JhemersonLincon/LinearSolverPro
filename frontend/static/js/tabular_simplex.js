function criarTabelaInteracoes() {
    var data = window.location.search;
    var params = new URLSearchParams(data);

    try {
        var dados = JSON.parse(decodeURIComponent(params.get("Iteracoes")));
        var resultado = JSON.parse(decodeURIComponent(params.get("resultado")));

        var ladoE = JSON.parse(decodeURIComponent(params.get("ladoE")));
        var ladoD = JSON.parse(decodeURIComponent(params.get("ladoD")));
        console.log(dados);
        console.log(resultado);
        console.log(ladoE)
        console.log(ladoD)
        
        const container = document.getElementById('tabela-container');

        // Iterar sobre os conjuntos de interações
        dados.forEach((interacoes, index) => {
            const tabela = document.createElement('table');
            tabela.setAttribute("class", "table table-hover table-bordered");
            tabela.setAttribute("id", `tabela_${index}`);

            // Adicionar título
            const titulo = document.createElement('h2');
            titulo.textContent = `Conjunto de Iterações ${index + 1}`;
            container.appendChild(titulo);

            // Criar cabeçalho
            const cabecalho = tabela.createTHead();
            const linhaCabecalho = cabecalho.insertRow();
            for (let i = 0; i < interacoes[0].length; i++) {
                const celulaCabecalho = linhaCabecalho.insertCell();
                celulaCabecalho.style.textAlign = 'center';
                celulaCabecalho.style.fontWeight = 'bolder';
                celulaCabecalho.style.fontSize = '22px';
                celulaCabecalho.style.color = '#fff';
                celulaCabecalho.textContent = `x${i + 1}`;
            }

            // Adicionar linhas de dados
            const corpo = document.createElement('tbody');
            interacoes.forEach(interacao => {
                const linha = corpo.insertRow();
                interacao.forEach(valor => {
                    const celula = linha.insertCell();
                    celula.textContent = valor;
                });
            });

            tabela.appendChild(corpo);
            container.appendChild(tabela);
        });

        // Adicionar resultados como divs
        const resultadoContainer = document.createElement('div');
        resultadoContainer.setAttribute("id", "resultado");

        for (let i = 0; i < resultado.length; i++) {
            let elementos = document.createElement('div');
            elementos.setAttribute("class", `resultado_${i}`);
            if (i < resultado.length - 1) {
                elementos.textContent = `x${i + 1} = ${resultado[i]}`;
            } else {
                elementos.textContent = `Z* = ${resultado[i]}`;
            }
            resultadoContainer.appendChild(elementos);
        }

        container.appendChild(resultadoContainer);

    } catch (e) {
        console.error("Erro ao analisar JSON: ", e);
    }
}

// Chamar a função após definir
criarTabelaInteracoes();



function plotarFuncoesRestricao({matrizPrincipal, vetorDireito}) {
    console.log(matrizPrincipal);

    google.charts.setOnLoadCallback(drawChart);

    function drawChart() {
        const constraints = [];
        for (let i = 0; i < matrizPrincipal.length; i++) {
            constraints.push({a: matrizPrincipal[i][0], b: matrizPrincipal[i][1], c: vetorDireito[i], label: `Restrição ${i+1}`});
        }

        // Cálculo dos pontos das funções de restrição
        function calculateConstraintPoints(a, b, c) {
            const points = [];
            const pointX = [];
            for (let x = -10; x <= 10; x += 0.5) {
                pointX.push(x);
            }
            const pointY = [];
            for (let y = -10; y <= 10; y += 0.5){
                pointY.push(y);
            }
            
            for(let i = 0; i <= pointX.length; i += 1){
                for(let j = 0; j <= pointY.length; j += 1){
                    const z = a * pointX[i] + b * pointY[j];
                    if(z == c) {
                        points.push({x: pointX[i], y: pointY[j]});
                    }
                }
            }
            console.log("equação: a: %d b:%d", a, b);
            console.log(points);
            return points;
        }
    }
}