PREFECTURE = "prefecture"
DROP_TABLE = "DROP TABLE IF EXISTS `{}`;"
INSERT_STATEMENT = {
    'prefecture': "INSERT INTO prefecture (region_admin_code, departement_code, departement_name, prefecture_name, region_name, longitude, latitude) VALUES (%s, %s, %s, %s, %s, %s, %s)"    
}

CREATE_TABLE = {
    'prefecture': """CREATE TABLE prefecture (
        region_admin_code VARCHAR(14)    PRIMARY KEY,
        departement_code VARCHAR (2)     NOT NULL,
        departement_name VARCHAR (255)   NOT NULL,
        prefecture_name VARCHAR (255)   NOT NULL,
        region_name     VARCHAR (255)   NOT NULL,
        longitude       DOUBLE (17, 14),
        latitude        DOUBLE (16, 14)
    );
    """
}
