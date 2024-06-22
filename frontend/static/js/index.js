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

// Exemplo de uso
document.addEventListener('DOMContentLoaded', function() {
    const matrizPrincipal = [[2, 4], [4,2], [5,6]];
    const vetorDireito = [7, 5, 20];
    plotarFuncoesRestricao({matrizPrincipal, vetorDireito});
});