SELECT 
    cc.CAR_ID, 
    cc.CAR_TYPE, 
    ROUND(cc.DAILY_FEE * (1 - dp.DISCOUNT_RATE / 100) * 30) AS FEE
FROM 
    CAR_RENTAL_COMPANY_CAR cc
INNER JOIN 
    CAR_RENTAL_COMPANY_DISCOUNT_PLAN dp 
ON 
    cc.CAR_TYPE = dp.CAR_TYPE 
    AND dp.DURATION_TYPE = '30일 이상' -- 30일 이상 대여 시 할인 정책만 적용
WHERE 
    cc.CAR_TYPE IN ('세단', 'SUV') -- 자동차 종류가 세단 또는 SUV
    AND cc.CAR_ID NOT IN (
        -- 대여 기간이 2022-11-01 ~ 2022-11-30과 겹치는 자동차 ID를 조회
        SELECT CAR_ID
        FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
        WHERE 
            (START_DATE BETWEEN '2022-11-01' AND '2022-11-30')
            OR (END_DATE BETWEEN '2022-11-01' AND '2022-11-30')
            OR (START_DATE <= '2022-11-01' AND END_DATE >= '2022-11-30')
    )
GROUP BY 
    cc.CAR_ID, cc.CAR_TYPE, FEE
HAVING 
    FEE >= 500000 AND FEE < 2000000 -- 대여 금액이 500,000원 이상, 2,000,000원 미만
ORDER BY 
    FEE DESC, cc.CAR_TYPE ASC, cc.CAR_ID DESC;
