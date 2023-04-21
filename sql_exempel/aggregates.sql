/**
* min(), max()
**/

SELECT
    g.id,
    g.firstname,
    min(b.startdate) as first_visit, -- Gästens första besök i vårt hotell
    max(b.startdate) as last_visit -- Gästens senaste besök i vårt hotell
FROM
    hotel_guest g
INNER JOIN 
    hotel_booking b
ON g.id = b.guest_id

GROUP BY g.id -- Gruppera aggregatfunktionen enligt gäst

ORDER by g.firstname

/**
* count()
**/

SELECT 
    room_id,
    count(*) AS bookings_count
FROM
    hotel_booking
GROUP BY room_id
