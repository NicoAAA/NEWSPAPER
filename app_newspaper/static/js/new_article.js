document.addEventListener('DOMContentLoaded', function() {
    const inputs = document.querySelectorAll('.new-article-form input, .new-article-form textarea');
  
    inputs.forEach(input => {
      input.addEventListener('focus', function() {
        input.style.borderColor = 'var(--color-boton)';
      });
      input.addEventListener('blur', function() {
        input.style.borderColor = 'var(--color-linea)';
      });
    });
  });
  