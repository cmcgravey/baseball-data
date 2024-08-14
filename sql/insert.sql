COPY Players(ID, player_id, yearID, stint, teamID, lgID, G, AB, R, H, "2B", "3B", HR, RBI, SB, CS, BB, SO, IBB, HBP, SH, SF, GIDP, AVG, PA, OBP, "1B", TB, SLG, OPS)
FROM 'hitting_data.csv'
DELIMITER ','
CSV HEADER;