# 🛒 SmartShelf: Retail Space Allocation via Basket Clustering

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-green)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-orange)
![Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-yellow)

## 📂 Dataset

The dataset used in this project is the **Instacart Market Basket Analysis Dataset**.

You can access and download the dataset directly from Kaggle:

[📥 Download Dataset - Instacart Market Basket Analysis](https://www.kaggle.com/datasets/psparks/instacart-market-basket-analysis)

## 📖 Project Overview

Retailers traditionally allocate shelf space based on vendor influence or historical decisions, which often leads to inefficient store layouts, missed cross-selling opportunities, and poor customer experience.

**SmartShelf** replicates professional **Category Management** solutions used by industry leaders such as Nielsen and IRI by leveraging customer purchase behavior.

Using the **Instacart Market Basket Analysis dataset**, this project discovers hidden product relationships by analyzing which items are frequently purchased together and converts these insights into actionable shelf-layout recommendations.

---

# 🎯 Key Deliverables

## 🗂️ 1. Shelf Plan (CSV)

A structured mapping of store aisles into affinity-based clusters.

Example:

> Place Fresh Fruits and Packaged Vegetables in the same retail zone because customers frequently purchase them together.

---

## 📊 2. Executive Power BI Dashboard

A visual macro-layout plan that highlights:

- High-value category pairings
- Co-purchase frequency between aisles
- Affinity clusters
- Recommended store zones

Helping category managers make data-driven shelf placement decisions.

---

## 🔎 3. Product Lookup Logic

A recommendation engine that allows users to:

- Search for any product
- Find its strongest complementary products
- Support micro-level shelf arrangement decisions

---

# 🛠️ Project Workflow & Methodology

## Step 1: Data Loading & Sampling

The Instacart dataset contains millions of transactions.

To optimize processing:

- Loaded the raw transaction data
- Extracted a strategic **30% random user sample**
- Maintained statistical representation while reducing computational cost

---

## Step 2: Exploratory Data Analysis (EDA)

Performed initial analysis to understand purchasing behavior:

- Identified top-selling products
- Analyzed category demand distribution
- Visualized the top 10 most purchased products

---

## Step 3: Data Integration

Merged multiple datasets into one analytical table:

- Orders
- Products
- Order Products
- Aisles
- Departments

Creating a unified dataset suitable for:

- Machine learning
- Visualization
- Power BI reporting

---

## Step 4: Building Co-Purchase Matrix

Converted transaction data into a basket representation:

- `1` → Category purchased in an order
- `0` → Category not purchased

Then calculated the dot product to generate a:

**Co-Purchase Frequency Matrix**

This matrix measures how often aisles are purchased together.

---

## Step 5: Customer Affinity Clustering Using K-Means

Applied **K-Means Clustering** on the co-purchase matrix to discover natural product groups.

The model identifies:

- Similar shopping behaviors
- Related product categories
- Optimal store zones

These clusters represent the recommended macro shelf layout.

---

## Step 6: Cluster Visualization

Created heatmaps using:

- Seaborn
- Matplotlib

The visualization highlights strong purchasing relationships between aisles.

High-frequency areas indicate categories that should be positioned closer together.

---

## Step 7: Power BI Dashboard Development

Converted analytical results into an executive dashboard.

Dashboard features:

- Category affinity matrix
- Cluster-based shelf zones
- Conditional formatting
- Macro store layout visualization

Designed for easy interpretation by retail managers.

---

# 📊 Tech Stack

## Programming & Data Processing

- Python
- Pandas
- NumPy

## Machine Learning

- Scikit-Learn
- K-Means Clustering

## Data Visualization

- Matplotlib
- Seaborn
- Power BI

## Application Concepts

- Streamlit
- Product Recommendation Lookup Logic

---

# 📈 Business Impact

SmartShelf helps retailers:

✅ Optimize shelf arrangement  
✅ Increase cross-selling opportunities  
✅ Improve customer shopping experience  
✅ Reduce manual category planning effort  
✅ Make data-driven merchandising decisions  

---

# 📁 Project Structure
