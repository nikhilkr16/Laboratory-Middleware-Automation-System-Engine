# LIMS Dashboard - GitHub Pages

This folder contains the files for the GitHub Pages deployment of the LIMS Quality Dashboard.

## 📊 Live Dashboard

The LIMS Dashboard is now available online at:
**[https://nikhilkr16.github.io/Laboratory-Middleware-Automation-System-Engine/](https://nikhilkr16.github.io/Laboratory-Middleware-Automation-System-Engine/)**

## 📁 Contents

- **index.html** - The main dashboard application with interactive visualizations and filtering
- **.nojekyll** - Configuration file to prevent Jekyll processing (preserves HTML as-is)

## 🔄 How It Works

This directory is automatically deployed to GitHub Pages via GitHub Actions workflow (`.github/workflows/deploy-pages.yml`):

1. Any push to `main` or `master` branch triggers the workflow
2. The workflow uploads the contents of this `docs/` folder
3. GitHub Pages serves the files at `https://nikhilkr16.github.io/Laboratory-Middleware-Automation-System-Engine/`

## 🎨 Dashboard Features

The dashboard provides:
- Real-time LIMS data visualization
- Quality control metrics and charts
- Out-of-Specification (OOS) flagging
- Sample filtering and search
- Audit trail tracking
- ALCOA+ compliance indicators

## 🔧 Making Changes

To update the dashboard:
1. Modify `docs/index.html` or regenerate from the root `dashboard.html`
2. Push changes to `main` or `master`
3. GitHub Actions automatically deploys the changes
4. View the updated dashboard at the GitHub Pages URL

## 📝 Notes

- The GitHub Pages site is publicly accessible
- No additional hosting or server setup required
- Updates are deployed automatically via CI/CD pipeline
- The dashboard is a static HTML/JavaScript application (no backend required for viewing)

---

For more information about the LIMS system, see the main [README.md](../README.md)
