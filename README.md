# 🚀 dbt Learning Project - Analytics Engineering Fundamentals

This project is designed to learn dbt from basics to advanced. Perfect for transitioning to Analytics Engineer role!

## 📋 Prerequisites

```bash
# Install dbt-snowflake
pip install dbt-snowflake

# Snowflake trial account (free)
# Sign up at: https://signup.snowflake.com/
```

## 🏗️ Project Structure

```
dbt-sandbox/
├── dbt_project.yml          # Project configuration
├── profiles.yml             # Database connection
├── models/
│   ├── staging/            # Layer 1: Data cleaning & standardization
│   │   ├── _sources.yml    # Define data sources
│   │   └── stg_*.sql       # Staging models
│   └── marts/              # Layer 2: Business logic & transformations
│       └── *.sql           # Analytics models
├── seeds/                  # CSV files for sample data
├── tests/                  # Custom tests
└── macros/                 # Reusable SQL functions
```

## 🎯 Learning Path

### Step 1: Setup & Basics
- [ ] Create Snowflake trial account
- [ ] Install dbt-snowflake
- [ ] Configure profiles.yml with Snowflake credentials
- [ ] Run dbt debug to test connection
- [ ] Load sample data (seeds)
- [ ] Understand sources

### Step 2: Staging Models
- [ ] Create staging models
- [ ] Apply naming conventions
- [ ] Add basic transformations

### Step 3: Marts (Business Logic)
- [ ] Create fact tables
- [ ] Create dimension tables
- [ ] Apply business logic

### Step 4: Testing & Documentation
- [ ] Add generic tests
- [ ] Add custom tests
- [ ] Write documentation

## 🚀 Quick Start

```bash
# 1. Test Snowflake connection
dbt debug

# 2. Load sample data
dbt seed

# 3. Run models
dbt run

# 4. Test data quality
dbt test

# 5. Generate documentation
dbt docs generate
dbt docs serve
```

## 📚 Key Concepts

### Materialization Types
- **View**: Saved query, fast to build, slower to query
- **Table**: Physical table, slower to build, fast to query
- **Incremental**: Update only new/changed data
- **Ephemeral**: CTEs, doesn't persist in database

### Model Layers
1. **Staging**: 1:1 with source tables, cleaning & standardization
2. **Intermediate**: Reusable business logic
3. **Marts**: Final models for analytics/BI tools

### Naming Conventions
- Staging: `stg_<source>_<entity>.sql`
- Intermediate: `int_<entity>_<verb>.sql`
- Marts: `fct_<entity>.sql` (facts) or `dim_<entity>.sql` (dimensions)

## 💡 Tips
- Always start from staging layer
- 1 staging model = 1 source table
- Don't apply business logic in staging
- Use refs, not hardcoded table names
- Test everything!

## 🔗 Useful Resources

- **dbt Fundamentals Course**: https://learn.getdbt.com/learn/course/dbt-fundamentals-vs-code
- **dbt Docs**: https://docs.getdbt.com/
- **Snowflake + dbt Guide**: https://docs.getdbt.com/docs/core/connect-data-platform/snowflake-setup
- **dbt Community Slack**: https://community.getdbt.com/
