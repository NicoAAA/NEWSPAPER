document.addEventListener('DOMContentLoaded', function() {
    const inputs = document.querySelectorAll('.password-change-form input, .password-change-form textarea');
  
    inputs.forEach(input => {
      input.addEventListener('focus', function() {
        input.style.borderColor = 'var(--color-boton)';
      });
      input.addEventListener('blur', function() {
        input.style.borderColor = 'var(--color-linea)';
      });
    });
  });
  