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


-- Topic: Count function
-- query: that determines counts of every single column. With these counts, can you tell which column has the most null values?
SELECT  Count(year) AS year_count,
        Count(month) AS month_count,
        COUNT(date) AS date_count,
        COUNT(open) AS open_count,
        COUNT(low) AS low_count,
        COUNT(high) AS high_count,
        COUNT(close) AS close_count,
        COUNT(volume) AS vol_count
                
FROM tutorial.aapl_historical_stock_price
-- The column which returns the lowest count has the most Null values.



-- Topic: Sum function
-- query:  calculate the average opening price
SELECT SUM(open) / COUNT(open) AS avg_opening_price
FROM tutorial.aapl_historical_stock_price


-- Topic: MIN & MAX function
-- query: What was the highest single-day increase in Apple's share value?
SELECT MAX(close - open) AS highest_increase
FROM tutorial_aapl_historical_stock_price

-- query: What was Apple's lowest stock price (at the time of this data collection)?
SELECT MIN(low) AS lowest_price
FROM tutorial_aapl_historical_stock_price


-- Topic: Average function
-- query: Write a query that calculates the average daily trade volume for Apple stock.
SELECT AVG(volume) AS avg_daily_vol
FROM tutorial_aapl_historical_stock_price


-- Topic: Having clause
-- query: Find every month during which AAPL stock worked its way over $400/share.
SELECT year,
       month,
       MAX(high) AS month_high
FROM tutorial_aapl_historical_stock_price
GROUP BY year, month
HAVING MAX(high) > 400
ORDER BY year, month



-- Topic: CASE statement
-- query: column that is flagged "yes" when a player is from California, and sort the results with those players first
SELECT player_name,
       CASE WHEN hometown = 'CA' THEN 'yes'
       ELSE 'no' END AS from_california
FROM benn.college_football_players
ORDER BY from_california


/* query: Write a query that includes players' names and a column that 
classifies them into four categories based on height. Keep in mind that the
 answer we provide is only one of many possible answers, since you could divide players' heights in many ways.
 */
 SELECT player_name,
        height,
        CASE WHEN height > 75 THEN 'over_75'
        WHEN height > 73 AND height <= 75 THEN '74-75'
        WHEN height > 70 AND height <= 73 THEN '71-73'
        ELSE 'under_70' END AS height_group
FROM benn_college_football_players

-- query: selects all columns from benn.college_football_players and adds an additional column that displays the player's name if that player is a junior or senior.
SELECT *,
       CASE WHEN year IN('JR', 'SR') THEN player_name
       ELSE NULL END AS additional_column
FROM benn_college_football_players


-- query: count the number of 300lb+ players for each of the following regions: West Coast (CA, OR, WA), Texas, and Other (everywhere else).
SELECT CASE WHEN state IN('CA', 'OR', 'WA') THEN 'west coast'
       WHEN state = 'TX' THEN 'Texas'
       ELSE 'other' END AS weight_region_group,
       COUNT(state) AS 'players'
FROM benn_college_football_players
WHERE weight >= 300
GROUP BY weight_region_group


/* query: display the number of players in each state, with FR, SO, JR, and SR players 
in separate columns and another column for the total number of players. 
Order results such that states with the most players come first. */
SELECT state,
       COUNT(CASE WHEN year = 'FR' THEN 1 ELSE NULL END) AS 'fr_count',
       COUNT(CASE WHEN year = 'SO' THEN 1 ELSE NULL END) AS 'so_count',
       COUNT(CASE WHEN year = 'JR' THEN 1 ELSE NULL END) AS 'jr_count',
       COUNT(CASE WHEN year = 'SR' THEN 1 ELSE NULL END) AS 'sr_count',
       COUNT(1) AS players_count
FROM benn_college_football_players
GROUP BY state
ORDER BY players_count DESC


-- query: show the number of players at schools with names that start with A through M,
-- and the number at schools with names starting with N - Z.
SELECT CASE WHEN school_name >= 'n' THEN 'N-Z'
       WHEN school_name < n THEN 'A-M'
       ELSE NULL END AS school_group
       COUNT(1) AS players_count
FROM benn_college_football_players
GROUP BY 1



-- Topic: DISTINCT
-- query: returns the unique values in the year column, in chronological order.
SELECT DISTINCT year
FROM tutorial_aapl_historical_stock_price
ORDER BY year


-- query: count the number of unique values in the month column for each year.
SELECT year,
      COUNT(DISTINCT month) AS distinct_month
FROM tutorial_aapl_historical_stock_price
GROUP BY year
ORDER BY year


-- query: separately counts the number of unique values in the month column and the number of unique values in the `year` column.
SELECT COUNT(DISTINCT year) AS distinct_year,
       COUNT(DISTINCT month) AS distinct_month
FROM tutorial_aapl_historical_stock_price



/*Topic: query that selects the school name, player name, position, and 
weight for every player in Georgia, ordered by weight (heaviest to lightest)
Be sure to make an alias for the table, and to reference all column names
 in relation to the alias.
*/
SELECT players.player_name,
      players.school_name,
      players.position,
      players.weight
FROM benn_college_football_players players
WHERE players.state = 'GA'
ORDER BY players.weight DESC

-- Topic: Inner Join
SELECT players.*,
       teams.*
FROM benn_college_football_players players
JOIN benn_college_football_teams teams
ON players.school_name = teams.school_name


-- query: displays player names, school names and conferences for schools in the "FBS (Division I-A Teams)" division
SELECT players.player_name,
       players.school_name,
       teams.conference
FROM benn_college_football_players players
JOIN benn_college_football_teams teams
ON players.school_name = teams.school_name
WHERE teams.division = 'FBS (Division I-A Teams)'



---------------------------------------------------------------------------

-- query: list every product under 900 USD, cheapest first
SELECT name, price
FROM products
WHERE price <= 900
ORDER BY price;


-- query: Find every customer whose name contains the letter 'a' anywhere
SELECT name
FROM customers
WHERE name LIKE '%a%';

-- query: List the 3 most recent transactions by created_at.
SELECT transaction_id, created_at
FROM transactions
ORDER BY created_at;

-- query: Find customer whose email or age is NULL.
SELECT name AS customer_name, email, age
FROM customers
WHERE email IS NULL OR age IS NULL;


-- query: Find customers whose values are not NUll.
SELECT *
FROM customers
WHERE email IS NOT NULL AND age IS NOT NULL


-- query: Find product that have price between 200 and 1000
SELECT name, price, stock
FROM products
WHERE price BETWEEN 200 AND 1000

-- query: Using most of the clause for query
SELECT customer_id, SUM(amount) AS total_spend
FROM transactions
WHERE satus = 'completed'
GROUP BY customer_id
HAVING SUM(amount) > 1000
ORDER BY total_spend DESC


-- query: 
SELECT product_id, name
FROM products
WHERE stock >= 30 AND (category = 'electronics')


-- query:
SELECT DISTINCT customer_id
FROM transactions

-- query:
SELECT *
FROM products
WHERE category IN('electronics', 'home')

-- query: Total revenue from transactions with status = 'completed' only
SELECT SUM(amount)
FROM transactions
WHERE status = 'completed'


-- query: 
SELECT category, MAX(price) as max_price
FROM products
GROUP BY category

-- query:
SELECT status, AVG(amount) AS avg_price
FROM transactions
GROUP BY status

-- query:
SELECT category, MIN(price) AS min_price
FROM products
GROUP BY category

-- query:
SELECT COUNT(*) AS total_rows, COUNT(age) AS age, COUNT(created_at) AS date, COUNT(email) AS email
FROM customers;

-- query:
SELECT category, AVG(price) as avg_price
FROM products
GROUP BY category
HAVING AVG(price) > 1000;


-- query:
SELECT customer_id, COUNT(*) AS total_transactions, SUM(amount) AS amount_sum
FROM transactions
WHERE status = 'completed'
GROUP BY customer_id
HAVING COUNT(*) > 1;

-- query:
SELECT customer_id, COUNT(*) AS total_transactions, SUM(amount) AS amount_sum
FROM transactions
WHERE status = 'pending'
GROUP BY customer_id
HAVING COUNT(*) > 1;

-- query:
SELECT customer_id, COUNT(*) total_transactions, SUM(amount) amount_sum
FROM transactions
WHERE status = 'completed'
GROUP BY customer_id
HAVING COUNT(*) >= 2 AND SUM(amount) > 1000;


-- query: 
SELECT customer_id, COUNT(*) total_transactions
FROM transactions
GROUP BY customer_id, status
HAVING COUNT(*)> 1 AND status = 'completed';

-- This will throw an error because any column in HAVING clause must be either
-- in GROUP BY, or wrapped in an aggregate function.


-- query:
SELECT COUNT(DISTINCT category) AS distinct_category
FROM products;

-- query:
SELECT COUNT(DISTINCT customer_id) AS customer_id
FROM transactions
WHERE status = 'completed';


-- query:
SELECT p.name
FROM products p
LEFT JOIN transactions t ON p.product_id = t.product_id
WHERE t.transaction_id IS NULL

-- query:
SELECT c1.name AS customer_1, c2.name AS customer_2
FROM customers c1
INNER JOIN customers c2 ON c1.age = c2.age
WHERE c1.customer_id < c2.customer_id

-- query:
-- First part: THE LEFT JOIN
SELECT c.name, t.transaction_id
FROM customers c
LEFT JOIN transactions t ON c.customer_id = t.customer_id

UNION

-- Second part: THE RIGHT JOIN
SELECT c.name, t.transaction_id
FROM customers c
RIGHT JOIN transactions t ON c.customer_id = t.customer_id


-- query:
SELECT c.name, COUNT(t.customer_id)
FROM customers c
LEFT JOIN transactions t ON c.customer_id = t.customer_id AND t.status = 'completed'
GROUP BY c.name


-- query:
SELECT c1.name AS customer1, c2.name AS customer2
FROM customers c1
CROSS JOIN customers c2
WHERE c1.customer_id < c2.customer_id
     AND (c1.age >= c2.age + 10 OR c2.age >= c1.age + 10)


-- query:
SELECT c.name, t.transaction_id
FROM customers c
FULL OUTER JOIN transactions t ON c.customer_id = t.customer_id

/* Customers with no transactions will have NULL in their transaction_id column.
Trnsaction with no customer will have NULL in their name column. */


WITH avg_spends AS (
    SELECT customer_id, AVG(amount) AS avg_spend
	FROM transactions
	WHERE status = 'completed'
	GROUP BY customer_id
)

SELECT c.name
FROM customers c
LEFT JOIN avg_spends as1 ON c.customer_id = as1.customer_id
WHERE c.customer_id IN(SELECT customer_id FROM transactions t WHERE t.amount > avg_spend)