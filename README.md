# 🧪 LIMS: Laboratory Information Management System

> **A hands-on interview preparation project for aspiring pharma/biotech engineers**
> 
> Learn real LIMS database logic, regulatory compliance, and data validation 
<img width="1144" height="624" alt="image" src="https://github.com/user-attachments/assets/d12d14ab-4e1b-4c46-bfa1-b58b191e9f49" />

## Dashboard : 

---

## ✨ What This Project Shows

✅ **Real-world LIMS workflow** — instrument data → validation → compliance → database  
✅ **Regulatory thinking** — ALCOA+ principles embedded in code  
✅ **Database architecture** — master ledger design and data accumulation  
✅ **Quality control logic** — Out-of-Specification (OOS) detection  
✅ **Audit trail management** — Every result tracked with timestamps and metadata  
✅ **File handling and archiving** — Production-grade data organization  

---

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│           LAB INSTRUMENT (Simulated)                        │
│           instrument.py                                     │
│  • Generates sample data with concentrations, temps         │
│  • Creates timestamped raw output files                     │
│  • Mimics real lab instrument behavior                      │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼ (raw CSV files)
┌─────────────────────────────────────────────────────────────┐
│           LAB RAW DATA (Watch Folder)                       │
│           lab_raw_data/                                     │
│  • Incoming instrument data                                 │
│  • Monitored for processing                                 │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────┐
│         LIMS PROCESSOR (Middleware)                         │
│         lims_processor.py                                   │
│  ✓ Data validation (95-105 mg/mL specs)                     │
│  ✓ OOS detection & flagging                                 │
│  ✓ ALCOA+ metadata addition                                 │
│  ✓ Timestamp & traceability                                 │
│  ✓ Database transaction logging                             │
└──────────────────────┬──────────────────────────────────────┘
                       │
        ┌──────────────┼──────────────┐
        │              │              │
        ▼              ▼              ▼
    ✅ PASS        ❌ FAIL      🗂️ ARCHIVE
        │              │              │
        ▼              ▼              ▼
  Master Ledger   OOS Report    lab_archive/
```

---

## 📚 What I Learn

### 1. **Data Validation & Quality Control**
   - Implementing specification checks (95-105 mg/mL)
   - Out-of-Specification (OOS) detection
   - Result flagging and reporting

### 2. **ALCOA+ Compliance** (Even pharma auditors check this!)
   - **Attributable**: Who created/modified data?
   - **Legible**: Human and system-readable formats
   - **Contemporaneous**: Real-time recording with timestamps
   - **Original**: Immutable master records
   - **Accurate**: Validated and verified data
   - **Plus**: Smudge resistance, system suitability, audit trail

### 3. **Database Architecture**
   - Master ledger design
   - Transaction-based updates
   - Audit trail logging
   - CSV as a simple database (scalable to SQL)

### 4. **File Handling & Organization**
   - Raw data ingestion
   - Processed file archiving
   - Metadata preservation
   - Batch processing

### 5. **Audit Trail Management**
   - Complete data lineage
   - User/system attribution
   - Timestamp validation
   - Revision tracking

### 6. **Error Handling & Edge Cases**
   - Missing data scenarios
   - Duplicate entries
   - Data format issues
   - Graceful failure modes

---

## 📂 Project Structure

```
learn/lab_digitalization/
│
├── instrument.py                    # Instrument simulator 
├── lims_processor.py                # script represents the LIMS Core Engine processing sample data and applying quality checks.
├── lims_master_ledger.csv           #  represents the central relational database.
│
├── lab_raw_data/                    # folder represents the SDMS (Scientific Data Management System) collecting raw files from instruments.
│   └── [incoming raw CSV files]     # just like ELN 
│
├── lab_archive/                     # Processed files (output)
│   ├── raw_output_SMP-1001.csv
│   ├── raw_output_SMP-1002.csv
│   └── ... [28+ archived files]
│
└── README.md                        # This file
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.7+
- pandas (`pip install pandas`)
- Basic CSV knowledge

### Installation

```bash
# Navigate to project directory
cd "e:\learn\lab digitalization"

# Install dependencies
pip install pandas

# Verify files exist
ls -la  # or dir (Windows)
```

### Running the Project

#### Step 1: Generate Instrument Data
```bash
python instrument.py
```

**What happens:**
- Simulates a lab instrument taking measurements
- Generates random sample data (SMP-XXXX)
- Creates CSV files in `lab_raw_data/`
- Each file contains: Sample ID, Concentration, Temperature, Timestamp

**Example output:**
```
Generated: lab_raw_data/raw_data_20260525_143022.csv
Samples created: SMP-2401, SMP-2402, SMP-2403
```

#### Step 2: Process with LIMS Middleware
```bash
python lims_processor.py
```

**What happens:**
- Reads all raw data files
- Validates concentration against specs (95-105 mg/mL)
- Flags out-of-spec (OOS) results
- Adds ALCOA+ metadata (timestamp, user, version, etc.)
- Updates master ledger
- Archives processed files
- Generates audit trail

**Example output:**
```
LIMS Processor Started
[PROCESSING] raw_data_20260525_143022.csv
[VALIDATION] SMP-2401: 102.3 mg/mL ✓ PASS
[VALIDATION] SMP-2402: 92.1 mg/mL ✗ OOS - Below spec
[AUDIT] Added 3 results to master ledger
[ARCHIVE] Moved to lab_archive/
Processing Complete: 147 results, 3 OOS flagged
```

---

## 📊 Example Outputs

### Raw Instrument Data
```csv
Sample_ID,Concentration_mgmL,Temperature_C,Timestamp,Instrument_ID
SMP-2401,102.3,25.1,2026-05-25 14:30:22,HPLC-01
SMP-2402,92.1,25.0,2026-05-25 14:31:05,HPLC-01
SMP-2403,104.8,25.2,2026-05-25 14:32:44,HPLC-01
```

### Master Ledger (After LIMS Processing)
```csv
Sample_ID,Concentration_mgmL,Temperature_C,Status,OOS_Flag,User,Timestamp,ALCOA_Version,Audit_Date
SMP-2401,102.3,25.1,ACCEPTED,N,System,2026-05-25 14:30:22,1.0,2026-05-25 14:35:01
SMP-2402,92.1,25.0,ACCEPTED,Y,System,2026-05-25 14:31:05,1.0,2026-05-25 14:35:02
SMP-2403,104.8,25.2,ACCEPTED,N,System,2026-05-25 14:32:44,1.0,2026-05-25 14:35:03
```

### Audit Trail (Compliance Log)
```
[2026-05-25 14:35:01] USER: System | ACTION: Data_Validation | SAMPLE: SMP-2401 | RESULT: PASS | STATUS: Logged
[2026-05-25 14:35:01] USER: System | ACTION: Ledger_Update | SAMPLE: SMP-2401 | RECORDS_ADDED: 1 | STATUS: Committed
[2026-05-25 14:35:02] USER: System | ACTION: OOS_Detection | SAMPLE: SMP-2402 | OOS_REASON: Below_Spec | STATUS: Flagged
```

---

## 🔐 Compliance Concepts Demonstrated

### ALCOA+ (21 CFR Part 11)

| Principle | How This Project Demonstrates It |
|-----------|----------------------------------|
| **Attributable** | Every entry logged with timestamp, user ID, and action type |
| **Legible** | Human-readable CSV format + machine-parseable structure |
| **Contemporaneous** | Real-time data recording with millisecond timestamps |
| **Original** | Master ledger as immutable source of truth |
| **Accurate** | Validation rules prevent bad data entry |
| **Complete** | Full audit trail with before/after states |
| **Consistent** | Standardized data format across all samples |
| **Secure** | File-based archiving with version control |

### OOS (Out-of-Specification)

Results outside the acceptable range (95-105 mg/mL) are:
- Flagged with OOS_Flag = 'Y'
- Logged in audit trail
- Marked for investigation
- Never deleted (audit trail preservation)

### Audit Trail

Every transaction is logged:
```
[TIMESTAMP] USER: [who] | ACTION: [what] | SAMPLE: [which] | RESULT: [outcome] | STATUS: [committed/rejected]
```

---







## 📖 References

- **21 CFR Part 11**: Electronic Records; Electronic Signatures (FDA)
- **ALCOA+**: Data integrity principles in regulated labs
- **ISO 17025**: Requirements for testing laboratories
- **LIMS Standards**: LabVantage, SLIMS, and industry best practices

---

