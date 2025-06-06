# 1. Schedule Hourly Job
# POST http://127.0.0.1:5000/schedule
#
# JSON BODY
# {
#   "type": "hourly",
#   "minute": 15,
#   "job_id": "hourly_job"
# }

# 2. Schedule Daily Job
# URL:
# POST http://127.0.0.1:5000/schedule
#
# JSON Body:
#
# {
#   "type": "daily",
#   "hour": 14,
#   "minute": 30,
#   "job_id": "daily_job"
# }
# This runs the job every day at 2:30 PM.

# 3. Schedule Weekly Job
# URL:
# POST http://127.0.0.1:5000/schedule
#
#  JSON Body:
# {
#   "type": "weekly",
#   "day_of_week": "wed",
#   "hour": 10,
#   "minute": 0,
#   "job_id": "weekly_job"
# }
#  This runs the job every Wednesday at 10:00 AM.
