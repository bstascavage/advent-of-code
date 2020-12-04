from modules.helper import Helper


class Day3:
    def __init__(self, map_file):
        self.map = []
        preprocessed_map = Helper.load_file(map_file)

        # Converting file into 2D array
        for line in preprocessed_map:
            self.map.append(list("".join([line])))

    def find_trees_in_path(self, right_mov, down_mov):
        current_right = right_mov
        tree_count = 0

        # Looping through each row of the map, skipping every N rows, where N is down_mov-1
        for i in range(0, len(self.map), down_mov):
            # Need to skip index 0 since we start the count at 1
            if i == 0:
                continue

            # "Wrap-around" logic.  If current_right exceeds the size of the inner loop, we need to reset it.
            if current_right > (len(self.map[i]) - 1):
                current_right = current_right - len(self.map[i])

            if self.map[i][current_right] == "#":
                tree_count += 1
            current_right += right_mov

        return tree_count
