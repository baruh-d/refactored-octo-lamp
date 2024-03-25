#!/usr/bin/env python3

from models import User, Transaction, Category
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()
# initialize the seed value to ensure random data generated by Faker remains consistent across multiple runs
#by initializing to zero . This will generate a new set of "random" values each time you run the script. 
Faker.seed(0)

# Connect to the database
engine = create_engine('sqlite:///finance_tracker.db', echo=True)
Session = sessionmaker(bind=engine)  

Session.bind = engine #bind engine to session
def generate_data(n_users, n_categories, num_transactions):
    """Populate the database with fake data."""
    db_session = Session()
    #calculating based of of start and end dates for random generated dates
    start_date = '2017-01-01T00:00:00.000Z' #any date
    end_date = datetime.now() + timedelta(days=100) 
    end_date = end_date.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    
    #generating user data
    users = [User(name=fake.name(), email=fake.email()) for _ in range(n_users)]
    #set passwords for each user
    for user in users:
        user.set_password(fake.password())
    #add all users
    db_session.bulk_save_objects(users)
    #commit changes to db
    db_session.commit()
    
     #generating categories
    categories = set(Category(label=fake.word()) for _ in range(n_categories))
    db_session.bulk_save_objects(list(categories))
    #commit changes
    db_session.commit()
    
    #extracting category IDs
    category_ids = {category.id for category in categories}
    
    #generating transaction data using associated classes/methods 
    transactions_data = []
    for user in users:
        num_transactions = random.randint(5, 20)
        for _ in range(num_transactions):
            # user = random.choice(users)
            amount = random.randint(1, 999999) #amount range to rep ksh
            transaction_type = random.choice(['debit', 'credit'])
            category_id = random.choice(list(category_ids)) #converting the set to list for random choice
            #generating random date within the specified range
            random_date = fake.date.between(start_date=start_date, end_date=end_date)
            transaction_data = Transaction(
                user_id=user.id, 
                category_id=category_id,
                description=fake.text(), 
                amount=amount,
                transaction_type=transaction_type,
                date=random_date.strftime('%Y-%m-%d %H:%M:%S.%f'),
            )
            transactions_data.append(transaction_data)
            
    db_session.bulk_save_objects(transactions_data)
    db_session.commit()
    db_session.close()

def populate(n_users=15, n_categories=7, num_transactions=100):
    generate_data(n_users, n_categories, num_transactions)
    
if __name__ == "__main__":
    populate()    