from flask import Flask
from flask import request
from flask import jsonify
import json
from flask import render_template
from Metodos.DualSimplexMethod import DualSimplexMethod
from Metodos.MethodSimplex import MethodSimplex
app = Flask(__name__, template_folder="../frontend/templates", static_folder="../frontend/static")

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/tabela_retricoes", methods=["GET"])
def tabela_restricoes():
    objetivo = request.args.get('objetivo')
    metodo = request.args.get('metodo')
    num_variaveis = request.args.get('num_variaveis')
    num_restricoes = request.args.get('num_restricoes')
    
    return render_template("tabela_restricoes.html",objetivo=objetivo, metodo=metodo, num_variaveis=num_variaveis, num_restricoes=num_restricoes)
    
@app.route("/simplexMethod")
def simplex_area():
    return render_template("index.html")

@app.route("/plot")
def plot():
    return render_template("plot.html")


@app.route("/simplexMethod", methods=["POST"] )
def prog_linear():
    response = request.get_json()
    
    funçãoZ = response["funcao"]
    minMax = response["minMax"]
    ladoE = response["ladoEsquerdo"]
    restrições = response["restricoes"]
    ladoD = response["ladoDireito"]
    
    print(f"Função Z: {funçãoZ}\n")
    print(f"MinMax: {minMax}")
    print(f"Lado E: {ladoE}\n")
    print(f"Restrições: {restrições}")
    print(f"Lado D: {ladoD}\n")
    
    if minMax == "Max":
        result = MethodSimplex(ladoE, restrições, ladoD, funçãoZ)
    else:
        result = DualSimplexMethod(ladoE, ladoD, funçãoZ)
        
    resposta_json = {
        "simplex":  result.metodoSimplex(),
        "simplex_inteiro": result.branch_and_bound()
    }
    
    # Verifica se há erro na resposta dos dados
    
    
    # Se não houver erro, retorna os dados normalmente
    return jsonify(resposta_json)

@app.route("/tabular_simplex")
def tabular_simplex():
    interação = request.args.get("Iteracoes") 
    resultado = request.args.get("resultado")
    print("Em interações_______________________________________________________________________________")
    print(interação)
    return render_template("tabular_Simplex.html", Interacoes=interação, resultado=resultado)



if __name__ == "__main__":
    app.run(debug=True, port=3000)
