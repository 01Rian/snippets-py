class HandleFile:
    def __init__(self):
        self.numbers = []

    def read_file(self, file_path):
        """Reads the file and returns its lines."""
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                return file.readlines()
        except FileNotFoundError:
            print(f"Erro: Arquivo '{file_path}' não encontrado.")
            return []
        except Exception as e:
            print(f"Ocorreu um erro: {e}")
            return []

    def format_number(self, line):
        """Formats a line to a float number if possible."""
        line = line.strip().replace("\r", "").replace("\n", "").replace(" ", "").replace(",", ".")
        if line:
            try:
                return float(line)
            except ValueError:
                pass
        return None

    def read_formatted_numbers(self, file_path):
        """Reads and formats numbers from a file."""
        lines = self.read_file(file_path)
        self.numbers = [self.format_number(line) for line in lines if self.format_number(line) is not None]
        return self.numbers