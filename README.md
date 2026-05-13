# Case_Harumi

**Autor:** Hanna Pamplona Hortencio  
**Data:** 13/05/2026  

---

## Descrição do Projeto

Este repositório contém a solução para um **problema de roteirização de técnicos** (Workforce Scheduling and Routing Problem – WSRP), onde uma empresa precisa atribuir clientes a técnicos e definir a sequência de visitas, respeitando:

- Capacidade máxima de 8 horas diárias por técnico;
- Tempo máximo por rota;
- Múltiplos pontos de partida;
- Necessidade de múltiplos dias.

Foram implementadas **duas abordagens**:

1. **Modelo exato** com o solver Gurobi (sem sucesso para encontrar solução factível em 1 hora);
2. **Heurística Clarke & Wright adaptada** (entregou solução factível).
