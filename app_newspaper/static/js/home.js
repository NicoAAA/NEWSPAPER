document.addEventListener('DOMContentLoaded', function() {
    const featureCards = document.querySelectorAll('.feature-card');
    
    window.addEventListener('scroll', () => {
        featureCards.forEach(card => {
            const cardPosition = card.getBoundingClientRect().top;
            const screenPosition = window.innerHeight;
            if (cardPosition < screenPosition - 100) {
                card.classList.add('visible');
            }
        });
    });
});
