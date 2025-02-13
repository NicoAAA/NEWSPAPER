document.addEventListener("DOMContentLoaded", function () {
    // Animación para mostrar comentarios
    const comments = document.querySelectorAll(".fade-in");
    comments.forEach((comment, index) => {
        setTimeout(() => {
            comment.style.opacity = "1";
            comment.style.transform = "translateY(0)";
        }, index * 200);
    });

    // Habilitar el botón de enviar solo cuando se escriba algo
    const commentInput = document.querySelector(".comment-form textarea");
    const submitBtn = document.getElementById("submit-btn");

    if (commentInput) {
        commentInput.addEventListener("input", function () {
            submitBtn.disabled = this.value.trim() === "";
        });
    }
});