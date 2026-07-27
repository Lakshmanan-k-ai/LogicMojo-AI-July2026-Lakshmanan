def rectangle_area(width: float, height: float) -> float:
    return width * height

def greet(name: str, greeting: str = "Hello") -> str:
    return f"{greeting}, {name}"

# Calls
width = 3
height = 4
print(f"area of {width} x {height} =", rectangle_area(width, height))
print(greet("Ada"))
print(greet("Alan", "Hi"))