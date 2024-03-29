-- WHERE * IN (*) : 해당 조건에 일치하면 출력
-- Cat이 먼저 나오게 정렬 : GROUP BY

SELECT ANIMAL_TYPE, COUNT(*)
FROM ANIMAL_INS
WHERE ANIMAL_TYPE IN ('Cat', 'Dog')
GROUP BY ANIMAL_TYPE
ORDER BY ANIMAL_TYPE;
