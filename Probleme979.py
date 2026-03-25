N = 20
max_depth = N // 2

# Type A tiles have one common edge with previous layer
# Type B tiles have two common edges with previous layer
# Type S tile is starting tile
tile_child = {'B': 'BAB', 'A': 'BAAB'}

levels = ['S', 'A'*7] 
tiles_per_level = [len(level) for level in levels]

neighbor_tiles = {(0, 0): [(1, i) for i in range(tiles_per_level[1])]}
for i in range(tiles_per_level[1]):
    neighbor_tiles[(1, i)] = [(0, 0), (1, (i-1)%tiles_per_level[1]), (1, (i+1)%tiles_per_level[1])]

for i in range(2, max_depth + 1):
    r = '_'
    for j, tile in enumerate(levels[-1]):
        r = r[:-1] + tile_child[tile]
        neighbor_tiles[(i-1, j)] += [(i, k) for k in range(len(r)-1, len(r)-len(tile_child[tile])-1, -1)]
        for k in range(len(r)-1, len(r)-len(tile_child[tile])-1, -1):
            neighbor_tiles[(i,k)] = neighbor_tiles.get((i,k), []) + [(i-1, j)]
    levels.append(r[:-1])
    tiles_per_level.append(len(levels[-1]))
    # Neighbors end loop
    neighbor_tiles[(i-1, tiles_per_level[i-1]-1)].remove((i, tiles_per_level[i]))
    neighbor_tiles[(i-1, tiles_per_level[i-1]-1)].append((i, 0))
    neighbor_tiles[(i, 0)].append((i-1, tiles_per_level[i-1]-1))
    del neighbor_tiles[(i, tiles_per_level[i])]
    # Same level neighbors
    for j, tile in enumerate(levels[-1]):
        neighbor_tiles[(i, j)] += [(i, (j+1)%tiles_per_level[-1]), (i, (j-1)%tiles_per_level[-1])]

F = {(0, 0): {0: 1}}

for n in range(1, N+1):
    print(f"Calculating for {n=}")
    for i, level in enumerate(levels):
        for j in range(tiles_per_level[i]):
            tile = (i, j)
            value = sum([F.get(neighbor, {}).get(n-1, 0) for neighbor in neighbor_tiles[tile]])
            if tile not in F:
                F[tile] = {}
            F[tile][n] = value

print(F[(0, 0)][N])
