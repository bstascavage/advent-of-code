from modules.helper import Helper


class Day3:
    def __init__(self, map_file):
        self.map = []
        preprocessed_map = Helper.load_file(map_file)

        # We need to "repeat" the map to the right in order to transverse it.
        # This "repeats" each line N times, where N is the length of the original map.
        for line in preprocessed_map:
            self.map.append(list("".join([line]*len(preprocessed_map))))

    def find_trees_in_path(self, right_mov, down_mov):
        current_right = right_mov
        tree_count = 0

        # Looping through each row of the map, skipping every N rows, where N is down_mov-1
        for i in range(0, len(self.map), down_mov):
            # Need to skip index 0 since we start the count at 1
            if i == 0:
                continue
            if self.map[i][current_right] == "#":
                tree_count += 1
            current_right += right_mov

        return tree_count
