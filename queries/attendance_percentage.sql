-- =============================================
-- Returns users AVG attendance
-- =============================================
SELECT
  AVG(percentage)
FROM
  (
    SELECT
      person_id,
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
    GROUP BY
      person_id
  )