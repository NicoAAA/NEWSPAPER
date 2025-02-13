document.addEventListener('DOMContentLoaded', function() {
    const inputs = document.querySelectorAll('.login-form input, .login-form textarea');
    
    inputs.forEach(input => {
      input.addEventListener('focus', function() {
        input.style.borderColor = 'var(--color-boton)';
      });
      input.addEventListener('blur', function() {
        input.style.borderColor = 'var(--color-linea)';
      });
    });
  });
  