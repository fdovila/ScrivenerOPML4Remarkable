# ScrivenerOPML4Remarkable
Towards a sync between scrivener and Remarkable2

## Introduction
This repository contains two powerful Python scripts for writers and developers working with Scrivener and text-based systems. `ScribOPML2TextsFolders_Converter.py` and `Text2ScribOPML_Converter.py` facilitate the conversion between Scrivener's OPML format and a structured text format, enabling a seamless transition between different writing environments.

## Done: 
### 1. OPML and Text Conversion Tools. (WINDOWS ONLY)
-   1.1 Pitfalls:
    -   1.1.1 when inported back it creates the draft structure, but for the non-draft, research and trash folders, they are wrongly located to INSIDE the draft tree.
    -   1.1.2 when inported back it creates the draft structure, but duplicates it. In theory the draft tree could be deleted, and just keep working with the one imported from text-2-scrib-opml
## To do:
### 2. Improve conversion (1.1)
-   2.1 Solve 1.1.1 and 1.1.2 Meanwhile, deleting manually is not hard. The most important bit, the draft structure is kept.

### 3. FUTURE
- 3.1 Integrate both scripts into separate modules and a main
- 3.2 POC to edit the textfiles from Remarkable, manually drag and droping from folder to remarkable desktop.
- 3.3 POC to do 3.2 automatically.

## Requirements
- Python 3.x: Ensure Python is installed on your system. It can be downloaded from [Python's official website](https://www.python.org/downloads/).
  - Libraries: xml.etree.ElementTree, os, logging, tkinter
- Scrivener: The scripts have been tested with Scrivener 3.0.3 for Windows. It has not been tested on Mac OS.
    
## Installation
The scripts do not require additional installations apart from Python. Simply clone or download this repository to your local machine.

## Usage

### OPMLToTextConverter
Converts an OPML file exported from Scrivener into a directory structure with text files, preserving the hierarchy and synopses.

**Usage Command:**
```bash
python OPMLToTextConverter.py <path_to_opml_file> <output_directory>

### OPMLToTextConverter
Converts an OPML file from Scrivener into a directory structure with text files, preserving the hierarchy and synopses.

**Usage Command:**
```bash
python OPMLToTextConverter.py <path_to_opml_file> <output_directory>
