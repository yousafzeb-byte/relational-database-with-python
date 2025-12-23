"""
Hands-On Assignment: Relational Databases with SQLAlchemy
Coding Temple - Relational Databases & API REST Development

Author: Yousaf Zeb
Date: December 23, 2025
"""

# Part 1: Setup
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# Create engine and base
engine = create_engine('sqlite:///shop.db')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


# Part 2: Define Tables
class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    
    # Relationship: A User can have many Orders
    orders = relationship('Order', back_populates='user', cascade='all, delete-orphan')
    
    def __repr__(self):
        return f"<User(id={self.id}, name='{self.name}', email='{self.email}')>"


class Product(Base):
    __tablename__ = 'products'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    
    # Relationship: A Product can appear in many Orders
    orders = relationship('Order', back_populates='product')
    
    def __repr__(self):
        return f"<Product(id={self.id}, name='{self.name}', price=${self.price})>"


class Order(Base):
    __tablename__ = 'orders'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    quantity = Column(Integer, nullable=False)
    status = Column(Boolean, default=False)  # Part 6: Bonus - False = not shipped, True = shipped
    
    # Relationships
    user = relationship('User', back_populates='orders')
    product = relationship('Product', back_populates='orders')
    
    def __repr__(self):
        return f"<Order(id={self.id}, user_id={self.user_id}, product_id={self.product_id}, quantity={self.quantity}, shipped={self.status})>"


# Part 3: Create Tables
print("=" * 60)
print("Creating database tables...")
print("=" * 60)
Base.metadata.create_all(engine)
print("✓ Tables created successfully!\n")


# Part 4: Insert Data
print("=" * 60)
print("Inserting sample data...")
print("=" * 60)

# Add 2 users
user1 = User(name='Alice Johnson', email='alice@example.com')
user2 = User(name='Bob Smith', email='bob@example.com')

session.add_all([user1, user2])
session.commit()
print("✓ Added 2 users")

# Add 3 products
product1 = Product(name='Laptop', price=999)
product2 = Product(name='Wireless Mouse', price=25)
product3 = Product(name='USB-C Cable', price=15)

session.add_all([product1, product2, product3])
session.commit()
print("✓ Added 3 products")

# Add 4 orders
order1 = Order(user_id=user1.id, product_id=product1.id, quantity=1, status=True)  # Shipped
order2 = Order(user_id=user1.id, product_id=product2.id, quantity=2, status=False)  # Not shipped
order3 = Order(user_id=user2.id, product_id=product3.id, quantity=3, status=False)  # Not shipped
order4 = Order(user_id=user2.id, product_id=product1.id, quantity=1, status=True)  # Shipped

session.add_all([order1, order2, order3, order4])
session.commit()
print("✓ Added 4 orders\n")


# Part 5: Queries
print("=" * 60)
print("Part 5: Running Queries")
print("=" * 60)

# 1. Retrieve all users
print("\n1. All Users:")
print("-" * 40)
users = session.query(User).all()
for user in users:
    print(f"   ID: {user.id}, Name: {user.name}, Email: {user.email}")

# 2. Retrieve all products
print("\n2. All Products:")
print("-" * 40)
products = session.query(Product).all()
for product in products:
    print(f"   {product.name} - ${product.price}")

# 3. Retrieve all orders with user name, product name, and quantity
print("\n3. All Orders:")
print("-" * 40)
orders = session.query(Order).all()
for order in orders:
    print(f"   Order #{order.id}: {order.user.name} ordered {order.quantity} x {order.product.name} (Shipped: {order.status})")

# 4. Update a product's price
print("\n4. Updating Product Price:")
print("-" * 40)
laptop = session.query(Product).filter_by(name='Laptop').first()
old_price = laptop.price
laptop.price = 899
session.commit()
print(f"   Updated 'Laptop' price from ${old_price} to ${laptop.price}")

# 5. Delete a user by ID
print("\n5. Deleting User:")
print("-" * 40)
user_to_delete = session.query(User).filter_by(id=1).first()
if user_to_delete:
    print(f"   Deleting user: {user_to_delete.name} (ID: {user_to_delete.id})")
    session.delete(user_to_delete)
    session.commit()
    print("   ✓ User deleted successfully")
    
    # Verify deletion
    remaining_users = session.query(User).count()
    print(f"   Remaining users: {remaining_users}")


# Part 6: Bonus (Optional)
print("\n" + "=" * 60)
print("Part 6: Bonus Queries")
print("=" * 60)

# Query all orders that are not shipped
print("\n1. Orders Not Yet Shipped:")
print("-" * 40)
unshipped_orders = session.query(Order).filter_by(status=False).all()
if unshipped_orders:
    for order in unshipped_orders:
        print(f"   Order #{order.id}: {order.user.name} - {order.quantity} x {order.product.name}")
else:
    print("   All orders have been shipped!")

# Count the total number of orders per user
print("\n2. Total Orders Per User:")
print("-" * 40)
users = session.query(User).all()
for user in users:
    order_count = len(user.orders)
    print(f"   {user.name}: {order_count} order(s)")


print("\n" + "=" * 60)
print("Assignment Complete! ✓")
print("=" * 60)
print(f"Database file created: shop.db")
print("All CRUD operations executed successfully!")

# Close the session
session.close()
