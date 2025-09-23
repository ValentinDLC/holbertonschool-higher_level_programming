# Python - More Classes and Objects 

## Description

This project, titled **"More Classes and Objects"**, is an in-depth exploration of Python's Object-Oriented Programming (OOP) paradigm. It focuses on a variety of advanced concepts and best practices beyond the basics of creating a simple class. Throughout this project, we develop a `Rectangle` class, incrementally adding features to demonstrate key OOP principles like data encapsulation, special methods, class and static methods, and property decorators.

---

## What I Learned from This Project

This project was a comprehensive journey into the more advanced aspects of Python's Object-Oriented Programming. Here’s a summary of the key skills and concepts I gained:

* **Mastered Class and Instance Attributes:** 

I learned the critical difference between data that belongs to the class itself (`number_of_instances`) and data that belongs to each individual object (`width`, `height`), and how to properly manage them.

* **Effective Data Encapsulation:** 

By using private instance attributes (`__width`, `__height`) and implementing them with `@property` decorators, I learned how to create robust and secure classes where data access is controlled and validated, preventing invalid values.

* **Understanding Special Methods:** 

I now have a solid grasp of how to use special methods like `__init__`, `__str__`, and `__repr__` to create objects that are easy to instantiate, print in a human-readable format, and represent unambiguously for developers. The ability to use `eval(repr(my_object))` to recreate an instance is a particularly powerful concept I explored.

* **Advanced Method Types:** 

The project introduced the practical application of `@classmethod` and `@staticmethod`. I learned to use a class method to create factory-like functions (`square()`) and a static method to perform utility-like functions that don't depend on the instance or class state (`bigger_or_equal()`).

* **Resource Management:** 

The `__del__` destructor provided insight into the lifecycle of objects in Python, allowing me to perform cleanup actions or simply track when an instance is garbage-collected. This is a fundamental concept for understanding memory management.

Each task built upon the last, reinforcing the principles and leading to a complete, well-documented, and functional `Rectangle` class that demonstrates a wide array of Python OOP features.

---