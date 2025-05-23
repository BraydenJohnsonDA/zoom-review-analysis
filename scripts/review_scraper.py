import requests
import pandas as pd
import time

# App ID for Zoom Cloud Meetings from the Apple App Store
app_id = "546505307"

# Store all reviews
df_all = []

# Scrape first 5 pages of customer reviews
for page in range(1, 6):
    print(f"Scraping page {page}...")

    url = f"https://itunes.apple.com/rss/customerreviews/page={page}/id={app_id}/sortby=mostrecent/json"
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Failed to fetch page {page}")
        continue

    data = response.json()
    entries = data.get("feed", {}).get("entry", [])[1:]  # Skip metadata

    for entry in entries:
        review_text = entry.get("content", {}).get("label", "").strip()
        title = entry.get("title", {}).get("label", "").strip()
        rating = entry.get("im:rating", {}).get("label", "").strip()
        date = entry.get("updated", {}).get("label", "").strip()

        # Filter out very short reviews
        if review_text and len(review_text) > 20:
            df_all.append({
                "title": title,
                "rating": rating,
                "text": review_text,
                "date": date
            })

    time.sleep(1)  # Be respectful of Apple's servers

# Check if any reviews were gathered
if not df_all:
    print("No reviews found. Check the app ID or Apple review feed.")
    exit()

# Save to CSV
df = pd.DataFrame(df_all)
df.to_csv("apple_app_reviews_raw.csv", index=False)

print(f"Scraped {len(df)} reviews. Data saved to apple_app_reviews_raw.csv")
input("\nPress Enter to exit...")
