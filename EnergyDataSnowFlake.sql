-- ============================================
-- STEP 1: VIEW CURRENT DATA
-- ============================================

SELECT * FROM "MY_ENERGY_DATABASE"."PUBLIC"."ENERGYDATA" LIMIT 10;


-- ============================================
-- STEP 2: BASIC EXPLORATORY ANALYSIS
-- ============================================

SELECT 
    COUNT(*) as total_records,
    COUNT(DISTINCT YEAR) as unique_years,
    COUNT(DISTINCT COUNTRYNAME) as unique_countries,
    MIN(YEAR) as earliest_year,
    MAX(YEAR) as latest_year,
    COUNT(DISTINCT PRICE) as unique_price_types
FROM "MY_ENERGY_DATABASE"."PUBLIC"."ENERGYDATA";


-- ============================================
-- STEP 3: PRICE TRENDS OVER TIME
-- ============================================

SELECT 
    YEAR,
    COUNTRYNAME,
    PRICE,
    CURRENCY::FLOAT as price_value,
    LAG(CURRENCY::FLOAT) OVER (ORDER BY YEAR) as previous_year_price,
    ROUND((CURRENCY::FLOAT - LAG(CURRENCY::FLOAT) OVER (ORDER BY YEAR)) / LAG(CURRENCY::FLOAT) OVER (ORDER BY YEAR) * 100, 2) as year_over_year_change_pct
FROM "MY_ENERGY_DATABASE"."PUBLIC"."ENERGYDATA"
WHERE CURRENCY IS NOT NULL
ORDER BY YEAR;


-- ============================================
-- STEP 4: PRICE STATISTICS BY PRICE TYPE
-- ============================================

SELECT 
    PRICE,
    COUNT(*) as frequency,
    ROUND(MIN(CURRENCY::FLOAT), 4) as min_price,
    ROUND(MAX(CURRENCY::FLOAT), 4) as max_price,
    ROUND(AVG(CURRENCY::FLOAT), 4) as avg_price,
    ROUND(STDDEV(CURRENCY::FLOAT), 4) as std_deviation
FROM "MY_ENERGY_DATABASE"."PUBLIC"."ENERGYDATA"
WHERE CURRENCY IS NOT NULL
GROUP BY PRICE
ORDER BY frequency DESC;


-- ============================================
-- STEP 5: DECADE ANALYSIS
-- ============================================

SELECT 
    CASE 
        WHEN YEAR >= 2000 AND YEAR < 2010 THEN '2000s'
        WHEN YEAR >= 2010 AND YEAR < 2020 THEN '2010s'
    END as decade,
    COUNT(*) as records,
    ROUND(AVG(CURRENCY::FLOAT), 4) as avg_price,
    ROUND(MIN(CURRENCY::FLOAT), 4) as min_price,
    ROUND(MAX(CURRENCY::FLOAT), 4) as max_price
FROM "MY_ENERGY_DATABASE"."PUBLIC"."ENERGYDATA"
WHERE YEAR IS NOT NULL AND CURRENCY IS NOT NULL
GROUP BY decade
ORDER BY decade;


-- ============================================
-- STEP 6: IDENTIFY PRICE ANOMALIES
-- ============================================

WITH price_stats AS (
    SELECT 
        AVG(CURRENCY::FLOAT) as mean_price,
        STDDEV(CURRENCY::FLOAT) as std_price
    FROM "MY_ENERGY_DATABASE"."PUBLIC"."ENERGYDATA"
    WHERE CURRENCY IS NOT NULL
)
SELECT 
    YEAR,
    PRICE,
    CURRENCY::FLOAT as price_value,
    ROUND((CURRENCY::FLOAT - ps.mean_price) / ps.std_price, 2) as z_score
FROM "MY_ENERGY_DATABASE"."PUBLIC"."ENERGYDATA", price_stats ps
WHERE CURRENCY IS NOT NULL AND ABS((CURRENCY::FLOAT - ps.mean_price) / ps.std_price) > 1.5
ORDER BY z_score DESC;


-- ============================================
-- STEP 7: CREATE A SUMMARY VIEW (FOR RESUME!)
-- ============================================

CREATE OR REPLACE VIEW GASOLINE_PRICE_ANALYSIS AS
SELECT 
    YEAR,
    COUNTRYNAME,
    PRICE,
    CURRENCY::FLOAT as price_value,
    ROUND(AVG(CURRENCY::FLOAT) OVER (ORDER BY YEAR ROWS BETWEEN 2 PRECEDING AND CURRENT ROW), 4) as moving_avg_3year,
    LAG(CURRENCY::FLOAT) OVER (ORDER BY YEAR) as prev_year_price,
    ROUND((CURRENCY::FLOAT - LAG(CURRENCY::FLOAT) OVER (ORDER BY YEAR)) / LAG(CURRENCY::FLOAT) OVER (ORDER BY YEAR) * 100, 2) as yoy_change_pct,
    CASE 
        WHEN CURRENCY::FLOAT > AVG(CURRENCY::FLOAT) OVER () THEN 'Above Average'
        WHEN CURRENCY::FLOAT < AVG(CURRENCY::FLOAT) OVER () THEN 'Below Average'
        ELSE 'Average'
    END as price_category
FROM "MY_ENERGY_DATABASE"."PUBLIC"."ENERGYDATA"
WHERE CURRENCY IS NOT NULL
ORDER BY YEAR;


-- ============================================
-- STEP 8: QUERY YOUR NEW VIEW
-- ============================================

SELECT * FROM GASOLINE_PRICE_ANALYSIS;