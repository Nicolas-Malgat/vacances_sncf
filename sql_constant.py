from enum import Enum


class table(Enum):
    prefecture = 'prefecture'
    route = 'route'
    voyage = 'voyage'
    gare = 'gare'
    journey = 'journey'
    route_gare = 'route_gare'
    route_journey = 'route_journey'


DROP_TABLE = "DROP TABLE IF EXISTS `{}`;"

SELECT_STATEMENT = {
    'prefecture': "SELECT * FROM prefecture",
    'route': "SELECT * FROM route",
    'voyage': "SELECT * FROM voyage ORDER BY voyage.duree LIMIT 1",
    'journey': "SELECT * FROM journey",
    'route_gare': "SELECT * FROM route_gare",
    'route_journey': "SELECT * FROM route_journey"
}

LOAD_STATEMENT = {
    'journey': "SELECT * FROM journey WHERE journey.voyage_id = {} ORDER BY ordre",
    # 'route_journey': "SELECT * FROM route_journey WHERE route_journey.journey_id = {} ORDER BY ordre",
    'route': "SELECT  route.id_route, route.gare_depart, route.gare_arrivee FROM route, route_journey WHERE route.id_route = route_journey.route_id and route_journey.journey_id = {} order by route_journey.ordre",
    'voyage': "SELECT * FROM voyage WHERE id_voyage = {}"
}

INSERT_STATEMENT = {
    'prefecture': "INSERT INTO prefecture (region_admin_code, departement_code, departement_name, prefecture_name, region_name, longitude, latitude) VALUES (%s, %s, %s, %s, %s, %s, %s)",
    'route': "INSERT INTO route (id_route, gare_depart, gare_arrivee) VALUES (%s, %s, %s)",
    'voyage': "INSERT INTO voyage (id_voyage, date_time_requete, gare_depart_id, gare_arrivee_id, date_time_depart, date_time_arrivee, duree, pollution) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
    'gare': "INSERT INTO gare (id_gare, region_admin, gare_nom, longitude, latitude) VALUES (%s, %s, %s, %s, %s)",
    'journey': "INSERT INTO journey (id_trajet, trajet_duree, heure_depart, heure_arrivee, heure_requete, gare_depart_id, gare_arrivee_id, pollution, voyage_id, ordre) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
    'route_gare': "INSERT INTO route_gare (route_id, gare_id) VALUES (%s, %s)",
    'route_journey': "INSERT INTO route_journey (route_id, journey_id, ordre) VALUES (%s, %s, %s)"
}

CREATE_TABLE = {
    'prefecture': """CREATE TABLE prefecture (
        region_admin_code VARCHAR(14)    PRIMARY KEY,
        departement_code VARCHAR (2)     NOT NULL,
        departement_name VARCHAR (255)   NOT NULL,
        prefecture_name VARCHAR (255)   NOT NULL,
        region_name     VARCHAR (255)   NOT NULL,
        longitude       DOUBLE (17, 14) NOT NULL,
        latitude        DOUBLE (16, 14) NOT NULL
    );
    """,

    'route': """CREATE TABLE route (
        id_route    VARCHAR(50)    PRIMARY KEY,
        gare_depart VARCHAR (25)     NOT NULL,
        gare_arrivee VARCHAR (25)   NOT NULL
    );
    """,

    'voyage': """CREATE TABLE voyage (
        id_voyage    VARCHAR(50)    PRIMARY KEY,
        date_time_requete   VARCHAR (15) NOT NULL,
        gare_depart_id  VARCHAR(25)     NOT NULL,
        gare_arrivee_id VARCHAR(25)     NOT NULL,
        date_time_depart    VARCHAR(15) NOT NULL,
        date_time_arrivee   VARCHAR(15) NOT NULL,
        duree   INT(6)  NOT NULL,
        pollution   DOUBLE(8, 3) NOT NULL
    );
    """,

    'gare': """CREATE TABLE gare (
        id_gare VARCHAR(25)    PRIMARY KEY,
        region_admin VARCHAR(14),
        gare_nom VARCHAR (255)   NOT NULL,
        longitude       DOUBLE (17, 14) NOT NULL,
        latitude        DOUBLE (16, 14) NOT NULL,
        CONSTRAINT FK_prefecture
            FOREIGN KEY (region_admin) REFERENCES prefecture (region_admin_code)
    );
    """,

    'journey': """CREATE TABLE journey (
        id_trajet   VARCHAR(50)    PRIMARY KEY,
        trajet_duree    INT(6) NOT NULL,
        heure_depart    VARCHAR(15) NOT NULL,
        heure_arrivee   VARCHAR(15) NOT NULL,
        heure_requete   VARCHAR(15) NOT NULL,
        gare_depart_id  VARCHAR(25) NOT NULL,
        gare_arrivee_id VARCHAR(25) NOT NULL,
        pollution   DOUBLE(8, 3) NOT NULL,
        voyage_id   VARCHAR(50) NOT NULL,
        ordre INT NOT NULL,

        FOREIGN KEY (voyage_id) REFERENCES voyage(id_voyage)
    );
    """,

    'route_gare': """CREATE TABLE route_gare (
        route_id    VARCHAR(50)     NOT NULL,
        gare_id     VARCHAR(25)  NOT NULL,
        PRIMARY KEY (route_id, gare_id),
        FOREIGN KEY (route_id) REFERENCES route(id_route),
        FOREIGN KEY (gare_id) REFERENCES gare(id_gare)
    );
    """,

    'route_journey': """CREATE TABLE route_journey (
        route_id    VARCHAR(50)     NOT NULL,
        journey_id     VARCHAR(50)  NOT NULL,
        ordre INT NOT NULL,

        PRIMARY KEY (route_id, journey_id),
        FOREIGN KEY (route_id) REFERENCES route(id_route),
        FOREIGN KEY (journey_id) REFERENCES journey(id_trajet)
    );
    """
}
