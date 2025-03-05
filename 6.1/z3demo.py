import z3

def simple_example():
    # Create a solver instance
    s = z3.Solver()
    
    # Declare integer variables
    x = z3.Int('x')
    y = z3.Int('y')
    
    # Add constraints
    s.add(x > 0, y > 0)       # both x and y are positive
    s.add(x + y == 10)        # x + y = 10
    s.add(x < y)              # x is less than y
    
    # Check satisfiability
    if s.check() == z3.sat:
        # Get a model (a solution)
        model = s.model()
        print("Solution found:")
        print(f"x = {model[x]}")
        print(f"y = {model[y]}")
    else:
        print("No solution exists.")

if __name__ == "__main__":
    simple_example()


irbugzv1v^x1t^jo1v^e5^v@2^9i3c@138
