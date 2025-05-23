# Zoom Review Sentiment Analysis

This project analyzes customer reviews of the Zoom Cloud Meetings app from the Apple App Store. Using Python and Excel, I scraped recent reviews, cleaned and processed the text, performed sentiment classification, and visualized key insights. The goal was to practice end-to-end data analysis using real-world, unstructured data.

## Tools Used

- Python (`requests`, `pandas`, `nltk`)
- Excel (charts, pivot tables, sentiment tagging)
- GitHub (version control and project documentation)

## Key Findings

- Approximately **71%** of user reviews were classified as **positive or neutral**
- Frequently used terms focused on **performance, reliability, and audio quality**
- Negative feedback often referenced **recent bugs and UI issues**

## Project Structure

```
zoom-review-analysis/
├── scripts/
│   ├── review_scraper.py           # Collects reviews from Apple App Store
│   └── common_words.py             # Analyzes frequent nouns/adjectives
├── zoom_review_sentiment_analysis.xlsx   # Raw data, sentiment tags, charts
├── README.md
```

vbnet
Copy
Edit

## How It Works

1. **`review_scraper.py`**: Pulls reviews from the Apple App Store using the Zoom App ID (`546505307`)
2. **`common_words.py`**: Cleans the text, removes stopwords, and identifies the most common descriptive terms
3. **`zoom_review_sentiment_analysis.xlsx`**: Includes raw reviews, manual sentiment labels, pivot tables, and visual summaries

## How to Run

1. Clone this repository
2. Run both Python scripts inside the `scripts/` folder (Python 3 environment recommended)
3. Open the Excel file to explore the results and visuals

## About

This project is part of my **self-directed learning journey into data analytics**. It highlights my ability to:
- Work with APIs and JSON data
- Clean and preprocess unstructured text
- Apply basic natural language processing (NLP)
- Visualize and communicate insights clearly

Feel free to explore or fork this repository. Feedback is always welcome!
