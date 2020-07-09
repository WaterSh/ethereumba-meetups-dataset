-- =============================================
-- Returns the amount of RSVP for each day and event
-- =============================================
SELECT
  name,
  date,
  rsvp_day,
  count(*) rsvp_per_day
FROM
  (
    SELECT
      meetup_id,
      meetups.name,
      meetups.date,
      strftime('%Y-%m-%d', rsvp_date) as rsvp_day
    FROM
      meetup_attendance
      JOIN meetups ON meetup_attendance.meetup_id = meetups.id
  )
GROUP BY
  meetup_id,
  rsvp_day
ORDER BY
  date,
  rsvp_day