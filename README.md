# 🛍️ Customer Segmentation using KMeans

This project applies **unsupervised learning (KMeans Clustering)** to segment customers based on their demographics and transaction behavior. The goal is to help businesses understand customer groups, identify high-value customers, and design targeted marketing strategies.



## 📊 Dataset
The dataset contains:
- **CustomerID**
- **CustomerDOB → Age (derived)**
- **CustGender**
- **CustLocation**
- **CustAccountBalance**
- **TransactionDate & TransactionTime**
- **TransactionAmount (INR)**



## 🧮 Project Workflow
1. **Data Cleaning**
   - Converted DOB → Age
   - Fixed invalid ages (removed negatives)
   - Encoded categorical features (Gender, Location)

2. **Feature Selection**
   - Age
   - CustGender
   - CustLocation
   - CustAccountBalance
   - TransactionAmount (INR)

3. **Feature Scaling**
   - Applied `StandardScaler` for normalization

4. **Clustering**
   - Used **Elbow Method** to find optimal `k=4`
   - Applied **KMeans** to segment customers

5. **Visualization**
   - Plotted clusters across:
     - Age vs Transaction Amount
     - Age vs Account Balance
     - Account Balance vs Transaction Amount
Basic EDA Outputs:

1.Heatmap of account:

<img width="586" height="391" alt="image" src="https://github.com/user-attachments/assets/5cdff1ed-e260-4f6f-9811-b93ef0c561bb" />

2.Cutsomer Account Balance vs Gender:

<img width="523" height="406" alt="image" src="https://github.com/user-attachments/assets/aaf90a15-b1b8-4202-974c-05066a371f4e" />

3.Top Locations according to accountbalance:

<img width="643" height="356" alt="image" src="https://github.com/user-attachments/assets/d0d2f21a-dab4-4b1b-84a3-f40b0fc9f043" />

4.Elbow method to find no of clusters for target variables:

<img width="570" height="371" alt="image" src="https://github.com/user-attachments/assets/a4754f68-d8be-43e9-8f54-f1fc25410c3c" />

Clustering Results:
1:Age vs Transaction Amount:

<img width="525" height="416" alt="image" src="https://github.com/user-attachments/assets/31065dcd-caeb-42e0-b614-e148a539119a" />


2:Age vs Accounmt Balance:

<img width="510" height="414" alt="image" src="https://github.com/user-attachments/assets/d53c0403-c404-44f8-bcea-2e6607f04e8b" />


3:Account Balance vs Transaction Amount:

<img width="522" height="410" alt="image" src="https://github.com/user-attachments/assets/b8135d99-60d5-4220-9625-1fa8ce3d0eb2" />
