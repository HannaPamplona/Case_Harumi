import gurobipy as gp
from gurobipy import GRB
import os

# Caminho da pasta de entrada
input_folder = "/temporario2/9717617/Input_1"

# Encontrar o arquivo .lp na pasta
lp_files = [f for f in os.listdir(input_folder) if f.endswith('.lp')]

if not lp_files:
    raise FileNotFoundError("Nenhum arquivo .lp encontrado na pasta Input_1")

# Usar o primeiro arquivo .lp encontrado (ou modifique para escolher um específico)
input_file = os.path.join(input_folder, lp_files[0])

# Extrair o nome base do arquivo (sem extensão)
base_name = os.path.splitext(lp_files[0])[0]

# Gerar nomes dos arquivos de saída baseados no nome do arquivo de entrada
output_file = os.path.join(input_folder, f"{base_name}_output.txt")
error_file = os.path.join(input_folder, f"{base_name}_error.txt")

print(f"Arquivos .lp encontrados: {lp_files}")
print(f"Arquivo de entrada selecionado: {input_file}")
print(f"Arquivo existe? {os.path.exists(input_file)}")

try:
    # Criar o ambiente Gurobi
    env = gp.Env() 

    # Carregar o modelo do arquivo LP
    model = gp.read(input_file, env=env)
    model.setParam(GRB.Param.TimeLimit, 18000)
    model.optimize()

    # Escrever a saída padronizada para qualquer status
    with open(output_file, "w", encoding="utf-8") as f:
        # Caso o modelo tenha solução viável
        if model.SolCount > 0:
            var_inteiras =sum (1 for v in model.getVars() if v.vType == 'I')
            var_binarias =sum (1  for v in model.getVars() if v.vType == 'B')
            var_reais = sum (1 for v in model.getVars() if v.vType == 'C')

            f.write(f"{model.numconstrs}\n")
            f.write(f"{var_inteiras}\n") 
            f.write(f"{var_binarias}\n")             
            f.write(f"{var_reais}\n")
            f.write(f"{model.objVal}\n")
            f.write(f"{model.MIPGap * 100:.2f}\n")
            f.write(f"{model.ObjBound}\n")
            f.write(f"{model.Runtime}\n")
            for v in model.getVars():
                f.write(f"{v.varName} = {v.x}\n")
        
        # Mensagem adicional para outros status
        if model.status == GRB.OPTIMAL:
            f.write("\nSolução ótima encontrada.\n")
        elif model.status == GRB.INFEASIBLE:
            f.write("\nO modelo é inviável.\n")
        elif model.status == GRB.UNBOUNDED:
            f.write("\nO modelo é ilimitado.\n")
        else:
            f.write(f"\nStatus do modelo: {model.status}\nNenhuma solução factível encontrada.\n")

except gp.GurobiError as e:
    with open(error_file, "w", encoding="utf-8") as f:
        f.write(f"Erro Gurobi: {str(e)}\n")

except Exception as e:
    with open(error_file, "w", encoding="utf-8") as f:
        f.write(f"Erro Geral: {str(e)}\n")
