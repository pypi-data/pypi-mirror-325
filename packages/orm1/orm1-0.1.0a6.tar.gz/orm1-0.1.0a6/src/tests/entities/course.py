from dataclasses import dataclass
from datetime import datetime
from orm1 import auto


@auto.mapped(primary_key=("semester_id", "subject_id"))
@dataclass(eq=False)
class Course:
    semester_id: str
    subject_id: str
    created_at: datetime
    modules: list["CourseModule"]
    attachments: list["CourseAttachment"]


@auto.mapped(parental_key=("course_semester_id", "course_subject_id"))
@dataclass(eq=False)
class CourseAttachment:
    id: str
    media_uri: str
    created_at: datetime
    course_semester_id: str | None = None
    course_subject_id: str | None = None


@auto.mapped(parental_key=("course_semester_id", "course_subject_id"))
@dataclass(eq=False)
class CourseModule:
    id: str
    title: str
    created_at: datetime
    materials: list["CourseModuleMaterial"]
    course_semester_id: str | None = None
    course_subject_id: str | None = None


@auto.mapped(parental_key="course_module_id")
@dataclass(eq=False)
class CourseModuleMaterial:
    id: str
    media_uri: str
    created_at: datetime
    course_module_id: str | None = None
