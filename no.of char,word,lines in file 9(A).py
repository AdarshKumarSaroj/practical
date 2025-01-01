class FileAnalyzer:
    def __init__(self, file_name):
        self.file_name = file_name
        self.content = ""
        self.lines = []

    def read_file(self):
        try:
            file = open(self.file_name, 'r')
            self.content = file.read()
            file.seek(0)
            self.lines = file.readlines()
        except FileNotFoundError:
            print(f"Error: The file '{self.file_name}' was not found.")
        except Exception as e:
            print(f"An unexpected error occured '{e}'")

    def analyze(self):
        try:
            total_char = len(self.content)
            total_wrds = len(self.content.split())
            total_lines = len(self.lines)
            print(f"TOTAL CHARACTERS ='{total_char}'")
            print(f"TOTAL WORDS ='{total_wrds}'")
            print(f"TOTAL LINES ='{total_lines}'")
        except Exception as e:
            print(f"An error occured :'{e}'")

filename = input("ENTER FILE NAME:")
file_analyzer = FileAnalyzer(filename)
file_analyzer.read_file()
file_analyzer.analyze()
