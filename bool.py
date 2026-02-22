x = 5
y = 3

b0 = x == y
b1 = x != y
b2 = x > y
b3 = x < y
b4 = x >= y
b5 = x <= y
b6 = True

print(f"{x} == {y} : {b0} ({type(b0)})")
print(f"{x} != {y} : {b1} ({type(b1)})")
print(f"{x} > {y} : {b2} ({type(b2)})")
print(f"{x} < {y} : {b3} ({type(b3)})")
print(f"{x} >= {y} : {b4} ({type(b4)})")
print(f"{x} <= {y} : {b5} ({type(b5)})")
print(f"True value: {b6} ({type(b6)})")