from fastapi import FastAPI

app = FastAPI(
	title="AI Job Matcher API",
	description="API for analyzing resumes and matching candidates with job descriptions.",
	version="0.1.0",
)


@app.get("/")
def root():
	return {
		"message": "AI Job Matcher API is running",
		"version": "0.1.0",
	}


@app.get("/health")
def health_check():
	return {
		"status": "healthy"
	}
