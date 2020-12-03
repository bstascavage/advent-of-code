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

        for i in range(1, len(self.map)):
            # If the row we are on wouldn't be transversed with our "down movement"
            # value, then skip it
            if i % down_mov:
                continue
            if self.map[i][current_right] == "#":
                tree_count += 1
            current_right += right_mov

        return tree_count
