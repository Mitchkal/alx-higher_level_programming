--lists records with same score in second_table
USE hbtn_0c_0;
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY NUMBER desc, score DESC;
