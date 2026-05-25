import os
import time
import pandas as pd
from datetime import datetime

# Folder paths
WATCH_FOLDER = "lab_raw_data"
ARCHIVE_FOLDER = "lab_archive"
MASTER_DATABASE = "lims_master_ledger.csv"

os.makedirs(ARCHIVE_FOLDER, exist_ok=True)

# Strict Quality Specs defined by Regulatory Affairs
MIN_ACCEPTABLE_CONC = 95.0
MAX_ACCEPTABLE_CONC = 105.0

print("⚙️ LIMS Middleware Pipeline Active... Scanning for raw files.")

def process_file(file_path):
    # 1. Read the raw instrument data
    df = pd.read_csv(file_path)
    
    # 2. Extract value to evaluate against core business logic
    conc = df.loc[0, "Concentration_mg_mL"]
    sample_id = df.loc[0, "Sample_ID"]
    
    # 3. LIMS Logic: Out-of-Specification (OOS) evaluation
    if MIN_ACCEPTABLE_CONC <= conc <= MAX_ACCEPTABLE_CONC:
        status = "PASS"
    else:
        status = "FAIL (OOS - Out of Specification)"
        
    # 4. Injecting ALCOA+ Audit Trail Metadata for regulatory compliance
    df["LIMS_Status"] = status
    df["Processed_By_System"] = "LIMS_Engine_V1"
    df["Ingestion_Timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    df["Data_Integrity_Hash"] = hash(f"{sample_id}_{conc}_{status}") # Simple security check
    
    # 5. Commit data to the central Master Database
    if not os.path.exists(MASTER_DATABASE):
        df.to_csv(MASTER_DATABASE, index=False)
    else:
        df.to_csv(MASTER_DATABASE, mode='a', header=False, index=False)
        
    print(f"✅ Processed {sample_id} | Status: {status} | Appended to Master Ledger.")

try:
    while True:
        # Scan folder for newly arrived files
        files = [f for f in os.listdir(WATCH_FOLDER) if f.endswith('.csv')]
        
        for file in files:
            full_path = os.path.join(WATCH_FOLDER, file)
            
            # Execute processing logic
            process_file(full_path)
            
            # Move file to archive folder so it isn't processed twice (Maintains a clean workspace)
            os.rename(full_path, os.path.join(ARCHIVE_FOLDER, file))
            
        time.sleep(2)  # Scan folder every 2 seconds

except KeyboardInterrupt:
    print("\n🛑 LIMS pipeline shut down safely.")
