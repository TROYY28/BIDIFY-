/**
 * BIDIFY - Tender Management Platform
 * Main JavaScript File
 */

// ============================================================================
// UTILITY FUNCTIONS
// ============================================================================

/**
 * Format date to readable format
 * @param {string} dateString - Date in YYYY-MM-DD format
 * @returns {string} Formatted date
 */
function formatDate(dateString) {
    const options = { year: 'numeric', month: 'long', day: 'numeric' };
    return new Date(dateString).toLocaleDateString('en-US', options);
}

/**
 * Debounce function to prevent excessive function calls
 * @param {function} func - Function to debounce
 * @param {number} wait - Wait time in milliseconds
 */
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// ============================================================================
// SEARCH & FILTER FUNCTIONALITY
// ============================================================================

const searchInput = document.querySelector('.search-input');
if (searchInput) {
    searchInput.addEventListener('keyup', debounce(function() {
        // Form will submit naturally or trigger search
        console.log('Search triggered:', this.value);
    }, 300));
}

// ============================================================================
// FORM VALIDATION
// ============================================================================

/**
 * Validate form before submission
 */
function validateTenderForm(form) {
    const title = form.querySelector('[name="title"]')?.value.trim();
    const description = form.querySelector('[name="description"]')?.value.trim();
    const category = form.querySelector('[name="category"]')?.value;
    const deadline = form.querySelector('[name="deadline"]')?.value;
    const budget = form.querySelector('[name="budget"]')?.value.trim();
    const location = form.querySelector('[name="location"]')?.value.trim();
    const contactName = form.querySelector('[name="contact_name"]')?.value.trim();
    const contactEmail = form.querySelector('[name="contact_email"]')?.value.trim();
    const contactPhone = form.querySelector('[name="contact_phone"]')?.value.trim();
    
    const errors = [];
    
    if (!title) errors.push('Tender title is required');
    if (!description || description.length < 10) errors.push('Description must be at least 10 characters');
    if (!category) errors.push('Category is required');
    if (!deadline) errors.push('Deadline is required');
    if (!budget) errors.push('Budget is required');
    if (!location) errors.push('Location is required');
    if (!contactName) errors.push('Contact name is required');
    if (!contactEmail || !isValidEmail(contactEmail)) errors.push('Valid email is required');
    if (!contactPhone) errors.push('Contact phone is required');
    
    if (errors.length > 0) {
        alert('Please fix the following errors:\n\n' + errors.join('\n'));
        return false;
    }
    
    return true;
}

/**
 * Validate email format
 * @param {string} email - Email to validate
 * @returns {boolean}
 */
function isValidEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}

// Attach form validation to tender forms
const tenderForms = document.querySelectorAll('.tender-form');
tenderForms.forEach(form => {
    form.addEventListener('submit', function(e) {
        if (!validateTenderForm(this)) {
            e.preventDefault();
        }
    });
});

// ============================================================================
// MODAL FUNCTIONALITY
// ============================================================================

/**
 * Close all modals
 */
function closeAllModals() {
    const modals = document.querySelectorAll('.modal');
    modals.forEach(modal => {
        modal.style.display = 'none';
    });
}

/**
 * Close modal when clicking outside of it
 */
window.addEventListener('click', function(event) {
    if (event.target.classList.contains('modal')) {
        event.target.style.display = 'none';
    }
});

// ============================================================================
// COPY TO CLIPBOARD
// ============================================================================

/**
 * Copy text to clipboard
 * @param {string} text - Text to copy
 */
function copyToClipboard(text) {
    navigator.clipboard.writeText(text).then(() => {
        showNotification('Copied to clipboard!', 'success');
    }).catch(err => {
        showNotification('Failed to copy', 'error');
        console.error('Copy error:', err);
    });
}

// ============================================================================
// NOTIFICATIONS
// ============================================================================

/**
 * Show notification message
 * @param {string} message - Message to display
 * @param {string} type - Type of notification (success, error, info, warning)
 * @param {number} duration - Duration in milliseconds
 */
function showNotification(message, type = 'info', duration = 3000) {
    // For now, just log to console
    // In a production app, you'd show a visual notification
    console.log(`[${type.toUpperCase()}] ${message}`);
}

// ============================================================================
// DATE UTILITIES
// ============================================================================

/**
 * Set minimum date to today in date input
 */
function setMinimumDate() {
    const dateInputs = document.querySelectorAll('input[type="date"]');
    const today = new Date().toISOString().split('T')[0];
    
    dateInputs.forEach(input => {
        if (input.name === 'deadline') {
            input.min = today;
        }
    });
}

// Call on page load
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', setMinimumDate);
} else {
    setMinimumDate();
}

// ============================================================================
// INITIALIZATION
// ============================================================================

console.log('BIDIFY Application Loaded Successfully');
