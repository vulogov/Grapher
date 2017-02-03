-- Grapher database schema for SQLITE3
-- DO NOT RECOMMENDED FOR PRODUCTION !!!
-- Yopu've been warned


CREATE TABLE IF NOT EXISTS OBJECT (
    uuid TEXT,
    ver  INTEGER,
    stamp REAL,
    dtype TEXT,
    d_real REAL,
    d_num INTEGER,
    d_data TEXT
);
-- CREATE INDEX O1 ON (uuid,ver);

CREATE TABLE IF NOT EXISTS RELATION (
    o_uuid TEXT,
    o_ver  INTEGER,
    d_uuid TEXT,
    d_ver  INTEGER,
    l_name TEXT
);
-- CREATE INDEX R_1 (o_uuid,o_ver);
-- CREATE INDEX R_1 (d_uuid,d_ver);



CREATE TABLE IF NOT EXISTS NTYPE (
    t_uuid TEXT UNIQUE PRIMARY KEY,
    t_name TEXT
);

CREATE TABLE IF NOT EXISTS LTYPE (
    l_uuid TEXT UNIQUE PRIMARY KEY,
    l_name TEXT
);