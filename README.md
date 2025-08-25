
# Object-Oriented Programming

## Advanced OOP Topics
- ✅ Decorators  
- ✅ Core syntax implementation  
- ✅ Class & static methods  
- ✅ Abstract methods  
- ✅ Inheritance vs. composition  
- ✅ Attribute encapsulation  
- ✅ Exception chaining  
- ✅ Object persistence  
- ✅ Metaprogramming
- 
## Key Concepts
- **class** → blueprint / recipe for instances
- **instance** → instantiation of a class (a.k.a. object)
- **object** → representation of data + methods
- **attribute** → trait of class/object (variable or method)
- **method** → function defined in a class, bound to objects
- **type** → the class used to instantiate an object

⚡️ **Remember**: Even classes are instances in Python (metaclasses).

# Classes in Python

## Definition
- A **class** expresses an idea; it’s a blueprint or recipe for an instance. It describes **attributes** (data) + **methods** (behavior). In other words, a **class** is a place which binds data with the code.

## Inheritance
- Classes can:
  - **Inherit** from other classes → specialized subclasses
  - Be **superclasses** → base for other classes

---

## Syntax Example
```python
class Duck:
    def __init__(self, height, weight, sex):
        self.height = height
        self.weight = weight
        self.sex = sex

    def walk(self):
        pass

    def quack(self):
        print("Quack")
```
# Instances vs Objects

## Definitions
- **Instance** → one specific instantiation of a class
  - Occupies memory
  - Has its own data (state)
  - Accessed with `self` inside class

- **Object** → *everything* in Python (class, instance, list, dict, function, etc.)

- ⚡️ The term **instance** is very often used interchangeably with the term **object**, because **object** refers to a particular instance of a class. It’s a bit of a simplification, because the term **object** is more general than **instance**.

## Relation
- One **class** → unlimited **instances**
- **State** = per-instance variables (attributes)
- **Behavior** = shared methods (functions bound to class)

## Example
```python
duckling = Duck(height=10, weight=3.4, sex="male")
drake   = Duck(height=25, weight=3.7, sex="male")
hen     = Duck(height=20, weight=3.4, sex="female")
```
# Attributes in Python

## Definition
- **Attribute** = class trait (two kinds):
  - **Variables** → hold data (per-class or per-instance)
  - **Methods** → functions bound to class/instance (*callable attributes*)

⚡️ Methods are just **callable attributes**.

## Attribute Access
- **Dot notation** → `object.attribute`
- Built-ins:
  - `getattr(obj, "attr")` → get attribute dynamically

# Type in Python

## Definition
- **type** = fundamental and abstract concept in Python
  - Base of all classes (every class ultimately inherits from `type`)
  - Describes *what kind* of object something is
  - A **function** that:
    - With **1 arg** → returns the object’s class
    - With **3 args** → creates a new type (used in metaclasses)

## Example
```python
class Duck:
    def __init__(self, sex):
        self.sex = sex
    def quack(self):
        print("Quack")

duckling = Duck("male")

print(type(Duck))           # <class 'type'>
print(type(duckling))       # <class '__main__.Duck'>
print(type(duckling.sex))   # <class 'str'>
print(type(duckling.quack)) # <class 'method'>
