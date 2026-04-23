student = {
    "name": "John",
    "age": 21,
    "marks": {"math": 80, "science": 90}
}

# Access value using get()
print(student.get("name"))

# Add new key-value pair
student["grade"] = "A"

# Update existing key
student.update({"age": 22})

# Remove last inserted item
student.popitem()

# View dictionary structure
print(student.keys())
print(student.values())
print(student.items())

# Add key only if not present
student.setdefault("city", "New York")

# Merge another dictionary
new_data = {"email": "john@example.com", "phone": "123-456-7890"}
student.update(new_data)

# Remove specific key
student.pop("age")