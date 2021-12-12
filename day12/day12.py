#!/usr/bin/env python3

# https://adventofcode.com/2021/day/12


def load_data(filename, parser = None, data = []) -> []:
    with open(filename) as my_file:
        for line in my_file:
            if parser:
                line = parser(line, data)
            if type(data) is list:
                data.append(line)
    return data


def parser(s, data) -> int:
    k,v = s.strip().split('-')
    if k in data:
        data[k].append(v)
    else:
        data[k] = [v]


found_paths = []


def dfs(graph, currentVertex, visited):
    visited.append(currentVertex)
    if currentVertex != 'end':
        for vertex in graph[currentVertex]:
            # don't visit if visited unless it's a big room (uppercase)
            if vertex not in visited or vertex[0].isupper():
                dfs(graph, vertex, visited.copy())
    if visited[-1] == 'end':
        found_paths.append(visited)


def main():
    data = load_data('input.txt', parser, {})
    #print(data)

    # make sure each node is in the graph
    temp_data = data.copy()
    for k in temp_data:
        for l in temp_data[k]:
            if not (l in temp_data):
                data[l] = []

    # add reverse direction links
    for k in data:
        for l in data[k]:
            print(l)
            if not (k in data[l]):
                data[l].append(k) 
    #print(data)

    dfs(data, 'start', [])
    for path in found_paths:
        print(path)
    print(f'{len(found_paths)} paths found')


if __name__ == "__main__":
    main()
