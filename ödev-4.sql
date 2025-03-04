
use sýnýf

UPDATE dbo.ogrenciler
SET bolum = 'Hukuk'
WHERE id = 231015028;

SELECT * FROM ogrenciler

SELECT * FROM ogrenciler
WHERE bolum = 'Bilgisayar Mühendisliði';

SELECT * FROM ogrenciler
ORDER BY dogum_tarihi DESC;

SELECT * FROM dersler
INNER JOIN ogrenciler
ON dersler.bolum = ogrenciler.bolum;

SELECT ders_adi FROM dersler

SELECT ders_adi 
FROM dersler
WHERE bolum IN (SELECT bolum FROM ogrenciler WHERE ad = 'Ecem');

SELECT AVG(kredi) AS Ortalama
FROM dersler;

SELECT MAX(kredi) AS Maksimum
FROM dersler;

DELETE FROM ogrenciler
WHERE id = 231015023;

UPDATE dersler
SET ders_adi = 'OOP'
WHERE ders_id = 3;

select ders_adi from dersler