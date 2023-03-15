# Factory or Abstract Factory patrón de diseño

- Presentación: explicación del patrón de diseño
- Diagrama de clases: Diagrama de clases para el patrón definido
- Codigo: Que funcione, lenguaje to your choice

## Buscar

Buscar información, los ejemplos se encuentran de manera más frecuente implementado el abstract factory

## Factory design pattern

El patrón de diseño factory hacer parte de uno de los modelos descritos por
cuatro ingenieros en C los cuales escribieron el libro *Design Patterns - Elements of reausable Object oriented Software*
el cual describe a la perfección los modelos y patrones de diseño que permiten
a la resolución de problemas que se pueden enfrentar en la creación de software


Los modelos descritos son los siguients:

- Patrón Creacional: Como los objetos són creados
- Patrón Estructural: Como estos objetos se relacionan unos con los otros
- Patrón de Comportamiento: Como estos objetos se comunican unos con otros

El patrón de diseño factory se caracteriza por lo siguiente:

- **En vez de usar la palabra reservada new para la instanciar el objeto, se usa un metodo o función que lo haga por nosotros**

Ejemplo

- Tenemos una app movíl multiplataforma que correra en IOS o android dependiendo de los requerimientos del cliente
- Queremos implementar un botón básico para la plataforma pero para esto debemos usar condicionales para poder determinar que botón debemos crear 

A largo este codigo no es mantenible, ya que el estar validando la condicional para crear
un botón a largo plazo se vuelve repetitivo

- Se crea un clase auxiliar o función que nos permita determinar cual botón se debe crear
ahora en vez de repetir la logíca condicional usamos la subclase para crear los botónes según la plataforma

```
class AndroidButton:
    pass

class IOSButton:
    pass

# Definimos la clase Factory para crear nuestro botón

class ButtonFactory:
    def create_button(self, os):
        if os == 'ios':
            return IOSButton
        else:
            return AndroidButton


factory = ButtonFactory()
button = factory.create_button('ios')

```

# Ejemplo

Imaginemos que queremos una hamburguesa, pero no quieres tener que saber que ingredientes lleva la hamburguesa, por lo que solo quieres ordenarla
podemos usar el patrón de diseño factory poder tener la función ordenar hamburguesa  

## Pros y contras del patrón

- **Pros**
    - Evitamos un acoplamiento fuerte entre el creador y los productos concretos
    - Podemos mover el código de creación de producto a un lugar del programa, haciendo que el código sea más facil de mantener
    - Podemos incorporar nuevos tipos de productos en el programa sin descomponer el código fuente exisitente
    
- **Cons**
    - Al momento de ir incorporando productos, el código que se produce se puede volver complejo, ya que debes implementar nuevas
      subclases al momento de implementar el patrón

## TIPS: 

- Se debe mirar el codigo en que ide fue implementado

> Contacto: carloaiza@umanizales.edu.co, Telefono: 3016052808

