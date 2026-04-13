class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # ✅ Initialize pointers to boundaries of the current square layer
        # l = left column index, r = right column index
        l, r = 0, len(matrix[0]) - 1

        # Looping Through Matrix Layers
        while l < r:
            # Rotating Each Group of 4 Cells
            # Each i handles one offset from the left
            for i in range(r - l):
                top, bottom = l, r  # top and bottom row indices of this layer

                # 🧊 Step 1: Save the top-left cell so it's not lost in overwriting
                topLeft = matrix[top][l + i]

                # 🔄 Step 2: Move bottom-left into top-left position
                matrix[top][l + i] = matrix[bottom - i][l]

                # 🔄 Step 3: Move bottom-right into bottom-left position
                matrix[bottom - i][l] = matrix[bottom][r - i]

                # 🔄 Step 4: Move top-right into bottom-right position
                matrix[bottom][r - i] = matrix[top + i][r]

                # 🔄 Step 5: Move saved top-left into top-right position
                matrix[top + i][r] = topLeft

            # ⏩ Move inward to the next layer
            l += 1
            r -= 1