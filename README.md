# 🏢 BIDIFY - Tender Management Platform

A modern, easy-to-use web application for discovering and managing tenders for your company.

## 🚀 Quick Start (5 minutes)

### Option 1: Windows (Easiest)

1. **Download Python** (if you don't have it):
   - Visit [python.org](https://www.python.org/downloads/)
   - Download Python 3.11+
   - **Important:** Check "Add Python to PATH" during installation

2. **Run the app:**
   - Open Command Prompt in your project folder
   - Copy & paste this:
   ```bash
   pip install -r requirements.txt
   python app.py
   ```
   - Open your browser to: **http://localhost:5000**

### Option 2: macOS/Linux

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Then open: **http://localhost:5000**

---

## 📋 What Does BIDIFY Do?

✅ **View Tenders** - Browse all available tenders by category  
✅ **Filter & Search** - Find tenders by status, category, deadline  
✅ **Add Tenders** - Submit new tender opportunities  
✅ **Track Status** - Monitor tender progress (Open, Under Review, Awarded, Closed)  
✅ **Export Data** - Download tender reports  

---

## 🎨 Features

### Categories Supported
- Asbestos Management
- Painting Services
- Water Purification
- Roofing Solutions
- Gas Installation
- Road Marking
- Automotive Repair

### Status Tracking
- **Open** - New tenders accepting bids
- **Under Review** - Bids submitted, under evaluation
- **Awarded** - Contract awarded
- **Closed** - Tender closed

---

## 📁 Project Structure

```
BIDIFY-/
├── app.py                 # Main application (START HERE)
├── requirements.txt       # Python dependencies
├── database.py           # Database setup
├── templates/            # HTML pages
│   ├── base.html        # Main layout
│   ├── index.html       # Home page
│   ├── add_tender.html  # Add tender form
│   └── view_tender.html # Tender details
├── static/              # CSS & images
│   ├── css/
│   │   └── style.css    # All styling
│   └── js/
│       └── script.js    # Interactive features
├── data/               # SQLite database (auto-created)
│   └── tenders.db      # Tender data storage
└── README.md           # This file
```

---

## ⚙️ Installation Details

### What Gets Installed?

When you run `pip install -r requirements.txt`, these packages are installed:

| Package | Purpose |
|---------|----------|
| **Flask** | Web framework (the engine) |
| **SQLAlchemy** | Database management |
| **python-dotenv** | Configuration management |

**Total size:** ~50MB (very lightweight)

### Database

- **SQLite** - Built into Python, no extra installation needed
- **Location:** `data/tenders.db` (auto-created on first run)
- **No passwords required** - Perfect for local development

---

## 🔥 Common Issues & Solutions

### ❌ Error: "python is not recognized"

**Solution:**
1. Reinstall Python from [python.org](https://www.python.org/downloads/)
2. **IMPORTANT:** Check "Add Python to PATH" ✅
3. Restart Command Prompt
4. Try again

### ❌ Error: "pip is not recognized"

**Solution:**
```bash
python -m pip install -r requirements.txt
```

### ❌ Error: "Module not found"

**Solution:**
```bash
pip install -r requirements.txt
```

### ❌ Port 5000 already in use?

**Solution:** In `app.py`, change line at bottom:
```python
app.run(debug=True, port=8080)  # Changed from 5000 to 8080
```

---

## 🎓 How to Use

### 1. **View Tenders**
   - Go to home page
   - Browse all tenders
   - Click any tender to see details

### 2. **Add a New Tender**
   - Click "+ Add Tender" button
   - Fill in the form
   - Click "Submit"

### 3. **Search & Filter**
   - Use the search box at top
   - Filter by category
   - Filter by status

### 4. **Edit/Delete**
   - Click tender to open
   - Click "Edit" or "Delete"
   - Confirm changes

---

## 🚀 Deployment (Going Live)

### Deploy to Free Hosting

**Option 1: Heroku (Recommended for beginners)**

1. Create account at [heroku.com](https://www.heroku.com)
2. Install Heroku CLI
3. Run these commands:
   ```bash
   heroku login
   heroku create your-app-name
   git push heroku main
   ```

**Option 2: PythonAnywhere**

1. Go to [pythonanywhere.com](https://www.pythonanywhere.com)
2. Sign up (free tier available)
3. Upload this folder
4. Configure web app settings
5. Your app is live!

---

## 📊 Sample Tender Data

The app comes with sample tenders:

| ID | Title | Category | Status | Deadline |
|----|-------|----------|--------|----------|
| 1 | Asbestos Survey | Asbestos Mgmt | Open | 2026-06-30 |
| 2 | Factory Repainting | Painting | Open | 2026-07-15 |
| 3 | Water Treatment | Water Purif. | Under Review | 2026-08-01 |

---

## 🛠️ Development

### Running in Debug Mode

The app starts in debug mode by default:
- Auto-reloads when you change code
- Shows detailed error messages
- Helpful for development

### Making Changes

1. Edit `.html` files in `templates/`
2. Edit `.css` in `static/css/`
3. Save
4. Refresh browser (F5)

**The app automatically detects changes!**

---

## 📞 Support

### Check These First

1. **Is Python installed?** → Run `python --version`
2. **Are dependencies installed?** → Run `pip install -r requirements.txt`
3. **Is the port free?** → Check port 5000 isn't in use
4. **Check the terminal** → Error messages appear there

### Still Need Help?

- Check the "Common Issues" section above
- Review `app.py` comments for more details
- Check Flask documentation: [flask.palletsprojects.com](https://flask.palletsprojects.com)

---

## 📝 Next Steps

### After Getting It Running:

1. ✅ Verify the app loads at http://localhost:5000
2. ✅ Add a test tender via the form
3. ✅ Search/filter tenders
4. ✅ Explore the code

### To Customize:

1. Edit `app.py` to change business logic
2. Edit `templates/` to change appearance
3. Edit `static/css/style.css` to customize colors
4. Add your company logo to `static/`

---

## 📦 What's Included

✅ Complete working application  
✅ Sample tender data  
✅ Database (SQLite - no setup needed)  
✅ Responsive design (works on phone/tablet)  
✅ Search & filter functionality  
✅ Add/edit/delete tenders  
✅ Status tracking  
✅ Professional styling  

---

## 🔐 Security Notes

This is a **local development version**. Before deploying to production:

1. Set `debug=False` in `app.py`
2. Use a proper database (PostgreSQL recommended)
3. Add user authentication
4. Use HTTPS
5. Implement proper permissions

---

## 📄 License

Free to use and modify for your needs.

---

## 🎯 Version

**BIDIFY v1.0** - May 2026

Built for reliable tender management.
