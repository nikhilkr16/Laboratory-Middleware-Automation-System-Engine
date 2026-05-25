import os
import time
import random
import pandas as pd
from datetime import datetime

# Setup the folder where your "lab machine" drops its data
INPUT_FOLDER = "lab_raw_data"
os.makedirs(INPUT_FOLDER, exist_ok=True)

print("🧪 Lab Instrument Simulator Started... Press Ctrl+C to stop.")

sample_counter = 1001

try:
    while True:
        # Generate random lab data
        sample_id = f"SMP-{sample_counter}"
        # Simulating active drug concentration (Target is usually around 100 mg/mL)
        concentration = round(random.uniform(90.0, 110.0), 2) 
        temperature = round(random.uniform(21.5, 25.5), 1)
        operator = random.choice(["Dr. Smith", "Analyst Jones", "Dr. Alcoa"])
        
        # Create a dataframe
        data = {
            "Sample_ID": [sample_id],
            "Concentration_mg_mL": [concentration],
            "Temperature_C": [temperature],
            "Operator": [operator],
            "Timestamp": [datetime.now().strftime("%Y-%m-%d %H:%M:%S")]
        }
        df = pd.DataFrame(data)
        
        # Save as a raw instrument CSV log file
        file_name = f"{INPUT_FOLDER}/raw_output_{sample_id}.csv"
        df.to_csv(file_name, index=False)
        print(f"📦 Instrument generated data for {sample_id} -> Saved to {file_name}")
        
        sample_counter += 1
        time.sleep(5)  # Generates a new file every 5 seconds

except KeyboardInterrupt:
    print("\n🛑 Instrument simulator stopped safely.")
