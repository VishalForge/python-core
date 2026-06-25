-- Topic: IS NULL
-- query: get all the rows for which song name is null
SELECT *
FROM tutorial_billboard_top_100_year_end
WHERE song_name IS NULL OR TRIM(song_name) = '';

-- Topic: Logical operators: AND, OR, NOT
-- query: get all the rows for top 10 songs in which ludacris was part of the group
SELECT *
  FROM tutorial_billboard_top_100_year_end
 WHERE year_rank <= 10
   AND "group_name" ILIKE '%ludacris%'

-- query: get all the rows for top 10 songs that featured katy perry or bon jovi
SELECT *
FROM tutorial_billboard_top_100_year_end
WHERE year_rank <= 10 AND
    ("group_name" ILIKE '%katy perry%' OR "group_name" ILIKE '%bon jovi%')

--query: get all the rows that have 'california' word in it in the 1970s or 1990s
SELECT *
FROM tutorial_billboard_top_100_year_end
WHERE "song_name" ILIKE '%california%' AND
    (year BETWEEN 1970 AND 1979 OR year BETWEEN 1990 AND 1999)

--query: get all the rows that lists all top-100 recordings that feature Dr. Dre before 2001 or after 2009
SELECT *
FROM tutorial_billboard_top_100_year_end
WHERE "group_name" ILIKE '%Dr. Dre%' AND
    (year <= 2000 OR year >= 2010)  AND year_rank <= 100

--query: get all all rows for songs that were on the charts in 2013 and do not contain the letter "a"
SELECT *   FROM tutorial.billboard_top_100_year_end
  WHERE year = 2013 AND "song_name" NOT ILIKE '%a%'


-- Topic: ORDER BY
--query: get all rows from 2012, ordered by song title from Z to A
SELECT *
FROM tutorial.billboard_top_100_year_end
 WHERE year = 2012
 ORDER BY song_name DESC

-- query: all rows from 2010 ordered by rank, with artists ordered alphabetically for each song
SELECT *
FROM tutorial_billboard_top_100_year_end
WHERE year = 2010
ORDER BY year_rank, artist

-- query: get all rows for which T-Pain was a group member, ordered by rank on the charts, from lowest to highest rank (from 100 to 1)
SELECT *
FROM tutorial_billboard_top_100_year_end
WHERE "group_name" ILIKE '%t-pain%'
ORDER BY year_rank DESC

/* query: that returns songs that ranked between 10 and 20 (inclusive) 
in 1993, 2003, or 2013. Order the results by year and rank, 
and leave a comment on each line of the WHERE clause to indicate what that line does */

SELECT *
FROM tutorial_billboard_top_100_year_end
WHERE year IN (1993, 2003, 2013) --select the years that we want 
    (year_rank BETWEEN 10 AND  20) -- limits the year rank between 10 and 20
ORDER BY year, year_rank


-- Topic: SELECT & FROM
--query: select all of the columns in the tutorial.us_housing_units table without using *.
SELECT year,
       month,
       month_name,
       west,
       midwest,
       south,
       northeast
  FROM tutorial.us_housing_units

-- query: all of the columns in tutorial.us_housing_units and rename them so that their first letters are capitalized
SELECT  year AS "Year", 
        month AS "MONTH",
        month_name AS "MONTH NAME",
        west AS "WEST",
        midwest AS "MID WEST",
        south AS "SOUTH",
        northeast AS "NORTH EAST"
FROM tutorial.us_housing_units


-- query: that uses the LIMIT command to restrict the result set to only 15 rows.
SELECT *
FROM tutotial.us_housing_units
LIMIT 15


-- Topic: Comparison operators
-- query: Did the West Region ever produce more than 50,000 housing units in one month?
SELECT *
FROM tutorial.us_housing_units
WHERE west > 50

-- query: Did the South Region ever produce 20,000 or fewer housing units in one month?
SELECT *
FROM tutorial.us_housing_units
WHERE south <= 20

-- query: Write a query that only shows rows for which the month name is February.
SELECT *
FROM tutorial.us_housing_units
WHERE month_name = 'February'


-- query: Write a query that only shows rows for which the month_name starts with the letter "N" or an earlier letter in the alphabet.
SELECT *
FROM tutorial.us_housing_units
WHERE month_name <= 'N'

-- query: Write a query that calculates the sum of all four regions in a separate column.
SELECT year,
       month,
       west,
       midwest,
       south,
       northeast,
       west + midwest + south + northeast AS regions_sum
FROM tutorial.us_housing_units
 

-- query: Write a query that returns all rows for which more units were produced in the West region than in the Midwest and Northeast combined
SELECT year,
       month,
       west,
       midwest, 
       northeast
FROM tutorial.us_housing_units
WHERE west > (midwest + northeast)


/* query: that calculates the percentage of all houses completed in the United States represented by each region. 
Only return results from the year 2000 and later. */
SELECT year,
       month,
       west / (west + midwest + south + northeast) * 100 AS west_pct,
       midwest / (west + midwest + south + northeast) * 100 AS midwest_pct,
       south / (west + midwest + south + northeast) * 100 AS south_pct,
       northeast / (west + midwest + south + northeast) * 100 AS northeast_pct
FROM tutorial.us_housing_units
WHERE year >= 2000


-- Topic: GROUP BY
-- query: Calculate the total number of shares traded each month. Order your results chronologically.
SELECT year,
       month,
       SUM(volume) AS vol_sum
FROM tutorial_aapl_historical_stock_price
GROUP BY year, month
ORDER BY year, month


-- query: to calculate the average daily price change in Apple stock, grouped by year
SELECT year,
       AVG(close - open) AS avg_daily_price_change
FROM tutorial_aapl_historical_stock_price
GROUP BY 1
ORDER BY 1

-- query: that calculates the lowest and highest prices that Apple stock achieved each month.
SELECT year,
       month,
       MIN(low) AS lowest_price,
       MAX(high) AS highest_price
FROM tutorial_aapl_historical_stock_price
GROUP BY 1, 2
ORDER BY 1, 2

