from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import uuid
from datetime import datetime


app = FastAPI(title="DevOps Platform API", version="1.0.0")

deployments = {}


# --------------------------------------------------
# BASIC APPLICATION ENDPOINTS
# --------------------------------------------------

@app.get("/")
def home():
    return {
        "message": "DevOps Platform is running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.get("/info")
def info():
    return {
        "project": "DevOps Platform",
        "version": "1.0.0",
        "status": "running"
    }


# --------------------------------------------------
# DATA MODELS
# --------------------------------------------------

class Deployment(BaseModel):
    application: str
    environment: str
    version: str


class DeploymentStatus(BaseModel):
    status: str = Field(pattern="^(RUNNING|SUCCESS|FAILED)$")


class DeploymentResponse(BaseModel):
    deployment_id: str
    application: str
    environment: str
    version: str
    status: str
    created_at: datetime
    updated_at: datetime


# --------------------------------------------------
# CREATE DEPLOYMENT
# --------------------------------------------------

@app.post("/deploy", response_model=DeploymentResponse)
def deploy(deployment: Deployment):

    deployment_id = str(uuid.uuid4())
    now = datetime.now()

    deployments[deployment_id] = {
        "deployment_id": deployment_id,
        "application": deployment.application,
        "environment": deployment.environment,
        "version": deployment.version,
        "status": "RUNNING",
        "created_at": now,
        "updated_at": now
    }

    return deployments[deployment_id]


# --------------------------------------------------
# UPDATE DEPLOYMENT STATUS
# --------------------------------------------------

@app.put(
    "/deploy/{deployment_id}/status",
    response_model=DeploymentResponse
)
def update_status(
    deployment_id: str,
    status: DeploymentStatus
):

    if deployment_id not in deployments:
        raise HTTPException(
            status_code=404,
            detail="Deployment not found"
        )

    if deployments[deployment_id]["status"] != "RUNNING":
        raise HTTPException(
            status_code=409,
            detail="Deployment has already completed"
        )

    deployments[deployment_id]["status"] = status.status
    deployments[deployment_id]["updated_at"] = datetime.now()

    return deployments[deployment_id]


# --------------------------------------------------
# GET SINGLE DEPLOYMENT
# --------------------------------------------------

@app.get(
    "/deploy/{deployment_id}",
    response_model=DeploymentResponse
)
def get_deployment(deployment_id: str):

    if deployment_id not in deployments:
        raise HTTPException(
            status_code=404,
            detail="Deployment not found"
        )

    return deployments[deployment_id]


# --------------------------------------------------
# GET ALL DEPLOYMENTS
# --------------------------------------------------

@app.get("/deployments")
def get_deployments():
    return deployments


# --------------------------------------------------
# DELETE DEPLOYMENT
# --------------------------------------------------

@app.delete("/deploy/{deployment_id}")
def delete_deployment(deployment_id: str):

    if deployment_id not in deployments:
        raise HTTPException(
            status_code=404,
            detail="Deployment not found"
        )

    deleted_deployment = deployments.pop(deployment_id)

    return {
        "message": "Deployment deleted",
        "deployment_id": deployment_id,
        "application": deleted_deployment["application"]
    }
