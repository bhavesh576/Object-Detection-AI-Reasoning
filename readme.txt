Microsoft Windows [Version 10.0.19045.6466]
(c) Microsoft Corporation. All rights reserved.

C:\Users\dell>cd C:\Users\dell\Desktop\tools

C:\Users\dell\Desktop\tools>python organize.py
Renaming + Organizing Completed Successfully!

instruction :-

1. Overview

This tool automatically:

Renames all images in a folder

Organizes them into a clean output folder

Uses a uniform naming pattern:
img_0001.jpg, img_0002.jpg, …

Useful for preparing raw client data before annotation.

2. Supported Formats

.jpg

.jpeg

.png

.webp

3. Requirements

Python installed

No external libraries needed

4. How to Use

Create a file named organize.py

Copy–paste the script inside it

Edit these two lines:

source_folder = r"C:\path\to\raw\data"
output_folder = r"C:\path\to\organized\output"


Open terminal and run:

python organize.py

5. What Happens After Running

All images are renamed in sequence

Renamed images are copied into the output folder

Original images are untouched

Output folder becomes clean, sorted, and ready for annotation

6. Notes

Safe to use on large datasets

Does not require internet

No subscription or cost

Designed for beginners


