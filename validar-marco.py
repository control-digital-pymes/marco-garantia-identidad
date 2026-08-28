#!/usr/bin/env python3
"""
validar-marco.py — Control Digital Pymes

Comprueba que un fichero de marco de garantía de identidad es coherente con
los criterios definidos en docs/criterios.md.

No juzga si la clasificación es acertada: comprueba que se ha aplicado la regla
de decisión de forma consistente. Si una entrada declara un nivel distinto al
que resulta de sus ejes, el fichero no es válido.

Uso:
    python3 validar-marco.py marco/tramites-tipo.yaml

Códigos de salida:
    0  marco válido
    1  se han encontrado errores
    2  error de uso o de lectura del fichero
"""

import sys
import hashlib
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: falta PyYAML. Instalar con: pip install pyyaml")
    sys.exit(2)


EJES = ("impacto", "reversibilidad", "alcance", "detectabilidad")
NIVELES = ("bajo", "sustancial", "alto")
ORDEN = {"bajo": 0, "sustancial": 1, "alto": 2}
ACREDITAR = ("identificacion", "atributo", "representacion")


def nivel_base(impacto):
    """Paso 1 de la regla de decisión: el nivel base lo fija E1."""
    if impacto <= 2:
        return "bajo"
    if impacto == 3:
        return "sustancial"
    return "alto"


def condiciones_elevacion(ejes):
    """Paso 2: devuelve la lista de condiciones de elevación que concurren."""
    cond = []
    if ejes["reversibilidad"] >= 3:
        cond.append("E2>=3 (daño no reversible con facilidad)")
    if ejes["alcance"] >= 3:
        cond.append("E3>=3 (alcanza a terceros o a la seguridad)")
    if ejes["detectabilidad"] >= 3 and ejes["impacto"] >= 2:
        cond.append("E4>=3 con E1>=2 (podría no detectarse)")
    return cond


def calcular_nivel(ejes):
    """Aplica la regla completa. Devuelve (nivel, condiciones_que_concurren)."""
    base = nivel_base(ejes["impacto"])
    cond = condiciones_elevacion(ejes)
    if cond and ORDEN[base] < ORDEN["alto"]:
        nivel = NIVELES[ORDEN[base] + 1]
    else:
        nivel = base
    return nivel, cond


def validar(ruta):
    errores = []
    avisos = []

    try:
        datos = yaml.safe_load(Path(ruta).read_text(encoding="utf-8"))
    except Exception as e:
        print(f"ERROR: no se puede leer {ruta}: {e}")
        return 2

    for campo in ("version", "fecha", "tramites"):
        if campo not in datos:
            errores.append(f"Falta el campo obligatorio de cabecera: {campo}")

    tramites = datos.get("tramites") or []
    if not tramites:
        errores.append("El marco no contiene ningún trámite.")

    vistos = set()

    for i, t in enumerate(tramites, 1):
        ref = t.get("id", f"(sin id, posición {i})")

        if "id" not in t:
            errores.append(f"[{ref}] falta el campo 'id'")
        elif t["id"] in vistos:
            errores.append(f"[{ref}] identificador duplicado")
        else:
            vistos.add(t["id"])

        for campo in ("nombre", "nivel", "ejes", "acreditar"):
            if campo not in t:
                errores.append(f"[{ref}] falta el campo '{campo}'")

        ejes = t.get("ejes") or {}
        ejes_ok = True
        for eje in EJES:
            if eje not in ejes:
                errores.append(f"[{ref}] falta el eje '{eje}'")
                ejes_ok = False
            elif not isinstance(ejes[eje], int) or not 1 <= ejes[eje] <= 4:
                errores.append(
                    f"[{ref}] el eje '{eje}' vale {ejes[eje]!r}; "
                    "debe ser un entero entre 1 y 4"
                )
                ejes_ok = False

        for extra in set(ejes) - set(EJES):
            avisos.append(f"[{ref}] eje no reconocido, se ignora: '{extra}'")

        acreditar = t.get("acreditar") or {}
        for campo in ACREDITAR:
            if campo not in acreditar:
                errores.append(f"[{ref}] falta 'acreditar.{campo}'")
            elif not isinstance(acreditar[campo], bool):
                errores.append(
                    f"[{ref}] 'acreditar.{campo}' debe ser true o false"
                )

        declarado = t.get("nivel")
        if declarado is not None and declarado not in NIVELES:
            errores.append(
                f"[{ref}] nivel '{declarado}' no reconocido; "
                f"valores admitidos: {', '.join(NIVELES)}"
            )
        elif ejes_ok and declarado is not None:
            calculado, cond = calcular_nivel(ejes)
            if calculado != declarado:
                errores.append(
                    f"[{ref}] nivel declarado '{declarado}' pero de los ejes "
                    f"resulta '{calculado}'"
                )
            if len(cond) > 1 and not t.get("notas"):
                avisos.append(
                    f"[{ref}] concurren {len(cond)} condiciones de elevación "
                    "y no hay notas que lo documenten"
                )

        # Coherencia interna: si acredita representación, necesita identificación
        if acreditar.get("representacion") and not acreditar.get("identificacion"):
            avisos.append(
                f"[{ref}] acredita representación sin identificación; "
                "revisar si es intencionado"
            )

    huella = hashlib.sha256(Path(ruta).read_bytes()).hexdigest()

    print(f"Fichero:  {ruta}")
    print(f"Versión:  {datos.get('version', '(sin versión)')}")
    print(f"Trámites: {len(tramites)}")
    print(f"SHA-256:  {huella}")
    print()

    if avisos:
        print(f"AVISOS ({len(avisos)}):")
        for a in avisos:
            print(f"  · {a}")
        print()

    if errores:
        print(f"ERRORES ({len(errores)}):")
        for e in errores:
            print(f"  ✗ {e}")
        print()
        print("Marco NO válido.")
        return 1

    print("Marco válido: todos los niveles declarados son coherentes con sus ejes.")
    return 0


def main():
    if len(sys.argv) != 2:
        print(__doc__.strip())
        return 2
    return validar(sys.argv[1])


if __name__ == "__main__":
    sys.exit(main())
