-- creates table force_name without fail
-- dtabase name passed as argument

CREATE TABLE IF NOT EXISTS force_name (
	id INT,
	name VARCHAR(256) NOT NULL
);
