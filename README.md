# Interview Agent

An AI-powered interview agent that helps with interview preparation and practice.

## Prerequisites

- Python 3.8+
- Redis
- Virtual environment (recommended)

## Setup

1. Clone the repository
2. Create and activate a virtual environment:
   ```bash
   python -m venv myenv
   source myenv/bin/activate  # On Windows: myenv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Create a `.env` file with the following variables:
   ```
   REDIS_URL=redis://localhost:6379/0
   GEMINI_API_KEY=your_key_here
   CELERY_BROKER_URL=redis://localhost:6379/0
   CELERY_RESULT_BACKEND=redis://localhost:6379/0
   ```

## Running the Application

### Option 1: Using start.sh (Recommended for Development)

This script starts both Redis and Celery worker in the background:

```bash
# Make the script executable
chmod +x start.sh

# Run the start script
./start.sh
```

This will:
1. Activate the virtual environment
2. Start Redis server with secure configuration
3. Start the Celery worker

### Option 2: Using run.sh (For API Server)

This script starts the FastAPI server:

```bash
# Make the script executable
chmod +x run.sh

# Run the API server
./run.sh
```

This will:
1. Activate the virtual environment
2. Start the FastAPI server on http://localhost:8000

## API Usage

### 1. Create a New Interview Task

Send a POST request to create a new interview task:

```bash
curl -X POST http://localhost:8000/api/v1/interview \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "What are your strengths and weaknesses?"
  }'
```

Response:
```json
{
    "task_id": "123e4567-e89b-12d3-a456-426614174000",
    "status": "queued"
}
```

### 2. Get Task Result

Use the task_id from the previous response to check the status and get the result:

```bash
curl http://localhost:8000/api/v1/tasks/123e4567-e89b-12d3-a456-426614174000
```

Response:
```json
{
    "task_id": "123e4567-e89b-12d3-a456-426614174000",
    "status": "SUCCESS",
    "result": "Based on my experience..."
}
```

Possible status values:
- `queued`: Task is waiting to be processed
- `STARTED`: Task is being processed
- `SUCCESS`: Task completed successfully
- `FAILURE`: Task failed
- `PENDING`: Task is waiting to be picked up by a worker

## API Endpoints

- `POST /api/v1/interview`: Create a new interview task
  - Request body: `{"prompt": "your question here"}`
  - Returns: task_id and initial status
- `GET /api/v1/tasks/{task_id}`: Get the result of a specific task
  - Returns: task_id, current status, and result (if completed)

## Development

The application uses:
- FastAPI for the web server
- Celery for task queue
- Redis as message broker and result backend
- Google's Gemini AI for AI capabilities

## Security

- Redis is configured to run in protected mode
- All services are bound to localhost by default
- Environment variables are used for sensitive configuration 