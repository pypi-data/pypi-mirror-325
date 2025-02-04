import re

class StructureParser:
    @staticmethod
    def parse_line(line):
        line = line.rstrip("\n").strip()
        if not line or line.startswith("#"):
            return None

        # Regex to capture indentation and name
        match = re.match(r'^([ │]*)(├──|└──)?\s*(.*?)$', line)
        if not match:
            return None

        indent = match.group(1)
        name = match.group(3).strip()
        is_dir = name.endswith("/") or ("." not in name)
        name = name.rstrip("/")

        # Calculate level based on indentation (4 characters per level)
        level = len(indent) // 4
        return {"level": level, "name": name, "is_dir": is_dir}

    @staticmethod
    def parse_file(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            lines = [line for line in f if line.strip()]

        if not lines:
            raise ValueError("File is empty")

        structure = []
        for line in lines:
            entry = StructureParser.parse_line(line)
            if entry:
                structure.append(entry)

        return structure