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