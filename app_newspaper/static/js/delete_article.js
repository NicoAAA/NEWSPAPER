document.addEventListener('DOMContentLoaded', function() {
    const deleteButton = document.querySelector('.delete-button');
    
    deleteButton.addEventListener('click', function() {
      // Agrega una clase temporal para una animación de clic, si lo deseas
      deleteButton.classList.add('clicked');
      setTimeout(() => {
        deleteButton.classList.remove('clicked');
      }, 300);
    });
  });
  