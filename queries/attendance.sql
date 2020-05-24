-- =============================================
-- Returns the amount of people responded yes to a RSVP for each meetup
-- =============================================
SELECT
  meetups.name,
  meetups.date,
  COUNT(*) as subscribed
FROM
  meetup_attendance
  JOIN meetups ON meetup_attendance.meetup_id = meetups.id
GROUP BY
  meetup_id
ORDER BY
  meetups.date ASC