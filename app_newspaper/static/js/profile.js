document.addEventListener('DOMContentLoaded', function() {
    const postCards = document.querySelectorAll('.post-card');
  
    function revealPosts() {
      postCards.forEach(card => {
        const rect = card.getBoundingClientRect();
        if (rect.top < window.innerHeight - 100) {
          card.classList.add('visible');
        }
      });
    }
  
    window.addEventListener('scroll', revealPosts);
    revealPosts(); // Ejecuta al cargar la página
  });
  