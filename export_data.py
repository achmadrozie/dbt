#!/usr/bin/env python3
"""
Export data from Snowflake to local CSV files
This script pulls both RAW and ANALYTICS data from Snowflake
"""

import snowflake.connector
import pandas as pd
import os
from datetime import datetime

# Snowflake connection config
SNOWFLAKE_CONFIG = {
    'user': 'ACHMADROZIE97',
    'password': 'doaIbu101004@@@@@@@',
    'account': 'HDUGJRP-WK03995',
    'host': 'HDUGJRP-WK03995.snowflakecomputing.com',
    'warehouse': 'transforming',
}

# Create data directory if it doesn't exist
data_dir = 'exported_data'
if not os.path.exists(data_dir):
    os.makedirs(data_dir)
    print(f"Created directory: {data_dir}")

# Create timestamp for file naming
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')

try:
    print("Connecting to Snowflake...")
    conn = snowflake.connector.connect(**SNOWFLAKE_CONFIG)
    print("✓ Connected successfully!\n")

    # RAW DATA EXPORTS
    print("=" * 60)
    print("EXPORTING RAW DATA")
    print("=" * 60)

    # Raw Customers
    print("Pulling raw.jaffle_shop.customers...")
    raw_customers = pd.read_sql(
        "SELECT * FROM raw.jaffle_shop.customers",
        conn
    )
    customers_file = f"{data_dir}/raw_customers_{timestamp}.csv"
    raw_customers.to_csv(customers_file, index=False)
    print(f"✓ Saved {len(raw_customers)} rows to {customers_file}\n")

    # Raw Orders
    print("Pulling raw.jaffle_shop.orders...")
    raw_orders = pd.read_sql(
        "SELECT * FROM raw.jaffle_shop.orders",
        conn
    )
    orders_file = f"{data_dir}/raw_orders_{timestamp}.csv"
    raw_orders.to_csv(orders_file, index=False)
    print(f"✓ Saved {len(raw_orders)} rows to {orders_file}\n")

    # Raw Payments
    print("Pulling raw.stripe.payment...")
    raw_payments = pd.read_sql(
        "SELECT * FROM raw.stripe.payment",
        conn
    )
    payments_file = f"{data_dir}/raw_payments_{timestamp}.csv"
    raw_payments.to_csv(payments_file, index=False)
    print(f"✓ Saved {len(raw_payments)} rows to {payments_file}\n")

    # ANALYTICS DATA EXPORTS
    print("=" * 60)
    print("EXPORTING ANALYTICS DATA")
    print("=" * 60)

    # Get all tables in analytics.marts_marts schema (dbt created models)
    print("Listing all tables in analytics.marts_marts and analytics.marts_staging schemas...")
    cursor = conn.cursor()

    # Export marts (dimension and fact tables)
    print("\n--- MARTS TABLES ---")
    try:
        cursor.execute(
            "SELECT table_name FROM analytics.information_schema.tables WHERE table_schema='MARTS_MARTS'"
        )
        tables = cursor.fetchall()

        if tables:
            for table in tables:
                table_name = table[0]
                print(f"Pulling analytics.marts_marts.{table_name}...")
                try:
                    df = pd.read_sql(
                        f"SELECT * FROM analytics.marts_marts.{table_name}",
                        conn
                    )
                    file_path = f"{data_dir}/marts_{table_name}_{timestamp}.csv"
                    df.to_csv(file_path, index=False)
                    print(f"✓ Saved {len(df)} rows to {file_path}\n")
                except Exception as e:
                    print(f"✗ Error exporting {table_name}: {e}\n")
        else:
            print("No tables found in analytics.marts_marts schema\n")
    except Exception as e:
        print(f"Error querying marts_marts schema: {e}\n")

    # Export staging tables
    print("\n--- STAGING TABLES ---")
    try:
        cursor.execute(
            "SELECT table_name FROM analytics.information_schema.tables WHERE table_schema='MARTS_STAGING'"
        )
        tables = cursor.fetchall()

        if tables:
            for table in tables:
                table_name = table[0]
                print(f"Pulling analytics.marts_staging.{table_name}...")
                try:
                    df = pd.read_sql(
                        f"SELECT * FROM analytics.marts_staging.{table_name}",
                        conn
                    )
                    file_path = f"{data_dir}/staging_{table_name}_{timestamp}.csv"
                    df.to_csv(file_path, index=False)
                    print(f"✓ Saved {len(df)} rows to {file_path}\n")
                except Exception as e:
                    print(f"✗ Error exporting {table_name}: {e}\n")
        else:
            print("No tables found in analytics.marts_staging schema\n")
    except Exception as e:
        print(f"Error querying marts_staging schema: {e}\n")

    conn.close()
    print("=" * 60)
    print("Export completed successfully! ✓")
    print(f"All files saved to: {data_dir}/")
    print("=" * 60)

except Exception as e:
    print(f"Error: {e}")
    print("Please check your Snowflake credentials and connection")
