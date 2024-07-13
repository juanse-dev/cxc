import pandas as pd
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError
import hashlib
from config import Config

from models.catalog import Employee, Agency, Profession, Gender, Ethnicity

def generate_md5(row):
    md5_hash = hashlib.md5()
    md5_hash.update(f"{row.first_name}{row.last_name}{row.class_title}{row.ethnicity}{row.gender}".encode('utf-8'))
    return md5_hash.hexdigest()

def get_id_map(session, model):
    records = session.query(model).all()
    return {record.name: record.id for record in records}

def load_employees(file_path, batch_size=100):
    usecols = ['agency_name', 'last_name', 'first_name', 'class_title', 'ethnicity', 'gender', 'monthly']
    employees_df = pd.read_csv(file_path, delimiter=',', usecols=usecols)

    employees_df = employees_df.map(lambda x: x.strip() if isinstance(x, str) else x)

    engine = create_engine(Config.DATABASE_URL)
    session_factory = sessionmaker(bind=engine)
    session = session_factory()

    agency_id_map = get_id_map(session, Agency)
    profession_id_map = get_id_map(session, Profession)
    gender_id_map = get_id_map(session, Gender)
    ethnicity_id_map = get_id_map(session, Ethnicity)

    md5_set = set()

    num_rows = len(employees_df)
    for start in range(0, num_rows, batch_size):
        print(f"Processing rows {start} - {min(start + batch_size, num_rows)}")
        end = min(start + batch_size, num_rows)
        batch_df = employees_df.iloc[start:end]

        employees = []
        for row in batch_df.itertuples(index=False):
            md5_row = generate_md5(row)
            if md5_row not in md5_set:
                md5_set.add(md5_row)
                employee = Employee(
                    name=row.first_name,
                    last_name=row.last_name,
                    agency_id=agency_id_map[row.agency_name],
                    profession_id=profession_id_map[row.class_title],
                    gender_id=gender_id_map[row.gender],
                    ethnicity_id=ethnicity_id_map[row.ethnicity],
                    monthly_salary=row.monthly,
                    md5=generate_md5(row),
                )
                employees.append(employee)
        try:
            session.bulk_save_objects(employees)
            session.commit()
        except IntegrityError as e:
            print(f"Unable to insert batch {start} - {end}: {e}")
            session.rollback()
    
    session.close()

if __name__ == "__main__":
    file_path = 'src/data/employees.csv'
    batch_size = 10000
    load_employees(file_path, batch_size)