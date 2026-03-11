def right_triangle(n: int) -> str:
    pattern = []
    
    for i in range(1, n + 1):
        pattern.append("*" * i)
        
    return "\n".join(pattern)