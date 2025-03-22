# Activate the virtual environment
source interview_agent_env/bin/activate

# Terminal 1: Start Redis with configuration
redis-server redis.conf &

# Terminal 2: Start Celery worker
celery -A celery_config worker --loglevel=info
