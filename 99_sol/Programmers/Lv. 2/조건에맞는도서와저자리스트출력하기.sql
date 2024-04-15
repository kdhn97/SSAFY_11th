SELECT  BOOK.BOOK_ID, AUTHOR.AUTHOR_NAME, date_format(BOOK.PUBLISHED_DATE, '%Y-%m-%d')
FROM AUTHOR 
INNER JOIN BOOK 
ON BOOK.AUTHOR_ID = AUTHOR.AUTHOR_ID
WHERE BOOK.CATEGORY = '경제'
ORDER BY PUBLISHED_DATE;

-- < 풀이 >
-- SELECT 출력할 컬럼명 -> 이때 BOOK의 PUBLISHED_DATE는 ('yyyy-mm-dd' 형태로 출력하기)
-- FROM 테이블명
-- INNER JOIN 연결할 테이블
-- ON 연결하기 위한 공통된 값
-- WHERE 조건 -> '경제' 카테고리
-- ORDER BY 오름차순 정렬