BEGIN;


CREATE TABLE IF NOT EXISTS public.order_detail
(
    id character(36) COLLATE pg_catalog."default" NOT NULL,
    amount integer,
    unit_price character(5) COLLATE pg_catalog."default",
    person_id character(36) COLLATE pg_catalog."default",
    product_id character(36) COLLATE pg_catalog."default",
    CONSTRAINT order_detail_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.person
(
    id character(36) COLLATE pg_catalog."default" NOT NULL,
    name character varying(250) COLLATE pg_catalog."default",
    user_name character varying(250) COLLATE pg_catalog."default",
    birthday date,
    CONSTRAINT person_pkey1 PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.product
(
    id character(36) COLLATE pg_catalog."default" NOT NULL,
    name character varying(250) COLLATE pg_catalog."default",
    price character(10) COLLATE pg_catalog."default",
    description character varying(250) COLLATE pg_catalog."default",
    CONSTRAINT product_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.request
(
    id character(36) COLLATE pg_catalog."default" NOT NULL,
    date date,
    state boolean,
    CONSTRAINT order_pkey PRIMARY KEY (id)
);

ALTER TABLE IF EXISTS public.order_detail
    ADD CONSTRAINT order_detail_person_id_fkey FOREIGN KEY (person_id)
    REFERENCES public.person (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION;


ALTER TABLE IF EXISTS public.order_detail
    ADD CONSTRAINT order_detail_product_id_fkey FOREIGN KEY (product_id)
    REFERENCES public.product (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION;

END;