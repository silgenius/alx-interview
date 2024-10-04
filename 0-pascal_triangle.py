def pascal_triangle(n):
    if n <= 0:
        return []
  
    tri = []
    for i in range(n):
        row = [1] * (i + 1)  # Initialize a row with 1s
        for j in range(1, i):
            row[j] = tri[i - 1][j - 1] + tri[i - 1][j]  # Compute values based on the previous row
        tri.append(row)
    
    return tri
