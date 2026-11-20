# DevOps Platform

[![DevOps Platform CI](https://github.com/Tarunk1099/devops-platform/actions/workflows/ci.yml/badge.svg)](https://github.com/Tarunk1099/devops-platform/actions/workflows/ci.yml)

A deployment-management API built to practice and demonstrate professional Git and GitHub workflows.

## Project Overview

DevOps Platform is a lightweight deployment-management API built with FastAPI.

The current focus is practicing professional Git and GitHub collaboration workflows, repository management, pull requests, code review practices, and CI automation.

## Git & GitHub Project Checklist

- [x] Create application repository
- [x] Initialize Git repository
- [x] Initial commit
- [x] Create GitHub repository
- [x] Push local repository to GitHub
- [x] README documentation
- [x] .gitignore configuration
- [x] Branch creation and management
- [x] Feature branch workflow
- [x] Commit conventions
- [x] Push feature branches
- [x] Pull Requests
- [x] Merge Pull Requests
- [x] Merge conflicts practice
- [x] Remote and local branch management
- [x] git fetch / pull / merge practice
- [x] CONTRIBUTING.md
- [x] Pull Request template
- [x] Issue template
- [x] GitHub Actions workflow
- [x] Automated API tests in CI
- [x] CI failure testing
- [x] CI recovery verification
- [x] Branch ruleset / protection
- [ ] Final repository review
- [ ] Final Git/GitHub project completion

## Tech Stack

- Git
- GitHub
- GitHub Actions
- Python
- FastAPI
- Pytest

## Running Locally

Clone the repository:

    git clone https://github.com/Tarunk1099/devops-platform.git

Navigate into the project:

    cd devops-platform

Create a virtual environment:

    python3 -m venv venv

Activate it:

    source venv/bin/activate

Install dependencies:

    pip install -r requirements.txt

Run the application:

    uvicorn app:app --reload

API documentation:

    http://127.0.0.1:8000/docs

## Running Tests

    pytest -v

## Project Objective

Practice professional Git and GitHub workflows through a hands-on project, including branching, commits, pull requests, repository collaboration practices, and automated CI validation.
