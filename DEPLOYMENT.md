# Deployment Guide

## Required GitHub Secrets

Add these repository secrets before running the workflow:

- `SSH_HOST`
- `SSH_USER`
- `SSH_PRIVATE_KEY`
- `SSH_PORT`
- `GHCR_USERNAME`
- `GHCR_TOKEN`
- `APP_CONTAINER_NAME`

## Workflow Behavior

The `deploy.yml` workflow does two jobs:

1. Build and push Docker image to `ghcr.io`.
2. Connect over SSH and deploy the new image on the server.

## Trigger

Deployment runs on:

- Push to `main`
- Manual run (`workflow_dispatch`)
