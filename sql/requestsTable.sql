DROP TABLE IF EXISTS prefecture;
CREATE TABLE prefecture (
    id              INTEGER         PRIMARY KEY AUTO_INCREMENT,
    department_code VARCHAR (2)     NOT NULL,
    department_name VARCHAR (255)   NOT NULL,
    prefecture_name VARCHAR (255)   NOT NULL,
    region_name     VARCHAR (255)   NOT NULL,
    longitude       DOUBLE (17, 14),
    latitude        DOUBLE (16, 14),
    region_admin    VARCHAR (14)     NOT NULL
);
