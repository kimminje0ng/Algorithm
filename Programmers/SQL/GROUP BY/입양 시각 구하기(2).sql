-- 변수 선언 : SET @변수명 := 변수값;
-- 반복문 : SELECT 안에 index++하면서 WHERE에 break 조건.
--          SELECT 안에 실행문 넣기
SET @HOUR := -1;

SELECT (@HOUR := @HOUR+1), (SELECT COUNT(*)
                            FROM ANIMAL_OUTS
                            WHERE HOUR(DATETIME) = @HOUR)
FROM ANIMAL_OUTS 
WHERE @HOUR < 23;


-- [Recursive]
-- WITH RECURSIVE 함수명 AS (실행내용) : 반복문 대용으로 사용하는 recursive문
-- LEFT JOIN : 
WITH RECURSIVE PLS AS (SELECT 0 AS NHOUR
                      UNION ALL
                      SELECT NHOUR+1
                      FROM PLS
                      WHERE NHOUR < 23)

SELECT NHOUR, COUNT(HOUR(DATETIME))
FROM PLS
LEFT JOIN ANIMAL_OUTS
ON NHOUR = HOUR(DATETIME)
GROUP BY NHOUR
ORDER BY NHOUR;


-- AS 사용
WITH RECURSIVE PLS AS (SELECT 0 AS HOUR
                      UNION ALL
                      SELECT HOUR+1
                      FROM PLS
                      WHERE HOUR < 23)

SELECT PLS.HOUR, COUNT(HOUR(ANIMAL_OUTS.DATETIME))
FROM PLS
LEFT JOIN ANIMAL_OUTS
ON PLS.HOUR = HOUR(ANIMAL_OUTS.DATETIME)
GROUP BY PLS.HOUR
ORDER BY PLS.HOUR;