CREATE TABLE Players(
    ID SERIAL, 
    player_id VARCHAR(50),
    yearID INTEGER,
    stint INTEGER,
    teamID INTEGER,
    lgID INTEGER,
    G INTEGER,
    AB INTEGER,
    R INTEGER,
    H INTEGER,
    2B INTEGER,
    3B INTEGER,
    HR INTEGER,
    RBI INTEGER,
    SB INTEGER,
    CS INTEGER,
    BB INTEGER,
    SO INTEGER,
    IBB INTEGER,
    HBP INTEGER,
    SH INTEGER,
    SF INTEGER,
    GIDP INTEGER,
    AVG REAL,
    PA INTEGER,
    OBP REAL,
    1B INTEGER,
    TB INTEGER,
    SLG REAL,
    OPS REAL,
    PRIMARY KEY (ID)
);
