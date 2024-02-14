-- Task 4. ID can't be null
-- Create the table id_not_null if it does not already exist
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);