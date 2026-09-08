def generate_binary_strings(n):
    def backtrack(current):
        if len(current) == n:
            print(current)
            return
        # Choice 1: Add '0'
        backtrack(current + "a")
        # Choice 2: Add '1'
        backtrack(current + "b")
    
    backtrack("")
generate_binary_strings(2)

