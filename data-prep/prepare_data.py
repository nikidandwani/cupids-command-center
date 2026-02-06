"""
Cupid's Command Center - Data Preparation Script
================================================
This script consolidates and prepares all datasets for the Command Center dashboard.
"""

import pandas as pd
import os
from datetime import datetime, timedelta
import random
import json

# Paths
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_SOURCE = os.path.join(BASE_PATH, "data-source", "edition_1_valentines", "data")
OUTPUT_PATH = os.path.join(BASE_PATH, "data-prep", "processed")

def ensure_output_dir():
    """Create output directory if it doesn't exist."""
    os.makedirs(OUTPUT_PATH, exist_ok=True)
    print(f"✅ Output directory ready: {OUTPUT_PATH}")

def load_chocolate_global():
    """Load the star schema tables from Cupid Chocolate Global dataset."""
    print("\n📊 Loading Cupid Chocolate Global dataset...")
    
    chocolate_path = os.path.join(DATA_SOURCE, "cupid_chocolate_global", "data")
    
    tables = {}
    table_names = ["DimCustomer", "DimProduct", "DimDate", "DimStore", 
                   "DimPromotion", "DimSupplier", "FactSales"]
    
    for table in table_names:
        file_path = os.path.join(chocolate_path, f"{table}.csv")
        if os.path.exists(file_path):
            tables[table] = pd.read_csv(file_path)
            print(f"   ✓ {table}: {len(tables[table]):,} rows")
        else:
            print(f"   ⚠ {table}: File not found at {file_path}")
    
    return tables

def load_supply_chain():
    """Load supply chain dataset."""
    print("\n📦 Loading Supply Chain dataset...")
    
    # Try different possible locations
    possible_paths = [
        os.path.join(DATA_SOURCE, "supply_chain", "data", "dataset_cupid_supply_chain.csv"),
        os.path.join(BASE_PATH, "data-source", "edition_1_valentines", "data", "dataset_cupid_supply_chain.csv"),
        os.path.join(BASE_PATH, "data-source", "data", "dataset_cupid_supply_chain.csv"),
    ]
    
    for path in possible_paths:
        if os.path.exists(path):
            df = pd.read_csv(path)
            print(f"   ✓ Supply Chain: {len(df):,} rows")
            return df
    
    print("   ⚠ Supply Chain file not found, creating sample data")
    return create_sample_supply_chain()

def load_global_routing():
    """Load global routing/network performance dataset."""
    print("\n🌍 Loading Global Routing dataset...")
    
    possible_paths = [
        os.path.join(DATA_SOURCE, "dataset_cupid_global_routing.csv"),
        os.path.join(BASE_PATH, "data-source", "data", "dataset_cupid_global_routing.csv"),
    ]
    
    for path in possible_paths:
        if os.path.exists(path):
            df = pd.read_csv(path)
            print(f"   ✓ Global Routing: {len(df):,} rows")
            return df
    
    print("   ⚠ Global Routing file not found, creating sample data")
    return create_sample_routing()

def load_gift_recommender():
    """Load gift recommender dataset."""
    print("\n🎁 Loading Gift Recommender dataset...")
    
    gift_path = os.path.join(DATA_SOURCE, "gifts", "data", "GiftRecommender.csv")
    
    if os.path.exists(gift_path):
        df = pd.read_csv(gift_path)
        print(f"   ✓ Gift Recommender: {len(df):,} rows")
        return df
    
    print("   ⚠ Gift Recommender file not found")
    return None

def create_sample_supply_chain():
    """Create sample supply chain data if not available."""
    products = [f"PROD{str(i).zfill(3)}" for i in range(1, 67)]
    regions = ["Europe", "North America", "Asia Pacific", "Latin America"]
    delay_reasons = ["Weather", "Customs", "Supplier Issue", "Transport Strike", "None", "None", "None"]
    
    data = []
    for i in range(100):
        data.append({
            "order_id": f"ORD{str(i+1).zfill(5)}",
            "product_id": random.choice(products),
            "vendor_lead_time_days": random.randint(3, 21),
            "stock_level": random.randint(0, 500),
            "order_quantity": random.randint(10, 200),
            "delay_reason": random.choice(delay_reasons),
            "region": random.choice(regions),
            "cost_per_unit": round(random.uniform(5, 50), 2),
            "sustainability_score": round(random.uniform(0.5, 1.0), 2)
        })
    
    return pd.DataFrame(data)

def create_sample_routing():
    """Create sample routing data if not available."""
    regions = ["EU-West", "EU-North", "EU-South", "US-East", "US-West", 
               "APAC-East", "APAC-South", "LATAM-North", "LATAM-South"]
    
    data = []
    for region in regions:
        for _ in range(11):
            data.append({
                "region": region,
                "request_count_per_min": random.randint(100, 5000),
                "p95_latency_ms": random.randint(50, 500),
                "failure_rate": round(random.uniform(0.001, 0.05), 4),
                "weather_factor": round(random.uniform(0.8, 1.2), 2)
            })
    
    return pd.DataFrame(data)

def create_command_center_summary(tables, supply_chain, routing, gifts):
    """Create aggregated summary tables for the Command Center dashboard."""
    print("\n🎯 Creating Command Center summary tables...")
    
    summaries = {}
    
    # 1. Sales Summary by Region/Store
    if "FactSales" in tables and "DimStore" in tables:
        sales = tables["FactSales"].merge(tables["DimStore"], on="store_id", how="left")
        
        # Group by store/region (using country_code instead of country)
        sales_summary = sales.groupby(["store_id", "store_name", "country_code"]).agg({
            "total_amount": "sum",
            "quantity_sold": "sum",
            "profit_margin": "sum",
            "sale_id": "count"
        }).reset_index()
        sales_summary.columns = ["store_id", "store_name", "country", "total_sales", 
                                  "total_quantity", "total_profit", "transaction_count"]
        summaries["sales_by_region"] = sales_summary
        print(f"   ✓ Sales by Region: {len(sales_summary)} rows")
    
    # 2. Product Performance
    if "FactSales" in tables and "DimProduct" in tables:
        product_sales = tables["FactSales"].merge(tables["DimProduct"], on="product_id", how="left")
        
        product_summary = product_sales.groupby(["product_id", "product_name", "category"]).agg({
            "total_amount": "sum",
            "quantity_sold": "sum",
            "profit_margin": "sum"
        }).reset_index()
        product_summary.columns = ["product_id", "product_name", "category", 
                                    "total_sales", "total_quantity", "total_profit"]
        summaries["product_performance"] = product_summary
        print(f"   ✓ Product Performance: {len(product_summary)} rows")
    
    # 3. Supply Chain Risk Assessment
    if supply_chain is not None:
        supply_chain["risk_level"] = supply_chain.apply(calculate_risk_level, axis=1)
        supply_chain["alert_status"] = supply_chain["risk_level"].apply(
            lambda x: "🔴 Critical" if x > 7 else ("🟡 Warning" if x > 4 else "🟢 OK")
        )
        summaries["supply_chain_risks"] = supply_chain
        print(f"   ✓ Supply Chain Risks: {len(supply_chain)} rows")
    
    # 4. Regional Performance
    if routing is not None:
        regional_perf = routing.groupby("region").agg({
            "request_count_per_min": "mean",
            "p95_latency_ms": "mean",
            "failure_rate": "mean"
        }).reset_index()
        regional_perf["health_score"] = 100 - (regional_perf["failure_rate"] * 1000) - (regional_perf["p95_latency_ms"] / 10)
        regional_perf["health_score"] = regional_perf["health_score"].clip(0, 100)
        summaries["regional_performance"] = regional_perf
        print(f"   ✓ Regional Performance: {len(regional_perf)} rows")
    
    # 5. Customer Segments (if gifts data available)
    if gifts is not None:
        customer_summary = gifts.groupby("customer_id").agg({
            "event_id": "count",
            "loyalty_tier": "first"
        }).reset_index()
        customer_summary.columns = ["customer_id", "event_count", "loyalty_tier"]
        summaries["customer_segments"] = customer_summary
        print(f"   ✓ Customer Segments: {len(customer_summary)} rows")
    
    return summaries

def calculate_risk_level(row):
    """Calculate risk level for supply chain item (0-10 scale)."""
    risk = 0
    
    # Low stock = higher risk
    if row.get("stock_level", 100) < 50:
        risk += 3
    elif row.get("stock_level", 100) < 100:
        risk += 1
    
    # Delay reason = higher risk
    if row.get("delay_reason", "None") not in ["None", ""]:
        risk += 4
    
    # Long lead time = higher risk
    if row.get("vendor_lead_time_days", 7) > 14:
        risk += 2
    elif row.get("vendor_lead_time_days", 7) > 10:
        risk += 1
    
    # High order quantity with low stock = critical
    if row.get("order_quantity", 0) > row.get("stock_level", 100):
        risk += 3
    
    return min(risk, 10)

def create_realtime_kpis(tables, supply_chain):
    """Create KPI metrics for the dashboard."""
    print("\n📈 Calculating KPIs...")
    
    kpis = {}
    
    # Sales KPIs
    if "FactSales" in tables:
        sales = tables["FactSales"]
        kpis["total_revenue"] = sales["total_amount"].sum()
        kpis["total_orders"] = len(sales)
        kpis["avg_order_value"] = sales["total_amount"].mean()
        kpis["total_profit"] = sales["profit_margin"].sum()
        kpis["profit_margin"] = (kpis["total_profit"] / kpis["total_revenue"]) * 100
    
    # Supply Chain KPIs
    if supply_chain is not None:
        kpis["at_risk_orders"] = len(supply_chain[supply_chain["delay_reason"] != "None"])
        kpis["low_stock_items"] = len(supply_chain[supply_chain["stock_level"] < 50])
        kpis["avg_lead_time"] = supply_chain["vendor_lead_time_days"].mean()
    
    # Customer KPIs
    if "DimCustomer" in tables:
        kpis["total_customers"] = len(tables["DimCustomer"])
    
    print(f"   ✓ Calculated {len(kpis)} KPIs")
    return kpis

def save_processed_data(tables, summaries, kpis):
    """Save all processed data to CSV files."""
    print("\n💾 Saving processed data...")
    
    # Save original tables
    for name, df in tables.items():
        output_file = os.path.join(OUTPUT_PATH, f"{name}.csv")
        df.to_csv(output_file, index=False)
        print(f"   ✓ Saved {name}.csv")
    
    # Save summary tables
    for name, df in summaries.items():
        output_file = os.path.join(OUTPUT_PATH, f"summary_{name}.csv")
        df.to_csv(output_file, index=False)
        print(f"   ✓ Saved summary_{name}.csv")
    
    # Save KPIs as JSON
    kpis_file = os.path.join(OUTPUT_PATH, "kpis.json")
    with open(kpis_file, "w") as f:
        json.dump(kpis, f, indent=2, default=str)
    print(f"   ✓ Saved kpis.json")

def main():
    """Main execution function."""
    print("=" * 60)
    print("🎯 CUPID'S COMMAND CENTER - Data Preparation")
    print("=" * 60)
    
    # Ensure output directory exists
    ensure_output_dir()
    
    # Load all datasets
    tables = load_chocolate_global()
    supply_chain = load_supply_chain()
    routing = load_global_routing()
    gifts = load_gift_recommender()
    
    # Create summaries
    summaries = create_command_center_summary(tables, supply_chain, routing, gifts)
    
    # Calculate KPIs
    kpis = create_realtime_kpis(tables, supply_chain)
    
    # Save everything
    save_processed_data(tables, summaries, kpis)
    
    print("\n" + "=" * 60)
    print("✅ Data preparation complete!")
    print(f"📁 Output location: {OUTPUT_PATH}")
    print("=" * 60)
    
    # Print KPIs summary
    print("\n📊 Key Performance Indicators:")
    for key, value in kpis.items():
        if isinstance(value, float):
            print(f"   • {key}: {value:,.2f}")
        else:
            print(f"   • {key}: {value:,}")

if __name__ == "__main__":
    main()
