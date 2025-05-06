// Wait for DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
    // Get the form element
    const dietForm = document.getElementById('dietForm');
    
    // Add form validation
    if (dietForm) {
        dietForm.addEventListener('submit', function(event) {
            // Check if the form is valid
            if (!dietForm.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
            }
            
            dietForm.classList.add('was-validated');
        });
        
        // Add input validation for numerical fields
        const numericInputs = dietForm.querySelectorAll('input[type="number"]');
        numericInputs.forEach(input => {
            input.addEventListener('input', function() {
                const value = parseFloat(this.value);
                const min = parseFloat(this.min);
                const max = parseFloat(this.max);
                
                if (value < min) {
                    this.setCustomValidity(`Value must be at least ${min}`);
                } else if (value > max) {
                    this.setCustomValidity(`Value cannot exceed ${max}`);
                } else {
                    this.setCustomValidity('');
                }
            });
        });
    }
    
    // Add functionality to dismiss alerts
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        const closeButton = alert.querySelector('.btn-close');
        if (closeButton) {
            closeButton.addEventListener('click', function() {
                alert.classList.add('d-none');
            });
        }
    });
    
    // Add smooth scrolling for anchors
    const anchors = document.querySelectorAll('a[href^="#"]');
    anchors.forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;
            
            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                e.preventDefault();
                window.scrollTo({
                    top: targetElement.offsetTop - 70,
                    behavior: 'smooth'
                });
            }
        });
    });
});
