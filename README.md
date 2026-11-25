# AI-Powered E-Commerce Decision Intelligence & Customer Analytics Platform

A data analytics project built to analyze e-commerce sales, customer behavior, product performance, RFM segmentation, and delivery operations using Python, SQL, Power BI, and AI-assisted business insights.

## Project Overview

This project transforms raw e-commerce data into actionable business insights through data cleaning, exploratory analysis, SQL analytics, customer segmentation, and an interactive Power BI dashboard.

The project follows an end-to-end analytics workflow:

**Raw Data → Python Data Cleaning → SQL Analysis → Customer & RFM Analysis → Power BI Dashboard → AI-Assisted Business Insights**

## Business Objectives

- Analyze sales and order trends
- Identify high-performing product categories
- Understand customer purchasing behavior
- Analyze repeat vs one-time customers
- Segment customers using RFM analysis
- Evaluate delivery and operational performance
- Identify business opportunities using automated insights

## Tools & Technologies

- **Python** – Pandas, NumPy
- **SQL** – MySQL
- **Power BI** – DAX, Data Modeling, Interactive Dashboards
- **Excel** – Data analysis and validation
- **Git & GitHub** – Version control
- **Git LFS** – Power BI dashboard storage


### Dataset Source

Olist Brazilian E-Commerce Public Dataset

Source:
https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce

The original dataset is provided by Olist.

Users can download the dataset from the original source for reproducing the analysis, subject to its applicable license and usage terms.

## Dataset

**Olist Brazilian E-Commerce Public Dataset**

The dataset contains approximately 100K e-commerce orders from the Brazilian marketplace Olist and includes information about:

- Customers
- Orders
- Order Items
- Payments
- Reviews
- Products
- Sellers
- Geolocation
- Product Categories

## Data Analytics Process

### 1. Data Cleaning & Preparation

Python was used to:

- Inspect dataset structure
- Identify missing values
- Detect duplicate records
- Standardize data types
- Clean product and customer data
- Convert date fields
- Validate relationships between datasets
- Generate cleaned datasets for analysis

### 2. SQL Business Analysis

MySQL was used to analyze:

- Total orders
- Total sales value
- Average order value
- Monthly sales trends
- Top product categories
- Repeat vs one-time customers
- Customer spending
- Delivery performance

### 3. Customer Analytics

Customer behavior was analyzed using:

- Customer purchase frequency
- Customer spending
- Repeat customer rate
- Customer state performance
- Customer spend segmentation

### 4. RFM Customer Segmentation

Customers were segmented using:

- **Recency** – How recently a customer purchased
- **Frequency** – How often a customer purchased
- **Monetary** – How much a customer spent

Customer segments include:

- Champions
- Loyal Customers
- Potential Loyalists
- New Customers
- At Risk
- Lost Customers

### 5. Power BI Dashboard

The interactive dashboard contains six analytical pages:

1. **E-Commerce Executive Overview**
2. **Sales & Product Performance Analysis**
3. **Customer Analytics & Retention**
4. **RFM Customer Segmentation & Value Analysis**
5. **Operations & Delivery Performance Analysis**
6. **AI-Assisted Business Insights**

The dashboard provides interactive analysis of sales, customers, products, RFM segments, delivery performance, payments, reviews, and operational metrics.

### 6. AI-Assisted Business Insights

A Python-based automated insights layer evaluates key business metrics and predefined business conditions to generate analytical observations and recommendations.

Examples include:

- Customer retention opportunities
- RFM-based customer targeting
- Delivery performance opportunities
- Customer spending patterns
- Operational improvement areas

> **Note:** The current implementation is rule-based automated business insights, not a Generative AI or predictive ML model.

## Key Findings

- **99,441** total orders analyzed
- **96,096** unique customers
- **15.84M** total sales value
- **3.12%** repeat customer rate
- Champions represent the highest-spending RFM customer segment
- Health & Beauty was among the highest sales-value product categories
- Delivery performance analysis identified opportunities to reduce late deliveries

## Project Structure

```text
AI-Ecommerce-Decision-Intelligence/
│
├── ai/
│   └── ai_business_insights.py
│
├── documentation/
│   └── ai_business_insights.txt
│
├── power bi/
│   └── dashboard.pbix
│
├── python/
│   ├── Data cleaning scripts
│   ├── Exploratory analysis
│   ├── Customer analysis
│   ├── RFM analysis
│   ├── Product analysis
│   └── Operational analysis
│
├── sql/
│   ├── Database setup
│   └── Business analysis queries
│
├── .gitignore
└── .gitattributes
```

## Skills Demonstrated

**Data Analysis | Data Cleaning | Exploratory Data Analysis | SQL | MySQL | Python | Pandas | NumPy | Power BI | DAX | Data Modeling | Customer Segmentation | RFM Analysis | Dashboard Development | Business Intelligence | Business Insights | Git | GitHub**

## Future Enhancements

- Generative AI-powered business insights
- Predictive customer analytics
- Customer churn prediction
- Sales forecasting
- Automated dashboard refresh
- Advanced machine learning models

## Author

**Jana M**

B.E. Computer Science Engineering | Aspiring Data Analyst

GitHub: [Jana M](https://github.com/jana304)
