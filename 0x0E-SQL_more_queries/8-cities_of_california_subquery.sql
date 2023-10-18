-- lists all cities of california in hbtn_0d_usa
-- result sorted in ascending city id

SELECT id, name
  FROM cities
 WHERE state_id = (SELECT id FROM states WHERE name = "California") GROUP BY id ORDER BY id ASC; 
