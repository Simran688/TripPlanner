# Deploying to Vercel

This guide will help you deploy the Travel Planner Streamlit app to Vercel.

## Prerequisites

1. A Vercel account (sign up at [vercel.com](https://vercel.com))
2. Git installed on your local machine
3. Node.js installed (for Vercel CLI)
4. Python 3.8+ installed

## Deployment Steps

### 1. Install Vercel CLI

```bash
npm install -g vercel
```

### 2. Login to Vercel

```bash
vercel login
```

### 3. Deploy the Application

From the root directory of the project, run:

```bash
vercel
```

Follow the prompts:
- Set up and deploy: `Y`
- Which scope: Select your account
- Link to existing project: `N`
- What's your project's name: `travel-planner` (or your preferred name)
- In which directory is your code located: `.`
- Want to override the settings: `N`

### 4. Set Up Environment Variables

If your application uses any environment variables (like API keys), set them in the Vercel dashboard:

1. Go to your project in the Vercel dashboard
2. Click on Settings > Environment Variables
3. Add your environment variables

### 5. Deploy

Vercel will automatically detect the project type and deploy it. Once deployed, you'll receive a URL where your app is live.

## Updating Your Deployment

To update your deployment after making changes:

```bash
git add .
git commit -m "Your commit message"
git push
vercel --prod
```

## Important Notes

1. **Streamlit on Vercel**: This setup uses a FastAPI wrapper to run Streamlit in a serverless environment. For production use, consider using Streamlit Cloud or a dedicated server for better performance.

2. **Environment Variables**: Make sure all required environment variables are set in your Vercel project settings.

3. **Dependencies**: All Python dependencies are listed in `requirements.txt` and will be installed automatically during deployment.

4. **File System Access**: Vercel has a read-only file system except for the `/tmp` directory. Make sure your app doesn't try to write to the file system.

## Troubleshooting

- If you encounter build errors, check the deployment logs in the Vercel dashboard
- Make sure all required files are included in your Git repository
- Check that all environment variables are properly set
- For Streamlit-specific issues, consult the [Streamlit documentation](https://docs.streamlit.io/)

## Alternative Deployment Options

If you encounter issues with Vercel, consider these alternatives:

1. **Streamlit Cloud**: Native hosting for Streamlit apps
2. **Heroku**: Another popular platform for Python applications
3. **AWS/GCP/Azure**: For more control and scalability
