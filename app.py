import pandas as pd

def load_and_clean_data(file_path):
    print("⏳ Data load ho raha hai...")
    df = pd.read_csv(file_path)
    print(f"📊 Original Data Shape: {df.shape}")

    # Text ko numbers mein convert karna aur errors theek karna
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
    df['TotalCharges'] = df['TotalCharges'].fillna(0)
    
    print("✅ Data cleaning successful!")
    return df

if __name__ == "__main__":
    raw_file_name = "Telco-Customer-Churn.csv.csv" 
    
    try:
        cleaned_data = load_and_clean_data(raw_file_name)
        
        export_name = "cleaned_churn_data.csv"
        cleaned_data.to_csv(export_name, index=False)
        
        print(f"🚀 File '{export_name}' Power BI ke liye ready hai!")
    except FileNotFoundError:
        print("❌ Error: Raw CSV file folder mein nahi mili.")