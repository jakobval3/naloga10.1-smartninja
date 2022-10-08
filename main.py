with open("data.csv", 'r') as data_file:
    data = data_file.read().splitlines()

    for row in data:
        row_data = row.split(",")
        print(f"{row_data[0]} is {row_data[1]} years old and {row_data[2]}.")