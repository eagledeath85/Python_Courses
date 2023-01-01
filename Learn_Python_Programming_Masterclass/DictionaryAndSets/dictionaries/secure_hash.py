import hashlib


python_program = """for i in range(10):
print(i)"""
print(python_program)

original_hash = hashlib.sha256(python_program.encode('utf8'))
print(f"SHA256 of original string: {original_hash.hexdigest()}")
print()

python_program += "Some code changes"
new_hash = hashlib.sha256(python_program.encode('utf8'))
print(f"SHA256 of updated string: {new_hash.hexdigest()}")

if new_hash.hexdigest() == original_hash.hexdigest():
    print("The code hasn't changed")
else:
    print("The code has been changed")