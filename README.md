# Marco de garantía de identidad por trámite

La primera pieza de un modelo de identidad digital: **qué nivel de confianza en
la identidad exige cada trámite** de una organización, escrito de forma
explícita y reproducible, y traducido a requisitos que el sistema que lo
implemente deberá cumplir.

---

## El problema

Imaginemos que se contrata a alguien para comprobar si una puerta es segura.
Puede empujarla, mirar la cerradura y decir que parece resistente. Pero no puede
decir si **cumple**, porque nadie ha establecido antes qué debe aguantar: una
patada, un taladro, media hora de ataque sostenido.

Sin criterio previo, verificar no significa nada.

Lo mismo ocurre con la identidad digital. Cuando no está escrito qué exige cada
trámite, pasa siempre lo mismo: se pide certificado digital para consultar algo
trivial —una barrera innecesaria para el ciudadano— y se acepta un documento
escaneado por correo para algo que sí importa. No es descuido: es que nadie ha
decidido antes, de forma explícita, qué hace falta en cada caso.

Y no es una decisión tecnológica. Es de riesgo.

---

## El hueco que llena

El Reglamento de Ejecución (UE) 2015/1502 define qué tiene que cumplir un medio
de identificación electrónica para poder llamarse de nivel bajo, sustancial o
alto: cómo se probó la identidad al darlo de alta, cuántos factores de
autenticación usa, frente a qué perfil de atacante resiste, qué régimen de
comprobación requiere.

Lo que esa norma **no** dice, deliberadamente, es qué nivel necesita cada
trámite. Lo deja a cada organización.

> La norma construye la escala. Nadie dice qué va en cada peldaño.

Esto es lo que va en los peldaños. Y es la parte del modelo que hay que escribir
antes de elegir ningún mecanismo, porque es la que determina contra qué se mide
cualquiera de ellos.

---

## Qué hay aquí

```
docs/criterios.md                   Cómo se decide el nivel de cada trámite
docs/criterios-de-aceptacion.md     Cómo cada nivel se traduce en requisitos
marco/tramites-reales.yaml          Trámites especificados
pruebas/catalogo.yaml               Criterios de aceptación derivados (selección)
validar-marco.py                    Comprueba la coherencia interna
cobertura.py                        Cruza la especificación con sus criterios
```

La especificación vive en formato estructurado y versionado, no en un documento.
Eso permite tres cosas que un informe no permite: comprobar automáticamente que
es coherente consigo misma, ver qué cambió entre dos revisiones, y derivar
directamente de ella los requisitos que el sistema deberá cumplir.

Un documento se archiva. Una especificación se ejecuta.

---

## Cómo se decide el nivel

Cada trámite se valora en cuatro ejes, de 1 a 4, con definiciones cerradas:

| Eje | Pregunta |
|---|---|
| **E1 · Impacto** | Qué obtiene quien suplanta a otro con éxito |
| **E2 · Reversibilidad** | Si el daño puede deshacerse |
| **E3 · Alcance** | A quién alcanza |
| **E4 · Detectabilidad** | Cuándo se notaría, si es que se nota |

El nivel base lo fija el impacto. Los demás ejes solo pueden elevarlo, nunca
reducirlo. El resultado es uno de los tres niveles del marco europeo.

Las definiciones completas de cada valor y la regla de decisión están en
[`docs/criterios.md`](docs/criterios.md).

**El criterio de calidad:** si dos personas especifican el mismo trámite y
obtienen niveles distintos, el fallo está en la definición de los ejes, no en
quien decide. Las herramientas existen para que eso no pase inadvertido.

---

## Las tres preguntas por trámite

**Qué nivel exige.** Resuelto por los cuatro ejes.

**Qué hace falta acreditar.** Tres cosas distintas, y rara vez hacen falta las
tres: saber quién es la persona, que posee algo o cumple una condición, o que
actúa en nombre de otro. Un trámite que solo requiere acreditar un atributo
puede resolverse sin recoger datos identificativos, lo que reduce la
información personal tratada y la exposición si algo falla.

**Qué ocurre cuando el canal principal no está.** Esta es la que suele faltar.
Un trámite no tiene un solo camino: cuando el canal electrónico no está
disponible, la gestión se desplaza al teléfono, al correo o al mostrador. El
canal principal puede exigir dos factores y verificación documental; el
alternativo suele ser una persona atendiendo una llamada, sin criterio escrito
sobre qué debe comprobar.

El nivel declarado deja de cumplirse sin que nadie lo advierta. Por eso la
especificación lo declara: un trámite cuya vía alternativa está sin determinar
es un trámite cuyo nivel real se desconoce.

---

## Lo que aparece al aplicarlo

En el conjunto de trámites incluido, dos observaciones se sostienen sin
necesidad de conocer la organización por dentro.

**Los niveles no se reparten como cabría esperar.** La inscripción en una lista
de espera para un puesto de atraque resulta de nivel alto, por encima de
trámites que intuitivamente parecen más serios. La razón es que la antigüedad
en esa lista tiene valor económico directo, de modo que una inscripción
indebida desplaza a un tercero identificable, no se detecta salvo reclamación,
y revertirla exige procedimiento formal. Tres condiciones de elevación a la vez.

**Ningún trámite tiene determinada su vía alternativa.** Los diez figuran como
`no-determinada`, y esa constancia es en sí misma un resultado: los niveles
asignados describen el canal electrónico y solo se sostienen mientras ese canal
funcione.

---

## De la especificación al sistema

La especificación es la primera de tres fases.

**La especificación** define qué exige cada trámite.

**Los criterios de aceptación** traducen cada nivel a requisitos concretos sobre
el sistema que se implante: qué debe aceptar, qué debe rechazar, qué debe
registrar y qué no debe conservar nunca. Los criterios de rechazo y los de traza
son donde está la protección real; comprobar que un sistema acepta lo correcto
es sencillo, y un sistema que lo acepta todo cumple cualquier criterio de ese
tipo. Aplicado al conjunto incluido, un trámite de nivel bajo recibe seis
requisitos y uno de nivel alto con representación llega a diecinueve. El detalle
está en [`docs/criterios-de-aceptacion.md`](docs/criterios-de-aceptacion.md).

**La comprobación** aplica esos criterios en la recepción del sistema y de forma
periódica, comparando cada ejecución con la anterior. El resultado es un acta
donde cada afirmación va acompañada del comando que la produjo, su fecha y su
huella, sellada mediante servicio de sellado de tiempo independiente.

Que la especificación exista **antes** de la contratación es lo que permite
incorporarla al pliego como prescripción técnica, y vincular el cumplimiento de
los criterios de aceptación a la recepción del trabajo.

---

## Uso

```bash
python3 validar-marco.py marco/tramites-reales.yaml
python3 cobertura.py marco/tramites-reales.yaml pruebas/catalogo.yaml
```

El **comprobador de coherencia** no juzga si un nivel es el acertado: comprueba
que la regla de decisión se ha aplicado de forma consistente. Si una entrada
declara un nivel distinto al que resulta de sus ejes, la especificación no es
válida.

La **matriz de cobertura** cruza la especificación con los criterios de
aceptación y produce, para cada trámite, los requisitos que le corresponden.
Avisa cuando un trámite se queda sin requisitos en alguna área y cuando un
requisito no aplica a ningún trámite. Es lo que hace que la trazabilidad vaya en
los dos sentidos: de la especificación a los requisitos y de los requisitos a la
especificación.

Ambos devuelven `0` si todo está en orden y `1` si encuentran problemas, de modo
que pueden integrarse en un control automático.

Requiere Python 3 y PyYAML.

---

## Estado y alcance

Versión inicial.

Los trámites incluidos son **reales**, tomados de información publicada por la
propia organización. La **especificación es propia y no ha sido validada** por
ella: se presenta como punto de partida para discutir, no como diagnóstico. La
versión definitiva solo puede escribirse con quien gestiona esos trámites,
porque exige conocer su casuística.

Lo que esta especificación **no** hace, declarado de partida:

- No dice qué tecnología usar. Dice qué garantía hace falta. Sigue siendo válida
  cuando cambie el mecanismo que la proporciona.
- No sustituye al análisis de riesgos de la organización. Se ocupa de un riesgo
  concreto: que alguien no sea quien dice ser.
- No es una norma. Es un instrumento de trabajo, y su valor depende de que la
  organización lo revise y lo adopte como propio.

---

## Sobre el autor

Dragos C. I. Andrei — Control Digital Pymes
Perito informático forense · Málaga

Regla profesional: no auditar lo que se implanta, ni implantar lo que se audita.
El propio Reglamento (UE) 2015/1502 recoge esa separación al exigir comprobación
independiente a partir del nivel sustancial, e independiente y externa en el
nivel alto.

Ningún dato entra en un informe sin haber sido obtenido con herramienta
trazable, con su comando, su fecha y su huella.

[controldigitalpymes.es](https://controldigitalpymes.es)
