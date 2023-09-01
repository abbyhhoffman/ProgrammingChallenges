conn=DBI::dbConnect(RSQLite::SQLite())

#QUERY 1
SELECT date, SUM(impressions) AS total_impressions
FROM Marketing
GROUP BY date
ORDER BY date;

#QUERY 2
SELECT state, SUM(revenue) AS total_revenue
FROM Website
GROUP BY state
ORDER BY total_revenue DESC
LIMIT 3;

#The third best performing state by revenue was Ohio with a total revenue of $37,577.

#QUERY 3 

SELECT c.name AS campaign_name, 
       SUM(mp.cost) AS total_cost,
       SUM(mp.impressions) AS total_impressions,
       SUM(mp.clicks) AS total_clicks,
       SUM(wr.revenue) AS total_revenue
FROM  Campaign c
JOIN Marketing mp ON c.id = mp.campaign_id
JOIN Website wr ON c.id = wr.campaign_id
GROUP BY c.name;


#QUERY 4 
SELECT c.name AS campaign_name, wr.state,
SUM(mp.conversions) AS total_conversions
FROM  Campaign c
JOIN Marketing mp ON c.id = mp.campaign_id
JOIN Website wr ON c.id = wr.campaign_id
WHERE c.name = "Campaign5"
GROUP BY wr.state
ORDER BY total_conversions DESC
LIMIT 1;

#Georgia performed the most conversions in Campaign 5

#QUERY5
SELECT c.name AS campaign_name,
       SUM(mp.cost) / SUM(mp.conversions) AS cost_per_conversion
FROM Campaign c
JOIN Marketing mp ON c.id = mp.campaign_id
GROUP BY c.name
ORDER BY cost_per_conversion ASC
LIMIT 1;

#Assuming efficiency is measured by cost per conversion, 
#Campaign 4 was the cheapest cost per conversion campaign.

#BONUS
SELECT DATENAME(day, '2017/08/25 08:36') AS day_of_week;
       AVG(impressions) AS avg_impressions
FROM Marketing
GROUP BY day_of_week
ORDER BY avg_impressions DESC
LIMIT 1;

