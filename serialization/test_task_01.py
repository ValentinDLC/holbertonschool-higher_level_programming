#!/usr/bin/env python3
from task_01_pickle import CustomObject

obj = CustomObject(name="john", age=25, is_student=True)
print("Ordiginal Object:")
obj.display()

obj.serialize("object.pkl")

new_obj = CustomObject.deserialize("object.pkl")
print("\nDeserialized object:")
new_obj.display()