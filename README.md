# 🧠 Crontab Explainer

Ever forget what a cron expression like `0 2 * * 1` means?

This tool converts your cron expression into a **clear, human-readable schedule**, with optional next run info.

---

## 🚀 Example

```bash
$ python3 explain_cron.py "0 2 * * 1"
```
## ✅ Cron Expression Breakdown:

- ⏰ This job runs at 2:0 on every Monday
- 📆 Next run: 2025-07-07 02:00:00

## 🛠️ Installation
```
pip install -r requirements.txt
```
## 📘 Cron Format Reminder

```
┌───────────── minute (0 - 59)
│ ┌───────────── hour (0 - 23)
│ │ ┌───────────── day of month (1 - 31)
│ │ │ ┌───────────── month (1 - 12)
│ │ │ │ ┌───────────── day of week (0 - 7) (Sunday = 0 or 7)
│ │ │ │ │
│ │ │ │ │
* * * * *
```
## 💡 Use Cases
- Understand unfamiliar cron jobs
- Debug Jenkins/K8s scheduled jobs
- Convert to readable text for documentation


## 🔐 License
- MIT License

## 🙌 Contributions
- Star ⭐ it | Fork 🍴 it | Make it better 🚀
