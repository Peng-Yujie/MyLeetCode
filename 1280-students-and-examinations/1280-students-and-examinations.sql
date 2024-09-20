/* Write your T-SQL query statement below */
SELECT stu.student_id, stu.student_name, sub.subject_name, COUNT(exam.subject_name) AS attended_exams
FROM Students stu
CROSS JOIN Subjects sub
LEFT JOIN Examinations exam
    ON exam.student_id = stu.student_id AND sub.subject_name = exam.subject_name
GROUP BY stu.student_id, stu.student_name, sub.subject_name
ORDER BY stu.student_id, sub.subject_name