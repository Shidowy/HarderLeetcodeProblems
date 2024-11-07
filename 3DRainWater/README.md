# 3D Trapping Rainwater in Enclosed Terrain

## Problem Description

You are given a **3D mountain range** represented by an `N×M×P` grid. Each cell `(i, j, k)` in this grid has a non-negative integer height, representing the terrain height at that location. The terrain forms various peaks, valleys, and ridges, creating natural basins where water can collect.

This terrain is **fully enclosed** by higher cells on all sides, so no water can escape. After a rainstorm, water will collect in the low areas of the terrain, filling up valleys to the lowest surrounding heights.

Your task is to calculate the **maximum volume of water** that could be trapped within this terrain after rainfall.

## Rules
1. **Fully Enclosed**: The terrain is surrounded on all sides by higher or equal-height cells, meaning no water can leak out.
2. **Water Collection**: Water is trapped in valleys, pooling up to the height of the lowest surrounding barrier.

## Input

- `terrain: List[List[List[int]]]`: A 3D list with dimensions `N×M×P`, where each cell `(i, j, k)` contains a non-negative integer representing the height of the terrain at that location.

## Output

Return a single integer, `trapped_water`, which is the total volume of water that can be trapped in valleys within the terrain.

## Example

```python
terrain = [
    [[5, 2], [3, 5]],
    [[4, 1], [2, 4]]
]

# Expected Output:
# trapped_water = 12
