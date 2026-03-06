-- Create id_not_null table; id defaults to 1 when omitted
CREATE TABLE IF NOT EXISTS id_not_null (
    id   INT DEFAULT 1,
    name VARCHAR(256)
);