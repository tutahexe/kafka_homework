CREATE TABLE IF NOT EXISTS results (
    id SERIAL PRIMARY KEY,
    url VARCHAR(55) NOT NULL,
    response_time NUMERIC(8,6) NOT NULL,
    status_code INTEGER NOT NULL,
    regexp BOOLEAN
);