/* 2023-03-21 */

SELECT T1.BOOK_ID, T2.AUTHOR_NAME, TO_CHAR(T1.PUBLISHED_DATE,'YYYY-MM-DD')
FROM BOOK T1
    , AUTHOR T2
WHERE T1.CATEGORY = '경제'
    AND T1.AUTHOR_ID = T2.AUTHOR_ID
ORDER BY T1.PUBLISHED_DATE

-- JOIN 사용
SELECT T1.BOOK_ID, T2.AUTHOR_NAME, TO_CHAR(T1.PUBLISHED_DATE,'YYYY-MM-DD')
FROM BOOK T1
INNER JOIN AUTHOR T2
ON T1.AUTHOR_ID = T2.AUTHOR_ID
WHERE T1.CATEGORY = '경제'
ORDER BY T1.PUBLISHED_DATE