-- creates table id_not_null
-- does not fail if table exists
-- database name passed as argument

CREATE TABLE IF NOT EXISTS id_not_null (
	id INT DEFAULT 1,
	name VARCHAR(256)
);

