# Los criterios de aceptación

La especificación dice **qué nivel de garantía exige cada trámite**. Los
criterios de aceptación dicen **qué debe cumplir el sistema que la implemente**.

Sin lo primero, lo segundo no tiene contra qué medirse. Sin lo segundo, lo
primero se queda en un documento.

Escritos antes de la contratación, estos criterios pueden incorporarse al pliego
como prescripción técnica y vincularse a la recepción del trabajo.

---

## De dónde salen

Los criterios no se inventan: se derivan de lo que la norma exige para cada
nivel. El Reglamento de Ejecución (UE) 2015/1502 organiza sus especificaciones
en cuatro bloques. El catálogo reproduce esa estructura y añade una quinta
área.

| Área | Qué comprueba | Origen |
|---|---|---|
| **A1 · Prueba de identidad** | Cómo se verifica quién es la persona al darse de alta | Bloque de inscripción |
| **A2 · Gestión del medio** | Emisión, entrega, revocación y renovación de la credencial | Bloque de gestión del medio |
| **A3 · Autenticación** | Cómo se demuestra en cada uso que se sigue siendo el titular | Bloque de autenticación |
| **A4 · Trazabilidad y minimización** | Qué queda registrado y qué no debería quedar | Bloque de gestión y organización, y principio de minimización |
| **A5 · Continuidad en vía alternativa** | Si el nivel se sostiene cuando el canal principal no está | Adición propia |

**A5 no deriva de la norma.** Es una adición, y es la que cubre el punto ciego
que ninguna especificación técnica contempla: los trámites tienen vías
alternativas —teléfono, correo, mostrador— y ahí el nivel declarado se desploma
sin que nadie lo advierta, porque nadie ha escrito qué debe comprobar quien
atiende.

---

## Los tres tipos de criterio

Esta clasificación es lo que distingue un catálogo útil de una lista de
comprobaciones.

**De aceptación.** El sistema acepta lo que debe aceptar. Es el más fácil de
escribir y el que todo el mundo hace.

**De rechazo.** El sistema rechaza lo que debe rechazar. Es donde está la
protección real: un sistema que lo acepta todo cumple cualquier criterio de
aceptación.

**De traza.** El sistema registra lo que debe registrar, y **no conserva lo que
no debe conservar**. Es la más incómoda de las tres, porque comprueba ausencias,
y comprobar una ausencia exige más rigor que comprobar una presencia.

En un informe pericial existe siempre un apartado dedicado a lo que *no* se ha
encontrado. Los criterios de traza son ese principio convertido en instrumento.

---

## Qué escala entre niveles

La norma no endurece todo a la vez. Endurece cosas concretas, y el catálogo se
organiza sobre esas escaladas:

**En la prueba de identidad**, la escalada va de suponer a verificar, y de
verificar a verificar contrastando además que quien presenta la documentación es
su titular.

**En el medio de identificación**, de un factor de autenticación a dos de
categorías distintas, y de ahí a protección de la credencial frente a
duplicación y manipulación.

**En la autenticación**, del perfil de atacante básico mejorado al moderado, y
de ahí al alto, con autenticación dinámica a partir del nivel sustancial.

**En la auditoría**, de interna a independiente, y de independiente a externa.

Cada uno de esos saltos genera criterios distintos. Un sistema que aspire a nivel
alto tiene que cumplir los de alto y todos los anteriores.

---

## Cómo se sabe qué criterios aplican a cada trámite

Un criterio aplica a un trámite cuando se cumplen dos condiciones:

1. El nivel exigido por el trámite alcanza o supera el nivel mínimo del criterio.
2. Si el criterio requiere una condición concreta —por ejemplo, que el trámite
   necesite acreditar representación— el trámite la declara.

La consecuencia práctica es que **la cobertura se calcula, no se supone**. El
script `cobertura.py` cruza la especificación con el catálogo y produce,
para cada trámite, la lista de criterios que le corresponden. Y avisa en dos casos:

- Un trámite sin ningún criterio aplicable en alguna área.
- Un criterio del catálogo que no aplica a ningún trámite, porque suele indicar
  una condición mal declarada.

Esa es la trazabilidad en los dos sentidos: de la especificación a los
criterios y de los criterios a la especificación. Ningún requisito se queda sin cubrir en silencio, y
ningún criterio sobra sin que se note.

---

## Estructura de un criterio

```yaml
- id: P-A1-04
  area: prueba-identidad
  nivel_minimo: alto
  tipo: negativa
  titulo: "Documento asociado a dos identidades distintas"
  criterio: >
    Qué exige la norma o el marco que justifica esta comprobación.
  procedimiento: >
    Qué se hace, redactado de forma que otra persona pueda repetirlo.
  resultado_esperado: >
    Qué debe ocurrir. Redactado de forma binaria: o pasa o no pasa.
  evidencia: >
    Qué se captura como prueba de la ejecución.
```

El campo `resultado_esperado` se redacta siempre de forma que admita una única
lectura. Si al ejecutar la prueba hay que decidir si el resultado cuenta como
correcto, el criterio está mal escrito.

---

## Los documentos de prueba

Los criterios de las áreas A1 y A2 necesitan documentos. Todos se fabrican para
esa finalidad y **ninguno contiene datos personales reales**.

El corpus se versiona junto al catálogo, de modo que dos ejecuciones separadas
en el tiempo usan exactamente el mismo material y son comparables.

---

## Aplicación y control de regresión

Los criterios se aplican en dos momentos.

**En la recepción del sistema**, antes de darlo por bueno. El resultado es un
acta de verificación con el alcance, la fecha, cada resultado con su evidencia y
la huella del conjunto, sellada mediante servicio de sellado de tiempo
independiente.

**De forma periódica**, comparando cada ejecución con la anterior. Un sistema
que cumplía los criterios el día de la entrega puede dejar de hacerlo tras una
actualización, un cambio de proveedor o una modificación normativa. Comparar
ejecuciones es lo que convierte una comprobación puntual en vigilancia continua:
si algo cambia, se ve, y se ve cuándo.

---

## Límites declarados

**Los criterios se refieren a comportamiento observable, no a arquitectura
interna.** Mide
qué acepta el sistema, qué rechaza y qué registra. No audita su código ni su
diseño. Es una limitación real y también la razón por la que puede ejecutarse
sin acceso privilegiado y sin depender de la colaboración del proveedor.

**Cumplir los criterios no acredita ausencia de riesgo.** Acredita que el
sistema se ajusta a la especificación vigente en la fecha de aplicación. Son cosas distintas y
conviene no confundirlas.

**Los criterios de resistencia frente a perfiles de atacante requieren
evaluación especializada.** Este catálogo comprueba que existen los controles y
que funcionan como se declara; no sustituye a una evaluación formal de resistencia
criptográfica.

**El catálogo no es exhaustivo.** Es un instrumento vivo: crece cuando aparece
un caso que ningún criterio cubría. Cada incorporación queda versionada, de modo
que siempre se sabe contra qué versión del catálogo se levantó un acta.
