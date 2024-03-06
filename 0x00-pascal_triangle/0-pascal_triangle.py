#!/usr/bin/python3
def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        prev_row = triangle[-1]
        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])
        row.append(1)
        triangle.append(row)

    return triangle

def print_pascal_triangle(triangle):
    for row in triangle:
        print(' '.join(map(str, row)))

if __name__ == "__main__":
    n = 5  # Change this value to generate Pascal's triangle of different heights
    triangle = pascal_triangle(n)
    print_pascal_triangle(triangle)

