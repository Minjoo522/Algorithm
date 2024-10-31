SELECT
    i.ID,
    n.FISH_NAME,
    i.LENGTH
FROM
    FISH_INFO i
INNER JOIN
    FISH_NAME_INFO n
ON
    i.FISH_TYPE = n.FISH_TYPE
WHERE
    i.LENGTH = (
        SELECT MAX(i2.LENGTH)
        FROM FISH_INFO i2
        WHERE i2.FISH_TYPE = i.FISH_TYPE
    )
ORDER BY
    i.ID ASC;