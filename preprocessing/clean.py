import pandas as pd
import re

# Function to clean Fake.csv
def clean_title(title):
    # Handle NaN values
    if pd.isna(title):
        return ''
    
    # Convert to string if not already
    title = str(title)
    
    # Remove text between () and []
    title = re.sub(r'\([^)]*\)', '', title)  # Remove (text)
    title = re.sub(r'\[[^]\}]*[\]}]', '', title)  # Remove [text] and [text}
    title = re.sub(r'\[[^\[]*\[', '', title)  # Remove [text[
    
    # Clean up all extra whitespace and strip leading/trailing spaces
    title = ' '.join(title.split()).strip()
    
    return title

try:
    # Read the CSV
    df = pd.read_csv('Fake.csv')
    print(f"Initial rows: {len(df)}")
    
    # Show a few original titles
    print("\nBefore cleaning:")
    for idx, title in enumerate(df['title'].head(3)):
        print(f"{idx + 1}. '{title}'")  # Added quotes to see whitespace

    # Clean the title column
    df['title'] = df['title'].apply(clean_title)
    
    # Remove duplicates
    df = df.drop_duplicates(subset=['title'], keep='first')

    # Save cleaned file
    df.to_csv('Fake_cleaned.csv', index=False)
    print("Cleaning complete. Saved as Fake_cleaned.csv")
    
    print("\nAfter cleaning:")
    for idx, title in enumerate(df['title'].head(10)):
        print(f"{idx + 1}. '{title}'")  # Added quotes to see whitespace
    
except Exception as e:
    print(f"Error processing file: {str(e)}")

# Function to clean Real.csv
def clean_text(text):
    # Handle NaN values
    if pd.isna(text):
        return ''
    
    # Convert to string if not already
    text = str(text)
    
    # Remove city and source pattern, case insensitive for source
    text = re.sub(r'^[A-Z\s]+,?\s*[A-Za-z\.]+(?:/[A-Z\s]+)*\s*\([A-Za-z]+\)\s*-?\s*', '', text)
    
    # Remove Reuters patterns with extra text inside parentheses; for row 233
    text = re.sub(r'^[A-Z\s]+\s*\([Rr][Ee][Uu][Tt][Ee][Rr][Ss][^)]*\)\s*-?\s*', '', text)

    # Remove standalone (REUTERS) or (Reuters) with optional dash
    text = re.sub(r'\s*\([Rr][Ee][Uu][Tt][Ee][Rr][Ss]\)\s*-?\s*', '', text)
    
    # Clean up all extra whitespace and strip leading/trailing spaces
    text = ' '.join(text.split()).strip()
    
    return text

try:
    # Read the CSV
    df = pd.read_csv('True.csv')
    print(f"Initial rows: {len(df)}")
    
    # Show a few original texts
    print("\nBefore cleaning:")
    for idx, text in enumerate(df['text'].head(3)):
        print(f"{idx + 1}. '{text}'")  # Added quotes to see whitespace

    # Clean the text column
    df['text'] = df['text'].apply(clean_text)
    
    # Remove duplicates
    df = df.drop_duplicates(subset=['title'], keep='first')

    # Save cleaned file
    df.to_csv('True_cleaned.csv', index=False)
    print("Cleaning complete. Saved as Real_cleaned.csv")
    
    print("\nAfter cleaning:")
    for idx, text in enumerate(df['text'].head(10)):
        print(f"{idx + 1}. '{text}'")  # Added quotes to see whitespace
    
except Exception as e:
    print(f"Error processing file: {str(e)}")