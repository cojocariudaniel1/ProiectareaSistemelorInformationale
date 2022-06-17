from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://admin:1395@localhost:5432/fisa_tehnologica')

Session = sessionmaker(bind=engine)

Base = declarative_base()


