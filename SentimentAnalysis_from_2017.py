import re
import csv
from collections import defaultdict
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Preprocess data
def preprocess_data(data):
    processed_data = []
    for headline, date in data:
        headline = re.sub(r'[^\w\s]', '', headline)  # Remove special characters
        headline = headline.lower()  # Convert to lowercase
        processed_data.append((headline, date))
    return processed_data

# Group headlines by date
def group_by_date(data):
    grouped_data = defaultdict(list)
    for headline, date in data:
        grouped_data[date].append(headline)
    return grouped_data

# Perform sentiment analysis
def analyze_sentiment(headlines):
    analyzer = SentimentIntensityAnalyzer()
    compound_scores = [analyzer.polarity_scores(headline)['compound'] for headline in headlines]
    return sum(compound_scores) / len(compound_scores) if compound_scores else 0

# Main function
def main():
    data = []
    with open(r'C:\Users\MANISH\Desktop\MiniProject_MTech\FinanceNewsData_from_2017.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader)  # Get header
        for row in reader:
            headline, date = row
            data.append((headline, date))

    processed_data = preprocess_data(data)
    grouped_data = group_by_date(processed_data)
    
    sentiment_scores = {}
    for date, headlines in grouped_data.items():
        sentiment_scores[date] = analyze_sentiment(headlines)
    
    # Write sentiment scores back to CSV file
    with open(r'C:\Users\MANISH\Desktop\MiniProject_MTech\FinanceNewsData_from_2017_with_scores.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(header + ['Sentiment Score'])  # Write header with additional column
        with open(r'C:\Users\MANISH\Desktop\MiniProject_MTech\FinanceNewsData_from_2017.csv', 'r', encoding='utf-8') as file:
            reader = csv.reader(file)  # Reopen the file
            next(reader)  # Skip header
            for row in reader:
                headline, date = row
                score = sentiment_scores.get(date, 0)  # Get sentiment score for the date
                writer.writerow(row + [score])  # Write row with sentiment score

if __name__ == "__main__":
    main()
