def number_triangle(n: int) -> str:
    pattern = []
    
    for i in range(1, n + 1):
        row = ""
        for j in range(1, i + 1):
            row += str(j)
        pattern.append(row)
    
    return "\n".join(pattern)