SELECT
    i.ANIMAL_ID,
    i.NAME
FROM
    ANIMAL_INS i
INNER JOIN
    ANIMAL_OUTS o
ON
    i.ANIMAL_ID = o.ANIMAL_ID
WHERE
    TIMEDIFF(o.DATETIME, i.DATETIME) < 0
ORDER BY
    i.DATETIME ASC;