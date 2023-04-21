
/**
* INNER JOIN
**/
SELECT
    b.id,
    b.startdate,
    b.guest_id,
    b.info AS booking_info,
    r.room_number,
    r.size AS room_size,
    g.firstname || ' ' || g.lastname AS guest_name -- konkatenering med ||
FROM
    hotel_booking AS b -- b = alias för hotel_booking
INNER JOIN
    hotel_room AS r
    ON b.room_id = r.id 
INNER JOIN
    hotel_guest AS g
    ON b.guest_id = g.id
ORDER BY b.startdate DESC;

/**
* LEFT JOIN
**/
SELECT
    g.id,
    g.firstname,
    b.startdate,
    b.room_id
FROM
    hotel_guest g
LEFT JOIN -- Tar med också rader som inte matchar joinen
    hotel_booking b
ON g.id = b.guest_id
ORDER by g.firstname