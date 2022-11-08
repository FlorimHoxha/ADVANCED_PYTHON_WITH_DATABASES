import pandas
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql+mysqlconnector://root:mysqlpass@localhost:3306/redtech30', echo=True)

Base = declarative_base()
class Selling(Base):
    __tablename__ = 'sales'
    __table_args__ = {"schema":"redtech30"}

    order_num = Column(Integer, primary_key=True)
    order_type = Column(String(30))
    cust_name = Column(String(30))
    prod_number = Column(String(30))
    prod_name = Column(String(50))
    quantity = Column(Integer)
    price = Column(Float)
    discount = Column(Float)
    order_total = Column(Float)

    def __repr__(self):
        return '''<Selling(order_num='{0}', order_type='{1}',
                cust_name='{2}', prod_number='{3}',
                prod_name='{4}', quantity='{5}',
                price='{6}', discount_amount='{7}',
                order_total='{8}')>'''.format(self.order_num, self.order_type,
                self.cust_name, self.prod_number,
                self.prod_name, self.quantity, 
                self.price, self.discount,
                self.order_total)

    
Base.metadata.create_all(engine)

file_name = 'red30.csv'
df = pandas.read_csv(file_name)

df.to_sql(con=engine, name=Selling.__tablename__, if_exists='replace', index=False)

session = sessionmaker()
session.configure(bind=engine)
s = session()

overall_max = s.query(func.max(Selling.order_total)).scalar()
# overall_max = s.query((Selling.cust_name, Selling.order_total)func.max(Selling.order_total)).scalar()
print(overall_max)

# results = s.query(Selling).order_by(Selling.order_total.desc()).limit(20)

# for r in results:
#     print(r)