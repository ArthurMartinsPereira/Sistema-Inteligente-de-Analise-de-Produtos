Product Analytics
A product and sales data analysis application built with Python. The
project aims to turn raw product, inventory, and sales data into useful
insights through data exploration, interactive visualizations, automated
reports, and introductory machine learning techniques.
Project status: Early development. The database foundation and
initial Streamlit interface are being built. Features described as
planned are part of the project roadmap and may not be implemented
yet.

Overview
Product Analytics is designed to help users explore commercial data
without having to manually inspect large datasets. Users will be able to
import product and sales records, query information, review key business
metrics, and explore trends through an interactive dashboard.

As the project evolves, it will also explore machine learning techniques
to identify patterns, detect unusual behavior, and experiment with sales
forecasting.
Objectives
- Build a modular Python application with a clear separation of
  responsibilities.
- Store and manage product, category, and sales data in a relational
  database.
- Practice database modeling and database operations using SQLAlchemy.
- Import and process datasets with Pandas.
- Generate descriptive statistics and interactive business insights.
- Create charts and dashboards for exploring commercial data.
- Apply selected machine learning techniques to real-world-style
  datasets.
- Develop good software engineering practices, including testing,
  documentation, and version control.
Planned Features
The following features describe the intended direction of the project.
They will be implemented incrementally.
Data management
- Import product and sales data from CSV files.
- Store product, category, and sales records in a SQLite database.
- Search, filter, create, update, and delete product records.
- Validate imported data and handle invalid or incomplete records.
Data analysis and visualization
- Calculate revenue, gross profit, sales volume, and other business
  metrics.
- Identify best-selling products and categories.
- Explore sales performance over time.
- Compare product prices, costs, and sales performance.
- Display results through charts and dashboard indicators.
Machine learning experiments
- Group products with similar characteristics using clustering.
- Detect unusual changes or patterns in sales data.
- Experiment with sales forecasting using historical records.
Machine learning will be introduced after the data model and basic
analytical features are reliable. Not every analytical task requires
machine learning; straightforward queries and statistical methods will
be preferred when they are more appropriate.
Reports
- Generate summaries of selected datasets.
- Highlight relevant metrics and trends.
- Export analytical results for further use.
Technology Stack
  Technology     Purpose
  Python         Main programming language
Streamlit      Interactive web interface and dashboard
SQLAlchemy     Object-relational mapping (ORM) and database access
SQLite         Relational database
Pandas         Data loading, cleaning, transformation, and analysis
NumPy          Numerical operations
Matplotlib     Data visualization
Scikit-learn   Machine learning experiments

Some technologies are part of the planned stack and will be integrated
as development progresses.
Project Architecture
The application is being organized into modules so that the user
interface, database access, business logic, and analytical code can
evolve independently.
ProductAnalytics/
│
├── app.py
├── requirements.txt
├── README.md
│
├── pages/
│   ├── 1_Overview.py
│   ├── 2_Products.py
│   ├── 3_Sales.py
│   └── 4_Analytics.py
│
├── database/
│   ├── __init__.py
│   ├── connection.py
│   └── models.py
│
├── repositories/
│   ├── product_repository.py
│   └── sales_repository.py
│
├── services/
│   ├── import_service.py
│   └── report_service.py
│  
├── analytics/
│   ├── descriptive.py
│   └── visualizations.py
│
├── ml/
│   ├── sales_prediction.py
│   ├── clustering.py
│   └── anomaly_detection.py
│
├── data/
│   └── sample/
│
└── tests/
    ├── test_products.py
    └── test_analytics.py
This is the target structure. Directories and modules will be added as
the corresponding features are developed.
Architectural responsibilities
- pages/ --- Streamlit pages and user interaction.
- database/ --- Database engine, sessions, and SQLAlchemy
  models.
- repositories/ --- Queries and persistence operations for each
  entity.
- services/ --- Application workflows, data imports, and report
  generation.
- analytics/ --- Descriptive analysis and visualizations.
- ml/ --- Machine learning models and experiments.
- tests/ --- Automated tests.
Database Design
The initial relational data model is planned around four entities:
- Categories --- product category information.
- Products --- product details, SKU, current price, cost, and
  stock.
- Sales --- sale-level information, such as date and sales
  channel.
- SaleItems --- individual products and quantities included in
  each sale.
A sale can contain multiple sale items, and each sale item references a
product.

The sale item will preserve the unit price and unit cost recorded at the
time of the sale. This is important because a product's current price or
cost may change over time, while historical sales should retain their
original values.

Monetary values are intended to be stored as integer minor units (for
example, cents) to avoid common floating-point precision issues in
financial calculations.
Getting Started
Prerequisites
- Python 3.10 or newer recommended.
- pip.
- Git (optional, but recommended).
Installation
1. Clone the repository:
   git clone <repository-url>
   cd ProductAnalytics
2. Create a virtual environment:
   python -m venv .venv
3. Activate the environment.
   Windows PowerShell:
   .venv\Scripts\Activate.ps1
   macOS / Linux:
   source .venv/bin/activate
4. Install the dependencies:
   pip install -r requirements.txt
Run the application
Start the Streamlit application from the project root:
streamlit run app.py
Streamlit will provide a local URL in the terminal and usually open the
application in your default browser.
The application is still under development, so available pages and
functionality may be limited.

Development Roadmap
The project will be developed in stages:
- [x] Create the initial Streamlit application.
- [x] Set up the initial SQLAlchemy engine and declarative base.
- [x] Define the first SQLAlchemy model (Product).
- [ ] Initialize the database and create tables.
- [ ] Implement database sessions and basic CRUD operations.
- [ ] Introduce repository classes.
- [ ] Add category and sales models and relationships.
- [ ] Implement CSV data import and validation.
- [ ] Build descriptive analysis and dashboard visualizations.
- [ ] Add machine learning experiments.
- [ ] Generate and export reports.
- [ ] Expand automated tests and complete project documentation.
Learning Goals
This project is also a practical learning exercise focused on applying
and consolidating concepts in:
- Object-oriented programming.
- Relational databases and SQL.
- SQLAlchemy and ORM concepts.
- Data manipulation and exploratory data analysis.
- Data visualization.
- Machine learning fundamentals.
- Modular application design and testing.
License
No license has been selected yet. Until a license is added to the
repository, all rights are reserved by the project author.