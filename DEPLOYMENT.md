# AI Trip Planner - Deployment Guide

This guide explains how to deploy the AI Trip Planner application to production.

## Prerequisites

- Node.js 16+ and npm 7+
- Python 3.9+
- Git
- Render.com account (or your preferred hosting provider)

## Backend Deployment

1. **Prepare Environment Variables**
   - Copy `.env.example` to `.env` in the backend directory
   - Update the values with your production configuration

2. **Deploy to Render**
   - Push your code to a Git repository
   - Go to [Render Dashboard](https://dashboard.render.com/)
   - Click "New" → "Web Service"
   - Connect your Git repository
   - Configure the service:
     - Name: `ai-trip-planner-backend`
     - Region: Choose closest to your users
     - Branch: `main` or your production branch
     - Runtime: Python 3
     - Build Command: `pip install -r requirements.txt`
     - Start Command: `gunicorn main:app --worker-class uvicorn.workers.UvicornWorker`
   - Add environment variables from your `.env` file
   - Click "Create Web Service"

## Frontend Deployment

1. **Prepare Environment Variables**
   - Copy `.env.example` to `.env.production` in the frontend directory
   - Update `VITE_API_URL` with your production backend URL
   - Set `NODE_ENV=production`

2. **Build the Application**
   ```bash
   cd frontend
   npm install
   npm run build
   ```

3. **Deploy to Render**
   - Go to [Render Dashboard](https://dashboard.render.com/)
   - Click "New" → "Static Site"
   - Connect your Git repository
   - Configure the site:
     - Name: `ai-trip-planner-frontend`
     - Branch: `main` or your production branch
     - Build Command: `npm install && npm run build`
     - Publish Directory: `dist`
   - Add environment variables from `.env.production`
   - Click "Create Static Site"

## Environment Variables

### Backend (.env)
```
# Required
PORT=8000
PYTHONUNBUFFERED=1

# Database
DATABASE_URL=postgresql://user:password@host:port/dbname

# Authentication
SECRET_KEY=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=1440

# External Services
OPENAI_API_KEY=your-openai-key
GOOGLE_MAPS_API_KEY=your-google-maps-key
```

### Frontend (.env.production)
```
VITE_API_URL=https://your-backend-url.onrender.com
NODE_ENV=production
VITE_APP_NAME="AI Trip Planner"
```

## Post-Deployment

1. **Verify the Deployment**
   - Check both frontend and backend logs in Render dashboard
   - Test the API endpoints using Postman or curl
   - Test the frontend UI and ensure it connects to the backend

2. **Set Up Monitoring**
   - Configure error tracking (e.g., Sentry)
   - Set up logging and monitoring
   - Configure alerts for errors and performance issues

3. **Set Up CI/CD (Optional)**
   - Configure GitHub Actions or similar for automated testing and deployment
   - Set up staging and production environments
   - Implement blue-green deployment for zero-downtime updates

## Troubleshooting

- **Frontend not loading**: Check the browser console for errors
- **API connection issues**: Verify CORS settings and network connectivity
- **Build failures**: Check the build logs in Render dashboard
- **Environment variables**: Ensure all required variables are set in production

## Maintenance

- Keep dependencies updated
- Regularly backup your database
- Monitor performance and optimize as needed
- Follow security best practices
