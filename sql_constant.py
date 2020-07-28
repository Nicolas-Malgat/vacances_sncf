from enum import Enum


class table(Enum):
    prefecture = 'prefecture'
    route = 'route'
    voyage = 'voyage'
    gare = 'gare'


DROP_TABLE = "DROP TABLE IF EXISTS `{}`;"

SELECT_STATEMENT = {
    'prefecture': "SELECT * FROM prefecture"
    'route': "SELECT * FROM route"
    'voyage': "SELECT * FROM voyage"
}

INSERT_STATEMENT = {
    'prefecture': "INSERT INTO prefecture (region_admin_code, departement_code, departement_name, prefecture_name, region_name, longitude, latitude) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    'route': "INSERT INTO route (id_route, gare_depart, gare_arrivee) VALUES (%s, %s, %s)"
    'voyage': "INSERT INTO voyage (id_voyage, date_time_requete, gare_depart_id, gare_arrivee_id, date_time_depart, date_time_arrivee, duree, pollution) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    'gare': "INSERT INTO gare (id_gare, fk_region_gare, gare_nom, longitude, latitude) VALUES (%s, %s, %s, %s, %s)" 
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

    'route': """CREATE TABLE route (
        id_route    INT(14)    PRIMARY KEY,
        gare_depart VARCHAR (14)     NOT NULL,
        gare_arrivee VARCHAR (14)   NOT NULL
    );
    """

    'voyage': """CREATE TABLE voyage (
        id_voyage    INT(14)    PRIMARY KEY,
        date_time_requete   VARCHAR (15) NOT NULL,
        gare_depart_id  VARCHAR(14)     NOT NULL,
        gare_arrivee_id VARCHAR(14)     NOT NULL,
        date_time_depart    VARCHAR(15) NOT NULL,
        date_time_arrivee   VARCHAR(15) NOT NULL,
        duree   INT(6)  NOT NULL,
        pollution   DOUBLE(8, 3), NOT NULL
    );
    """

    'gare': """CREATE TABLE gare (
        id_gare VARCHAR(14)    PRIMARY KEY,
        FOREIGN KEY fk_region_admin REFERENCES prefecture(region_admin_code),
        gare_nom VARCHAR (255)   NOT NULL,
        longitude       DOUBLE (17, 14),
        latitude        DOUBLE (16, 14)
    );
    """
}
