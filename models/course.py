class Course:
    def __init__(self, course_id=None, date=None, time=None, location_=0, description=None, cost_=None
                 , grading_format=None, event_type=None, grade_required=None, urgent=False,
                 grade=None, work_justification=None, employee_id=None,
                 supervisor_approval=False, department_head_approval=False,
                 benco_approval=False):
        self.course_id = course_id
        self.date = date
        self.time = time
        self.location_ = location_
        self.description = description
        self.cost_ = cost_
        self.grading_format = grading_format
        self.event_type = event_type
        self.grade_required = grade_required
        self.urgent = urgent
        self.grade = grade
        self.work_justification = work_justification
        self.employee_id = employee_id
        self.supervisor_approval = supervisor_approval
        self.department_head_approval = department_head_approval
        self.benco_approval = benco_approval

    def json(self):
        return {
            'courseId': self.course_id,
            'date': str(self.date),
            'time': str(self.time),
            'location': self.location_,
            'description': self.description,
            'cost': str(self.cost_),
            'gradingFormat': self.grading_format,
            'eventType': self.event_type,
            'gradeRequired': self.grade_required,
            'urgent': self.urgent,
            'grade': self.grade,
            'workJustification': self.work_justification,
            'employeeId': self.employee_id,
            'departmentHeadApproval': self.department_head_approval,
            'supervisorApproval': self.supervisor_approval,
            'bencoApproval': self.benco_approval
        }

    @staticmethod
    def json_parse(json):
        course = Course()
        course.course_id = json["courseId"] if "courseId" in json else None
        course.date = json["date"] if "date" in json else None
        course.time = json["time"] if "time" in json else None
        course.location_ = json["location"] if "location" in json else None
        course.description = json["description"] if "description" in json else None
        course.cost_ = json["cost"] if "cost" in json else None
        course.grading_format = json["gradingFormat"] if "gradingFormat" in json else None
        course.event_type = json["eventType"] if "eventType" in json else None
        course.grade_required = json["gradeRequired"] if "gradeRequired" in json else None
        course.urgent = json["urgent"] if "urgent" in json else False
        course.work_justification = json["workJustification"] if "workJustification" in json else None
        course.employee_id = json["employeeId"] if "employeeId" in json else None
        course.department_head_approval = json["departmentHeadApproval"] if "departmentHeadApproval" in json else None
        course.supervisor_approval = json["supervisorApproval"] if "supervisorApproval" in json else None
        course.benco_approval = json["bencoApproval"] if "bencoApproval" in json else None

        return course
