# *****FOLDER OF TXT FILES' STRUCTURE TO SCRIVENER OPML*****

# TextToScribOPMLConverter.py
# By F.B. Avila Rencoret 06012024 under GPL-3.0 license

# Works as a companion to ScribOPML2TextsFolders_Converter.py
# This script converts a folder of text files into an OPML file for import into Scrivener.

#   INPUT:     Folder of text files. The script will prompt the user to select the input folder.
#   OUTPUT:    OPML file formatted for Scrivener. The script will prompt the user to select the location for saving the OPML file.

#   USAGE:     Run the script from the command line or from an IDE.
#               If running from the command line, the script takes two arguments:
#                   1. Path to the input folder containing text files
#                   2. Path to save the OPML file
#               If running from an IDE, the script will prompt the user to select the input folder and location to save the OPML file.

#   BEHAVIOR:
#   - Each directory in the input folder will be converted into a folder element in the OPML file.
#   - Each text file in the input folder will be converted into a text file element in the OPML file.
#   - The title of each text file element will be derived from the name of the corresponding text file.
#   - The synopsis of each text file element will be extracted from the content of the corresponding text file, if present as a markdown comment.
#   - The synopsis for each folder element will be extracted from a `[folder_name]_synopsis.txt` file, if present in the corresponding directory.
#   - The title of each folder element will be derived from the name of the corresponding directory.

#   SCRIVENER IMPORT:
#   - To use the generated OPML file with Scrivener, import it into the original Scrivener project.
#   - In Scrivener, go to 'File' > 'Import' > 'OPML' and select the generated OPML file.
#   - The imported OPML file will recreate the folder and document structure within Scrivener.

# USAGE AS CONSOLE SCRIPT
# python TextToOPMLConverter.py /path/to/your/input/directory /path/to/output.opml

# USAGE INSIDE AN IDE:
# converter = TextToOPMLConverter('/path/to/your/input/directory', '/path/to/output.opml')
# converter.convert()


import xml.etree.ElementTree as ET
import os
import logging
import os
import tkinter as tk
from tkinter import filedialog

class TextToOPMLConverter:
    def __init__(self, input_dir, opml_file):
        self.input_dir = input_dir
        self.opml_file = opml_file
        logging.basicConfig(level=logging.INFO)

    def convert(self):
        root = ET.Element('opml', version='1.0')
        head = ET.SubElement(root, 'head')
        title = ET.SubElement(head, 'title')
        title.text = 'Converted from Text Structure'
        body = ET.SubElement(root, 'body')

        self._create_outline_from_structure(self.input_dir, body)

        tree = ET.ElementTree(root)
        tree.write(self.opml_file, encoding='utf-8', xml_declaration=True)
        logging.info(f"OPML file created successfully at {self.opml_file}")

    def _create_outline_from_structure(self, current_path, parent_element):
        for item in os.listdir(current_path):
            item_path = os.path.join(current_path, item)
            if os.path.isdir(item_path):
                outline_element = ET.SubElement(parent_element, 'outline', attrib={'text': item})
                self._create_outline_from_structure(item_path, outline_element)
            elif item.endswith('.txt') and not item.endswith('_synopsis.txt'):
                with open(item_path, 'r', encoding='utf-8') as file:
                    content = file.read().strip()
                    title, synopsis = self._extract_title_and_synopsis(content)
                    ET.SubElement(parent_element, 'outline', attrib={'text': title, '_note': synopsis})

    def _extract_title_and_synopsis(self, content):
        if content.startswith('<!--') and '-->\n\n' in content:
            synopsis = content[content.find('<!--') + 4 : content.find('-->\n\n')].strip()
            title = content[content.find('-->\n\n') + 5:].strip()
        else:
            title = content
            synopsis = ''
        return title, synopsis


# Main function Definition using Tkinter GUI
def main():
    # Prompt user for input folder-txt directory and the path to OPML file
    root = tk.Tk()
    root.withdraw()
    input_dir = filedialog.askdirectory()
    opml_file = filedialog.askopenfilename()
    
    # Convert text files to OPML file
    converter = TextToOPMLConverter(input_dir, opml_file)
    
    # TextToOPMLConverter(input_dir, opml_file)
    converter.convert()
    
# Main function call
if __name__ == '__main__':
    main()

# CONSOLE EXMAPLE 
# converter = TextToOPMLConverter('/path/to/your/input/directory', '/path/to/output.opml')
# converter.convert()