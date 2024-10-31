-- 수원 지역, 연도 별 평균 미세먼지 오염도, 평균 초미세먼지 오염도, 소수 셋째 반올림
SELECT
    YEAR(YM) AS YEAR,
    ROUND(AVG(PM_VAL1), 2) AS PM10,
    ROUND(AVG(PM_VAL2), 2) AS `PM2.5`
FROM
    AIR_POLLUTION
WHERE
    LOCATION2 = '수원'
GROUP BY
    YEAR
ORDER BY
    YEAR ASC;