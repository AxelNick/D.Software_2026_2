# Informe Técnico

* **Nombre:** Axel Alberto Reyes Baldeón
* **Código:** 20200485B


## Problema 1: Enrutador para SPA

**Descripción del problema:** 

Para esta parte se armó un simulador de enrutamiento enfocado en una Single Page Application (SPA). El código básicamente compara una ruta dada (que puede incluir parámetros dinámicos con la sintaxis `:id`) con las transiciones que ingresa el usuario. Si halla una coincidencia, extrae los parámetros y los muestra en pantalla; si la ruta no calza con ninguna opción, devuelve el clásico error `404 Not Found`.

### Código

```python
import sys

def resolver_enrutador():
    lineas = sys.stdin.read().splitlines()
    if not lineas: return
    
    N = int(lineas[0].strip())
    rutas = []
    for i in range(1, N + 1):
        linea = lineas[i].strip()
        if not linea: continue
        partes = linea.split(' ', 1)
        ruta_path = partes[0]
        # Limpiamos el contenido por si vienen caracteres extraños copiados
        contenido = partes[1].split()[0] if len(partes) > 1 else ""
        rutas.append((ruta_path, contenido))
            
    M_idx = N + 1
    if M_idx >= len(lineas): return
    M = int(lineas[M_idx].strip())
    transiciones = lineas[M_idx + 1 : M_idx + 1 + M]
    
    for trans in transiciones:
        trans = trans.strip()
        partes_trans = [p for p in trans.split('/') if p]
        encontrado = False
        
        for ruta, contenido in rutas:
            partes_ruta = [p for p in ruta.split('/') if p]
            
            if len(partes_ruta) != len(partes_trans):
                continue
                
            coincide = True
            parametros = []
            
            for pr, pt in zip(partes_ruta, partes_trans):
                if pr.startswith(':'):
                    parametros.append(pt)
                elif pr != pt:
                    coincide = False
                    break
                    
            if coincide:
                if parametros:
                    print(f"{contenido} {' '.join(parametros)}")
                else:
                    print(contenido)
                encontrado = True
                break
                
        if not encontrado:
            print("404 Not Found")

if __name__ == '__main__':
    resolver_enrutador()
```

### Ejemplo de ejecución

**Entrada simulada:**
```text
3
/ HomePage
/profile ProfilePage
/user/:id UserPage
4
/
/profile
/user/42
/settings
```

**Salida esperada:**
```text
HomePage
ProfilePage
UserPage 42
404 Not Found
```

**Evidencia:**
```bash
AXEL@DESKTOP-70IITE7 UCRT64 /c/Users/AXEL/OneDrive/Documentos/Codes/2026_2/Desarrollo de software
$ python problema1.py < entrada1.txt
HomePage
ProfilePage
UserPage 42
404 Not Found

```


## Problema 2: Fidelidad de Clientes (Banco de la Nación)

**Descripción del problema:**

Identificar al cliente más fiel (el que registre más transacciones) para cada uno de los socios del banco, basándose en las compras hechas desde sus terminales asignadas. Si llega a haber un empate en la cantidad de operaciones, el programa prioriza al usuario con el ID más bajo. Por otro lado, si un socio no registra movimientos, se imprime un `-1`.

### Código

```python
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
```

### Ejemplo de ejecución

**Entrada simulada:**
```text
4 6 9 
1 1
2 80
1 3
3 1000
2 150
4 20
1501 80
1502 150
1501 80
1501 150
1501 1
1501 3
1501 3
1501 3
1502 1000
1503 1000
```

**Salida esperada:**
```text
1 1501
2 1501
3 1502
4 -1
```

**Evidencia:**
```bash
AXEL@DESKTOP-70IITE7 UCRT64 /c/Users/AXEL/OneDrive/Documentos/Codes/2026_2/Desarrollo de software
$ python problema2.py < entrada2.txt
1 1501
2 1501
3 1502
4 -1

```