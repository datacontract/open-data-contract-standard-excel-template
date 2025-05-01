# Open Data Contract Standard (ODCS) - Excel Template

This repository contains an Excel template for authoring data contracts using the **Open Data Contract Standard V3**. 
It provides a user-friendly interface to define and share data contracts with stakeholders, especially those less familiar with YAML.

## 📥 Template

[odcs-template.xlsx](https://github.com/datacontract/open-data-contract-standard-excel-template/raw/refs/heads/main/odcs-template.xlsx)

## 💡 Example

[orders-example.xlsx](https://github.com/datacontract/open-data-contract-standard-excel-template/raw/refs/heads/main/examples/orders-example.xlsx)


## 🧾 What is a Data Contract?

A **data contract**, such as [ODCS](https://bitol-io.github.io/open-data-contract-standard/latest/), defines the structure, format, semantics, quality, and terms of use for data exchanged between a producer and one or more consumers.

While data contracts are typically written in YAML, this Excel template enables easier collaboration, review, and iteration—especially across business and technical teams.


## 📄 Template Overview

The Excel file includes the following sheets:

### 1. `Instructions`
Provides a quick guide on how to fill out the template.

### 2. `Fundamentals`
Captures general metadata for the data contract, including ID, Name, Version, Domain and Description.

### 3. `Schema <table_name>`
Defines the data model with all properties.

Copy this sheet for every table in your data contract.

### 4. `Custom Properties`

Use this optional sheet to define additional metadata or annotations.


## 🚀 Integrations

### Data Contract CLI
(coming soon)

Use the open-source Data Contract CLI to convert the Excel template to or from YAML.

### Data Mesh Manager

Upload the Excel directly in [Data Mesh Manager](https://datamesh-manager.com) using the “Import Excel” feature, and open existing ODCS data contracts in Excel.


## 📜 License

Created by Jochen Christ and Dr. Simon Harrer under MIT License
