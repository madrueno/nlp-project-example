"""ETL script to merge YouTube spam CSV files."""

import os
import pandas as pd


PATH_RAW_DATA = os.path.join('data', 'raw')


def load_youtube_csvs(raw_dir: str) -> pd.DataFrame:
    """
    Load all YouTube spam CSV files and merge into single DataFrame.

    Parameters
    ----------
    raw_dir : str
        Directory containing the youtube-spam-collection folder

    Returns
    -------
    pd.DataFrame
        Merged DataFrame with all columns from the CSV files
    """
    youtube_dir = os.path.join(raw_dir, 'youtube-spam-collection')

    # Find all CSV files
    csv_files = [f for f in os.listdir(youtube_dir) if f.endswith('.csv')]
    print(f"Found {len(csv_files)} CSV files")

    all_data = []
    for filename in sorted(csv_files):
        filepath = os.path.join(youtube_dir, filename)
        print(f"- Reading {filename}")
        df = pd.read_csv(filepath, encoding='utf-8')
        all_data.append(df)

    # Merge all dataframes
    merged_df = pd.concat(all_data, ignore_index=True)
    print(f"\nTotal rows: {len(merged_df)}")

    return merged_df


def main() -> None:
    """
    Merge all YouTube spam CSV files and save to interim.

    Loads all CSV files from data/raw/youtube-spam-collection/
    and saves merged file to data/interim/comments.csv.
    """
    df = load_youtube_csvs(PATH_RAW_DATA)

    # Save to interim
    interim_dir = os.path.join('data', 'interim')
    os.makedirs(interim_dir, exist_ok=True)
    output_path = os.path.join(interim_dir, 'comments.csv')

    print(f"\nSaving to {output_path}...")
    df.to_csv(output_path, index=False)
    print("Done!")


if __name__ == '__main__':
    main()
