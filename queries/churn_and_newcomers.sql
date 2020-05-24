-- =============================================
-- Returns, for each event, the last time a person responded the RSVP.
-- This could be interpreted as the last time this person had the intention to participate
-- in the meetup.
--
-- If `MAX` is replaced with `MIN` the fist time a person joined the meetup can be fetched.
-- =============================================

SELECT
  name,
  date,
  COUNT(*)
FROM
  (
    SELECT
      m.person_id,
      ms.name,
      ms.date
    FROM
      meetup_attendance m
      JOIN meetups ms ON m.meetup_id = ms.id
      JOIN people p on m.person_id = p.id
    GROUP BY
      m.person_id
    HAVING
      ms.date = MAX(ms.date) -- Replace with MIN to get the first time a person RSVP
  )
GROUP BY
  name
ORDER BY
  date asc