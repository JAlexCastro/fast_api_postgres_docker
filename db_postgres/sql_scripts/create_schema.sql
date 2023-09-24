CREATE schema store;

CREATE schema commercial;


CREATE TABLE commercial.users (
  id serial PRIMARY KEY,
  name character varying(50) NOT NULL,
  last_name character varying(50) NOT NULL,
  age integer NOT NULL
);

ALTER TABLE IF EXISTS commercial.users
    OWNER to fast_user;

-- Schema --> storage

CREATE TABLE store.products (
    code character varying(4) PRIMARY KEY,
    product_name varchar NOT NULL,
    stock integer NOT NULL,
    price float NOT NULL);

ALTER TABLE IF EXISTS store.products
    OWNER to fast_user;
