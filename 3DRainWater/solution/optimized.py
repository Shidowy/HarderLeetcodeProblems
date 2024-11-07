import heapq

def trap_water_3d(terrain):
    # Get the dimensions of the terrain
    N = len(terrain)
    M = len(terrain[0])
    P = len(terrain[0][0])

    # Min-heap to store cells with (height, i, j, k)
    min_heap = []
    
    # Visited array to keep track of processed cells
    visited = [[[False for _ in range(P)] for _ in range(M)] for _ in range(N)]

    # Directions for 3D neighbors (6 directions: up, down, left, right, front, back)
    directions = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]
    
    # Add all boundary cells to the heap
    for i in range(N):
        for j in range(M):
            for k in range(P):
                if i == 0 or i == N-1 or j == 0 or j == M-1 or k == 0 or k == P-1:
                    heapq.heappush(min_heap, (terrain[i][j][k], i, j, k))
                    visited[i][j][k] = True

    trapped_water = 0

    # Process the terrain starting from the boundary
    while min_heap:
        height, i, j, k = heapq.heappop(min_heap)

        # Explore all 6 possible neighbors
        for di, dj, dk in directions:
            ni, nj, nk = i + di, j + dj, k + dk

            # Skip out-of-bound cells and already visited cells
            if ni < 0 or ni >= N or nj < 0 or nj >= M or nk < 0 or nk >= P or visited[ni][nj][nk]:
                continue

            # Mark the neighbor as visited
            visited[ni][nj][nk] = True

            # If the neighbor is lower than the current water level, it will trap water
            if terrain[ni][nj][nk] < height:
                trapped_water += height - terrain[ni][nj][nk]

            # Push the neighbor into the heap with the new water level (max of its height or the current height)
            heapq.heappush(min_heap, (max(terrain[ni][nj][nk], height), ni, nj, nk))

    return trapped_water
