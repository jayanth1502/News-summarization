import feedparser
from transformers import pipeline
from datetime import datetime
import os, schedule, time

# 📂 Reports folder
REPORTS_DIR = "reports"
os.makedirs(REPORTS_DIR, exist_ok=True)

# 🤖 Load models
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
sentiment = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

# 🔎 Keywords
KEYWORDS = ["Hack", "regulation", "ETF"]

# --- Fetch News ---
def get_general_news(limit=5):  
    url = "https://cointelegraph.com/rss"
    feed = feedparser.parse(url)
    return feed.entries[:limit]

def get_token_news(token="BTC", limit=3):
    url = "https://cointelegraph.com/rss"
    feed = feedparser.parse(url)
    token_news = []
    for entry in feed.entries:
        if token.lower() in entry.title.lower() or token.lower() in entry.summary.lower():
            token_news.append(entry)
        if len(token_news) >= limit:
            break
    return token_news

# --- AI Summary ---
def summarize_text(text):
    try:
        return summarizer(text[:1000], max_length=60, min_length=20, do_sample=False)[0]['summary_text']
    except:
        return text[:200] + "..."

# Trading Signal 
def generate_signal(text):
    result = sentiment(text[:512])[0]
    label = result['label']
    if label == "POSITIVE":
        return "BUY ✅"
    elif label == "NEGATIVE":
        return "SELL ❌"
    else:
        return "HOLD ⚖️"

# Generate & Save Report
def generate_report():
    now = datetime.now()
    lines = []
    lines.append(f"=== Crypto News Report ({now}) ===\n")

    # General News
    general = get_general_news()
    lines.append("🌍 General Crypto News:\n")
    for entry in general:
        summary = summarize_text(entry.summary)
        signal = generate_signal(summary)
        lines.append(f"📰 {entry.title}")
        lines.append(f"🔗 {entry.link}")
        lines.append(f"🤖 AI Summary: {summary}")
        lines.append(f"💹 Signal: {signal}")

        # Keyword alerts under each news item
        for word in KEYWORDS:
            if word.lower() in entry.title.lower() or word.lower() in entry.summary.lower():
                lines.append(f"⚡ Keyword Alert: '{word}' in → {entry.title}")

        lines.append("-" * 60)

    # BTC Top 3 News
    btc_news = get_token_news("BTC")
    lines.append("\n=== BTC Top 3 News ===\n")
    for entry in btc_news:
        summary = summarize_text(entry.summary)
        signal = generate_signal(summary)
        lines.append(f"📰 {entry.title}")
        lines.append(f"🔗 {entry.link}")
        lines.append(f"🤖 AI Summary: {summary}")
        lines.append(f"💹 Signal: {signal}")

        # Keyword alerts under each news item
        for word in KEYWORDS:
            if word.lower() in entry.title.lower() or word.lower() in entry.summary.lower():
                
                lines.append(f"⚡ Keyword Alert: '{word}' in → {entry.title}")

        lines.append("-" * 60)

    # Save file with timestamp 
    filename = os.path.join(REPORTS_DIR, f"report_{now.strftime('%Y-%m-%d_%H-%M-%S')}.txt")
    with open(filename, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    # Print on console
    print("\n".join(lines))
    print(f"\n✅ Report saved at {filename}")

# Run once for demo
generate_report()

# Schedule daily at 9 PM EST
schedule.every().day.at("17:25").do(generate_report)

print("\n⏳ Scheduler running... waiting for 17:25 PM EST.\n")
while True:
    schedule.run_pending()
    time.sleep(30)
