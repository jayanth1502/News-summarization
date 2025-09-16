
````markdown
# Crypto News Summarizer & Trading Signal Generator

A Python-based tool that fetches the latest cryptocurrency news, generates AI-powered summaries, analyzes sentiment, highlights key keywords, and provides basic trading signals. Reports are saved as timestamped text files for easy reference.

---

## Features

- **Fetch General & Token-Specific News**  
  Retrieves the latest crypto news from CoinTelegraph RSS feeds. Supports filtering by specific tokens like BTC.

- **AI-Powered Summaries**  
  Uses `facebook/bart-large-cnn` to generate concise and informative summaries of news articles.

- **Sentiment Analysis & Trading Signals**  
  Uses `distilbert-base-uncased-finetuned-sst-2-english` to determine sentiment:  
  - Positive → `BUY ✅`  
  - Negative → `SELL ❌`  
  - Neutral → `HOLD ⚖️`

- **Keyword Alerts**  
  Highlights critical terms such as `Hack`, `Regulation`, `ETF`.

- **Automated Reporting**  
  Generates and saves timestamped reports in the `reports/` folder.

- **Scheduled Execution**  
  Automatically runs daily at a configured time (currently 17:25 EST).

---

## Installation

1. **Clone the repository**
```bash
git clone <repository-url>
cd <project-folder>
````

2. **Install dependencies**

```bash
pip install feedparser transformers schedule torch
```

---

## Usage

1. **Run the script**

```bash
python crypto_news_report.py
```

2. **Outputs**

* Console prints the latest news, AI summaries, trading signals, and keyword alerts.
* Reports are saved in the `reports/` folder with timestamped filenames:
  `report_YYYY-MM-DD_HH-MM-SS.txt`

3. **Scheduled Execution**

```python
schedule.every().day.at("17:25").do(generate_report)
```

---

## Configuration

* **Keywords to track**

```python
KEYWORDS = ["Hack", "regulation", "ETF"]
```

* **Token-specific news**
  Change the token in `get_token_news(token="BTC")` to track a different cryptocurrency.

* **Summary & Sentiment Limits**

  * Summarizer: first 1000 characters
  * Sentiment: first 512 characters

---

## Sample Report Output

```
=== Crypto News Report (2025-09-12 12:49:07) ===

🌍 General Crypto News:

 Michael Saylor’s Bitcoin obsession: How it all started
🔗 https://cointelegraph.com/news/michael-saylor-s-bitcoin-obsession-how-it-all-started?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
🤖 AI Summary: Explore Michael Saylor's Bitcoin playbook, Strategy’s debt-fueled purchases and the future outlook of corporate crypto investing.
💹 Signal: BUY ✅
------------------------------------------------------------
📰 Bitcoin is ‘made for us’: Africa’s first treasury company eyes unique opportunity
🔗 https://cointelegraph.com/news/africa-bitcoin-treasury-company-unique-opportunity?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
🤖 AI Summary: Africa has its first Bitcoin treasury company, but its utility goes far deeper than publicly-listed stocks tied to BTC holdings.
💹 Signal: BUY ✅
------------------------------------------------------------
📰 How to turn crypto news into trade signals using Grok 4
🔗 https://cointelegraph.com/news/how-to-turn-crypto-news-into-trade-signals-using-grok-4?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
🤖 AI Summary: Grok 4 can help you turn crypto headlines into market moves. It filters news and analyzes sentiment to create effective trade signals.
💹 Signal: SELL ❌
------------------------------------------------------------
📰 New ModStealer malware targets crypto wallets across operating systems
🔗 https://cointelegraph.com/news/modstealer-malware-crypto-wallets-fake-job-ads?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
🤖 AI Summary: Hacken’s Stephen Ajayi says basic wallet hygiene and endpoint hardening are essential to defend against threats like ModStealer.
💹 Signal: SELL ❌
⚡ Keyword Alert: 'Hack' in → New ModStealer malware targets crypto wallets across operating systems
------------------------------------------------------------
📰 How to day trade crypto using Google’s Gemini AI
🔗 https://cointelegraph.com/news/how-to-day-trade-crypto-using-google-s-gemini-ai?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
🤖 AI Summary: Google Gemini AI offers day traders new ways to cut through noise, manage risk and act on market catalysts with confidence.
💹 Signal: BUY ✅
------------------------------------------------------------

=== BTC Top 3 News ===

📰 Bitcoin is ‘made for us’: Africa’s first treasury company eyes unique opportunity
🔗 https://cointelegraph.com/news/africa-bitcoin-treasury-company-unique-opportunity?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
🤖 AI Summary: Africa has its first Bitcoin treasury company, but its utility goes far deeper than publicly-listed stocks tied to BTC holdings.
💹 Signal: BUY ✅
------------------------------------------------------------
📰 Bitcoin ‘sharks’ add 65K BTC in a week in key demand rebound
🔗 https://cointelegraph.com/news/bitcoin-sharks-add-65k-btc-in-week-demand-rebound?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
🤖 AI Summary: Bitcoin is a “buy” again for some investor cohorts, with sharks standing out after a week-long BTC buying spree.
💹 Signal: BUY ✅
------------------------------------------------------------
📰 Bitcoin reclaims $115K: Watch these BTC price levels next
🔗 https://cointelegraph.com/news/bitcoin-reclaims-115k-watch-these-btc-price-levels-next?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
🤖 AI Summary: Bitcoin price sees a modest recovery driven by derivatives. Big overhead resistance above $116,000 in place and several key support levels below.
💹 Signal: SELL ❌
------------------------------------------------------------
```

