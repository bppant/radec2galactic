# RA/Dec to Galactic Coordinates

A simple Python tool for converting **Right Ascension (RA)** and **Declination (Dec)** from the **ICRS (International Celestial Reference System)** frame to **Galactic coordinates**.

The program supports both single-coordinate conversion and batch conversion of RA/Dec coordinates from CSV files.

## Features

- Convert a single RA/Dec coordinate to Galactic coordinates
- Batch-convert RA/Dec columns from a CSV file
- Calculate Galactic longitude (`l`) and latitude (`b`)
- Input coordinates in degrees
- Preserve the original CSV data
- Automatically save converted CSV files
- Uses [Astropy](https://www.astropy.org/) for astronomical coordinate transformations
- Uses [Pandas](https://pandas.pydata.org/) for CSV processing

## Coordinate Transformation

The program performs the following transformation:

**ICRS Equatorial Coordinates**

- Right Ascension (RA)
- Declination (Dec)

↓

**Galactic Coordinates**

- Galactic longitude (`l`)
- Galactic latitude (`b`)

All coordinates are expressed in degrees.

## Requirements

- Python 3.9 or later
- Astropy
- Pandas

Install the dependencies with:

```bash
pip install -r requirements.txt
```
## Usage
Run the program with:
```bash
python radec2galactic.py
```
You will be given two options:
1. Convert a single RA/Dec coordinate
2. Convert RA/Dec columns from a CSV file

## Single Coordinate

Select option 1 and enter RA and Dec in degrees. The program returns: Galactic Longitude (l) and Galactic Latitude (b).

## CSV Batch Conversion

Select option 2 and provide the path to your CSV file. The program displays the available columns and asks you to specify the names of the columns that contain RA and Dec. Two new columns are added to the output: glon_deg, glat_deg. 

## Input

The program expects:

- Right Ascension (RA): 0 <= RA < 360 degrees
- Declination (Dec): -90 <= Dec <= +90 degrees
- Coordinate frame: ICRS

## Applications

This tool can be useful for:

- Astronomy and astrophysics
- Astronomical catalogs
- Stellar and Galactic coordinate analysis
- Sky surveys
- Astronomical databases
- Research data processing
- Coordinate conversion workflows
 
## License

This project is licensed under the BSD 3-Clause License. See the LICENSE file for details.

## Acknowledgements
This project uses Astropy for astronomical coordinate transformations and Pandas for CSV data processing.

***Keywords:*** Python, astronomy, astrophysics, RA, Dec, Right Ascension, Declination, ICRS, Galactic coordinates, Galactic longitude, Galactic latitude, astronomical coordinates, coordinate conversion, Astropy
