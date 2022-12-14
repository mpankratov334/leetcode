"""
An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color 
as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. 
Replace the color of all of the aforementioned pixels with color.

Return the modified image after performing the flood fill.
"""
def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        def closure(image, sr, sc, color):
            dirs = ((1, 0), (0, 1), (-1, 0), (0, -1))
            sum_pairs = lambda p1, p2: (p1[0] + p2[0], p1[1] + p2[1])
            length = len(image[0])
            heigth = len(image)
            start = image[sr][sc]
            visited = set()
            def recursion(r, c):
                nonlocal image, visited
                image[r][c] = color
                visited.add((r,c))
                for d in dirs:
                    cords = sum_pairs(d, (r, c))
                    if cords not in visited and 0 <= cords[1] < length and \
                        0 <= cords[0] < heigth and image[cords[0]][cords[1]] == start:
                        recursion(cords[0], cords[1])
                return image
            return recursion

        f = closure(image, sr, sc, newColor)
        return f(sr,sc)
