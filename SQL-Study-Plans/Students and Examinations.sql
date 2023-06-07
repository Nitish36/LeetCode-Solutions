Select 
  student.student_id, 
  student.student_name,
  subject.subject_name,
  count(exam.subject_name) as attended_exams
from Students student
join Subjects subject
left join Examinations exam
on student.student_id = exam.student_id 
  and subject.subject_name = exam.subject_name
group by student.student_id, subject.subject_name
order by student.student_id, subject.subject_name;
