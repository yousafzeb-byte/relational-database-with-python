# SQLAlchemy Relational Database Assignment

**Author:** Yousaf Zeb  
**Date:** December 23, 2025

## Overview

This assignment demonstrates the creation and management of a relational database using Python and SQLAlchemy, covering all fundamental CRUD operations.

## Files Created

- `sqlalchemy_assignment.py` - Main assignment script
- `shop.db` - SQLite database (auto-generated)

## What's Implemented

### ✅ Part 1: Setup

- Imported all necessary SQLAlchemy modules
- Created SQLite engine (`shop.db`)
- Set up Base and Session

### ✅ Part 2: Define Tables

**User Table:**

- `id` (Primary Key)
- `name` (String)
- `email` (String, Unique)
- Relationship: One-to-Many with Orders

**Product Table:**

- `id` (Primary Key)
- `name` (String)
- `price` (Integer)
- Relationship: One-to-Many with Orders

**Order Table:**

- `id` (Primary Key)
- `user_id` (Foreign Key → User)
- `product_id` (Foreign Key → Product)
- `quantity` (Integer)
- `status` (Boolean - for bonus part)
- Relationships: Many-to-One with User and Product

### ✅ Part 3: Create Tables

- Used `Base.metadata.create_all(engine)` to create all tables

### ✅ Part 4: Insert Data

- Added 2 users (Alice Johnson, Bob Smith)
- Added 3 products (Laptop, Wireless Mouse, USB-C Cable)
- Added 4 orders with varying quantities and shipping statuses

### ✅ Part 5: Queries

1. **Retrieve all users** - Displays ID, name, and email
2. **Retrieve all products** - Shows name and price
3. **Retrieve all orders** - Shows user name, product name, quantity, and shipping status
4. **Update product price** - Changed Laptop price from $999 to $899
5. **Delete user by ID** - Removed Alice Johnson (ID: 1) with cascade delete on orders

### ✅ Part 6: Bonus Features

- ✅ Added `status` column (Boolean) to Order table
- ✅ Query for unshipped orders
- ✅ Count total orders per user

## How to Run

```bash
# Make sure SQLAlchemy is installed
pip install sqlalchemy

# Run the assignment
python sqlalchemy_assignment.py
```

## Expected Output

The script produces formatted output showing:

- Table creation confirmation
- Data insertion success messages
- Query results for all CRUD operations
- Bonus query results
- Final success message

## Key Features

- **Clean code structure** with proper class definitions
- **Relationships** properly configured using `relationship()` and `back_populates`
- **Cascade delete** implemented (deleting a user removes their orders)
- **Formatted output** for easy reading and verification
- **All requirements met** including bonus features

## Database Schema

```
users                  products              orders
-----                  --------              ------
id (PK)                id (PK)               id (PK)
name                   name                  user_id (FK)
email (UNIQUE)         price                 product_id (FK)
                                             quantity
                                             status
```

## Assignment Complete! ✓

All parts (1-6) successfully implemented and tested.
