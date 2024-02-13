def pascals_triangle(row_number):
    if row_number == 1:
        return [1]

    previous_row = pascals_triangle(row_number - 1)
    current_row = []

    current_row.append(1)

    for i in range(0, len(previous_row) - 1):
        current_row.append(previous_row[i] + previous_row[i + 1])

    current_row.append(1)

    return current_row


print(pascals_triangle(7))
