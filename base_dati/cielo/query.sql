begin transaction;

select codice, comp
from Volo
where durataMinuti >= 180;

select distinct comp
from Volo
where durataMinuti >= 180;

select codice, comp
from ArrPart
where partenza = 'CIA';

select distinct comp
from ArrPart
where arrivo = 'FCO';

select codice, comp
from ArrPart
where partenza = 'FCO' and arrivo = 'JFK';

select distinct comp
from ArrPart
where partenza = 'FCO' and arrivo = 'JFK';

--Quali sono i nomi delle compagnie che hanno voli diretti dalla città di ‘Roma’ alla città di ‘New York’ ?

select distinct Volo.comp
from Volo
join  ArrPart on Volo.codice = ArrPart.codice and Volo.comp  = ArrPart.comp
join LuogoAeroporto L1 on  ArrPart.partenza = L1.aeroporto
join LuogoAeroporto L2 on   ArrPart.arrivo = L2.aeroporto
where L1.citta = 'Roma' and L2.citta = 'New York';

--Quali sono gli aeroporti (con codice IATA, nome e luogo) nei quali partono voli della compagnia di nome ‘MagicFly’ ?

SELECT DISTINCT LuogoAeroporto.aeroporto, Aeroporto.nome, LuogoAeroporto.citta
FROM LuogoAeroporto
JOIN Aeroporto ON LuogoAeroporto.aeroporto = Aeroporto.codice
JOIN ArrPart ON Aeroporto.codice = ArrPart.partenza
JOIN Volo ON ArrPart.codice = Volo.codice AND ArrPart.comp = Volo.comp
WHERE Volo.comp = 'MagicFly';

--9. Quali sono i voli che partono da un qualunque aeroporto della città di ‘Roma’ e atterrano ad un qualunque aeroporto della città di ‘New York’ ? Restituire: codice del volo, nome della compagnia, e aeroporti di partenza e arrivo.

SELECT DISTINCT Volo.codice, Volo.comp, ArrPart.partenza, ArrPart.arrivo
FROM Volo
JOIN ArrPart ON Volo.codice = ArrPart.codice AND Volo.comp = ArrPart.comp
JOIN LuogoAeroporto L1 ON ArrPart.partenza = L1.aeroporto
JOIN LuogoAeroporto L2 ON ArrPart.arrivo = L2.aeroporto
WHERE L1.citta = 'Roma' AND L2.citta = 'New York';

--10. Quali sono i possibili piani di volo con esattamente un cambio (utilizzando solo voli della stessa compagnia) da un qualunque aeroporto della città di ‘Roma’ ad un qualunque aeroporto della città di ‘New York’ ? Restituire: nome della compagnia, codici dei voli, e aeroporti di partenza, scalo e arrivo.

SELECT DISTINCT V1.comp, V1.codice, V2.codice, L1.citta, L2.citta, L3.citta
FROM Volo V1
JOIN ArrPart A1 ON V1.codice = A1.codice AND V1.comp = A1.comp
JOIN LuogoAeroporto L1 ON A1.partenza = L1.aeroporto
JOIN Volo V2 ON V1.comp = V2.comp AND V2.partenza = A1.arrivo
JOIN ArrPart A2 ON V2.codice = A2.codice AND V2.comp = A2.comp
JOIN LuogoAeroporto L2 ON A2.partenza = L2.aeroporto
JOIN LuogoAeroporto L3 ON A2.arrivo = L3.aeroporto
WHERE L1.citta = 'Roma' AND L3.citta = 'New York';

--11. Quali sono le compagnie che hanno voli che partono dall’aeroporto ‘FCO’, atterrano all’aeroporto ‘JFK’, e di cui si conosce l’anno di fondazione?

SELECT DISTINCT V.comp
FROM Volo V
JOIN ArrPart A ON V.codice = A.codice AND V.comp = A.comp
JOIN Compagnia C ON V.comp = C.nome
WHERE A.partenza = 'FCO' AND A.arrivo = 'JFK' AND C.annoFondaz IS NOT NULL;

--1. Quante sono le compagnie che operano (sia in arrivo che in partenza) nei diversi aeroporti?

select a.codice, a.nome, count(distinct comp)
from aeroporto a, ArrPart ap
where ap.partenza = a.codice or ap.arrivo = a.codice
group by a.codice, a.nome;

--2. Quanti sono i voli che partono dall’aeroporto ‘HTR’ e hanno una durata di almeno 100 minuti?

select count(*) as numeroVoli
from volo v, ArrPart ap
where v.codice = ap.codice and ap.partenza =  'HTR' and v.durataMinuti >= 100;

--3. Quanti sono gli aeroporti sui quali opera la compagnia ‘Apitalia’, per ogni nazione
--nella quale opera?

select la.nazione, count(distinct aeroporto)
from LuogoAeroporto la, ArrPart ap
where (ap.partenza = la.aeroporto or ap.arrivo = la.aeroporto) and ap.comp = 'Apitalia'
group by la.nazione;

--4. Qual è la media, il massimo e il minimo della durata dei voli effettuati dalla
--compagnia ‘MagicFly’ ?

select  round(avg(durataMinuti),2) as media, max(durataMinuti) as max, min(durataMinuti) as min
from volo v
where comp = 'MagicFly';

--5. Qual è l’anno di fondazione della compagnia più vecchia che opera in ognuno degli
--aeroporti?

select  a.codice, a.nome, min(c.annoFondaz)
from aeroporto a, compagnia c, ArrPart ap
where (a.codice = ap.arrivo or a.codice = ap.partenza) and ap.comp = c.nome
group by a.codice, a.nome;

--6. Quante sono le nazioni (diverse) raggiungibili da ogni nazione tramite uno o più
--voli?

select lp.nazione, count(distinct la.nazione)
from ArrPart ap, LuogoAeroporto lp, LuogoAeroporto la
where ap.partenza = lp.aeroporto and ap.arrivo = la.aeroporto
group by lp.nazione;

--7. Qual è la durata media dei voli che partono da ognuno degli aeroporti?



--8. Qual è la durata complessiva dei voli operati da ognuna delle compagnie fondate
--a partire dal 1950?



--9. Quali sono gli aeroporti nei quali operano esattamente due compagnie?



--10. Quali sono le città con almeno due aeroporti?



--11. Qual è il nome delle compagnie i cui voli hanno una durata media maggiore di 6
--ore?



--12. Qual è il nome delle compagnie i cui voli hanno tutti una durata maggiore di 100
--minuti?