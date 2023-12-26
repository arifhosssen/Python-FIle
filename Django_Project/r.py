import os

for i in range(1,40):
    os.renames(f"Data/Project {i}", f"Data/Project_{i}")
        