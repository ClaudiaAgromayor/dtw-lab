import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse
from pathlib import Path
import toml
from dtw_lab.lab1 import (
    read_csv_from_google_drive,
    visualize_data,
    calculate_statistic,
    clean_data,
)

# Initialize FastAPI application instance
# This creates our main application object that will handle all routing and middleware
app = FastAPI()

# Server deployment configuration function. We specify on what port we serve, and what IPs we listen to.
def run_server(port: int = 80, reload: bool = False, host: str = "127.0.0.1"):
    uvicorn.run("dtw_lab.lab2:app", port=port, reload=reload, host=host)

# Wrapper functions for script entry points
def run_server_dev():
    """Development server with hot reload on port 8000"""
    run_server(port=8000, reload=True)

def run_server_prod():
    """Production server on all interfaces"""
    run_server(reload=False, host='0.0.0.0')

# Define an entry point to our application.
@app.get("/")
def main_route():
    return {"message": "Hello world"}

@app.get("/statistic/{measure}/{column}")
def get_statistic(measure: str, column: str):
    # Read the CSV data, clean the data, and calculate the statistic.
    df = read_csv_from_google_drive("1eKiAZKbWTnrcGs3bqdhINo1E4rBBpglo")
    df = clean_data(df)
    return {f"The {measure} value for {column} is": calculate_statistic(measure, df[column])}
    

@app.get("/visualize/{graph_type}")
def get_visualization(graph_type: str):
    # Read the CSV data, clean the data, and visualize it.
    # This should create 3 files in the graphs folder.
    # Based on the graph_type input, return the corresponding image
    # HINT: Use FileResponse
    df = read_csv_from_google_drive("1eKiAZKbWTnrcGs3bqdhINo1E4rBBpglo")
    df = clean_data(df)
    visualize_data(df)
    return FileResponse(f"graphs/{graph_type}.png", media_type="image/png")

@app.get("/version")
def get_visualization_version():
    # Using the toml library, get the version field from the "pyproject.toml" file and return it.
    import toml
    with open("pyproject.toml", "r") as f:
        version = toml.load(f)["project"]["version"]
        return {"version": version}