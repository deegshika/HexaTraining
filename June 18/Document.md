# Overview of Data Governance and Unity Catalog

## What is Data Governance?

Data Governance is the process of managing data securely, accurately, and consistently across an organization.

It ensures that:

- The right users access the right data.
- Data quality is maintained.
- Compliance and security policies are followed.
- Data ownership and responsibilities are clearly defined.

### Why is Data Governance Important?

- Improves data security
- Reduces data duplication
- Ensures regulatory compliance
- Increases trust in data
- Supports better decision-making

---

# What is Unity Catalog?

Unity Catalog is Databricks' centralized governance solution for managing all data and AI assets across a Databricks environment.

It provides a single place to manage:

- Tables
- Views
- Files
- Models
- Dashboards
- Permissions

### Key Features

- Centralized Data Governance
- Fine-Grained Access Control
- Data Lineage
- Auditing and Monitoring
- Data Discovery
- Cross-Workspace Sharing

### Benefits

- Simplified permission management
- Improved security
- Better collaboration
- Easier compliance tracking
- Unified data access

---

# Create Unity Catalog Metastore and Enable a Databricks Workspace with Unity Catalog

## What is a Metastore?

A Metastore is the top-level container in Unity Catalog.

It stores metadata about:

- Catalogs
- Schemas
- Tables
- Views
- Permissions

Think of it as a central registry for all data assets.

---

## Steps to Create a Unity Catalog Metastore

### Step 1: Open Databricks Account Console

Navigate to:

Account Console → Data → Metastores

---

### Step 2: Create Metastore

Provide:

- Metastore Name
- Region
- Storage Location

Example:

```text
Metastore Name: Company_Metastore
Region: Central India
Storage Location: Azure Data Lake Storage
```

---

### Step 3: Assign Workspace

After creating the metastore:

- Select Workspace
- Assign Metastore

This enables Unity Catalog for the workspace.

---

### Step 4: Verify Unity Catalog

In Databricks Workspace:

```sql
SHOW CATALOGS;
```

If catalogs appear, Unity Catalog is enabled successfully.

---

# Overview of 3-Level Namespace in Unity Catalog

Unity Catalog uses a three-level hierarchy.

```text
Catalog
   └── Schema
          └── Table
```

### Structure

```text
catalog.schema.table
```

Example:

```text
hospital_catalog.patient_schema.patient_table
```

---

# Level 1: Catalog

A Catalog is the highest-level container.

It groups related schemas together.

### Example

```text
hospital_catalog
sales_catalog
finance_catalog
```

### Create Catalog

```sql
CREATE CATALOG hospital_catalog;
```

---

# Level 2: Schema

A Schema is a collection of tables and views.

It organizes data inside a catalog.

### Example

```text
patient_schema
doctor_schema
billing_schema
```

### Create Schema

```sql
CREATE SCHEMA hospital_catalog.patient_schema;
```

---

# Level 3: Table

A Table stores the actual data.

### Example

```text
patient_table
doctor_table
appointment_table
```

### Create Table

```sql
CREATE TABLE hospital_catalog.patient_schema.patient_table (
    patient_id INT,
    patient_name STRING,
    city STRING
);
```

---

# Creating Unity Catalog Objects

## Create Catalog

```sql
CREATE CATALOG hospital_catalog;
```

---

## Create Schema

```sql
CREATE SCHEMA hospital_catalog.patient_schema;
```

---

## Create Managed Table

```sql
CREATE TABLE hospital_catalog.patient_schema.patient_table (
    patient_id INT,
    patient_name STRING,
    city STRING
);
```

---

## Insert Data

```sql
INSERT INTO hospital_catalog.patient_schema.patient_table
VALUES
(101,'Rahul','Hyderabad'),
(102,'Priya','Bangalore');
```

---

## Query Data

```sql
SELECT *
FROM hospital_catalog.patient_schema.patient_table;
```

---

# Example of Complete Namespace

```text
hospital_catalog.patient_schema.patient_table
```

Where:

- hospital_catalog → Catalog
- patient_schema → Schema
- patient_table → Table

---

# Real-World Example

Consider a hospital organization.

```text
hospital_catalog
│
├── patient_schema
│     ├── patient_table
│     └── insurance_table
│
├── doctor_schema
│     ├── doctor_table
│     └── specialization_table
│
└── billing_schema
      ├── payments_table
      └── invoices_table
```

This structure helps manage permissions, organization, and governance efficiently.

---

# Advantages of Unity Catalog

- Centralized Governance
- Unified Security
- Data Discovery
- Data Lineage Tracking
- Access Auditing
- Cross-Workspace Data Sharing
- Fine-Grained Permissions
- Better Collaboration

---

# Summary

Data Governance ensures data is secure, accurate, and accessible.

Unity Catalog is Databricks' centralized governance solution that provides secure management of data assets through a three-level namespace:

```text
Catalog → Schema → Table
```

The key component is the Metastore, which manages metadata and permissions across all workspaces. Unity Catalog helps organizations maintain security, compliance, and efficient data management at scale.
