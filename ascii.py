from PIL import Image


class ASCIIArtStudio:
    """A simple ASCII art generator that converts images to ASCII art"""
    
    def __init__(self):
        """Initialize the ASCII Art Studio with empty image and filename.
        """
        self.current_image = None
        self.filename = None

    def run(self):
        """Run the main program loop for the ASCII Art Studio."""

        print("Welcome to ASCII Art Studio!")
        while True:
            command = input("AAS: ").strip().split()
            if not command:
                continue
            if command[0] == "load" and len(command) == 2:
                self.load_image(command[1])
            elif command[0] == "render":
                self.render_image()
            elif command[0] == "info":
                self.print_info()
            elif command[0] == "quit":
                print("Bye!")
                break
            else:
                print("Invalid command. Use 'load <filename>', 'render', 'info', or 'quit'.")

    def load_image(self, filename):
        """Load an image file and convert it to grayscale.
        
        Args:
            filename (str): Path to the image file to load.
        """
        try:
            with Image.open(filename) as img:
                img.load()
                self.current_image = img.convert('L')  # Convert to grayscale
                self.filename = filename
                print(f"Image '{filename}' loaded.")
        except Exception as e:
            print(f"Error: {e}")

    def render_image(self):
        """Render the loaded image as ASCII art."""

        if not self.current_image:
            print("No image loaded.")
            return
        
        # Resize image to width 50, maintain proportions
        width, height = self.current_image.size
        new_width = 50
        aspect_ratio = height / width
        new_height = int(new_width * aspect_ratio * 0.5)  # Adjust for font proportions
        resized_img = self.current_image.resize((new_width, new_height))
        
        # ASCII characters for grayscale (dark to light)
        ascii_chars = "@%#*+=-:. "
        
        # Convert each pixel to ASCII
        ascii_art = []
        for y in range(new_height):
            line = ""
            for x in range(new_width):
                pixel = resized_img.getpixel((x, y))
                line += ascii_chars[pixel // 32]  # 256 / 8 characters = 32 intervals
            ascii_art.append(line)
        
        print("\n".join(ascii_art))

    def print_info(self):
        """Print information about the currently loaded image."""

        if self.current_image:
            print(f"Filename: {self.filename}")
            print(f"Size: {self.current_image.size}")
        else:
            print("No image loaded.")


if __name__ == "__main__":
    studio = ASCIIArtStudio()
    studio.run()