import sys
from collections import defaultdict

def resolver_fidelidad():
    datos = sys.stdin.read().split()
    if not datos: return
    
    N = int(datos[0])
    M = int(datos[1])
    S = int(datos[2])
    
    idx = 3
    terminal_a_socio = {}
    for _ in range(M):
        p = int(datos[idx])
        t = int(datos[idx+1])
        terminal_a_socio[t] = p
        idx += 2
        
    clientes_por_socio = {p: defaultdict(int) for p in range(1, N + 1)}
    
    for _ in range(S):
        if idx >= len(datos): break
        c = int(datos[idx])
        t = int(datos[idx+1])
        idx += 2
        if t in terminal_a_socio:
            p = terminal_a_socio[t]
            clientes_por_socio[p][c] += 1
            
    for p in range(1, N + 1):
        if not clientes_por_socio[p]:
            print(f"{p} -1")
        else:
            # Ordena por cantidad desc, luego ID de cliente asc
            mejor_cliente = min(
                clientes_por_socio[p].keys(),
                key=lambda k: (-clientes_por_socio[p][k], k)
            )
            print(f"{p} {mejor_cliente}")

if __name__ == '__main__':
    resolver_fidelidad()