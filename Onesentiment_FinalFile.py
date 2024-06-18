import csv
from collections import defaultdict
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Perform sentiment analysis
def analyze_sentiment(headlines):
    analyzer = SentimentIntensityAnalyzer()
    compound_scores = [analyzer.polarity_scores(headline)['compound'] for headline in headlines]
    return sum(compound_scores)

# Main function
def main():
    data = defaultdict(list)
    with open(r'C:\Users\MANISH\Desktop\MiniProject_MTech\FinanceNewsData_from_2017_with_scores.csv', 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header if exists
        for row in reader:
            headline, date, sentiment_score = row
            data[date].append(float(sentiment_score))

    sentiment_scores = {}
    for date, scores in data.items():
        sentiment_scores[date] = sum(scores)

    # Write sentiment scores to CSV file
    with open(r'C:\Users\MANISH\Desktop\MiniProject_MTech\TotalsentimentFile.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Date', 'Total Sentiment Score'])  # Write header
        for date, score in sentiment_scores.items():
            writer.writerow([date, score])

if __name__ == "__main__":
    main()
