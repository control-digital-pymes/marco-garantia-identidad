#!/usr/bin/env python3
"""
cobertura.py — Control Digital Pymes

Cruza el marco de garantía por trámite con el catálogo de pruebas y produce la
matriz de cobertura: qué pruebas corresponden a cada trámite.

Es la pieza que cierra el sistema. Sin ella, marco y catálogo son dos documentos
sueltos. Con ella, la trazabilidad va en los dos sentidos: del criterio a las
pruebas y de las pruebas al criterio.

Avisa en dos casos que importan:
  · Un trámite sin ninguna prueba aplicable en alguna área.
  · Una prueba que no aplica a ningún trámite, lo que suele indicar una
    condición mal declarada.

Uso:
    python3 cobertura.py marco/tramites-reales.yaml pruebas/catalogo.yaml

Códigos de salida:
    0  cobertura completa
    1  hay huecos de cobertura
    2  error de uso o de lectura
"""

import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: falta PyYAML. Instalar con: pip install pyyaml")
    sys.exit(2)


ORDEN = {"bajo": 0, "sustancial": 1, "alto": 2}


def aplica(prueba, tramite):
    """Una prueba aplica si el nivel alcanza y se cumple la condición requerida."""
    if ORDEN[prueba["nivel_minimo"]] > ORDEN[tramite["nivel"]]:
        return False
    requisito = prueba.get("requiere")
    if requisito and not tramite.get("acreditar", {}).get(requisito):
        return False
    return True


def cargar(ruta):
    return yaml.safe_load(Path(ruta).read_text(encoding="utf-8"))


def main():
    if len(sys.argv) != 3:
        print(__doc__.strip())
        return 2

    try:
        marco = cargar(sys.argv[1])
        catalogo = cargar(sys.argv[2])
    except Exception as e:
        print(f"ERROR al leer los ficheros: {e}")
        return 2

    tramites = marco.get("tramites") or []
    pruebas = catalogo.get("pruebas") or []
    areas = [a["id"] for a in (catalogo.get("areas") or [])]

    if not tramites or not pruebas:
        print("ERROR: falta contenido en el marco o en el catálogo.")
        return 2

    print("=" * 72)
    print("MATRIZ DE COBERTURA")
    print("=" * 72)
    print(f"Marco:    {sys.argv[1]}  (versión {marco.get('version')})")
    print(f"Catálogo: {sys.argv[2]}  (versión {catalogo.get('version')})")
    print(f"Trámites: {len(tramites)}   Pruebas: {len(pruebas)}")
    print()

    huecos = []
    pruebas_usadas = set()

    for t in tramites:
        aplicables = [p for p in pruebas if aplica(p, t)]
        for p in aplicables:
            pruebas_usadas.add(p["id"])

        por_area = {a: [] for a in areas}
        for p in aplicables:
            por_area.setdefault(p["area"], []).append(p["id"])

        negativas = sum(1 for p in aplicables if p["tipo"] == "negativa")
        trazas = sum(1 for p in aplicables if p["tipo"] == "traza")

        print("-" * 72)
        print(f"{t['id']}  ·  nivel {t['nivel'].upper()}")
        print(f"  {t['nombre']}")
        print(f"  Pruebas aplicables: {len(aplicables)}"
              f"   (negativas: {negativas}, traza: {trazas})")
        for area in areas:
            ids = por_area.get(area, [])
            marca = "  " if ids else "! "
            print(f"  {marca}{area:22} {', '.join(ids) if ids else 'SIN COBERTURA'}")
            if not ids:
                huecos.append((t["id"], area))
        print()

    print("=" * 72)
    print("AVISOS")
    print("=" * 72)
    print()

    if huecos:
        print(f"Huecos de cobertura: {len(huecos)}")
        for tid, area in huecos:
            print(f"  · {tid} no tiene ninguna prueba en el área '{area}'")
        print()
        print("  Un hueco no siempre es un error: puede ser correcto que un")
        print("  trámite de nivel bajo no tenga pruebas en áreas que solo")
        print("  aplican a partir de sustancial. Lo que no debe ocurrir es que")
        print("  un hueco pase inadvertido.")
        print()

    sin_usar = [p["id"] for p in pruebas if p["id"] not in pruebas_usadas]
    if sin_usar:
        print(f"Pruebas que no aplican a ningún trámite: {len(sin_usar)}")
        for pid in sin_usar:
            print(f"  · {pid}")
        print()
        print("  Suele indicar una condición 'requiere' mal declarada, o una")
        print("  prueba escrita para un caso que el marco todavía no recoge.")
        print()

    if not huecos and not sin_usar:
        print("Sin huecos. Cada trámite tiene cobertura en todas las áreas y")
        print("cada prueba aplica al menos a un trámite.")
        print()

    return 1 if huecos else 0


if __name__ == "__main__":
    sys.exit(main())
