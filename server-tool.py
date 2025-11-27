# ============================================================
#  THREAD RENDERING ENGINE (NO EXTERNAL LIBRARIES REQUIRED)
# ============================================================

class ThreadPattern:
    """Base class for all thread patterns."""
    def __init__(self, width, height, char='x'):
        self.width = width
        self.height = height
        self.char = char

    def render(self):
        """Override in subclasses."""
        raise NotImplementedError


# ------------------------------------------------------------
# Straight vertical thread pattern
# ------------------------------------------------------------
class VerticalThreads(ThreadPattern):
    def render(self):
        canvas = []
        for _ in range(self.height):
            line = ""
            for _ in range(self.width):
                line += self.char + "   "
            canvas.append(line)
        return canvas


# ------------------------------------------------------------
# Diagonal thread pattern
# ------------------------------------------------------------
class DiagonalThreads(ThreadPattern):
    def render(self):
        canvas = []
        for row in range(self.height):
            line = ""
            for col in range(self.width):
                if (row + col) % self.width == col:
                    line += self.char + "   "
                else:
                    line += "    "
            canvas.append(line)
        return canvas


# ------------------------------------------------------------
# Interweaving / braided thread pattern
# ------------------------------------------------------------
class BraidedThreads(ThreadPattern):
    def render(self):
        canvas = []
        for row in range(self.height):
            line = ""
            for col in range(self.width):
                # Create a woven effect
                if (row % 4 == 0 and col % 2 == 0) or (row % 4 == 2 and col % 2 == 1):
                    line += self.char + "   "
                else:
                    line += "    "
            canvas.append(line)
        return canvas


# ------------------------------------------------------------
# Zig-zag thread pattern
# ------------------------------------------------------------
class ZigZagThreads(ThreadPattern):
    def render(self):
        canvas = []
        for row in range(self.height):
            line = ""
            offset = row % 4
            for col in range(self.width):
                if col == offset:
                    line += self.char + "   "
                else:
                    line += "    "
            canvas.append(line)
        return canvas


# ============================================================
#  THREAD DESIGNER: BUILDER + FACTORY
# ============================================================
class ThreadFactory:
    @staticmethod
    def create(style, width, height, char):
        style = style.lower()
        if style == "vertical":
            return VerticalThreads(width, height, char)
        if style == "diagonal":
            return DiagonalThreads(width, height, char)
        if style == "braid":
            return BraidedThreads(width, height, char)
        if style == "zigzag":
            return ZigZagThreads(width, height, char)
        raise ValueError("Unknown thread style: " + style)


class ThreadDesigner:
    """Constructs and renders chosen thread patterns."""
    def __init__(self, style="vertical", width=8, height=20, char="x"):
        self.style = style
        self.width = width
        self.height = height
        self.char = char

    def build(self):
        return ThreadFactory.create(self.style, self.width, self.height, self.char)

    def display(self):
        pattern = self.build()
        for line in pattern.render():
            print(line)


# ============================================================
#  MAIN EXECUTION BLOCK
# ============================================================
def main():
    print("=== THREAD PATTERN ENGINE ===\n")

    styles = ["vertical", "diagonal", "braid", "zigzag"]

    for style in styles:
        print(f"\n--- {style.upper()} THREADS ---")
        designer = ThreadDesigner(style=style, width=10, height=15, char='x')
        designer.display()


# Run the engine
main()
