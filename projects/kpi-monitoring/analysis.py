import pandas as pd
import numpy as np
from datetime import datetime

def load_data(file_path):
    df = pd.read_csv(file_path)
    df['date'] = pd.to_datetime(df['date'])
    return df

def calculate_kpi(df):
    total_revenue = df['revenue'].sum()
    avg_conversion = df['conversion_rate'].mean()
    total_customers = df['customers'].nunique()
    avg_order_value = df['revenue'].sum() / df['orders'].sum()
    kpi = {
        'total_revenue': total_revenue,
        'avg_conversion_rate': round(avg_conversion, 2),
        'total_customers': total_customers,
        'avg_order_value': round(avg_order_value, 2)
    }
    return kpi

def monthly_aggregation(df):
    monthly = df.groupby(df['date'].dt.to_period('M')).agg({
        'revenue': 'sum',
        'customers': 'nunique',
        'orders': 'sum',
        'conversion_rate': 'mean'
    }).reset_index()
    monthly.columns = ['month', 'revenue', 'customers', 'orders', 'conversion_rate']
    monthly['revenue_ma'] = monthly['revenue'].rolling(window=3).mean()
    monthly['orders_ma'] = monthly['orders'].rolling(window=3).mean()
    return monthly

def segment_customers(df):
    segments = df.groupby('customer_segment').agg({
        'revenue': 'sum',
        'customers': 'nunique',
        'orders': 'sum'
    }).reset_index()
    segments['revenue_share'] = (segments['revenue'] / segments['revenue'].sum() * 100).round(2)
    segments = segments.sort_values('revenue', ascending=False)
    return segments

def export_report(kpi, monthly, segments, output_path):
    with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
        pd.DataFrame([kpi]).to_excel(writer, sheet_name='kpi', index=False)
        monthly.to_excel(writer, sheet_name='monthly', index=False)
        segments.to_excel(writer, sheet_name='segments', index=False)

if __name__ == '__main__':
    df = load_data('data/kpi_metrics.csv')
    kpi = calculate_kpi(df)
    monthly = monthly_aggregation(df)
    segments = segment_customers(df)
    export_report(kpi, monthly, segments, 'output/kpi_report.xlsx')
    print('total revenue:', kpi['total_revenue'])
    print('avg conversion:', kpi['avg_conversion_rate'])
    print('report saved to output/kpi_report.xlsx')
