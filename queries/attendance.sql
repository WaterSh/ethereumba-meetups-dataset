-- =============================================
-- Returns the amount of people responded yes to a RSVP 
-- and the attendees for each meetup
-- =============================================
SELECT
  meetups.name,
  meetups.date,
  COUNT(*) as subscribed, 
  unknown_attendees + SUM(CASE WHEN attended THEN 1 ELSE 0 END) as attendees
FROM
  meetup_attendance
  JOIN meetups ON meetup_attendance.meetup_id = meetups.id
GROUP BY
  meetup_id
ORDER BY
  meetups.date ASC