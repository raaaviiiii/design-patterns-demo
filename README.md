# Design Patterns Demo

## Overview
This repository demonstrates design patterns in three categories:

- Creational
- Structural
- Behavioral

Each category contains pattern-specific folders.  
Each pattern folder includes:
- without/ → implementation without design pattern (bad practice)
- with/ → implementation using design pattern (good practice)

---

## Patterns Implemented

### Creational
- Factory Pattern

### Structural
- Adapter Pattern

### Behavioral
- Strategy Pattern

---

## Project Structure

design-patterns-demo/
│
├── creational/
│   └── factory/
│       ├── without/
│       └── with/
│
├── structural/
│   └── adapter/
│       ├── without/
│       └── with/
│
├── behavioral/
│   └── strategy/
│       ├── without/
│       └── with/
│
└── README.md

## Tech Stack
- Python
- VS Code
- Git

---

## How to Run

### 1. Clone the repository
git clone https://github.com/raaaviiiii/design-patterns-demo.git

cd design-patterns-demo

---

### 2. Run Creational Pattern (Factory)

Without Pattern:
cd creational/factory/without
python factory_without.py

With Pattern:
cd ../with
python factory_with.py

---

### 3. Run Structural Pattern (Adapter)

Without Pattern:
cd ../../../structural/adapter/without
python adapter_without.py

With Pattern:
cd ../with
python adapter_with.py

---

### 4. Run Behavioral Pattern (Strategy)

Without Pattern:
cd ../../../behavioral/strategy/without
python behavioral_without.py

With Pattern:
cd ../with
python behavioral_with.py