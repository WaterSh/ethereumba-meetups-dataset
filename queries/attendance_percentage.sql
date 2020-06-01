-- =============================================
-- Returns users AVG attendance 
-- =============================================
SELECT
  AVG(percentage)
FROM
  (
    SELECT
      ethba_user_id,
      COUNT(*) subscriptions,
      SUM(
        CASE
          WHEN attended THEN 1
          ELSE 0
        END
      ) * 100 / COUNT(*) as percentage
    FROM
      meetup_attendance
    WHERE
      meetup_id IN (13, 14, 15) -- FIXME: We just have this data as of now
      AND rsvp = 1 -- We only want to count people that RSVP yes
    GROUP BY
      ethba_user_id
  )