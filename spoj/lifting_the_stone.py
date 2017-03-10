# def get_center_rec(coordinates):
#     n = len(coordinates)
#     if n == 2:
#         return (coordinates[0][0] + coordinates[1][0]) / 2, (coordinates[0][1] + coordinates[1][1]) / 2
#     x_last_dot = coordinates[-1][0]
#     y_last_dot = coordinates[-1][1]
#     x_smaller_figure, y_smaller_figure = get_center(coordinates[:-1])
#
#     return (x_last_dot + (n - 1) * x_smaller_figure) / n, (y_last_dot + (n - 1) * y_smaller_figure) / n
#
#
# def get_center(coordinates):
#     x = (coordinates[0][0] + coordinates[1][0]) / 2
#     y = (coordinates[0][1] + coordinates[1][1]) / 2
#     n = 3
#
#     for point in coordinates[2:]:
#         x = (point[0] + (n - 1) * x) / n
#         y = (point[1] + (n - 1) * y) / n
#         n += 1
#
#     return x, y


def get_area(coordinates):
    area = 0
    for i in range(len(coordinates[:-1])):
        area += coordinates[i][0] * coordinates[i + 1][1] - coordinates[i + 1][0] * coordinates[i][0]
    return area


def get_center(coordinates):
    coord = coordinates  + [coordinates[0]]
    x = 0
    y = 0
    area = get_area(coord)
    for i in range(len(coord[:-1])):
        second_part = (coord[i][0] * coord[i + 1][1] - coord[i + 1][0] * coord[i][1])
        x += (coord[i][0] + coord[i + 1][0]) * second_part
        y += (coord[i][1] + coord[i + 1][1]) * second_part

    return x / (6 * area), y / (6 * area)

number_of_repetitions = int(input())
coordinates_of_centers = []
for i in range(number_of_repetitions):
    size = int(input())
    coordinates = []
    for j in range(size):
        point = input().split(' ')
        coordinates.append((float(point[0]), float(point[1])))
    coordinates_of_centers.append(get_center(coordinates))

for line in coordinates_of_centers:
    print('%.2f %.2f' % (line[0] if line[0] != 0 else 0, line[1] if line[1] != 0 else 0))
