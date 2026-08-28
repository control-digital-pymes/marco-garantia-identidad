# Marco de garantía de identidad por trámite

Instrumento para decidir, de forma explícita y reproducible, **qué nivel de
confianza en la identidad exige cada trámite** de una organización, y para
comprobar después si el sistema implantado lo cumple.

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
autenticación usa, frente a qué perfil de atacante resiste, qué auditoría
requiere.

Lo que esa norma **no** dice, deliberadamente, es qué nivel necesita cada
trámite. Lo deja a cada organización.

> La norma construye la escala. Nadie dice qué va en cada peldaño.

Este marco es lo que va en los peldaños.

---

## Qué hay aquí

```
docs/criterios.md            Los criterios de clasificación
docs/banco-de-pruebas.md     Cómo cada nivel se traduce en comprobaciones
marco/tramites-reales.yaml   Trámites reales clasificados
pruebas/catalogo.yaml        Pruebas derivadas del marco (selección)
validar-marco.py             Validador de coherencia del marco
cobertura.py                 Matriz de cobertura entre marco y pruebas
```

El marco vive en formato estructurado y versionado, no en un documento. Eso
permite tres cosas que un informe no permite: comprobarlo de forma automática,
ver qué cambió entre dos revisiones, y derivar de él las pruebas que verifican
su cumplimiento.

---

## Cómo funciona

Cada trámite se valora en cuatro ejes, de 1 a 4, con definiciones cerradas:

| Eje | Pregunta |
|---|---|
| **E1 · Impacto** | Qué obtiene quien suplanta a otro con éxito |
| **E2 · Reversibilidad** | Si el daño puede deshacerse |
| **E3 · Alcance** | A quién alcanza |
| **E4 · Detectabilidad** | Cuándo se notaría, si es que se nota |

El nivel base lo fija el impacto. Los demás ejes solo pueden elevarlo, nunca
reducirlo. El resultado es uno de los tres niveles del marco europeo.

Los criterios completos, con las definiciones de cada valor y la regla de
decisión, están en [`docs/criterios.md`](docs/criterios.md).

**El criterio de calidad del instrumento:** si dos personas clasifican el mismo
trámite y obtienen niveles distintos, el fallo está en la definición de los
ejes, no en quien clasifica. El validador existe para que eso no pase
inadvertido.

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

El nivel declarado deja de cumplirse sin que nadie lo advierta. Por eso el
marco lo declara: un trámite cuya vía alternativa está sin determinar es un
trámite cuyo nivel real se desconoce.

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

## Uso

```bash
python3 validar-marco.py marco/tramites-reales.yaml
python3 cobertura.py marco/tramites-reales.yaml pruebas/catalogo.yaml
```

El **validador** no juzga si la clasificación es acertada: comprueba que la regla
de decisión se ha aplicado de forma consistente. Si una entrada declara un nivel
distinto al que resulta de sus ejes, el marco no es válido.

La **matriz de cobertura** cruza el marco con el catálogo de pruebas y produce,
para cada trámite, las comprobaciones que le corresponden. Avisa cuando un
trámite se queda sin pruebas en alguna área y cuando una prueba no aplica a
ningún trámite. Es lo que hace que la trazabilidad vaya en los dos sentidos: del
criterio a las pruebas y de las pruebas al criterio.

Ambos devuelven `0` si todo está en orden y `1` si encuentran problemas, de modo
que pueden integrarse en un control automático.

Requiere Python 3 y PyYAML.

---

## Del marco a la verificación

El marco es la primera de tres fases.

**El marco** define qué exige cada trámite.

**El banco de pruebas** traduce cada nivel a comprobaciones ejecutables sobre el
sistema que se implante: qué debe aceptar, qué debe rechazar, qué debe registrar
y qué no debe conservar nunca. Las pruebas negativas y las de traza son donde
está la protección real; comprobar que un sistema acepta lo correcto es sencillo.
Aplicado al conjunto incluido, un trámite de nivel bajo recibe seis
comprobaciones y uno de nivel alto con representación llega a diecinueve. El
detalle está en [`docs/banco-de-pruebas.md`](docs/banco-de-pruebas.md).

**La verificación** ejecuta esas pruebas en la recepción del sistema y de forma
periódica, comparando cada ejecución con la anterior. El resultado es un acta
donde cada afirmación va acompañada del comando que la produjo, su fecha y su
huella, sellada mediante servicio de sellado de tiempo independiente.

Que el marco exista **antes** de la contratación es lo que permite incorporarlo
como criterio técnico del pliego, y vincular la superación del banco de pruebas
a la recepción del trabajo.

---

## Estado y alcance

Versión inicial.

Los trámites incluidos son **reales**, tomados de información publicada por la
propia organización. La **clasificación es propia y no ha sido validada** por
ella: se presenta como propuesta de trabajo, no como diagnóstico. La
clasificación definitiva de trámites reales solo puede hacerse con quien los
gestiona, porque exige conocer su casuística.

Lo que este marco **no** hace, declarado de partida:

- No dice qué tecnología usar. Dice qué garantía hace falta. Sigue siendo válido
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
El propio Reglamento (UE) 2015/1502 recoge esa separación al exigir auditoría
independiente y externa en el nivel alto.

Ningún dato entra en un informe sin haber sido obtenido con herramienta
trazable, con su comando, su fecha y su huella.

[controldigitalpymes.es](https://controldigitalpymes.es)
