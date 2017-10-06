# Reading spreadsheet data to produce one webpage per line and one printable sticker per line

This is a project for the Physical Computing Lab housed in the [IDeATe 
program](http://ideate.andrew.cmu.edu) at [Carnegie Mellon 
University](http://cmu.edu).

The intended workflow is to read our main inventory spreadsheet as the data source; it is 
interpreted by two different Python scripts: one to create labels, and one to generate 
webpages.

## Label maker

A Python script, `binLabeler.py`, ingests a CSV with specific columns present, reading the 
data in each row and incorporating an image stored in a separate directory, to ultimately 
create one output PNG per row of the CSV.

## Web pages generation

The IDeATe parts website is generated in two steps. 
1) A Python script `partsToJekyllPages.py` ingests a CSV with specific columns present and 
writes out a folder full 
of markdown documents. 
2) Jekyll (a static HTML site generator) reads that folder, recognizing each markdown 
document as the source for a single HTML page, and generates an HTML site.
