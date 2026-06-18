-- ==========================================
-- STORED PROCEDURE
-- Calculate Total Working Hours
-- ==========================================

USE employee_tracker;

DELIMITER //

CREATE PROCEDURE CalculateWorkingHours(
    IN empid INT
)
BEGIN

    SELECT
        employee_id,

        ROUND(
            SUM(
                TIMESTAMPDIFF(
                    MINUTE,
                    clock_in,
                    clock_out
                ) / 60
            ),
            2
        ) AS total_working_hours

    FROM attendance

    WHERE employee_id = empid
      AND clock_in IS NOT NULL
      AND clock_out IS NOT NULL

    GROUP BY employee_id;

END //

DELIMITER ;

-- ==========================================
-- EXECUTE PROCEDURE
-- ==========================================

CALL CalculateWorkingHours(1);
