SELECT 
    r.*,
    (SELECT count(*) 
        FROM hotel_booking 
        WHERE room_id = r.id) AS booking_count -- antal bokningar för varje rum
FROM
    hotel_room AS r