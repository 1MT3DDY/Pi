from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.utils.safestring import mark_safe
RESPUESTAS_FIJAS = {
    1: {
        'pregunta': "¿Es importante registrar ingresos y gastos?", 
        'respuesta': """<br>Registrar ingresos y gastos es uno de los pasos más fundamentales cuando una persona empieza su camino hacia el ahorro.
La razón es simple: no se puede controlar lo que no se conoce.
<br>
Muchas personas creen que no pueden ahorrar porque “no les alcanza” o porque “ganan poco”. Sin embargo, cuando realmente se ponen a registrar todo lo que gastan durante el mes, se dan cuenta de que una parte importante de su dinero se va en pequeñas compras, impulsivas o automáticas, que muchas veces pasan desapercibidas: una bebida, un delivery, un café, snacks, recargas, aplicaciones, caprichos pequeños, etc. Ese gasto, aunque parezca mínimo, acumulado mes a mes puede impedir ahorrar.
<br>
Registrar ingresos y gastos permite 3 cosas clave:<br>


<br>
<b>1. TOMAR CONCIENCIA DE TU SITUACION REAL</b><br><br>

La mayoría de las personas vive con una impresión de cuánto gasta, no con una cifra real.
Cuando anotas todo descubres cuáles son tus gastos inevitables (transporte, comida, cuentas). Y cuáles son gastos hormiga (pequeños gastos diarios que parecen inofensivos). Ese reconocimiento inicial suele ser impactante y genera un cambio de mentalidad:
“Ah, no es que no pueda ahorrar, es que no sabía en qué se me estaba yendo el dinero.” 
<br><br>
<b>2. ORDENAR PRIORIDADES</b>
<br><br>
Cuando ves tus gastos frente a tus ojos, puedes preguntarte:<br>

- ¿Este gasto era realmente necesario?<br>

- ¿Me aporta algo?<br>

- ¿Podría haber elegido una alternativa más económica?<br><br>

A veces lo que falta no es dinero, sino orden.<br><br>



<b>3. TOMAR DECISIONES PARA MEJORAR</b><br><br>

Una vez que sabes cuánto entra y cuánto sale, puedes:<br><br>

-Ajustar gastos innecesarios<br> 

-Crear un plan realista de ahorro, aunque sea pequeño,<br>

-Evitar endeudarte,<br>

Y avanzar hacia metas concretas (un viaje, estudios, independencia, etc.).<br>

Registrar no es para limitarte, es para empoderarte.
<br><br>
<b>¿Cómo se puede registrar de forma práctica?</b><br>

No necesitas algo complejo. Puedes usar:<br><br>

-Una libreta → Escribir cada gasto diario.<br>

-Una planilla Excel / Google Sheets → Más orden visual.<br><br>

<b>Apps gratuitas como:</b><br>

-Notion<br>

-Mobills<br>

-Fintonic<br>

-Spendee<br>

-Monefy<br><br>

Lo importante no es la herramienta, sino la constancia.<br><br>
Fuentes usadas:<br>
- <a href= "https://www.latercera.com/transformadores/noticia/flujo-de-caja-la-importancia-de-llevar-el-registro-de-los-ingresos-y-egresos/66JS35B2YJHUNLSF2MUONKJXGU/" target="_blank">laTercera</a><br>
- <a href= "https://www.appcopec.cl/blog/registro-gastos-mensuales/" target="_blank">Copec</a><br>
""",
'imagen_respuesta': 'ahorro_1.webp',
    },
    2: {
        'pregunta': "¿Que papel tiene el habito y disciplina?",
        'respuesta': """<br>Los hábitos y la disciplina financiera se complementan para gestionar el dinero de forma efectiva, permitiendo a las personas alcanzar sus metas financieras. 
        Es el control y la planificación para que esos hábitos se alineen con objetivos específicos, como crear un presupuesto y evitar deudas innecesarias.<br><br>
        <b>¿Cómo fortalecer tus hábitos y disciplina financiera?</b><br><br>  <b>CREA UN PRESUPUESTO:</b> Planifica cómo se gastará y se ahorrará tu dinero, revisándolo con frecuencia para adaptarlo a tu vida.<br> 
        <b>CONTROLA TUS GASTOS:</b> Analiza a dónde va tu dinero y reduce los gastos innecesarios, como salidas sociales costosas.<br> 
        <b>UTILIZA LA INTELIGENCIA EMOCIONAL:</b> Aprende a controlar los impulsos emocionales que pueden llevar a decisiones de gasto perjudiciales.<br>
        <b>SÉ CONSTANTE:</b> Los buenos hábitos se construyen con constancia. Sé disciplinado no solo con tus finanzas, sino también con otros hábitos saludables que influyen en tu bienestar general. <br><br>
        Un hábito es algo que repetimos automáticamente.
        Cuando el ahorro se vuelve hábito, ya no duele ni se siente como un sacrificio.
        Es simplemente parte de la rutina.<br><br>
Fuentes usadas:<br>
- <a href= "https://alansariexchange.com/blog/5-steps-to-achieving-financial-discipline/" target="_blank">alansariex change</a><br>
- <a href= "https://www.firstcitizens.com/personal/insights/family/financial-discipline" target="_blank">first citizens</a><br>""",
        'imagen_respuesta':'ahorro_2.webp',
    },
    3: {
        'pregunta': "¿Que es la regla 50/30/20?",
        'respuesta': """La regla 50/30/20 es una forma sencilla y práctica de organizar el dinero que recibimos cada mes.
     Su objetivo es ayudarte a saber cuánto gastar, cuánto disfrutar y cuánto ahorrar sin sentir que estás haciendo un sacrificio extremo.<br><br>
     Esta regla divide tus ingresos en tres partes:<br>
     <b>El 50% para las Necesidades:</b> Este porcentaje se destina a gastos indispensables; es decir, cosas que necesitas para vivir y no puedes dejar de pagar. Estos gastos se reflejan en alimentación, transporte (micro, metro, combustible), arriendo o dividendo 
     agua, luz, gas, internet. Si estos gastos superan el 50% de tus ingresos, puede ser señal de que
     estás viviendo en un lugar muy caro para tu presupuesto o que estás pagando servicios que no usas, la idea no es castigarte, sino ser consciente.<br><br>
     <b>El 30% para los Gustos:</b> Aquí entran todos los gastos que no son necesarios para vivir, pero sí para estar bien emocionalmente.
     Porque la vida no se trata solo de sobrevivir, sino también de disfrutarla. Lo importante no es eliminar los gustos, sino ponerles un límite sano.<br><br>
     <b>El 20% para Ahorro y Metas:</b> Este es el porcentaje más importante, porque representa tu yo del futuro.<br>
     <b>¿Para qué sirve este 20%?</b><br>
     Este 20% se poodra aprovechar de muchas maneras ya sea para estudios, viajes, herramientas de estudio o tambien se peude usar para invertir y crear fondos de emergencia.<br><br>
     La regla 50/30/20 no es una obligación rígida, sino una guía para que el dinero no se vaya sin que nos demos cuenta. Nos ayuda a vivir el presente, disfrutar, cubrir lo necesario y al mismo tiempo construir un futuro estable.<br><br>
Fuentes usadas:<br>
- <a href= "https://chile.larrainvial.com/lv-insights/finanzas-personales/formula-secreta-para-ahorrar" target="_blank">larrainvial</a><br>
     """,
     'imagen_respuesta':'ahorro_3.png',
    },
    4: {
        'pregunta': "¿Ahorro a corto o largo plazo?",
        'respuesta': """<br>El ahorro puede tener distintos objetivos y duraciones. No todos los ahorros son iguales, ya que cada uno cumple un propósito distinto dependiendo del tiempo y la necesidad. Por eso se habla de <b>ahorro a corto plazo</b> y <b>ahorro a largo plazo</b>.<br><br>

<b>AHORRO A CORTO PLAZO:</b><br>
Es el dinero que se guarda para metas o gastos que ocurrirán dentro de un período menor a 1 o 2 años. Este tipo de ahorro debe mantenerse en un lugar de fácil acceso y bajo riesgo, ya que podrías necesitarlo pronto.<br><br>
<b>Ejemplos:</b><br>
- Comprar un celular o computador.<br>
- Pagar una matrícula o materiales de estudio.<br>
- Reunir dinero para un viaje o una emergencia médica.<br><br>
<b>Características:</b><br>
- Baja rentabilidad (no se busca ganar mucho, sino proteger el dinero).<br>
- Alta liquidez (puedes retirarlo fácilmente).<br>
- Ideal para objetivos inmediatos o urgentes.<br><br>

<b>AHORRO A LARGO PLAZO:</b><br>
Es el dinero destinado a metas que se cumplirán dentro de varios años. Aquí el objetivo no es solo guardar, sino hacer crecer el dinero en el tiempo, incluso considerando invertir una parte.<br><br>
<b>Ejemplos:</b><br>
- Ahorrar para una vivienda.<br>
- Crear un fondo para estudios universitarios o postgrados.<br>
- Pensar en la jubilación o independencia financiera.<br><br>
<b>Características:</b><br>
- Mayor rentabilidad potencial (puede incluir inversiones).<br>
- Menor liquidez (no se necesita retirar de inmediato).<br>
- Requiere planificación, constancia y visión de futuro.<br><br>

Ambos tipos de ahorro son necesarios y se complementan. El corto plazo te da seguridad y respuesta frente a imprevistos, mientras que el largo plazo te entrega estabilidad y crecimiento financiero.  
Lo ideal es comenzar por el corto plazo —creando un fondo de emergencia— y luego avanzar hacia el largo plazo, donde puedes usar instrumentos que generen rentabilidad.  
Ahorrar no es elegir entre corto o largo plazo, sino saber equilibrarlos para cuidar el presente sin descuidar el futuro.<br><br>
Fuentes usadas:<br>
- <a href= "https://www.cmfchile.cl/portal/principal/613/articles-90068_recurso_4.pdf" target="_blank">cmf chile</a><br>
- <a href= "https://www.revistaeconomia.com/ahorro-a-corto-plazo-inversion-a-largo-plazo-claves-para-equilibrar-tus-finanzas-segun-tus-metas-2/" target="_blank">revista economía</a><br>
""",
'imagen_respuesta':'ahorro_4.jpg',
    },
    5: {
        'pregunta': "¿Es importante el fondo de emergencia en ahorro?",
        'respuesta':"""
<br>El <b>fondo de emergencia</b> es uno de los pilares fundamentales del ahorro personal. Representa una reserva de dinero creada específicamente para cubrir <b>situaciones imprevistas</b> sin tener que endeudarse o desestabilizar el presupuesto mensual.<br><br>

<b>¿POR QUÉ ES TAN IMPORTANTE?</b><br>
Porque la vida está llena de imprevistos: una enfermedad, la pérdida del empleo, una reparación urgente, o incluso una oportunidad que requiere dinero rápido.  
Sin un fondo de emergencia, cualquier gasto inesperado puede convertirse en un problema financiero grave, obligándote a usar tarjetas de crédito, pedir préstamos o vender tus pertenencias.<br><br>

<b>OBJETIVO DEL FONDO DE EMERGENCIA:</b><br>
- Brindar tranquilidad y estabilidad financiera.<br>
- Evitar el sobreendeudamiento.<br>
- Permitir tomar decisiones con calma, sin presión económica.<br><br>

<b>¿CUÁNTO DEBERÍA TENER UN FONDO DE EMERGENCIA?</b><br>
La recomendación general es ahorrar el equivalente a <b>3 a 6 meses de tus gastos básicos</b>.  
Por ejemplo, si tus gastos mensuales son de $400.000, tu fondo ideal debería estar entre $1.200.000 y $2.400.000.  
Si eso parece mucho, no te preocupes: lo importante es comenzar con pequeñas metas. Cada ahorro cuenta y se acumula con el tiempo.<br><br>

<b>¿DÓNDE GUARDARLO?</b><br>
- En una cuenta separada del dinero diario (para no gastarlo por error).<br>
- En un instrumento de bajo riesgo y alta liquidez, como una cuenta de ahorro o depósito a plazo.<br><br>

<b>ERRORES COMUNES:</b><br>
- Usar el fondo para gastos no urgentes (como compras impulsivas o vacaciones).<br>
- No reponerlo después de usarlo.<br><br>

El fondo de emergencia no es solo un ahorro más; es un escudo financiero.  
Te permite vivir con mayor seguridad y reducir el estrés ante los imprevistos.  
Antes de pensar en invertir, siempre se debe construir este fondo: es la base que sostiene todas las demás decisiones financieras.  
Ahorrar es importante, pero tener un fondo de emergencia bien planificado es lo que marca la diferencia entre la estabilidad y la incertidumbre.<br><br>
Fuentes usadas:<br>
- <a href= "https://www.cmfchile.cl/portal/prensa/615/w3-article-94614.html" target="_blank">cmf chile</a><br>
- <a href= "https://biblio.hacienda.cl/estrategia-nacional-de-inclusion-financiera/inclusion-financiera-en-chile-marco-legal-y-normativo-vigente-y-situacion-actual" target="_blank">biblio hacienda</a><br>
- <a href= "https://eselmomento.diariofinanciero.cl/la-importancia-de-tener-un-fondo-de-emergencia/" target="_blank">es el momento</a><br>
""",
'imagen_respuesta':'ahorro_5.jpg',
    },
    6: {
        'pregunta': "¿Ahorrar en efectivo o en instrumentos financieros?",
        'respuesta': """<br>Antes de ahorrar hay que determinar de que modo lo vas a hacer, mucha gente lo hace en efectivo ya que es una manera
        sencilla, pero tambien hay instrumentos y plataformas digitales que nos ayudan con nuestra meta de ahorrar, por eso hay que decidir de que manera vas a comenzar a guardar tu dinero ya que puede conllevar grandes beneficios el donde lo dejas.<br><br>

<b>AHORRAR EN EFECTIVO:</b><br>
Consiste en guardar dinero físico, generalmente en casa o en algún lugar de acceso rápido.<br><br>
<b>Ventajas:</b><br>
- Acceso inmediato al dinero.<br>
- No depende de sistemas bancarios o tecnología.<br>
- Útil para emergencias muy urgentes o para personas que manejan montos pequeños.<br><br>
<b>Desventajas:</b><br>
- <b>No genera intereses</b>: el dinero guardado no crece, pierde valor con el tiempo.<br>
- <b>Riesgo de robo o pérdida</b> (no está protegido).<br>
- <b>La inflación reduce su poder adquisitivo</b>: lo que hoy compras con $10.000, en un año puede costar más.<br><br>

<b>AHORRAR EN INSTRUMENTOS FINANCIEROS:</b><br>
Significa guardar o invertir dinero en productos ofrecidos por bancos o instituciones financieras.  
Estos instrumentos pueden generar rentabilidad y proteger el valor del dinero frente a la inflación.<br><br>
<b>Ejemplos:</b><br>
- <b>Cuentas de ahorro:</b> seguras, permiten retirar dinero fácilmente y a veces generan pequeños intereses.<br>
- <b>Depósitos a plazo:</b> ofrecen una tasa fija durante un periodo determinado, ideales para dinero que no necesitas usar pronto.<br>
- <b>Fondos mutuos o cuentas de inversión:</b> generan una rentabilidad mayor, aunque con algo más de riesgo.<br><br>
<b>Ventajas:</b><br>
- Protegen tu dinero de la inflación.<br>
- Pueden generar intereses o ganancias.<br>
- Algunos instrumentos están cubiertos por seguros o fondos de garantía.<br><br>
<b>Desventajas:</b><br>
- Menor liquidez: puede que no puedas retirar el dinero de inmediato.<br>
- Algunos instrumentos conllevan cierto riesgo financiero.<br><br>

<b>¿CUÁL ELEGIR?</b><br>
La decisión depende del objetivo del ahorro:<br>
- Si necesitas acceso rápido o manejas montos pequeños → <b>efectivo o cuenta de ahorro simple</b>.<br>
- Si ahorras para metas de mediano o largo plazo → <b>depósito a plazo o instrumentos financieros con rentabilidad</b>.<br><br>

Ahorrar en efectivo puede servir para emergencias inmediatas, pero a largo plazo hace que el dinero pierda valor.  
Los instrumentos financieros, en cambio, permiten que tus ahorros trabajen por ti, generando crecimiento y protección frente a la inflación.  
Un buen ahorro combina ambas estrategias: un poco de efectivo disponible y el resto en opciones seguras y rentables.<br><br>
Fuentes usadas:<br>
- <a href="https://depositoaplazo.cl/leyes-fomes-pero-importantes/" target="_blank">depositoaplazo chile</a><br>
- <a href="https://buscadorfinanciero.cl/wp-content/uploads/2021/02/garantia-estal-de-depositos.jpg" target="_blank">buscador financiero</a><br>
- <a href="https://www.bancoestado.cl/content/bancoestado-public/cl/es/home/home/productos-/ahorro-e-inversiones-/cuentas-de-ahorro-.html#/" target="_blank">BancoEstado</a>
""",
'imagen_respuesta':'ahorro_6.webp',
    },
    7: {
        'pregunta': "¿Como tiene que ser un buen lugar para guardar ahorro?",
        'respuesta': """
<br>Hay que tener claro que el lugar donde vas a dejar tu dinero es de mega importancia, ya que hay tomar en cuenta que no todos los
lugares son seguros para dejar lo ahorrado, a fin de cuentas el objetivo es proteger y hacer crecer nuestro dinero.<br><br>

<b>1. SEGURIDAD:</b><br>
Tu ahorro debe estar protegido contra robos, pérdidas o fraudes.  
Guardar dinero en casa puede parecer cómodo, pero no es seguro frente a incendios, robos o simples descuidos.  
Por eso, las instituciones financieras —como bancos, cooperativas o cajas de compensación— son preferibles, ya que están reguladas y resguardan tu dinero.<br><br>
<b>Consejo:</b> Elige entidades reconocidas y revisa si están supervisadas por la Comisión para el Mercado Financiero (CMF).<br><br>

<b>2. LIQUIDEZ (FACILIDAD DE ACCESO):</b><br>
No todos los ahorros se deben poder retirar de inmediato, pero sí debe existir un equilibrio.  
Un fondo de emergencia, por ejemplo, necesita alta liquidez (puedes acceder rápido), mientras que un ahorro a largo plazo puede estar en un depósito a plazo o fondo que genere intereses.<br><br>
<b>Consejo:</b> Divide tu dinero entre ahorro inmediato (para emergencias) y ahorro a largo plazo (para metas grandes).<br><br>

<b>3. RENTABILIDAD:</b><br>
Un buen lugar para ahorrar no solo guarda el dinero, sino que lo ayuda a crecer.  
Existen instrumentos financieros que ofrecen una tasa de interés o rentabilidad, protegiendo el dinero de la inflación.<br><br>
<b>Ejemplos:</b><br>
- Cuentas de ahorro con intereses.<br>
- Depósitos a plazo.<br>
- Cuentas de ahorro en UF (protegidas frente a la inflación).<br><br>

<b>4. FACILIDAD DE USO Y TRANSPARENCIA:</b><br>
El acceso digital hoy es importante. Un buen lugar para guardar ahorro debe permitirte revisar tus movimientos fácilmente, transferir dinero y entender las condiciones sin letras chicas.<br><br>
<b>Consejo:</b> Evita plataformas o “inversiones” que prometan ganancias muy altas sin explicar claramente cómo funcionan.  
Si suena demasiado bueno para ser verdad, probablemente no lo sea.<br><br>

Un buen lugar para guardar ahorro debe ser seguro, accesible y con posibilidad de rentabilidad.  
El dinero ahorrado no debe quedarse inmóvil, sino mantenerse protegido y, si es posible, crecer con el tiempo.  
Combinar seguridad con rendimiento es la clave para un ahorro inteligente y sostenible.  
No se trata solo de “guardar” dinero, sino de ponerlo en el lugar correcto para que trabaje a tu favor.<br><br>
Fuentes usadas:
-<a href="https://www.cmfchile.cl/educa/621/w3-article-27460.html" target="_blank">cmf chile</a><br>
-<a href="https://www.bancoestado.cl/content/bancoestado-public/cl/es/home/garantia-estatal-y-preferencias-para-los-depositos-y-captaciones.html" target="_blank">BancoEstado</a>""",
'imagen_respuesta':'ahorro_7.jpg',
    },
    8: {
        'pregunta': "¿Como debería empezar?",
        'respuesta': """<br>Comenzemos entendiendo que el ahorrar no significa un gran sacrificio, ya que si queremos poder evitar el mal uso de tu dinero
o simplemente guardar para un futuro, el ahorro se debe ver como una nueva relacion que formamos con nuestros habitos, si logras verlo de esa manera entonces ya tienes suelo por donde pararte<br><br>

<b>1. Identificar qué te está frenando:</b><br>
Antes de pensar en cuánto ahorrar, piensa en por qué no lo has hecho antes. Muchas veces no es por falta de dinero, sino por hábitos: gastos impulsivos, mala organización o la creencia de que “no vale la pena ahorrar poco”. Reconocer esto es el verdadero punto de partida. No necesitas tener suelto sobrante para empezar; necesitas claridad. Cuando entiendes tus propios patrones de gasto, ya das tu primer gran paso.<br><br>

<b>2. Hacer un compromiso contigo mismo, no con una cifra:</b><br>
La mayoría de la gente comienza intentando calcular un monto fijo, pero eso suele generar frustración. Es más efectivo comenzar con un compromiso personal simple: “Cada mes voy a separar algo, lo que pueda, pero siempre algo”. Esto crea un hábito flexible que se adapta a tu realidad y no te hace sentir obligado o culpable si tienes un mes más difícil. Desde ahí, podrás construir hacia montos más grandes.<br><br>

<b>3. Separar el dinero el mismo día que lo recibes:</b><br>
El error más común es guardar “lo que sobra”, porque casi nunca sobra. Un método mucho más útil es separar el ahorro inmediatamente al recibir tu sueldo o ingreso. Incluso si la cantidad es pequeña, esto marca una diferencia enorme porque tu mente empieza a tratar ese dinero como intocable. Este paso convierte el ahorro en una prioridad, no en una ocurrencia de último minuto.<br><br>

<b>4. Crear un lugar dedicado exclusivamente para tu ahorro:</b><br>
La clave no es solo guardar dinero, sino guardarlo lejos de tus gastos diarios. Puede ser una cuenta de ahorro, una cuenta digital o un fondo conservador, pero lo importante es que no esté mezclado con el dinero que usas día a día. Esta separación psicológica es más importante de lo que parece: cuando el dinero está “aparte”, cuesta mucho menos gastarlo impulsivamente.<br><br>

<b>5. Empezar con metas pequeñas y muy alcanzables:</b><br>
La mayoría de las personas abandona el ahorro porque se fijan metas poco realistas. Por eso es mejor comenzar con algo tan simple como: “Quiero juntar mi primer $50.000” o “Mi primer mes sin fallar ahorrando”. Cuando logras una meta pequeña, te demuestras a ti mismo que sí puedes, y eso te motiva a seguir avanzando. Las metas pequeñas son el motor que te lleva a metas grandes.<br><br>

<b>6. Elegir una estrategia que te haga la vida más fácil, no más difícil:</b><br>
Ahorrar no tiene por qué ser complicado. Puedes usar un método tradicional como el 50/30/20, pero si te resulta rígido, puedes crear el tuyo: porcentaje libre, ahorro semanal, ahorro por categorías o incluso ahorrar las monedas del vuelto. Lo importante no es la técnica exacta, sino que sea una que puedas mantener sin sentir que estás sacrificando demasiado.<br><br>

<b>7. Apoyarte en herramientas que te muestren tu progreso:</b><br>
Ver tu avance hace que el ahorro se sienta real. Puedes usar apps como Monefy, Spendee o incluso la app de tu banco para llevar un registro visual. También puedes usar métodos simples como un cuadro en papel o un archivo en Excel. Lo importante es que puedas ver cómo crece tu ahorro; esa visualización mantiene tu disciplina y te recuerda por qué empezaste.<br><br>

<b>8. Entender que ahorrar es un proceso emocional, no solo financiero:</b><br>
Habrá meses fáciles y meses difíciles. Lo importante no es ser perfecto, sino constante. Si un mes no puedes ahorrar lo que querías, no has fracasado; lo importante es no abandonar el hábito. Ahorrar es una conversación continua contigo mismo sobre tus prioridades y sobre la vida que quieres construir. Cada peso que separas es una afirmación de que estás pensando en tu propio futuro.<br><br>
Fuentes usadas:<br> 
- <a href= "https://www.latercera.com/servicios/noticia/conoce-estos-5-consejos-de-ahorro-para-personas-jovenes/MND4LD3FOZCPFI35X6KAFN72SQ/" target="_blank">La Tercera</a><br>
-<a href="https://educacionfinancierabancoestado.cl/docs/default-source/default-document-library/manual-de-educaci%C3%B3n-financiera---ahorro.pdf" target="_blank">BancoEstado</a><br>
-<a href="https://www.cmfchile.cl/educa/621/articles-80755_recurso_1.pdf" target="_blank">cmf chile</a>
""",
'imagen_respuesta':'ahorro_8.jpg',
    },
    #<a href="" target="_blank"></a>
    9: {
        'pregunta': "¿Que importancia tiene la fijacion de objetivos?",
        'respuesta': """<br>Fijar objetivos es el primer paso para construir una estrategia de inversión sólida y con sentido. Sin metas claras, cualquier decisión financiera se vuelve improvisada y puede llevar a perder dinero o no lograr lo que realmente se busca.<br><br>

La fijación de objetivos te permite establecer un rumbo. Invertir sin objetivos es como navegar sin mapa: puedes avanzar, pero sin saber si te estás acercando o alejando de tu destino.<br><br>

<b>1. Define tu propósito financiero:</b><br>
Antes de invertir, pregúntate: ¿para qué quiero invertir? Puede ser para comprar una casa, financiar estudios, asegurar la jubilación o alcanzar independencia económica. Cada meta requiere estrategias y plazos distintos.<br><br>

<b>2. Plantea objetivos SMART:</b><br>
Los objetivos deben ser <b>Específicos, Medibles, Alcanzables, Relevantes y con Tiempo definido</b>. Por ejemplo, “Ahorrar e invertir $1.000.000 en dos años para el pie de un departamento” es más claro y medible que simplemente “quiero ahorrar”.<br><br>

<b>3. Divide tus metas según el plazo:</b><br>

<b>Corto plazo (1-2 años):</b> Ideal para fondos de emergencia o metas pequeñas, usando instrumentos de bajo riesgo como depósitos a plazo o fondos conservadores.<br>
<b>Mediano plazo (3-5 años):</b> Puedes asumir un poco más de riesgo, como fondos balanceados o mixtos.<br>
<b>Largo plazo (5+ años):</b> Aquí entran inversiones más agresivas como acciones, ETFs o fondos de pensiones voluntarios (APV).<br>
<br>

<b>4. Ajusta tus objetivos con el tiempo:</b><br>
Tus metas pueden cambiar: tal vez tu ingreso mejora o surgen nuevas prioridades. Revisa tus objetivos cada 6 o 12 meses y ajusta tu estrategia de inversión si es necesario.<br><br>

<b>5. Usa herramientas de planificación:</b><br>
Puedes llevar control de tus metas con apps o plataformas como:<br>

- <a href="https://www.fintual.cl" target="_blank">Fintual</a> – para fijar metas y ver su progreso con simulaciones reales.<br>
- <a href="https://www.banchileinversiones.cl" target="_blank">Banchile Inversiones</a> – permite crear objetivos y asignar fondos según plazo y riesgo.<br>
- O simplemente usa una hoja de cálculo de Google Sheets o Excel con columnas de “meta”, “monto”, “plazo” y “avance”.<br>
<br>

Invertir sin objetivos es como correr sin saber hacia dónde vas. Cuando defines metas claras, tus decisiones financieras dejan de ser impulsivas y se transforman en pasos estratégicos hacia tu independencia económica.<br><br>
Fuentes usadas:<br>
- <a href= "https://www.principal.cl/informate/blog/actualidad/como-fijar-tus-objetivos-financieros" target="_blank">principal</a><br>
- <a href= "https://www.cmfchile.cl/educa/621/w3-article-1674.html" target="_blank">cmf chile</a><br>
- <a href= "https://www.generali.es/blog/generalimasqueseguros/objetivos-financieros-regla-smart/" target="_blank">generali</a><br>""",
'imagen_respuesta':'inversion_1.webp',
    },
    10: {
        'pregunta': "¿Que es el fondo de emergencia?",
        'respuesta': """<br>El fondo de emergencia es una parte esencial dentro de cualquier estrategia de inversión. Su objetivo no es generar grandes ganancias, sino proteger tus inversiones y tu estabilidad financiera ante imprevistos.<br><br>

Cuando inviertes, tu dinero puede estar en instrumentos que suben y bajan de valor con el tiempo. Si ocurre una urgencia —como perder el empleo o tener un gasto médico inesperado— podrías verte obligado a vender tus inversiones en un mal momento, perdiendo dinero. El fondo de emergencia evita justamente eso.<br><br>

<b>1. ¿Para qué sirve dentro de la inversión?</b><br>
Actúa como un “colchón financiero” que te da liquidez inmediata sin tener que tocar tus inversiones a largo plazo. En otras palabras, te permite mantener la calma y no vender en pérdidas.<br><br>

<b>2. ¿Cuánto debería tener?</b><br>
Generalmente se recomienda ahorrar entre 3 y 6 meses de tus gastos mensuales fijos. Si tu trabajo o fuente de ingresos es inestable, puedes ampliar ese margen.<br>
- Si gastas $500.000 al mes, tu fondo debería estar entre $1.500.000 y $3.000.000.<br>
- Si eres independiente o tienes ingresos variables, apunta a cubrir entre 6 y 9 meses de gastos.<br><br>

<b>3. ¿Dónde guardarlo?</b><br>
Debe estar en instrumentos seguros, líquidos y de bajo riesgo, aunque no renten mucho. Algunas opciones populares en Chile son:<br>
- Cuenta 2 de AFP: permite retirar el dinero rápidamente y tiene baja volatilidad.<br>
- Fondo “Rita Conservadora” de Fintual: pensado para objetivos de corto plazo con liquidez diaria.<br>
- Cuentas de ahorro a la vista o depósitos a plazo flexibles en bancos confiables.<br><br>

<b>4. Consejo clave:</b><br>
El fondo de emergencia no es una inversión en sí, sino un <b>seguro que protege tus inversiones reales</b>. Te permite invertir con mayor confianza, sabiendo que si ocurre algo inesperado, no tendrás que vender tus activos justo cuando el mercado cae.<br><br>

<b>5. Mantenlo separado:</b><br>
Guarda tu fondo de emergencia en una cuenta distinta de tus inversiones o gastos diarios. Así evitarás gastarlo por impulso o mezclarlo con dinero destinado a invertir.<br><br>

Un inversionista sin fondo de emergencia está construyendo sobre terreno inestable. Antes de buscar rentabilidad, asegúrate de tener estabilidad.<br><br>
Fuentes usadas:<br>
- <a href= "https://btgpactual.cl/inversiones-digitales/blog/aprende/finanzas-personales/como-crear-un-fondo-de-emergencia/" target="_blank">btgpactual</a><br>
- <a href= "https://www.cmfchile.cl/portal/prensa/615/w3-article-94614.html" target="_blank">cmf chile</a><br>
""",
'imagen_respuesta':'inversion_2.webp',
    },
    11: {
        'pregunta': "¿Que efecto tiene la inflacion?",
        'respuesta': """<br>La inflación es uno de los factores más importantes a considerar al invertir, porque afecta directamente el <b>poder adquisitivo de tu dinero</b>. En términos simples, la inflación es el aumento sostenido de los precios en una economía. Esto significa que con el tiempo, el mismo monto de dinero compra menos bienes y servicios.<br><br>

Por ejemplo, si hoy con $10.000 puedes comprar una determinada cantidad de productos, y la inflación es de un 5% anual, el próximo año necesitarás $10.500 para comprar exactamente lo mismo. Esa pérdida de valor es invisible, pero real.<br><br>

<b>1. Por qué es importante para los inversionistas:</b><br>
- La inflación reduce el valor del dinero guardado sin invertir.<br>
- Obliga a los inversionistas a buscar instrumentos que superen o al menos igualen la tasa de inflación.<br>
- Impacta de forma distinta según el tipo de inversión: los instrumentos de renta fija (como depósitos a plazo) sufren más con inflación alta, mientras que los activos reales o variables (como acciones o fondos ligados a la UF) pueden ofrecer mejor protección.<br><br>

<b>2. Cómo protegerte de la inflación:</b><br>
- Prefiere instrumentos que ajusten su valor con la inflación, como depósitos o bonos en UF (Unidad de Fomento).<br>
- Considera invertir parte de tu dinero en ETFs o fondos que incluyan activos internacionales, ya que te exponen a economías con diferentes niveles de inflación.<br>
- No dejes grandes montos guardados en efectivo o cuentas sin interés, ya que pierden valor cada mes.<br><br>

<b>3. Inflación y rentabilidad real:</b><br>
Lo importante no es solo cuánto ganas, sino cuánto ganas “en términos reales”. Si una inversión te da 4% anual y la inflación es del 5%, en realidad tu rentabilidad real es -1%. Estás perdiendo poder adquisitivo, aunque veas tu saldo subir.<br><br>

<b>4. Qué mirar en Chile:</b><br>
En Chile, la inflación se mide a través del Índice de Precios al Consumidor (IPC). Puedes revisar su evolución mensual en la página del <a href="https://www.ine.cl" target="_blank">Instituto Nacional de Estadísticas (INE)</a>.<br>
Además, el valor de la UF (Unidad de Fomento) se ajusta diariamente según el IPC, por lo que muchas inversiones la utilizan como referencia para mantener su valor real en el tiempo.<br><br>

La inflación es el enemigo silencioso del dinero inmóvil. Un buen inversionista entiende que no basta con ahorrar o invertir, sino hacerlo de forma que el dinero crezca más rápido de lo que suben los precios.<br><br>
Fuentes usadas:<br>
- <a href= "https://www.getsmarteraboutmoney.ca/learning-path/understanding-risk/inflation-your-investments/" target="_blank">getsmarter</a><br>
- <a href= "https://www.principal.cl/informate/blog/actualidad/impacto-de-la-inflacion" target="_blank">principal</a><br>
""",
'imagen_respuesta':'inversion_3.avif',
    },
    12: {
        'pregunta': "¿Como funciona el interes compuesto?",
        'respuesta': """<br>El interés compuesto es una de las fuerzas más poderosas del mundo de las inversiones. Se le llama así porque los intereses que ganas se reinvierten automáticamente, generando nuevos intereses sobre las ganancias anteriores. Es decir, tu dinero empieza a trabajar para ti, y después tus ganancias también trabajan por ti.<br><br>

A diferencia del interés simple —donde siempre ganas lo mismo sobre tu monto inicial— el interés compuesto hace que tus ganancias crezcan como una bola de nieve: pequeñas al principio, pero enormes con el paso de los años. Es la razón por la que los inversionistas exitosos valoran tanto el tiempo y la constancia.<br><br>

<b>1. El poder del tiempo en la inversión:</b><br>
El interés compuesto premia la paciencia. Cuanto antes empieces a invertir, aunque sea con montos pequeños, más tiempo tendrá tu dinero para multiplicarse. Por ejemplo, si inviertes $500.000 a una rentabilidad del 8% anual, al cabo de 10 años tendrás más de $1.000.000. Pero si mantienes esa inversión durante 20 años, el monto se acerca a los $2.300.000, sin agregar un peso más. Esa diferencia se debe solo al tiempo y a la reinversión de intereses.<br><br>

En palabras simples, el tiempo es más importante que el dinero. No necesitas grandes sumas para generar riqueza, sino empezar pronto y dejar que el interés compuesto haga su trabajo.<br><br>

<b>2. Cómo se calcula de forma sencilla:</b><br>
El funcionamiento del interés compuesto puede entenderse así:<br>
Monto final = dinero inicial + (interés sobre ese dinero) + (interés sobre los intereses generados)<br><br>
Cada periodo —ya sea un mes, trimestre o año— los intereses se suman al capital y se reinvierten, por lo que la base de cálculo crece constantemente. Mientras más tiempo dejes tu dinero invertido, más rápido se acumulará el efecto.<br><br>

<b>3. Un ejemplo realista en Chile:</b><br>
Imagina que inviertes $100.000 mensuales en un fondo que da un rendimiento promedio del 6% anual. Si mantienes ese ritmo durante 10 años, tendrás alrededor de $16 millones. Pero si sigues 10 años más, el monto casi se duplica, alcanzando cerca de $31 millones. Lo impresionante es que el segundo tramo de 10 años genera casi lo mismo que el primero, sin que hayas invertido un peso adicional. Eso es el interés compuesto en acción.<br><br>

<b>4. Consejos para aprovecharlo al máximo:</b><br>
- Empieza cuanto antes, aunque el monto sea pequeño. La constancia vale más que la cantidad.<br>
- Reinvierte siempre tus rendimientos o dividendos; no los retires si no los necesitas.<br>
- Evita cambiar de inversión con frecuencia, ya que cada cambio o retiro detiene el crecimiento compuesto.<br>
- Piensa en el largo plazo: los primeros años los resultados son modestos, pero con el tiempo se aceleran de forma notable.<br><br>

<b>5. Herramientas para visualizarlo:</b><br>
Hoy existen plataformas que te permiten simular el crecimiento de tus inversiones a lo largo del tiempo. En Chile puedes usar:<br>
- <a href="https://www.fintual.cl" target="_blank">Fintual</a>, que muestra cómo evoluciona tu inversión con interés compuesto a distintos plazos.<br>
- <a href="https://www.calculadorafinanciera.cl/interes-compuesto" target="_blank">Calculadora Financiera</a>, donde puedes estimar tus ganancias según monto, plazo y rentabilidad.<br>
- También puedes hacerlo en una hoja de Excel o Google Sheets, multiplicando cada periodo por su rentabilidad acumulada.<br><br>

<b>6. Una reflexión clave:</b><br>
El interés compuesto no depende de la suerte ni del mercado, sino de tus hábitos. Si inviertes con constancia, paciencia y sin retirar tus ganancias, el crecimiento será inevitable. En cambio, si retiras dinero con frecuencia, el ciclo se interrumpe y pierdes su efecto acumulativo.<br><br>

El interés compuesto es el motor silencioso del crecimiento financiero. Transforma pequeñas decisiones constantes en grandes resultados futuros. Mientras algunos buscan “la mejor inversión”, los inversionistas inteligentes se enfocan en dejar que el tiempo y la disciplina hagan el trabajo.<br><br>
Fuentes usadas:<br>
- <a href= "https://www.bbva.com/es/salud-financiera/guia-de-finanzas-para-no-financieros-interes-compuesto/" target="_blank">cmf chile</a><br>
- <a href= "https://ayuda.fintual.cl/es/articles/5152246-las-inversiones-de-fintual-usan-interes-compuesto" target="_blank">ayuda fintual</a><br>
""",
'imagen_respuesta':'inversion_4.png',
    },
    13: {
        'pregunta': "¿Que es el riesgo y retorno?",
        'respuesta': """<br>Cuando hablamos de invertir, el riesgo y el retorno (también llamado rentabilidad) son dos conceptos que van siempre de la mano. Entender su relación es fundamental para tomar buenas decisiones financieras y no dejarse llevar solo por la emoción o la promesa de ganar rápido.<br><br>

<b>1. Qué significa el riesgo:</b><br>
El riesgo es la posibilidad de que una inversión no salga como esperabas. En otras palabras, es la probabilidad de perder parte o todo el dinero invertido, o de ganar menos de lo que pensabas. Todas las inversiones tienen cierto nivel de riesgo: unas más, otras menos. Por ejemplo:<br>
- Un depósito a plazo tiene riesgo bajo, porque prácticamente siempre te devuelve tu dinero con un pequeño interés.<br>
- Las acciones o criptomonedas tienen riesgo alto, ya que su valor puede subir o bajar de forma rápida e impredecible.<br><br>

<b>2. Qué es el retorno:</b><br>
El retorno es la recompensa que obtienes por asumir ese riesgo. Se mide en porcentaje y representa cuánto ganas (o pierdes) respecto a lo que invertiste. Por ejemplo, si inviertes $100.000 y ganas $10.000, tu retorno fue del 10%.<br><br>

<b>3. La regla más importante:</b><br>
En inversión, siempre existe una relación directa: a mayor riesgo, mayor retorno potencial. Pero también mayor posibilidad de pérdida. Y al contrario: las inversiones más seguras suelen ofrecer retornos más pequeños. El secreto está en encontrar el equilibrio que se ajuste a tu perfil y tus metas personales.<br><br>

<b>4. Cómo decidir cuánto riesgo tomar:</b><br>
Antes de invertir, es importante conocer tu perfil de riesgo. Este perfil depende de tu edad, tus ingresos, tus objetivos y tu tolerancia emocional ante las pérdidas. Por ejemplo:<br>
- Si eres joven y tienes metas a largo plazo (como comprar una casa o jubilarte), puedes asumir un poco más de riesgo, ya que tienes tiempo para recuperarte si algo baja de valor.<br>
- Si necesitas el dinero pronto o no te sientes cómodo viendo que tus inversiones bajan temporalmente, es mejor optar por instrumentos más seguros y estables.<br><br>

<b>5. La importancia del equilibrio:</b><br>
Un inversionista inteligente no busca eliminar el riesgo, sino administrarlo. Eso se logra diversificando (como vimos antes) y combinando inversiones de bajo y alto riesgo para equilibrar el retorno total del portafolio. Por ejemplo:<br>
- 60% en inversiones seguras (depósitos a plazo, bonos).<br>
- 40% en inversiones con más potencial (acciones, fondos internacionales).<br><br>

<b>6. Un ejemplo simple:</b><br>
Imagina que tienes dos opciones:<br>
- Opción A: invertir en un fondo de renta fija que te da un 4% anual con bajo riesgo.<br>
- Opción B: invertir en un fondo de acciones que promete un 10% anual, pero puede subir o bajar según el mercado.<br><br>
Si mezclas ambas, podrías obtener un retorno intermedio, pero con menor riesgo de pérdida total. Esa es la idea: encontrar un punto medio donde tus inversiones te hagan crecer, pero sin poner en juego toda tu tranquilidad.<br><br>

<b>7. Consejos útiles para principiantes:</b><br>
- No te dejes llevar solo por la rentabilidad prometida; revisa siempre qué tan seguro es el instrumento.<br>
- Aprende a revisar el historial de rendimiento y la volatilidad de los fondos antes de invertir.<br>
- Si quieres medir el riesgo y retorno de tus inversiones, puedes usar herramientas como las que ofrecen <a href="https://www.fintual.cl" target="_blank">Fintual</a>, <a href="https://www.felp.cl" target="_blank">FELP</a> o <a href="https://www.cmfchile.cl" target="_blank">la CMF</a>, donde podrás comparar distintos instrumentos financieros chilenos.<br><br>

El riesgo y el retorno son dos caras de la misma moneda. No se trata de evitar el riesgo, sino de conocerlo y usarlo a tu favor. Cuanto más claro tengas tus objetivos y tu tolerancia al cambio, más fácil será tomar decisiones que te acerquen a tus metas sin perder la calma ni el control de tu dinero.<br><br>
Fuentes usadas:<br>
- <a href= "https://www.cmfchile.cl/educa/621/w3-article-510.html" target="_blank">cmf chile</a><br>
- <a href= "https://www.cmfchile.cl/portal/principal/613/w3-article-607" target="_blank">cmf chile</a><br>
- <a href= "https://www.df.cl/opinion/columnistas/riesgo-en-inversiones" target="_blank">diario finanzas</a><br>""",
'imagen_respuesta':'inversion_5.webp',
    },
    14: {
        'pregunta': "¿Que es el horizonte de inversion?",
        'respuesta': """<br>Empezar a invertir puede ser emocionante, pero también es un terreno lleno de trampas para quienes recién comienzan. Los errores más comunes no suelen venir de la falta de dinero o conocimientos técnicos, sino de la impaciencia, el miedo o el exceso de confianza. Entenderlos es clave para construir una mentalidad sólida y evitar perder dinero por decisiones impulsivas.<br><br>

<b>1. No tener un objetivo claro antes de invertir:</b><br>
Uno de los primeros errores es invertir sin saber para qué. Muchas personas colocan dinero en fondos o acciones solo porque escucharon que “están subiendo”, sin definir un propósito ni un plazo. Invertir sin objetivo es como subirse a un barco sin saber a qué puerto quieres llegar. Antes de mover tu dinero, define si buscas ahorrar para un proyecto, protegerte de la inflación o construir patrimonio a largo plazo.<br><br>

<b>2. Invertir dinero que podrías necesitar pronto:</b><br>
Otro error común es usar dinero destinado a gastos próximos o emergencias. Esto puede obligarte a vender tus inversiones en el peor momento, perdiendo parte de lo invertido. Por eso siempre se recomienda tener un fondo de emergencia antes de empezar a invertir, y usar solo el dinero que no afecte tu día a día.<br><br>

<b>3. Buscar ganancias rápidas:</b><br>
El deseo de “hacerse rico rápido” es probablemente el error más caro. Los nuevos inversionistas muchas veces caen en modas o recomendaciones virales sin analizar los riesgos. La inversión real se basa en el tiempo, la paciencia y el interés compuesto, no en la suerte o la especulación. Como se dice en finanzas: “quien busca doblar su dinero rápido, suele terminar perdiéndolo igual de rápido”.<br><br>

<b>4. No diversificar:</b><br>
Poner todo tu dinero en un solo lugar es una receta para el desastre. Si esa inversión falla, pierdes todo. En cambio, al diversificar —es decir, repartir tu dinero entre distintos activos como fondos, acciones o bonos— reduces el impacto de los errores o las caídas del mercado. Los ETFs son una excelente forma de hacerlo, ya que te permiten invertir en muchos activos con una sola compra.<br><br>

<b>5. No conocer tu nivel de riesgo:</b><br>
Cada persona tiene una tolerancia diferente al riesgo. Algunos se sienten cómodos viendo subir y bajar sus inversiones, mientras que otros se desesperan si pierden un poco. Si inviertes sin conocer tu perfil de riesgo, puedes terminar tomando decisiones impulsivas, como vender cuando el mercado baja. Las plataformas de inversión suelen ofrecer cuestionarios para ayudarte a descubrir tu perfil y elegir las opciones adecuadas.<br><br>

<b>6. Dejarse llevar por las emociones:</b><br>
Las emociones son uno de los enemigos más grandes del inversionista. El miedo, la euforia o la ansiedad pueden hacerte actuar en el momento equivocado. La clave es mantener la cabeza fría, no reaccionar por impulsos y seguir tu plan. Recuerda: los mercados suben y bajan, pero solo pierde quien se sale del camino antes de tiempo.<br><br>

<b>7. No informarse lo suficiente:</b><br>
Muchos comienzan a invertir sin entender cómo funciona lo que están comprando. Antes de invertir, dedica tiempo a leer, ver videos o usar simuladores. En Chile, puedes aprender gratuitamente en portales como <a href="https://www.cmfchile.cl" target="_blank">la CMF</a>, <a href="https://www.fintual.cl" target="_blank">Fintual</a> o <a href="https://www.bcentral.cl" target="_blank">el Banco Central</a>, donde hay recursos para principiantes.<br><br>

<b>8. No tener paciencia:</b><br>
La inversión es una carrera de largo aliento. Muchos se frustran porque no ven resultados inmediatos y abandonan antes de tiempo. Pero los grandes resultados llegan con el tiempo, gracias al poder del interés compuesto. La clave está en ser constante, revisar tus metas periódicamente y dejar que el tiempo haga su trabajo.<br><br>


Invertir no es un acto de suerte, sino de estrategia. Aprende de cada error, por pequeño que sea, y usa esa experiencia para mejorar. La meta no es evitar equivocarte, sino convertirte en alguien que sabe cómo reaccionar cuando el mercado cambia. En el mundo de las inversiones, la paciencia y la educación valen más que cualquier consejo rápido.<br><br>
Fuentes usadas:<br>
- <a href= "https://www.moonfare.com/glossary/time-horizon" target="_blank">moonfare</a><br>
""",
'imagen_respuesta':'inversion_6.png',
    },
    15: {
        'pregunta': "¿Que es diversificaion?",
        'respuesta': """<br>La diversificación es uno de los principios más importantes de toda estrategia de inversión. En palabras simples, significa no poner todos los huevos en la misma canasta. Su objetivo es reducir el riesgo sin tener que renunciar completamente a la rentabilidad. En lugar de depender del éxito o fracaso de una sola inversión, se busca equilibrar el portafolio para que unas ganancias compensen las posibles pérdidas de otras.<br><br>

Cuando una persona principiante empieza a invertir, suele concentrar todo su dinero en un solo activo o tipo de inversión: por ejemplo, en acciones de una empresa, o en un depósito a plazo. El problema es que si ese activo falla, todo el capital se ve afectado. La diversificación evita eso, distribuyendo el dinero entre distintas opciones, sectores o incluso países.<br><br>

<b>1. ¿Por qué es tan importante?</b><br>
El mercado financiero es impredecible. Un año las acciones pueden subir mucho, y al siguiente caer. Un fondo inmobiliario puede tener rendimientos estables, mientras las criptomonedas bajan. Nadie puede anticipar todo, por eso la diversificación actúa como una red de seguridad. No elimina el riesgo, pero lo reparte. De esta forma, si una inversión va mal, no afecta todo tu portafolio.<br><br>

<b>2. Cómo se puede diversificar:</b><br>
- Diversifica por tipo de activo: combina renta fija (bonos, depósitos a plazo) con renta variable (acciones, fondos mutuos, ETFs).<br>
- Diversifica por sector económico: no inviertas solo en tecnología o minería, incluye rubros como salud, energía, consumo o infraestructura.<br>
- Diversifica por ubicación geográfica: mezcla inversiones chilenas con internacionales, ya que las economías no siempre se comportan igual.<br><br>

<b>3. El papel de los ETFs y fondos mutuos:</b><br>
Los ETFs (Exchange Traded Funds) y los fondos mutuos son herramientas ideales para lograr diversificación sin tener que comprar decenas de activos distintos. Por ejemplo, un solo ETF puede incluir acciones de cientos de empresas en todo el mundo. Así, al invertir en uno, automáticamente estás distribuyendo tu riesgo entre muchos sectores y países.<br><br>

En Chile, plataformas como <a href="https://www.fintual.cl" target="_blank">Fintual</a>, <a href="https://www.banchileinversiones.cl" target="_blank">Banchile Inversiones</a> o <a href="https://www.inversiones.security.cl" target="_blank">Security Inversiones</a> ofrecen fondos con distintos niveles de riesgo y composición, permitiéndote diversificar sin conocimientos avanzados.<br><br>

<b>4. Cómo encontrar tu equilibrio:</b><br>
Diversificar no significa invertir al azar, sino armar una combinación coherente con tus objetivos y tolerancia al riesgo. Por ejemplo:<br>
- Si tu meta es a corto plazo, podrías tener más renta fija y menos renta variable.<br>
- Si tu meta es a largo plazo (más de 5 años), puedes asumir más riesgo y aumentar la proporción de acciones o ETFs globales.<br><br>

<b>5. Una forma de pensar la diversificación:</b><br>
Imagina que cada tipo de inversión es una pierna de una mesa. Si la mesa tiene solo una pierna, cualquier movimiento la derriba. Pero si tiene varias, puede mantenerse firme incluso si una falla. Así funciona la diversificación: le da estabilidad a tu dinero, aun cuando el mercado se mueve.<br><br>

<b>6. Errores comunes que debes evitar:</b><br>
- Poner todo el dinero en una inversión “de moda”.<br>
- No revisar la proporción de tus inversiones cada cierto tiempo.<br>
- Creer que diversificar significa tener muchas inversiones del mismo tipo (por ejemplo, varios fondos chilenos que en realidad invierten en lo mismo).<br><br>

La <b>diversificación es el escudo del inversionista inteligente</b>. No se trata solo de buscar ganancias, sino de proteger lo que tienes. Un portafolio diversificado resiste mejor las crisis, se adapta a los cambios del mercado y permite que tus inversiones crezcan de forma más estable y segura en el tiempo.<br><br>
Fuentes usadas:<br>
- <a href= "https://www.blackrock.com/mx/intermediarios/educacion/que-es-diversificacion" target="_blank">blackrock</a><br>
- <a href= "https://chile.larrainvial.com/lv-insights/finanzas-personales/todos-hablan-de-diversificacion-pero-que-es-realmente" target="_blank">larrainvial</a><br>
""",
'imagen_respuesta':'inversion_7.jpg',
    },
    # recuerdo pa tontos:
    # 3: {'pregunta': "¿Qué hago con un ingreso extra?", 'respuesta': "nadota we"
    16: {
        'pregunta': "¿Como debería empezar?",
        'respuesta': """<br>Lo primero que debemos entender es que no requerimos de tener un gran presupuesto, en la actualidad hay muchas formas de poder invertir gracias
a la gran cantidad de metodos y plataformas digitales que existen hoy en dia, las cuales permiten una inversion tomando en cuenta los presupuestos bajos, pero si tenemos que tener claro ciertos aspecto antes de empezar.<br><br>

<b>1. Cambiar la mentalidad es el primer paso:</b><br>
Invertir no es un privilegio de unos pocos, sino una herramienta para cualquiera que quiera mejorar su situación financiera. El error más grande no es tener poco dinero, sino no comenzar nunca. La inversión es un hábito, no un evento. Aunque empieces con $10.000 o $20.000 al mes, lo importante es la constancia, no la cantidad.<br><br>

<b>2. Aprovechar las plataformas digitales:</b><br>
Hoy existen muchas aplicaciones y sitios web que permiten invertir montos pequeños y de manera sencilla, sin trámites complicados ni grandes comisiones. En Chile, algunas opciones populares son:<br>
- <a href="https://www.fintual.cl" target="_blank">Fintual</a>: permite invertir desde $1.000 en fondos diversificados según tu perfil y objetivo.<br>
- <a href="https://www.cuotonline.cl" target="_blank">Cuotonline</a>: ofrece acceso a fondos mutuos nacionales e internacionales con bajos montos de entrada.<br>
- <a href="https://www.uf.cl" target="_blank">Tenpo Inversiones</a> o <a href="https://www.smartbricks.cl" target="_blank">SmartBricks</a>: plataformas que facilitan invertir en cuotas de instrumentos o bienes con bajos aportes iniciales.<br><br>

<b>3. Definir un objetivo concreto:</b><br>
Incluso si empiezas con poco, necesitas tener claro para qué estás invirtiendo. No se trata solo de “ver crecer el dinero”, sino de darle una dirección. Por ejemplo:<br>
- Ahorrar para un viaje o proyecto personal.<br>
- Construir un fondo de retiro o jubilación complementario.<br>
- Protegerte frente a la inflación o devaluación del dinero.<br><br>
Cuando tienes una meta clara, es más fácil mantener la constancia y resistir la tentación de retirar el dinero antes de tiempo.<br><br>

<b>4. Aprovechar el poder del interés compuesto:</b><br>
Aunque empieces con montos pequeños, el tiempo puede transformar una inversión modesta en una suma importante gracias al interés compuesto. Esto significa que los intereses que ganas también empiezan a generar más intereses, creando un efecto acumulativo. Mientras antes comiences, mayor será ese crecimiento, incluso si los aportes mensuales son bajos.<br><br>

<b>5. Usar estrategias automáticas:</b><br>
La mayoría de las plataformas permiten automatizar los aportes. Por ejemplo, puedes programar que todos los meses se inviertan $10.000 desde tu cuenta bancaria. Esta es una forma de “obligarte” a ser constante sin tener que pensarlo demasiado, convirtiendo el ahorro y la inversión en un hábito natural.<br><br>

<b>6. Diversificar aunque sea con poco:</b><br>
Aunque tengas poco dinero, puedes diversificar fácilmente usando fondos mutuos o ETFs. Estos instrumentos agrupan muchas inversiones dentro de una sola, por lo que tu dinero se reparte entre distintas empresas o activos sin que tengas que comprarlos uno por uno. Es una manera inteligente de reducir el riesgo desde el primer día.<br><br>

<b>7. Evitar los errores más comunes:</b><br>
Cuando se empieza con poco dinero, es común caer en errores por ansiedad o desconocimiento. Algunos ejemplos son:<br>
- Sacar la inversión antes de tiempo porque no se ven resultados inmediatos.<br>
- Seguir consejos de redes sociales sin entender el riesgo.<br>
- Invertir en cosas que no comprendes (como criptomonedas sin estudiar el tema).<br><br>
La clave está en la educación: entender en qué estás invirtiendo, cuánto riesgo estás dispuesto a asumir y cómo se comporta el instrumento con el tiempo.<br><br>

<b>8. Un ejemplo simple:</b><br>
Supongamos que inviertes $10.000 mensuales durante 5 años en un fondo que rinde un 6% anual. Al final del período habrás aportado $600.000, pero gracias al interés compuesto podrías tener cerca de $700.000. No te harás rico, pero habrás dado un gran paso: pasaste de “guardar dinero” a “hacer que el dinero trabaje por ti”.<br><br>
Fuentes usadas:<br>
- <a href= "https://www.cmfchile.cl/portal/principal/613/w3-article-821" target="_blank">cmf chile</a><br>
- <a href= "https://www.cmfchile.cl/educa/621/w3-article-1654.html" target="_blank">cmf chile</a><br>
- <a href= "https://www.bbva.com/es/12-errores-tipicos-que-debes-evitar-a-la-hora-de-invertir-2/" target="_blank">bbva</a><br>
""",
'imagen_respuesta':'inversion_8.webp',
    },
}

def textos_view(request):
    
    preguntas_ids = range(1, 17) 
    
    contexto = {
        'titulo_pagina': 'Preguntas y Respuestas',
        'preguntas_ids': preguntas_ids
    }
    return render(request, 'textos/index.html', contexto)

# Vista de Detalle (Para la respuesta bonita)
def pregunta_detalle(request, pregunta_id):
    pregunta_id = int(pregunta_id)
    if pregunta_id not in RESPUESTAS_FIJAS:
        raise Http404("La pregunta solicitada no existe")
    datos_pregunta = RESPUESTAS_FIJAS[pregunta_id]
    

    contexto = {
        'titulo_pagina': datos_pregunta['pregunta'],
        'respuesta_bonita': mark_safe(datos_pregunta['respuesta']),
        'imagen_respuesta': datos_pregunta['imagen_respuesta'],
    }
    return render(request, 'textos/preguntas_detalle.html', contexto)