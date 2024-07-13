CREATE TABLE IF NOT EXISTS test.agency (
    id bigserial NOT NULL,
    name varchar(50) NOT NULL,
    created_at timestamp(0) NOT NULL DEFAULT timezone('CDT'::text, now()),
    CONSTRAINT agency_pk PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS test.profession (
    id bigserial NOT NULL,
    name varchar(50) NOT NULL,
    created_at timestamp(0) NOT NULL DEFAULT timezone('CDT'::text, now()),
    CONSTRAINT profession_pk PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS test.ethnicity (
    id bigserial NOT NULL,
    name varchar(50) NOT NULL,
    created_at timestamp(0) NOT NULL DEFAULT timezone('CDT'::text, now()),
    CONSTRAINT ethnicity_pk PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS test.gender (
    id bigserial NOT NULL,
    name varchar(50) NOT NULL,
    created_at timestamp(0) NOT NULL DEFAULT timezone('CDT'::text, now()),
    CONSTRAINT gender_pk PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS test.employee (
    id bigserial NOT NULL,
    name varchar(50) NOT NULL,
    last_name varchar(50) NOT NULL,
    agency_id int4 NOT NULL,  
    profession_id int4 NOT NULL, 
    gender_id int4 NOT NULL,  
    ethnicity_id int4 NOT NULL, 
    monthly_salary numeric(16, 2) NOT NULL,
    md5 varchar(50) NOT NULL UNIQUE,
    created_at timestamp(0) NOT NULL DEFAULT timezone('CDT'::text, now()),
    CONSTRAINT employee_pk PRIMARY KEY (id),
    CONSTRAINT fk_agency_employee FOREIGN KEY (agency_id) REFERENCES test.agency(id),
    CONSTRAINT fk_profession_employee FOREIGN KEY (profession_id) REFERENCES test.profession(id),
    CONSTRAINT fk_gender_employee FOREIGN KEY (gender_id) REFERENCES test.gender(id),
    CONSTRAINT fk_ethnicity_employee FOREIGN KEY (ethnicity_id) REFERENCES test.ethnicity(id)
);
