# Power BI Dashboard Setup Guide

## Cupid's Command Center Dashboard

Follow these steps to create the Power BI dashboard for Cupid's Command Center.

---

## 1. Data Connection

### Import Data Files
1. Open Power BI Desktop
2. Click **Get Data** → **Text/CSV**
3. Navigate to `data-prep/processed/` folder
4. Import these files:
   - `FactSales.csv`
   - `DimCustomer.csv`
   - `DimProduct.csv`
   - `DimStore.csv`
   - `DimDate.csv`
   - `DimPromotion.csv`
   - `DimSupplier.csv`
   - `summary_supply_chain_risks.csv`
   - `summary_regional_performance.csv`

---

## 2. Data Model Relationships

Create these relationships in Model view:

```
FactSales.customer_id → DimCustomer.customer_id (Many to One)
FactSales.product_id → DimProduct.product_id (Many to One)
FactSales.store_id → DimStore.store_id (Many to One)
FactSales.date_id → DimDate.date_id (Many to One)
FactSales.promotion_id → DimPromotion.promotion_id (Many to One)
```

---

## 3. Dashboard Layout

### Page 1: Command Center Overview

```
┌─────────────────────────────────────────────────────────────────┐
│  💝 CUPID'S COMMAND CENTER           [Date Filter] [Region]     │
├─────────────────┬─────────────────┬─────────────────┬───────────┤
│   TOTAL REVENUE │   TOTAL ORDERS  │   RISK LEVEL    │  ALERTS   │
│     €247,832    │      3,847      │   🟡 Warning    │     3     │
│     +12% ▲      │     +8% ▲       │     (6/10)      │  Active   │
├─────────────────┴─────────────────┴─────────────────┴───────────┤
│                                                                  │
│  ┌──────────────────────────┐  ┌─────────────────────────────┐  │
│  │                          │  │                             │  │
│  │    SALES BY REGION       │  │     RISK RADAR              │  │
│  │       (Map Visual)       │  │   (Gauge or Traffic Light)  │  │
│  │                          │  │                             │  │
│  └──────────────────────────┘  └─────────────────────────────┘  │
│                                                                  │
│  ┌──────────────────────────┐  ┌─────────────────────────────┐  │
│  │                          │  │                             │  │
│  │   TOP PRODUCTS           │  │    INVENTORY ALERTS         │  │
│  │    (Bar Chart)           │  │      (Table with RAG)       │  │
│  │                          │  │                             │  │
│  └──────────────────────────┘  └─────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
```

### Page 2: Supply Chain Risk

```
┌─────────────────────────────────────────────────────────────────┐
│  📦 SUPPLY CHAIN RISK MONITOR                                   │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │  RISK TABLE                                              │    │
│  │  Product | Stock | Velocity | Hours Left | Risk | Alert │    │
│  │  ─────────────────────────────────────────────────────── │    │
│  │  🔴 Dark Truffles | 23 | 6/hr | 4 hrs | Critical        │    │
│  │  🔴 Heart Box L | 45 | 8/hr | 6 hrs | Critical          │    │
│  │  🟡 Rose Collection | 120 | 12/hr | 10 hrs | Warning    │    │
│  └─────────────────────────────────────────────────────────┘    │
│                                                                  │
│  ┌──────────────────────┐  ┌────────────────────────────────┐   │
│  │  DELAY REASONS       │  │  SUPPLIER PERFORMANCE          │   │
│  │   (Pie Chart)        │  │    (Bar Chart by Supplier)     │   │
│  └──────────────────────┘  └────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
```

### Page 3: Customer Insights

```
┌─────────────────────────────────────────────────────────────────┐
│  💑 CUSTOMER INSIGHTS                                           │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │  CUSTOMER SEGMENTS (Donut Chart by Loyalty Tier)         │   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                  │
│  ┌──────────────────────────┐  ┌────────────────────────────┐   │
│  │  ORDER VALUE DIST.       │  │  SALES BY CHANNEL          │   │
│  │   (Histogram)            │  │    (Bar: Online vs Retail) │   │
│  └──────────────────────────┘  └────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
```

---

## 4. Visual Specifications

### KPI Cards (Top Row)
- **Visual Type**: Card
- **Format**: 
  - Title size: 12pt, gray
  - Value size: 28pt, bold
  - Trend indicator below
  - Background: White with shadow

### Regional Map
- **Visual Type**: Filled Map or Azure Map
- **Location**: DimStore[country]
- **Value**: [Total Revenue]
- **Color saturation**: By revenue
- **Tooltip**: Custom with sales details

### Risk Gauge
- **Visual Type**: Gauge
- **Value**: [Risk Score]
- **Min**: 0, **Max**: 10
- **Target**: 4
- **Colors**: 
  - 0-4: Green
  - 4-7: Yellow  
  - 7-10: Red

### Inventory Alert Table
- **Visual Type**: Table
- **Columns**:
  - Product Name
  - Stock Level (with data bars)
  - Alert Status (emoji)
  - Hours Until Stockout
- **Conditional Formatting**:
  - Red background if stock < 25
  - Yellow background if stock < 50
  - Bold if alert = Critical

---

## 5. Color Theme

```json
{
  "name": "Cupid's Command Center",
  "dataColors": [
    "#E91E63",  // Cupid Pink (primary)
    "#9C27B0",  // Purple 
    "#673AB7",  // Deep Purple
    "#3F51B5",  // Indigo
    "#2196F3",  // Blue
    "#00BCD4",  // Cyan
    "#4CAF50",  // Green
    "#FF9800"   // Orange
  ],
  "background": "#FAFAFA",
  "foreground": "#333333",
  "tableAccent": "#E91E63"
}
```

---

## 6. Interactivity

### Cross-Filtering
- Enable cross-filtering between all visuals
- Map click → filters all other visuals
- Product click → shows specific product data

### Drillthrough
- From Overview → Supply Chain Details
- From Overview → Customer Details
- Right-click any data point to drill

### Bookmarks
Create bookmarks for:
1. "Overview" - Default view
2. "Risk Focus" - Highlights alerts
3. "Regional Deep Dive" - Expanded map

---

## 7. Measures to Add

Copy measures from `measures.dax` file into Power BI:
1. Go to **Modeling** → **New Measure**
2. Paste each measure
3. Format appropriately

Key measures:
- `Total Revenue`
- `Total Orders`
- `Risk Score`
- `Risk Level`
- `Hours Until Stockout`
- `Revenue vs Yesterday`

---

## 8. Publishing

1. Click **Publish** → Select workspace
2. Configure scheduled refresh (every 15 min)
3. Set up alerts:
   - Alert when Risk Score > 7
   - Alert when any stock < 25
4. Pin to dashboard for embedding

---

## 9. Embedding for Demo

For Copilot Studio integration:
```
Embed URL: https://app.powerbi.com/reportEmbed?reportId=YOUR_REPORT_ID
```

For Teams:
- Add Power BI tab to channel
- Select the Command Center report

---

*Happy dashboarding! 📊💝*
