# Criterios de clasificación

Este documento define cómo se asigna a cada trámite el nivel de garantía de
identidad que exige. Los criterios son explícitos y el resultado es
reproducible: ante los mismos datos de entrada, cualquier persona debe obtener
el mismo nivel de salida.

Si dos personas clasifican el mismo trámite y obtienen niveles distintos, el
fallo está en la definición de los ejes, no en el criterio de quien clasifica.
Esa es la prueba de que el instrumento funciona.

---

## 1. Las tres preguntas

Para cada trámite se responde a tres cosas independientes:

**Qué nivel de garantía exige.** Cuánta confianza hace falta tener en que la
persona es quien dice ser. Se resuelve con los cuatro ejes del apartado 2.

**Qué hace falta acreditar realmente.** Que no siempre es la identidad. Se
resuelve con el apartado 4.

**Qué ocurre cuando el canal principal no está disponible.** Porque el trámite
no desaparece: se desplaza al teléfono, al correo o al mostrador. Se resuelve
con el apartado 5.

Separar la primera de la segunda es lo que evita el error más común: pedir el
documento de identidad cuando lo único que hace falta saber es que alguien tiene
una titulación en vigor. Y añadir la tercera es lo que evita que el marco
describa solo el camino que funciona.

---

## 2. Los cuatro ejes

Cada eje se puntúa de 1 a 4. Las definiciones son cerradas: si un caso no encaja
en ninguna, se documenta como excepción y se revisa la definición del eje.

### E1 — Impacto del uso indebido

Qué obtiene quien suplanta a otro con éxito.

| Valor | Definición |
|---|---|
| 1 | Acceso a información no sensible, ya disponible por otras vías |
| 2 | Acceso a información personal o al contenido de un expediente |
| 3 | Contrae un compromiso económico, genera una obligación jurídica o modifica datos |
| 4 | Obtiene acceso físico a zona restringida, o dispone sobre bienes o derechos de terceros |

### E2 — Reversibilidad

Si el daño puede deshacerse una vez detectado.

| Valor | Definición |
|---|---|
| 1 | Reversible sin coste |
| 2 | Reversible con coste administrativo |
| 3 | Reversible solo por vía formal: recurso, procedimiento contradictorio |
| 4 | Irreversible en la práctica |

### E3 — Alcance del daño

A quién alcanza.

| Valor | Definición |
|---|---|
| 1 | Solo a la persona suplantada |
| 2 | A la persona suplantada y a la Agencia |
| 3 | A terceros identificables |
| 4 | A la seguridad de personas o instalaciones |

### E4 — Detectabilidad

Cuándo se notaría, si es que se nota.

| Valor | Definición |
|---|---|
| 1 | De forma inmediata y automática |
| 2 | En una revisión rutinaria |
| 3 | Solo si alguien reclama |
| 4 | Podría no detectarse nunca |

---

## 3. Regla de decisión

El nivel base lo fija **E1**, porque el impacto es lo que determina cuánto hay
que proteger. Los demás ejes solo pueden elevarlo, nunca reducirlo.

**Paso 1 — Nivel base según E1:**

- E1 = 1 o 2 → **bajo**
- E1 = 3 → **sustancial**
- E1 = 4 → **alto**

**Paso 2 — Elevar un nivel si se cumple cualquiera de estas condiciones:**

- E2 ≥ 3 (el daño no se deshace fácilmente)
- E3 ≥ 3 (alcanza a terceros o a la seguridad)
- E4 ≥ 3 **y** E1 ≥ 2 (podría no detectarse y hay algo que perder)

**Paso 3 — La elevación se aplica una sola vez.** Un trámite que ya es alto se
queda en alto. Si concurren varias condiciones de elevación, se documenta en el
campo de notas, porque es señal de que ese trámite merece atención específica.

Los tres niveles se corresponden con los del marco europeo de identificación
electrónica: bajo, sustancial y alto.

---

## 4. Qué hace falta acreditar

Independientemente del nivel, para cada trámite se declara qué se necesita
acreditar. Son tres cosas distintas y rara vez hacen falta las tres:

**Identificación.** Saber quién es la persona. Necesario cuando el trámite
genera una obligación personal o hay que poder localizar a alguien después.

**Atributo.** Acreditar que posee algo o cumple una condición: una titulación
en vigor, la propiedad de una embarcación, una habilitación profesional. No
requiere saber quién es, solo que lo tiene.

**Representación.** Acreditar que actúa en nombre de otra persona o entidad, y
con qué alcance.

Esta distinción tiene consecuencia práctica directa. Un trámite que solo
requiere acreditar un atributo puede resolverse sin recoger datos
identificativos, lo que reduce la información personal tratada y la exposición
en caso de incidente. Los mecanismos de identidad digital de nueva generación
permiten demostrar un atributo sin revelar el documento completo, de modo que
esta columna del marco deja de ser teórica.

---

## 5. La tercera pregunta: qué pasa cuando el canal falla

Un trámite no tiene un solo camino. Cuando el canal electrónico no está
disponible —por avería, por mantenimiento, o porque el usuario no puede
usarlo— la gestión no desaparece: se desplaza al teléfono, al correo o al
mostrador.

Y ahí es donde la garantía de identidad se desploma en silencio.

El canal principal puede exigir dos factores y verificación documental contra
fuente autorizada. El canal alternativo suele ser una persona atendiendo una
llamada, sin criterio escrito sobre qué debe comprobar. El nivel declarado para
ese trámite deja de cumplirse sin que nadie lo advierta, porque nadie ha
escrito qué nivel debía mantener la vía alternativa.

Por eso cada trámite del marco declara tres cosas y no dos:

**Qué nivel exige.** Resuelto por los cuatro ejes.

**Qué hace falta acreditar.** Identificación, atributo, representación.

**Qué ocurre por la vía alternativa.** Cuál es esa vía, y si mantiene o no el
nivel declarado.

La tercera no siempre tiene respuesta, y eso ya es información. Un trámite cuyo
canal alternativo está sin determinar es un trámite cuyo nivel real se
desconoce: el declarado solo se cumple mientras el canal principal funcione.

Esto no es una exigencia teórica. Cualquier organización tiene vías
alternativas y casi ninguna las ha clasificado, porque la atención por teléfono
o en mostrador no se percibe como parte del sistema de identidad. Lo es.

---

## 6. Qué no resuelve este marco

Declarado de partida:

- **No dice qué tecnología usar.** Dice qué garantía hace falta. Con qué
  mecanismo se consigue esa garantía es una decisión posterior, y el marco
  sigue siendo válido cuando el mecanismo cambie.

- **No sustituye al análisis de riesgos de la organización.** Se ocupa de un
  riesgo concreto: que alguien no sea quien dice ser. Otros riesgos quedan
  fuera.

- **No es una norma.** Es un instrumento de trabajo. Su valor depende de que la
  organización que lo aplica lo revise y lo adopte como propio.

- **La clasificación puede quedar obsoleta.** Un trámite cambia de nivel si
  cambia su procedimiento, su volumen o su normativa. Por eso el marco se
  versiona y cada entrada lleva fecha de revisión.
