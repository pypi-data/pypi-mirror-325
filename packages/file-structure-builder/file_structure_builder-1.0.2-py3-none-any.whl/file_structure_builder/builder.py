import os

class FileStructureBuilder:
    @staticmethod
    def build_structure(structure):
        if not structure:
            raise ValueError("Empty structure provided")

        # Process root directory from first entry
        root = structure[0]
        if not root["name"]:
            raise ValueError("Invalid root entry")

        base_path = os.path.join(".", root["name"])
        os.makedirs(base_path, exist_ok=True)
        dir_stack = [base_path]

        for entry in structure[1:]:
            # Maintain directory hierarchy
            while entry["level"] >= len(dir_stack):
                dir_stack.pop()

            parent_dir = dir_stack[entry["level"]]
            current_path = os.path.join(parent_dir, entry["name"])

            if entry["is_dir"]:
                os.makedirs(current_path, exist_ok=True)
                # Update directory stack for subsequent items
                if entry["level"] + 1 >= len(dir_stack):
                    dir_stack.append(current_path)
                else:
                    dir_stack[entry["level"] + 1] = current_path
            else:
                os.makedirs(os.path.dirname(current_path), exist_ok=True)
                with open(current_path, "w", encoding="utf-8") as f:
                    f.write("")