"""Post newly found internships to a Telegram channel.

Configured through two environment variables (GitHub Actions secrets):
    TELEGRAM_BOT_TOKEN  token from @BotFather
    TELEGRAM_CHAT_ID    "@channel_username" or a numeric "-100..." chat id

When either is missing the notifier is a no-op, so forks and local runs work
unchanged. Failures are reported but never fail the scrape.
"""
import html
import os
import re
import time
from collections import Counter

import requests

API_URL = "https://api.telegram.org/bot{token}/sendMessage"
SITE_URL = "https://emjumaev.github.io/FAANG-2027-Internships-Tracker-Europe/"
# Above this many new internships in one run (a backfill, or a scraper recovering
# after downtime) send a single summary instead of flooding the channel.
MAX_MESSAGES = 15
# Telegram allows ~20 messages/minute per channel.
SEND_INTERVAL_SECONDS = 3
TIMEOUT = 30


def channel_url():
    """Public t.me link for the channel, or None if it has no @username."""
    chat_id = os.environ.get("TELEGRAM_CHAT_ID", "")
    if chat_id.startswith("@"):
        return "https://t.me/{}".format(chat_id[1:])
    return None


def _hashtag(text):
    tag = re.sub(r"[^0-9A-Za-z]+", "_", text).strip("_")
    return "#" + tag if tag else ""


def _fmt_locations(locations, limit=3):
    locs = [l for l in locations if l]
    if not locs:
        return None
    shown = "; ".join(locs[:limit])
    extra = len(locs) - limit
    if extra > 0:
        shown += " (+{} more)".format(extra)
    return shown


def format_job(job):
    e = html.escape
    category = job.get("category") or "Software"
    details = [job["company"], category]
    if job.get("degrees"):
        details.append("/".join(job["degrees"]))
    lines = [
        "🆕 <b>{}</b>".format(e(job["title"])),
        "🏢 {}".format(" · ".join(e(d) for d in details)),
    ]
    locations = _fmt_locations(job.get("locations", []))
    if locations:
        lines.append("📍 {}".format(e(locations)))
    lines.append('<a href="{}">View internship →</a>'.format(e(job["url"], quote=True)))
    tags = [_hashtag(t) for t in [category, job["company"]] + list(job.get("degrees", []))]
    lines.append(" ".join(t for t in tags if t))
    return "\n".join(lines)


def format_summary(jobs):
    counts = Counter(j["company"] for j in jobs)
    lines = ["🆕 <b>{} new internships</b>\n".format(len(jobs))]
    for company, n in sorted(counts.items(), key=lambda kv: (-kv[1], kv[0])):
        lines.append("• {}: {}".format(html.escape(company), n))
    lines.append('\n<a href="{}">Browse all open internships →</a>'.format(SITE_URL))
    return "\n".join(lines)


def _send(token, chat_id, text):
    for _ in range(3):
        resp = requests.post(API_URL.format(token=token), timeout=TIMEOUT, data={
            "chat_id": chat_id,
            "text": text,
            "parse_mode": "HTML",
            "disable_web_page_preview": "true",
        })
        if resp.status_code == 429:
            retry_after = resp.json().get("parameters", {}).get("retry_after", 5)
            time.sleep(retry_after + 1)
            continue
        if not resp.ok:
            raise RuntimeError("HTTP {}: {}".format(resp.status_code, resp.text))
        return
    raise RuntimeError("rate-limited by Telegram")


def notify(added):
    """Post added internship dicts to the channel. Returns the number of messages sent."""
    token = os.environ.get("TELEGRAM_BOT_TOKEN")
    chat_id = os.environ.get("TELEGRAM_CHAT_ID")
    if not (token and chat_id) or not added:
        return 0

    if len(added) > MAX_MESSAGES:
        messages = [format_summary(added)]
    else:
        messages = [format_job(j) for j in
                    sorted(added, key=lambda j: (j["company"], j["title"]))]

    sent = 0
    for i, text in enumerate(messages):
        if i:
            time.sleep(SEND_INTERVAL_SECONDS)
        try:
            _send(token, chat_id, text)
            sent += 1
        except Exception as err:  # noqa: BLE001 - never fail the scrape over a notification
            print("[telegram] send failed: {}".format(err))
    return sent
