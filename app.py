"""BIDIFY - Tender Management Platform

A Flask web application for managing company tenders.
Run this file to start the application.
"""

from flask import Flask, render_template, request, jsonify, redirect, url_for
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Text
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime
import os
from pathlib import Path

# ============================================================================
# CONFIGURATION
# ============================================================================

app = Flask(__name__)
app.config['SECRET_KEY'] = 'bidify-secret-key-2026'

# Create data directory if it doesn't exist
data_dir = Path('data')
data_dir.mkdir(exist_ok=True)

# Database setup
DATABASE_URL = 'sqlite:///data/tenders.db'
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# ============================================================================
# DATABASE MODELS
# ============================================================================

class Tender(Base):
    """Tender database model"""
    __tablename__ = "tenders"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), index=True)
    description = Column(Text)
    category = Column(String(100), index=True)  # e.g., "Asbestos", "Painting", etc.
    status = Column(String(50), index=True)      # Open, Under Review, Awarded, Closed
    deadline = Column(String(50))                # Date in YYYY-MM-DD format
    budget = Column(String(100))                 # e.g., "$50,000 - $100,000"
    location = Column(String(255))               # Where the work will be done
    contact_name = Column(String(255))           # Contact person
    contact_email = Column(String(255))          # Contact email
    contact_phone = Column(String(20))           # Contact phone
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def to_dict(self):
        """Convert model to dictionary"""
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'category': self.category,
            'status': self.status,
            'deadline': self.deadline,
            'budget': self.budget,
            'location': self.location,
            'contact_name': self.contact_name,
            'contact_email': self.contact_email,
            'contact_phone': self.contact_phone,
            'created_at': self.created_at.strftime('%Y-%m-%d') if self.created_at else '',
            'updated_at': self.updated_at.strftime('%Y-%m-%d') if self.updated_at else '',
        }

# Create tables
Base.metadata.create_all(bind=engine)

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def get_db():
    """Get database session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def init_sample_data():
    """Initialize database with sample tenders (only if empty)"""
    db = SessionLocal()
    try:
        # Check if database is empty
        if db.query(Tender).count() == 0:
            sample_tenders = [
                Tender(
                    title="Asbestos Survey - Industrial Complex",
                    description="Comprehensive asbestos survey and assessment for large industrial facility. Includes testing and full documentation.",
                    category="Asbestos",
                    status="Open",
                    deadline="2026-06-30",
                    budget="$15,000 - $25,000",
                    location="Cape Town, Western Cape",
                    contact_name="John Smith",
                    contact_email="john@industrialco.com",
                    contact_phone="021-555-0100"
                ),
                Tender(
                    title="Factory Building Repainting",
                    description="Complete exterior and interior repainting of factory building. Area: 5,000 sqm. Weatherproof paint required.",
                    category="Painting",
                    status="Open",
                    deadline="2026-07-15",
                    budget="$40,000 - $60,000",
                    location="Strand, Western Cape",
                    contact_name="Maria Garcia",
                    contact_email="maria@factoryworks.com",
                    contact_phone="021-555-0101"
                ),
                Tender(
                    title="Water Treatment System Installation",
                    description="Installation of advanced water purification system for industrial use. Capacity: 10,000 liters/day.",
                    category="Water Purifying",
                    status="Under Review",
                    deadline="2026-08-01",
                    budget="$80,000 - $120,000",
                    location="Bellville, Western Cape",
                    contact_name="Ahmed Hassan",
                    contact_email="ahmed@watertech.com",
                    contact_phone="021-555-0102"
                ),
                Tender(
                    title="Commercial Roof Replacement",
                    description="Replacement of aging roof on commercial building. Area: 2,000 sqm. Materials and labor included.",
                    category="Roofing",
                    status="Open",
                    deadline="2026-06-15",
                    budget="$50,000 - $80,000",
                    location="Durbanville, Western Cape",
                    contact_name="Robert Johnson",
                    contact_email="robert@buildingco.com",
                    contact_phone="021-555-0103"
                ),
                Tender(
                    title="Gas Installation - New Facility",
                    description="Installation of gas supply system for new manufacturing facility. Safety certification required.",
                    category="Gas",
                    status="Open",
                    deadline="2026-07-20",
                    budget="$35,000 - $50,000",
                    location="Parow, Western Cape",
                    contact_name="Susan White",
                    contact_email="susan@gasindustries.com",
                    contact_phone="021-555-0104"
                ),
                Tender(
                    title="Highway Road Marking - N1 Corridor",
                    description="Road marking and line painting for N1 highway section. Length: 15km. Reflective paint required.",
                    category="Road Marking",
                    status="Awarded",
                    deadline="2026-05-31",
                    budget="$60,000 - $90,000",
                    location="Northern Corridor, South Africa",
                    contact_name="David Lee",
                    contact_email="david@roadworks.com",
                    contact_phone="021-555-0105"
                ),
                Tender(
                    title="Automotive Fleet Maintenance Contract",
                    description="Regular maintenance and repair services for company vehicle fleet (50 vehicles). 12-month contract.",
                    category="Automotive Repair",
                    status="Open",
                    deadline="2026-06-30",
                    budget="$100,000 - $150,000",
                    location="Johannesburg, Gauteng",
                    contact_name="Lisa Anderson",
                    contact_email="lisa@fleetco.com",
                    contact_phone="011-555-0106"
                ),
            ]
            
            db.add_all(sample_tenders)
            db.commit()
            print("✓ Sample data initialized successfully!")
    except Exception as e:
        print(f"Error initializing sample data: {e}")
    finally:
        db.close()

# ============================================================================
# ROUTES - HOME & DISPLAY
# ============================================================================

@app.route('/')
def index():
    """Home page - display all tenders"""
    db = SessionLocal()
    try:
        # Get filter parameters
        category = request.args.get('category', '')
        status = request.args.get('status', '')
        search = request.args.get('search', '')
        
        # Build query
        query = db.query(Tender)
        
        if category:
            query = query.filter(Tender.category == category)
        if status:
            query = query.filter(Tender.status == status)
        if search:
            query = query.filter(
                (Tender.title.ilike(f'%{search}%')) |
                (Tender.description.ilike(f'%{search}%'))
            )
        
        tenders = query.order_by(Tender.created_at.desc()).all()
        
        # Get unique categories for filter
        all_categories = db.query(Tender.category).distinct().all()
        categories = sorted([cat[0] for cat in all_categories if cat[0]])
        
        # Get unique statuses for filter
        all_statuses = db.query(Tender.status).distinct().all()
        statuses = sorted([s[0] for s in all_statuses if s[0]])
        
        return render_template(
            'index.html',
            tenders=tenders,
            categories=categories,
            statuses=statuses,
            current_category=category,
            current_status=status,
            current_search=search
        )
    finally:
        db.close()

@app.route('/tender/<int:tender_id>')
def view_tender(tender_id):
    """View tender details"""
    db = SessionLocal()
    try:
        tender = db.query(Tender).filter(Tender.id == tender_id).first()
        if not tender:
            return "Tender not found", 404
        return render_template('view_tender.html', tender=tender)
    finally:
        db.close()

# ============================================================================
# ROUTES - ADD/EDIT/DELETE TENDERS
# ============================================================================

@app.route('/add', methods=['GET', 'POST'])
def add_tender():
    """Add new tender"""
    if request.method == 'POST':
        db = SessionLocal()
        try:
            new_tender = Tender(
                title=request.form.get('title'),
                description=request.form.get('description'),
                category=request.form.get('category'),
                status=request.form.get('status', 'Open'),
                deadline=request.form.get('deadline'),
                budget=request.form.get('budget'),
                location=request.form.get('location'),
                contact_name=request.form.get('contact_name'),
                contact_email=request.form.get('contact_email'),
                contact_phone=request.form.get('contact_phone')
            )
            db.add(new_tender)
            db.commit()
            return redirect(url_for('index'))
        except Exception as e:
            print(f"Error adding tender: {e}")
            return "Error adding tender", 500
        finally:
            db.close()
    
    categories = [
        "Asbestos", "Painting", "Water Purifying", "Roofing",
        "Gas", "Road Marking", "Automotive Repair"
    ]
    statuses = ["Open", "Under Review", "Awarded", "Closed"]
    return render_template('add_tender.html', categories=categories, statuses=statuses)

@app.route('/edit/<int:tender_id>', methods=['GET', 'POST'])
def edit_tender(tender_id):
    """Edit existing tender"""
    db = SessionLocal()
    try:
        tender = db.query(Tender).filter(Tender.id == tender_id).first()
        if not tender:
            return "Tender not found", 404
        
        if request.method == 'POST':
            tender.title = request.form.get('title')
            tender.description = request.form.get('description')
            tender.category = request.form.get('category')
            tender.status = request.form.get('status')
            tender.deadline = request.form.get('deadline')
            tender.budget = request.form.get('budget')
            tender.location = request.form.get('location')
            tender.contact_name = request.form.get('contact_name')
            tender.contact_email = request.form.get('contact_email')
            tender.contact_phone = request.form.get('contact_phone')
            tender.updated_at = datetime.utcnow()
            
            db.commit()
            return redirect(url_for('view_tender', tender_id=tender_id))
        
        categories = [
            "Asbestos", "Painting", "Water Purifying", "Roofing",
            "Gas", "Road Marking", "Automotive Repair"
        ]
        statuses = ["Open", "Under Review", "Awarded", "Closed"]
        return render_template('edit_tender.html', tender=tender, categories=categories, statuses=statuses)
    finally:
        db.close()

@app.route('/delete/<int:tender_id>', methods=['POST'])
def delete_tender(tender_id):
    """Delete tender"""
    db = SessionLocal()
    try:
        tender = db.query(Tender).filter(Tender.id == tender_id).first()
        if tender:
            db.delete(tender)
            db.commit()
        return redirect(url_for('index'))
    finally:
        db.close()

# ============================================================================
# API ROUTES (for AJAX requests)
# ============================================================================

@app.route('/api/tenders', methods=['GET'])
def api_get_tenders():
    """Get all tenders as JSON"""
    db = SessionLocal()
    try:
        tenders = db.query(Tender).all()
        return jsonify([tender.to_dict() for tender in tenders])
    finally:
        db.close()

@app.route('/api/statistics', methods=['GET'])
def api_get_statistics():
    """Get tender statistics"""
    db = SessionLocal()
    try:
        total = db.query(Tender).count()
        open_tenders = db.query(Tender).filter(Tender.status == 'Open').count()
        under_review = db.query(Tender).filter(Tender.status == 'Under Review').count()
        awarded = db.query(Tender).filter(Tender.status == 'Awarded').count()
        closed = db.query(Tender).filter(Tender.status == 'Closed').count()
        
        return jsonify({
            'total': total,
            'open': open_tenders,
            'under_review': under_review,
            'awarded': awarded,
            'closed': closed
        })
    finally:
        db.close()

# ============================================================================
# ERROR HANDLERS
# ============================================================================

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(error):
    """Handle 500 errors"""
    return render_template('500.html'), 500

# ============================================================================
# APPLICATION STARTUP
# ============================================================================

if __name__ == '__main__':
    print("\n" + "="*60)
    print("🏢 BIDIFY - Tender Management Platform")
    print("="*60)
    print("\n✓ Initializing database...")
    init_sample_data()
    print("\n✓ Starting Flask application...")
    print("\n📱 Open your browser to: http://localhost:5000")
    print("\n💡 Tips:")
    print("   - Press Ctrl+C to stop the server")
    print("   - The app auto-reloads when you change code")
    print("   - Check the README.md for help")
    print("\n" + "="*60 + "\n")
    
    # Start the Flask development server
    app.run(debug=True, port=5000, host='127.0.0.1')
