def cyrus_beck_algorithm(vertices, edge_list, clip_plane):
    inside = lambda p: clip_plane[0] * p[0] + clip_plane[1] * p[1] + clip_plane[2] * p[2] + clip_plane[3] >= 0

    p1, p2 = vertices[edge_list[-1]], vertices[edge_list[0]]  # Последняя вершина соединяется с первой

    t1 = (clip_plane[3] - (clip_plane[0] * p1[0] + clip_plane[1] * p1[1] + clip_plane[2] * p1[2])) / (
                clip_plane[0] * (p2[0] - p1[0]) + clip_plane[1] * (p2[1] - p1[1]) + clip_plane[2] * (p2[2] - p1[2]))
    intersection_points = []  # Точки пересечения ребер с плоскостью отсечения

    for i in range(len(edge_list)):
        p1, p2 = vertices[edge_list[i - 1]], vertices[edge_list[i]]
        t2 = (clip_plane[3] - (clip_plane[0] * p1[0] + clip_plane[1] * p1[1] + clip_plane[2] * p1[2])) / (
                    clip_plane[0] * (p2[0] - p1[0]) + clip_plane[1] * (p2[1] - p1[1]) + clip_plane[2] * (p2[2] - p1[2]))

        if inside(p2):  # p2 внутри плоскости отсечения
            if not inside(p1):  # p1 снаружи плоскости отсечения
                intersection_points.append(
                    (p1[0] + t1 * (p2[0] - p1[0]), p1[1] + t1 * (p2[1] - p1[1]), p1[2] + t1 * (p2[2] - p1[2])))
            intersection_points.append((p2[0], p2[1], p2[2]))
        elif inside(p1):  # p1 внутри плоскости отсечения
            intersection_points.append(
                (p1[0] + t1 * (p2[0] - p1[0]), p1[1] + t1 * (p2[1] - p1[1]), p1[2] + t1 * (p2[2] - p1[2])))

        t1 = t2

    if len(intersection_points) > 2:


# Используйте точки пересечения для построения новых полигонов

# Отображаем оставшиеся полигоны

# Пример использования
vertices = [(0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0)]
edge_list = [0, 1, 2, 3]  # Индексы вершин полигонов
clip_plane = (0, 0, -1, 0)  # Плоскость отсечения: z=0

cyrus_beck_algorithm(vertices, edge_list, clip_plane)