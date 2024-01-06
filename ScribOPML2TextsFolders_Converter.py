# *****SCRIVENER OPML TO FOLDER OF TXT FILES' STRUCTURE*****

# ScribOPML2TextsFolders_Converter.py
# By F.B. Avila Rencoret 06012024 under GPL-3.0 license

# Works as a companion to TextToScribOPMLConverter.py
# This script converts an OPML file exported from Scrivener into a folder of text files.

#   SCRIVENER EXPORT:
#   - To use this script with Scrivener, first export your project as an OPML file.
#   - In Scrivener, go to 'File' > 'Export' > 'as OPML' and save the OPML file.

#   INPUT:     OPML file exported from Scrivener. The script will prompt the user to select the OPML file.
#   OUTPUT:    Folder of text files. The script will prompt the user to select the output folder.

#   USAGE:     Run the script from the command line or from an IDE.
#               If running from the command line, the script takes two arguments:
#                   1. Path to the OPML file
#                   2. Path to the output folder
#               If running from an IDE, the script will prompt the user to select the OPML file and output folder.

#   BEHAVIOR:
#   - Each folder in the OPML file will be converted into a directory in the output folder.
#   - Each text file in the OPML file will be converted into a text file in the output folder.
#   - The title of each text file will be the title of the text file in the OPML file.
#   - The synopsis of each text file will be the synopsis of the text file in the OPML file.
#   - The synopsis of each folder will be the synopsis of the folder in the OPML file.
#   - The title of each folder will be the title of the folder in the OPML file.

# USAGE AS CONSOLE SCRIPT
# python ScribOPML2TextsFolders_Converter.py /path/to/your/opml_file.opml /path/to/your/output/directory

# USAGE INSIDE AN IDE:
# converter = ScribOPML2TextsFolders_Converter('/path/to/your/opml_file.opml', '/path/to/your/output/directory')
# converter.convert()


import xml.etree.ElementTree as ET
import os
import logging
import tkinter as tk
from tkinter import filedialog

class OPMLToTextConverter:
    def __init__(self, opml_file, output_dir):
        self.opml_file = opml_file
        self.output_dir = output_dir
        logging.basicConfig(level=logging.INFO)

    def convert(self):
        try:
            tree = ET.parse(self.opml_file)
            root = tree.getroot()
            body = root.find('body')
            if body is None:
                raise ValueError("No body tag found in OPML file")

            os.makedirs(self.output_dir, exist_ok=True)
            self._create_text_structure_from_outline(body, self.output_dir)
            logging.info(f"Conversion completed successfully. Output at: {self.output_dir}")
        except Exception as e:
            logging.error(f"An error occurred during conversion: {e}")

    def _create_text_structure_from_outline(self, outline, current_path):
        for item in outline:
            title = item.attrib.get('text', 'Untitled').strip()
            safe_title = self._sanitize_title(title)
            new_path = os.path.join(current_path, safe_title)

            synopsis = item.attrib.get('_note', '').strip()
            if list(item):
                self._handle_directory(new_path, safe_title, synopsis, item)
            else:
                self._handle_file(new_path, title, synopsis)

    def _sanitize_title(self, title):
        return ''.join(e for e in title if e.isalnum() or e in [' ', '_']).rstrip()

    def _handle_directory(self, path, title, synopsis, item):
        logging.info(f"Creating directory: {path}")
        os.makedirs(path, exist_ok=True)
        if synopsis:
            self._write_synopsis_file(path, title, synopsis)
        self._create_text_structure_from_outline(item, path)

    def _write_synopsis_file(self, directory, title, synopsis):
        synopsis_path = os.path.join(directory, f'{title}_synopsis.txt')
        logging.info(f"Writing synopsis file: {synopsis_path}")
        with open(synopsis_path, 'w', encoding='utf-8') as file:
            file.write(synopsis)

    def _handle_file(self, path, title, synopsis):
        file_path = path + '.txt'
        logging.info(f"Creating text file: {file_path}")
        with open(file_path, 'w', encoding='utf-8') as file:
            if synopsis:
                file.write(f'<!-- {synopsis} -->\n\n')
            file.write(title)
            

# Main function Definition using Tkinter GUI
def main():
    # Prompt user for OPML file and output directory
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    output_dir = filedialog.askdirectory()
        # Convert OPML file to text files
    converter = OPMLToTextConverter(file_path, output_dir)
    converter.convert()
    
    # OPMLToTextConverter('/path/to/your/opml_file.opml', '/path/to/your/output/directory')
    converter.convert()
    
# Main function call
if __name__ == '__main__':
    main()

# CONSOLE EXMAPLE 
# converter = OPMLToTextConverter('/path/to/your/opml_file.opml', '/path/to/your/output/directory')
# converter.convert()