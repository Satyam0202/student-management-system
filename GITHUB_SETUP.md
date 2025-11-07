# 📦 GitHub Setup Guide

This guide will help you upload your Student Management System to GitHub.

## Prerequisites

- Git installed on your computer
- GitHub account created
- Project files ready

## Step-by-Step Instructions

### 1. Initialize Git Repository (if not already done)

Open your terminal/command prompt in the project folder and run:

```bash
git init
```

### 2. Configure Git (First Time Only)

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### 3. Add All Files to Git

```bash
git add .
```

### 4. Create Initial Commit

```bash
git commit -m "Initial commit: Professional Student Management System"
```

### 5. Create a New Repository on GitHub

1. Go to [GitHub](https://github.com)
2. Click the **+** icon in the top right
3. Select **New repository**
4. Fill in the details:
   - **Repository name**: `student-management-system`
   - **Description**: `A professional student management system built with Python and MySQL`
   - **Visibility**: Choose Public or Private
   - **DO NOT** initialize with README (we already have one)
5. Click **Create repository**

### 6. Connect Local Repository to GitHub

Copy the commands from GitHub (they will look like this):

```bash
git remote add origin https://github.com/YOUR_USERNAME/student-management-system.git
git branch -M main
git push -u origin main
```

Replace `YOUR_USERNAME` with your actual GitHub username.

### 7. Push Your Code

```bash
git push -u origin main
```

## 🎉 Done!

Your project is now on GitHub! Visit your repository at:
`https://github.com/YOUR_USERNAME/student-management-system`

## 📝 Making Updates

After making changes to your code:

```bash
# Check what files changed
git status

# Add changed files
git add .

# Commit with a message
git commit -m "Description of changes"

# Push to GitHub
git push
```

## 🔒 Important Security Notes

1. **Never commit sensitive data** like:
   - Database passwords
   - API keys
   - Personal information

2. **Update database credentials** before pushing:
   - In `student_management_system.py`, change the password to a placeholder
   - Add instructions in README for users to update credentials

3. **Use environment variables** for sensitive data (recommended for production)

## 📸 Adding Screenshots

1. Take screenshots of your application
2. Create a `screenshots` folder in your project
3. Add images to the folder
4. Update README.md with image links:

```markdown
![Screenshot 1](screenshots/main-screen.png)
```

## 🏷️ Adding Topics/Tags

On your GitHub repository page:
1. Click the ⚙️ icon next to "About"
2. Add topics: `python`, `tkinter`, `mysql`, `student-management`, `database`, `gui`, `desktop-app`
3. Save changes

## 📄 License

Your project includes an MIT License. This allows others to use, modify, and distribute your code.

## 🌟 Getting Stars

To make your repository more discoverable:
1. Write a detailed README (already done ✅)
2. Add screenshots/demo video
3. Share on social media
4. Add relevant topics/tags
5. Keep the code well-documented

---

**Need Help?** Check [GitHub Docs](https://docs.github.com) or open an issue in your repository.
