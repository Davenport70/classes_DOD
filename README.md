# OOP Basics

This repo will contain our OOP basics

We will look at:
- Abstraction
- Encapsulation
- Inheritance
- Polymorphism

### Class 
```
Is like a cookie cutter, that creates instances of cookies.

They wrap to define how an object looks and behaves.

Classes will wrap characteristics as attributes, and behaviours as methods.
```

### method VS functions
```
Methods are functions that belong to a specific data type.

Where functions are annonymous and anything can call and run them.

Where as **methods NEED the instance to be called**
```
### Characteristics / how an object looks like
```
these are attributes that are assigned to each instance.
```
## Instance
```
occurance of something.
```

### Self
```
Refers to the instance on which a method is being called.

self.name = 'ringo'

this means that specific object attribute name will have the string';ringo'
```
## Abstraction
```
The ability to hide complexity.

We do this using:
- Seperation of concerns
- documentation
    - specify which methods and how to use them.
- Inheritance --> causes some abstraction

real life examples are everywhere:
- changing gears
- heating up food with one button
- using our cards to pass security
## Inheritance
Is the ability to pass to child class all the methods and characteristics. 
This is one of the big reasons for OOP - it means you can re-use code!

you do this by passing the parent class as an argument of the child class

``` 
python

class Animal():
     pass
     
class Reptile(Animal):
    pass
```

**PROMISE OF RE-USABLE CODE**


## Encapsulation



## Polymorphism

It is the ability to **completely override methods**, and if need be, recall method from parent class using .super()

CRUD(Create, Read, Update, Delete)