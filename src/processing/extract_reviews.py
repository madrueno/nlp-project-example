"""ETL script to extract IMDB reviews from raw data to interim CSVs."""

import os
import pandas as pd


PATH_RAW_DATA = os.path.join('data', 'raw', 'aclImdb')


def fetch_reviews(path: str) -> list[str]:
    """
    Fetch all reviews from a directory.

    Parameters
    ----------
    path : str
        Path to directory containing review text files

    Returns
    -------
    list of str
        List of review texts
    """
    data = []
    files = [f for f in os.listdir(path)]
    for file in files:
        file_path = os.path.join(path, file)
        with open(file_path, "r", encoding='utf8') as f:
            data.append(f.read())

    return data


def main() -> None:
    """
    Extract IMDB reviews from raw data and save to interim CSVs.

    Processes both train and test splits, reading positive and negative
    reviews, creating DataFrames, and saving to data/interim/.
    """
    splits = ['train', 'test']
    sentiments = ['pos', 'neg']

    for split in splits:
        print(f"Processing {split} data...")

        # Gather reviews and labels
        reviews, labels = [], []
        for sentiment in sentiments:
            path = os.path.join(PATH_RAW_DATA, split, sentiment)
            print(f"- Reading from {path}")

            sentiment_reviews = fetch_reviews(path)
            label = 1 if sentiment == 'pos' else 0

            reviews.extend(sentiment_reviews)
            labels.extend([label] * len(sentiment_reviews))

        # Create DataFrame
        df = pd.DataFrame({
            'text': reviews,
            'label': labels
        })

        print(f"- Total reviews: {len(df)}")

        # Save to interim
        interim_dir = os.path.join('data', 'interim')
        os.makedirs(interim_dir, exist_ok=True)
        output_path = os.path.join(interim_dir, f'{split}.csv')
        df.to_csv(output_path, index=False)

        print(f"- Saved to {output_path}")
        print()


if __name__ == '__main__':
    main()
