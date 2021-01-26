def CountLetters(message):
    letters = {}
    for letter in message:
        letters.setdefault(letter, 0)
        letters[letter] = letters[letter] + 1
    print(letters)

message = ('''Uy, ayer te pensé más de una vez
y no logro sacarte de mi mente
Ey mami tú, te vistes tan fina y elegante
muy diferente y lo sabes

Di que me quieres que yo soy tu girl
Que no puedes vivir sin mi calor, confiésalo
Que no te duermes sin pensar en mí
Que quieres que te de to' mi amor, confiésalo

Cuando suena el tema nena pegate
Tenía mil pretendientes y yo me adelanté
En tu relación pasada perdiste la fe
Yo te enamoré, te comí otra vez
Recién bañadita quitarte la toalla
Nena yo quiero que tú nunca te vayas
En la cama ella lo hace como Sasha
Tiene tanta clase que ella ni lo ensaya
Que ganas de comerte
Aquí otra vez tenerte
Eres mi girl por siempre
Mami estoy esperando tu call

Y si tú me pasas tu ubicación
Enseguida yo me pongo en acción
Nos vamos directo a la situación
De fondo sonando nuestra canción
Dice que a nadie más necesita
Que si muere hoy por mi resucita
Que soy más buena que el agua bendita
De toda la nena la más bonita

Haces que enloquezca con solo bailarme así
bien pegada a mi,
Me he vuelto loco sabiendo que eres para mi
Solita pa mi

Di que me quieres que yo soy tu girl
Que no puedes vivir sin mi calor, confiésalo
Que no te duermes sin pensar en mí
Que quieres que te de to' mi amor, confiésalo

Dice que a nadie más necesita
Que si muere hoy por mi resucita
Que soy más buena que el agua bendita
De toda la nena la más bonita

Uy, ayer te pensé más de una vez
y no logro sacarte de mi mente

Di que me quieres que yo soy tu girl
Que no puedes vivir sin mi calor, confiésalo
Que no te duermes sin pensar en mi
Que quieres que te de to' mi amor, confiésalo


''')

CountLetters(message)
