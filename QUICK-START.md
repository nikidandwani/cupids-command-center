# 🚀 Quick Start Guide - Cupid's Command Center

## For New Team Members (5-minute setup)

### Step 1: Get the Files
Copy this entire folder to your laptop, OR run:
```powershell
git clone https://github.com/AndreeaDan27/GeeksterFY26.git data-source
```

### Step 2: Install Python (if needed)
```powershell
# Check if Python is installed
python --version

# If not, install via Microsoft Store or python.org
```

### Step 3: Prepare the Data
```powershell
cd data-prep
pip install pandas
python prepare_data.py
```

### Step 4: Open Power BI Desktop
1. Open Power BI Desktop
2. Click **Get Data** → **Text/CSV**
3. Navigate to `data-prep/processed/` folder
4. Import ALL CSV files:
   - FactSales.csv
   - DimCustomer.csv
   - DimProduct.csv
   - DimStore.csv
   - DimDate.csv
   - DimPromotion.csv
   - DimSupplier.csv
   - summary_supply_chain_risks.csv
   - summary_sales_by_region.csv
   - summary_product_performance.csv

### Step 5: Create Relationships
In Model view, connect:
- FactSales.customer_id → DimCustomer.customer_id
- FactSales.product_id → DimProduct.product_id
- FactSales.store_id → DimStore.store_id
- FactSales.date_id → DimDate.date_id

### Step 6: Add Measures
Copy measures from `powerbi/measures.dax` into Power BI

### Step 7: Build Visuals
Follow `powerbi/dashboard-setup.md` for visual specs

---

## 📦 What's in Each Folder

| Folder | What's Inside |
|--------|---------------|
| `data-source/` | Raw hackathon datasets (cloned repo) |
| `data-prep/processed/` | Ready-to-use CSV files for Power BI |
| `powerbi/` | DAX measures + setup guide |
| `copilot-studio/` | Bot configuration JSON |
| `power-automate/` | Flow definitions |
| `presentation/` | 4-minute demo script |

---

## ⚡ Troubleshooting

**"Python not found"**
→ Install from Microsoft Store: `winget install Python.Python.3.12`

**"pandas not found"**  
→ Run: `pip install pandas`

**"CSV files empty"**
→ Re-run: `python prepare_data.py`

**Power BI shows errors**
→ Check column names match (country_code not country, total_amount not sales_amount)

---

*Built for GeeksterFY26 Hackathon - February 6, 2026* 💝
