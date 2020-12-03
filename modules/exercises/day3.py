from modules.helper import Helper


class Day3:
    def __init__(self, map_file):
        self.map = []
        self.tree_count = 0
        preprocessed_map = Helper.load_file(map_file)
        multiplier = int(len(preprocessed_map))

        for line in preprocessed_map:
            new_line = "".join([line]*multiplier)
            self.map.append(list(new_line))

    def find_trees_in_path(self, right_mov, down_mov):
        current_right = right_mov
        for i in range(1, len(self.map)):
            if i % down_mov:
                continue
            if self.map[i][current_right] == "#":
                self.tree_count += 1
            current_right += right_mov

        return self.tree_count
