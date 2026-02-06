# 🏆 Cupid's Command Center

> **"What if Cupid had a real-time mission control to ensure no Valentine's Day goes wrong?"**

An AI-Powered Valentine's Operations Hub built for GeeksterFY26 Hackathon.

![Mission Control](https://img.shields.io/badge/Status-Mission%20Active-red)
![Tech](https://img.shields.io/badge/Powered%20By-Microsoft%20AI-blue)

---

## 🎬 The Story

*"It's February 14th. Millions of people are counting on the perfect gift arriving on time. But there's a snowstorm in Germany, a supplier delay in Belgium, and 2,000 chocolates stuck at customs. Cupid is overwhelmed.*

*Enter: **Cupid's Command Center** — the AI co-pilot that helps Cupid save Valentine's Day."*

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────┐
│           CUPID'S COMMAND CENTER                        │
├─────────────────────────────────────────────────────────┤
│  📊 REAL-TIME DASHBOARD (Power BI)                      │
│  ├─ Sales velocity by region (live updating)            │
│  ├─ Supply chain risk alerts (red/yellow/green)         │
│  └─ Customer sentiment score                            │
├─────────────────────────────────────────────────────────┤
│  🤖 AI COPILOT (Copilot Studio + Azure OpenAI)          │
│  ├─ "What's the biggest risk right now?"                │
│  ├─ "Suggest recovery plan for delayed shipments"       │
│  └─ "Draft customer apology email for region X"         │
├─────────────────────────────────────────────────────────┤
│  ⚡ AUTOMATED ACTIONS (Power Automate)                  │
│  ├─ Trigger alerts when stock < threshold               │
│  ├─ Auto-notify customers of delays                     │
│  └─ Escalate to human when AI confidence < 70%          │
└─────────────────────────────────────────────────────────┘
```

---

## 📊 Datasets Used

| Dataset | Purpose |
|---------|---------|
| Cupid Chocolate Global (7 tables) | Sales, customers, products, stores |
| Supply Chain | Delay predictions, stock alerts |
| Gift Recommender | Customer behavior patterns |
| Global Routing | Delivery performance metrics |
| Love Notes Telemetry | Message delivery success |

---

## 🚀 Quick Start (Run Dashboard in 2 Minutes)

### Prerequisites
- Python 3.10+ installed
- pip (Python package manager)

### Steps

```bash
# 1. Clone the repository
git clone https://github.com/nikidandwani/cupids-command-center.git
cd cupids-command-center

# 2. Install dependencies
pip install pandas plotly

# 3. Generate and open the dashboard
cd dashboard
python generate_dashboard.py
```

The dashboard will automatically open in your browser! 🎉

### Alternative: Direct HTML
If you just want to view the dashboard without regenerating:
1. Navigate to `dashboard/` folder
2. Open `cupids_command_center.html` in any browser

---

## 📊 Dashboard Features

| Feature | Description |
|---------|-------------|
| 📈 KPI Cards | Revenue, Orders, Risk Level, Alerts (clickable) |
| 🌍 Sales by Region | Interactive chart with drill-down |
| 🎯 Risk Radar | Gauge showing overall risk score |
| 📦 Inventory Alerts | Traffic light status table |
| 🚚 Delivery Delays | Region-specific delay information |
| 🤖 AI Copilot | Chat panel with quick actions |

---

## 🛠️ Full Setup (For Development)

### 1. Data Preparation
```bash
cd data-prep
python prepare_data.py
```

### 2. Power BI Dashboard
- Open `powerbi/CupidsCommandCenter.pbix`
- Connect to your data source

### 3. Copilot Studio Bot
- Import `copilot-studio/bot-config.json`
- Configure Azure OpenAI connection

### 4. Power Automate Flows
- Import flows from `power-automate/` folder

---

## 📁 Project Structure

```
cupids-command-center/
├── README.md
├── data-source/              # Cloned hackathon datasets
├── data-prep/                # Python scripts for data processing
├── powerbi/                  # Power BI dashboard files
├── copilot-studio/           # Bot configuration
├── power-automate/           # Automation flow definitions
├── azure-openai/             # Prompts and AI configuration
└── presentation/             # Demo script and slides
```

---

## 🎤 Demo Script (4 Minutes)

1. **Hook (30s):** "It's Valentine's Day. 50,000 orders. 3 suppliers delayed."
2. **Dashboard (60s):** Show real-time alerts, drill into problems
3. **AI Copilot (90s):** Natural language queries and responses
4. **Automation (30s):** Demonstrate auto-notifications
5. **Close (30s):** "We turned chaos into control."

---

## 👥 Team

Built with 💝 for GeeksterFY26 Hackathon - February 6th, 2026

---

*"May the odds be ever in your favor. Or at least in your regression models!"* ✨
