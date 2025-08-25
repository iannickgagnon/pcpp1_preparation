
# Introduction

Sometimes I like to challenge myself and get certifications and now I chose to do the PCPP1 from the Python Institute ([click here](https://pythoninstitute.org/pcpp1)). It's really just for the fun and challenge of it. I really don't have a lot of time for this one, so I chose something I am already familiar with, which is Python programming. That said, I don't really do a whole lot of GUI programming in Python, even less with Tkinter, and I  don't do any network programming at all, so this will at least involve _some_ challenge.

My methodology is quite simple: I read the open source test prep material from PI _once_, I don't run the test code unless I'm not 100% sure I understand it, but I always to the labs without external assistance (`code/`) tos imulate exam conditions. I also summarize each slide or page of content with the help of an LLM in Markdown format that I post here (for now). I will read these summaries or skim them whenever I have time, which is rarely.

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
