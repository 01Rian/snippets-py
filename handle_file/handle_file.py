class HandleFile:
    def __init__(self):
        self.numbers = []

    def read_file(self, file_path):
        """
        Reads the contents of a file and returns its lines.

        Parameters:
        file_path (str): The path to the file to be read.

        Returns:
        list: A list of strings, each representing a line from the file. 
              Returns an empty list if the file is not found or an error occurs.
        """
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
        """
        Converts a string line to a float number if possible.

        Parameters:
        line (str): The string to be formatted and converted to a float.

        Returns:
        float or None: Returns the float representation of the line if conversion is successful,
                       otherwise returns None if the line cannot be converted to a float.
        """
        line = line.strip().replace("\r", "").replace("\n", "").replace(" ", "").replace(",", ".")
        if line:
            try:
                return float(line)
            except ValueError:
                pass
        return None

    def read_formatted_numbers(self, file_path):
        """
        Reads and formats numbers from a specified file.

        Parameters:
        file_path (str): The path to the file containing the numbers to be read and formatted.

        Returns:
        list: A list of float numbers extracted from the file. The numbers are stripped of leading/trailing
              whitespace, carriage returns, newlines, spaces, and commas, and converted to float format.
              If a line cannot be converted to a float, it is ignored.
              Returns an empty list if the file is not found or an error occurs during reading or formatting.
        """
        lines = self.read_file(file_path)
        self.numbers = [self.format_number(line) for line in lines if self.format_number(line) is not None]
        return self.numbers