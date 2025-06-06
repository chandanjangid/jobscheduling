from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from flask import Flask, request, jsonify
import atexit

app = Flask(__name__)
scheduler = BackgroundScheduler()
scheduler.start()
atexit.register(lambda: scheduler.shutdown())

def hello_world(job_id):
    print(f"[{job_id}] Hello World")

@app.route('/schedule', methods=['POST'])
def schedule_job():
    data = request.json
    job_type = data.get('type')  # 'hourly', 'daily', 'weekly'
    job_id = data.get('job_id', f"job_{len(scheduler.get_jobs()) + 1}")

    try:
        if job_type == 'hourly':
            # e.g., {"type": "hourly", "minute": 30}
            trigger = CronTrigger(minute=data['minute'])

        elif job_type == 'daily':
            # e.g., {"type": "daily", "hour": 14, "minute": 0}
            trigger = CronTrigger(hour=data['hour'], minute=data['minute'])

        elif job_type == 'weekly':
            # e.g., {"type": "weekly", "day_of_week": "mon", "hour": 10, "minute": 0}
            trigger = CronTrigger(day_of_week=data['day_of_week'], hour=data['hour'], minute=data['minute'])

        else:
            return jsonify({"error": "Invalid job type"}), 400

        scheduler.add_job(hello_world, trigger, args=[job_id], id=job_id, replace_existing=True)
        return jsonify({"message": f"Job {job_id} scheduled successfully!"})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/jobs', methods=['GET'])
def list_jobs():
    jobs = scheduler.get_jobs()
    return jsonify([{
        "id": job.id,
        "next_run_time": str(job.next_run_time)
    } for job in jobs])

@app.route('/delete/<job_id>', methods=['DELETE'])
def delete_job(job_id):
    try:
        scheduler.remove_job(job_id)
        return jsonify({"message": f"Job {job_id} deleted successfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
