-- lists alll cities in database hbtn_0d_usa
-- display city id, name, state name, order by city id

SELECT cities.id, cities.name, states.name
  FROM cities
  JOIN states
 WHERE cities.state_id = states.id
ORDER BY cities.id ASC;
  
