-- 01. Querying data
  -- 테이블 employees에서 LastName 필드의 모든 데이터 조회
SELECT LastName FROM employees;
  -- 테이블 employees에서 LastName, FirstName 필드의 모든 데이터 조회
SELECT LastName, FirstName FROM employees;
  -- 테이블 employees에서 모든 필드 데이터를 조회
SELECT * FROM employees;
  -- 테이블 employees에서 FirstName 필드의 모든 데이터 조회 ( 조회 시 '이름'으로 출력 )
SELECT FirstName AS '이름' FROM employees;
  -- 테이블 tracks에서 Name, Milliseconds 필드의 모든 데이터 조회 ( 60000으로 나눠 분 단위 )
SELECT Name, Milliseconds / 60000 AS '재생 시간(분)' FROM tracks;

-- 02. Sorting data
  -- 테이블 employees에서 FirstName 필드의 모든 데이터를 오름차순으로 조회
  SELECT FirstName FROM employees ORDER BY FirstName;
  -- 테이블 employees에서 FirstName 필드의 모든 데이터를 내림차순으로 조회
  SELECT FirstName FROM employees ORDER BY FirstName DESC;
  -- Country 필드를 기준으로 내림차순 정렬한 다음 City 필드 기준으로 오름차순 정렬하여 조회
  SELECT Country, City FROM customers ORDER BY Country DESC, City;
  -- Milliseconds 필드를 기준으로 내림차순 정렬한 다음 Name, Milliseconds 필드의 모든 데이터 조회
  SELECT Name, Milliseconds / 60000 AS '재생 시간(분)' FROM tracks ORDER BY Milliseconds DESC;

-- NULL 정렬 예시
  -- NULL 값이 존재할 경우 오름차순 정렬 시 결과에 NULL이 먼저 출력
  SELECT ReportsTo FROM employees ORDER BY ReportsTo;


-- 03. Filtering data
  -- < DISTINCT >
  -- 테이블 customers에서 Country 필드의 모든 데이터를 중복없이 오름차순 조회
  SELECT DISTINCT Country FROM customers ORDER BY Country;

  -- < WHERE >
  -- 테이블 customers에서 City 필드 값이 Prague인 데이터의 LastName, FirstName, City 조회
  SELECT LastName, FirstName, City FROM customers WHERE City = 'Prague';
  -- 테이블 customers에서 City 필드 값이 'Prague'가 아닌 데이터의 LastName, FirstName, City 조회
  SELECT LastName, FirstName, City FROM customers WHERE City != 'Prague';
  -- Company 필드 값이 NULL이고 'USA'인 데이터의 LastName, FirstName, Company, Country 조회
  SELECT LastName, FirstName, Company, Country 
  FROM customers WHERE Company IS NULL AND Country = 'USA';
  -- Company 필드 값이 NULL이거나 'USA'인 데이터의 LastName, FirstName, Company, Country 조회
  SELECT LastName, FirstName, Company, Country 
  FROM customers WHERE Company IS NULL OR Country = 'USA';
  -- 테이블 track에서 Bytes 필드 값이 100,000 이상 500,000 이하인 데이터의 Name, Bytes 조회
  SELECT Name, Bytes FROM tracks WHERE Bytes BETWEEN 100000 AND 500000;
  -- Country 필드 값이 'Canada'또는 'Germany'또는 'France'인 LastName, FirstName, Country 조회
  SELECT LastName, FirstName, Country FROM customers
  WHERE Country IN ('Canada', 'Germany', 'France');
  -- Country 필드 값이 'Canada'또는 'Germany'또는 'France'가 아닌 LastName, FirstName, Country 조회
  SELECT LastName, FirstName, Country FROM customers
  WHERE Country NOT IN ('Canada', 'Germany', 'France');
  -- LastName 필드 값이 'son'으로 끝나는 데이터의 LastName, FirstName 조회
  SELECT LastName, FirstName FROM customers WHERE LastName LIKE '%son';
  -- FirstName 필드 값이 4자리면서 'a'로 끝나는 데이터의 LastName, FirstName 조회
  SELECT LastName, FirstName FROM customers WHERE FirstName LIKE '___a';

  -- < LIMIT >
  -- 테이블 tracks에서 TrackId, Name, Bytes 필드 데이터를 Bytes 기준 내림차순으로 7개만 조회
  SELECT TrackId, Name, Bytes From tracks ORDER BY Bytes DESC LIMIT 7;
  -- TrackId, Name, Bytes 필드 데이터를 Bytes 기준 내림차순으로 4번째부터 7번째 데이터만 조회
  SELECT TrackId, Name, Bytes From tracks ORDER BY Bytes DESC LIMIT 3, 4;

-- 04. Grouping data
  -- 테이블 tracks에서 Composer 필드를 그룹화하여 각 그룹에 대한 Bytes의 평균 값을 내림차순 조회
  SELECT Composer, AVG(Bytes) FROM tracks GROUP BY Composer ORDER BY AVG(Bytes) DESC;
  -- Composer 필드를 그룹화하여 각 그룹에 대한 Millisseconds의 평균 값이 10 미만인 데이터 조회
  --> HAVING : 집계 항목에 대한 세부 조건을 지정
  SELECT Composer, AVG(Milliseconds / 60000) AS avg0fMinute
  FROM tracks GROUP BY Composer HAVING avg0fMinute < 10;

  