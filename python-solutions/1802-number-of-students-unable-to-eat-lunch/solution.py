class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        student_counts = [students.count(0),students.count(1)]

        for sandwich in sandwiches:
            if student_counts[sandwich] > 0:
                student_counts[sandwich] -= 1
            else:
                break
        return student_counts[0] + student_counts[1]
        
            
