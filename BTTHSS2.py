from fastapi import FastAPI, HTTPException
courses = [
    {
        "id": 1,
        "code": "PY101",
        "name": "Python Basic",
        "level": "beginner",
        "price": 1500000
    },
    {
        "id": 2,
        "code": "FA101",
        "name": "FastAPI Basic",
        "level": "beginner",
        "price": 2000000
    }
]
app = FastAPI()
@app.get("/health")
def get_health():
    return {"message":"API is running"}
@app.get("/courses")
def list_courses():
    return {"message":"Danh sách tất cả khóa học",
            "data": courses}
@app.get("/courses/{course_id}")
def get_course_id(course_id: int):
    if course_id <= 0:
        raise HTTPException(
            status_code=400,
            detail="course_id phải lớn hơn 0"
        )
    for course in courses:
        if course["id"] == course_id:
            return {
                "message": "Tìm thấy khóa học",
                "data": course
            }
    raise HTTPException(
        status_code=404,
        detail="Không tìm thấy khóa học"
    )