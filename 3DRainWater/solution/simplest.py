def trap_water_3d_simple(terrain):
    # Get the dimensions of the terrain
    N = len(terrain)
    M = len(terrain[0])
    P = len(terrain[0][0])

    trapped_water = 0

    # Directions for the 6 possible neighbors (up, down, left, right, front, back)
    directions = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]

    # Check each cell (i, j, k) inside the grid
    for i in range(1, N-1):
        for j in range(1, M-1):
            for k in range(1, P-1):
                # Find the maximum height among the neighbors (up, down, left, right, front, back)
                max_height = terrain[i][j][k]

                for di, dj, dk in directions:
                    ni, nj, nk = i + di, j + dj, k + dk
                    max_height = max(max_height, terrain[ni][nj][nk])

                # Calculate trapped water if the current cell is lower than its surrounding neighbors
                if terrain[i][j][k] < max_height:
                    trapped_water += max_height - terrain[i][j][k]

    return trapped_water
