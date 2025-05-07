# Open Data Contract Standard (ODCS) - Excel Template

This repository contains an Excel template for authoring data contracts using the **Open Data Contract Standard V3**. 
It provides a user-friendly interface to define and share data contracts with stakeholders, especially those less familiar with YAML.

<a href="https://github.com/datacontract/open-data-contract-standard-excel-template/raw/refs/heads/main/odcs-template.xlsx">
<img width="1397" alt="image" src="https://github.com/user-attachments/assets/f9013cee-a9c8-4ba8-a111-0f4b2e9b6bf8" />
</a>


## 📥 Template

Download the Excel Template:
- [odcs-template.xlsx](https://github.com/datacontract/open-data-contract-standard-excel-template/raw/refs/heads/main/odcs-template.xlsx)

## 💡 Example

Open an Example Data Contract:

- [shipments-example.xlsx](https://github.com/datacontract/open-data-contract-standard-excel-template/raw/refs/heads/main/examples/shipments-odcs.xlsx)


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
Use the open-source [Data Contract CLI](https://github.com/datacontract/datacontract-cli) to convert the Excel template to or from YAML.

```
datacontract import --format excel --source odcs.xlsx
```

### Data Mesh Manager

Upload the Excel directly in [Data Mesh Manager](https://datamesh-manager.com) using the “Import Excel” feature, and open existing ODCS data contracts in Excel.

<img width="1257" alt="image" src="https://github.com/user-attachments/assets/993a15bf-c1a3-495a-95fc-a0ba4d765c87" />


## 📜 License

Created by Jochen Christ and Dr. Simon Harrer under MIT License
