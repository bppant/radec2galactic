"""
RA/Dec to Galactic Coordinates Converter.

Convert equatorial coordinates (Right Ascension and Declination)
from the ICRS/J2000 frame to Galactic longitude and latitude.

Supports:
1. Single RA/Dec coordinate conversion.
2. Batch conversion of RA/Dec columns in a CSV file.

Author: Bhanu Prakash Pant
"""

import os

import astropy.units as u
import pandas as pd
from astropy.coordinates import SkyCoord


def convert_coordinates(coord):
    """
    Convert SkyCoord coordinates to Galactic longitude and latitude.

    Parameters
    ----------
    coord : astropy.coordinates.SkyCoord
        Input coordinates in the ICRS frame.

    Returns
    -------
    tuple
        Galactic longitude (l) and latitude (b), both in degrees.
    """
    galactic = coord.galactic
    return galactic.l.deg, galactic.b.deg


def convert_single_coordinate():
    """Convert a single RA/Dec coordinate entered by the user."""
    try:
        ra = float(input("Enter Right Ascension (RA) in degrees: "))
        dec = float(input("Enter Declination (Dec) in degrees: "))

        if not 0 <= ra < 360:
            print("Error: RA must be between 0 and 360 degrees.")
            return

        if not -90 <= dec <= 90:
            print("Error: Declination must be between -90 and +90 degrees.")
            return

        coord = SkyCoord(ra=ra * u.deg, dec=dec * u.deg, frame="icrs")

        glon, glat = convert_coordinates(coord)

        print("\nResult:")
        print(f"Galactic Longitude (l): {glon:.6f} deg")
        print(f"Galactic Latitude (b):  {glat:.6f} deg")

    except ValueError:
        print("Error: Please enter valid numerical values.")


def convert_csv_file():
    """Convert RA/Dec columns in a CSV file to Galactic coordinates."""
    file_path = input("Enter the path to your CSV file: ").strip()

    if not os.path.isfile(file_path):
        print(f"Error: File '{file_path}' not found.")
        return

    try:
        df = pd.read_csv(file_path, sep=None, engine="python")

        print("\nAvailable columns:")
        for column in df.columns:
            print(f"  - {column}")

        ra_col = input("\nEnter the name of the RA column: ").strip()
        dec_col = input("Enter the name of the Dec column: ").strip()

        if ra_col not in df.columns:
            print(f"Error: RA column '{ra_col}' does not exist.")
            return

        if dec_col not in df.columns:
            print(f"Error: Dec column '{dec_col}' does not exist.")
            return

        # Convert input columns to numeric values.
        ra_values = pd.to_numeric(df[ra_col], errors="coerce")
        dec_values = pd.to_numeric(df[dec_col], errors="coerce")

        invalid_rows = ra_values.isna() | dec_values.isna()

        if invalid_rows.any():
            print(
                f"\nWarning: {invalid_rows.sum()} row(s) contain "
                "invalid or missing RA/Dec values."
            )

        # Create an output dataframe column initialized with NaN.
        df["glon_deg"] = float("nan")
        df["glat_deg"] = float("nan")

        valid = ~invalid_rows

        if valid.any():
            coord = SkyCoord(
                ra=ra_values[valid].values * u.deg,
                dec=dec_values[valid].values * u.deg,
                frame="icrs",
            )

            glon, glat = convert_coordinates(coord)

            df.loc[valid, "glon_deg"] = glon
            df.loc[valid, "glat_deg"] = glat

        output_path = os.path.join(
            os.path.dirname(file_path),
            "converted_" + os.path.basename(file_path),
        )

        df.to_csv(output_path, index=False)

        print(f"\nSuccess!")
        print(f"Converted file saved to: {output_path}")

    except Exception as error:
        print(f"An error occurred: {error}")


def main():
    """Run the RA/Dec to Galactic coordinate converter."""
    print("=" * 45)
    print("     RA/Dec to Galactic Coordinates")
    print("=" * 45)
    print("\n1. Convert a single RA/Dec coordinate")
    print("2. Convert RA/Dec columns from a CSV file")

    choice = input("\nEnter your choice (1 or 2): ").strip()

    if choice == "1":
        convert_single_coordinate()

    elif choice == "2":
        convert_csv_file()

    else:
        print("Invalid choice. Please select 1 or 2.")


if __name__ == "__main__":
    main()

