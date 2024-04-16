-- 정답
SELECT MCDP_CD AS '진료과코드', COUNT(*) AS '5월예약건수' 
FROM APPOINTMENT 
WHERE APNT_YMD LIKE '2022-05-%'
GROUP BY MCDP_CD
ORDER BY COUNT(*), MCDP_CD;
ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
-- 설명
-- SELECT 해당 필드에서 조회 AS '컬럼명 지정'
-- FROM 해당 테이블에서 조회
-- WHERE 해당 필드에서 LIKE '해당 문자를 가진 정보를 조회'
-- GROUP BY 해당 필드별로 그룹화 시켜서 조회
-- ORDER BY 오름차순으로 정렬