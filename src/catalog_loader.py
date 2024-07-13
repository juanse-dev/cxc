import pandas as pd
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models.base import Base
from models.catalog import Agency, Profession, Ethnicity, Gender
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

def load_catalog(file_path):
    catalogos_df = pd.read_csv(file_path, delimiter=';')

    engine = create_engine(DATABASE_URL)
    session_factory = sessionmaker(bind=engine)
    session = session_factory()

    agencies = catalogos_df['agency_name'].str.strip().dropna().unique()
    for agency in agencies:
        session.add(Agency(name=agency))

    professions = catalogos_df['class_title'].str.strip().dropna().unique()
    for profession in professions:
        session.add(Profession(name=profession))

    ethnicities = catalogos_df['ethnicity'].str.strip().dropna().unique()
    for ethnicity in ethnicities:
        session.add(Ethnicity(name=ethnicity))

    genders = catalogos_df['gender'].str.strip().dropna().unique()
    for gender in genders:
        session.add(Gender(name=gender))

    session.commit()
    session.close()

if __name__ == "__main__":
    load_catalog('src/data/catalogos.csv')