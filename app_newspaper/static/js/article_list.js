document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll(".post-container").forEach(post => {
        let commentToggleBtn = post.querySelector(".custom-comment-toggle");
        let commentsSection = post.querySelector(".comments-section");
        let addCommentBtn = post.querySelector(".add-comment");
        let commentInput = post.querySelector(".new-comment");
        let commentList = post.querySelector(".comment-list");

        // Alternar visibilidad de los comentarios
        if (commentToggleBtn) {
            commentToggleBtn.addEventListener("click", function (event) {
                event.stopPropagation();
                commentsSection.style.display = (commentsSection.style.display === "none" || commentsSection.style.display === "") ? "flex" : "none";
            });
        }

        // Agregar nuevo comentario usando AJAX
        if (addCommentBtn) {
            addCommentBtn.addEventListener("click", function (event) {
                event.preventDefault();
                let commentText = commentInput.value.trim();
                if (commentText) {
                    let newComment = document.createElement("div");
                    newComment.classList.add("mb-2");
                    newComment.innerHTML = `<strong>Tú</strong> &middot; <small class="text-muted">Just now</small><p class="mb-0">${commentText}</p>`;
                    commentList.appendChild(newComment);
                    commentInput.value = "";

                    // Hacer scroll hacia abajo cuando se agregue un nuevo comentario
                    commentList.scrollTop = commentList.scrollHeight;

                    // Enviar el comentario al servidor usando AJAX
                    fetch('', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                            'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
                        },
                        body: JSON.stringify({
                            'comment': commentText,
                            'article_id': post.querySelector('[name="article_id"]').value
                        })
                    }).then(response => response.json())
                      .then(data => {
                          // Aquí puedes hacer algo con la respuesta del servidor si lo necesitas
                      });
                }
            });
        }
    });

    
});

//  Ahora este código es independiente y funciona correctamente
document.querySelectorAll(".menu-toggle").forEach(button => {
    button.addEventListener("click", function (event) {
        event.stopPropagation();
        let menuContainer = this.closest(".menu-container");
        menuContainer.classList.toggle("active");

        // Cerrar otros menús abiertos
        document.querySelectorAll(".menu-container").forEach(container => {
            if (container !== menuContainer) {
                container.classList.remove("active");
            }
        });
    });
});


/* document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll(".post-container").forEach(post => {
        // Tus listeners actuales para like, dislike, comentarios, etc.
        let likeBtn = post.querySelector(".like-btn");
        let dislikeBtn = post.querySelector(".dislike-btn");
        let likeCountElement = post.querySelector(".like-count");
        let dislikeCountElement = post.querySelector(".dislike-count");
        
        let commentToggleBtn = post.querySelector(".comment-toggle");
        let commentsSection = post.querySelector(".comments-section");
        let addCommentBtn = post.querySelector(".add-comment");
        let commentInput = post.querySelector(".new-comment");
        let commentList = post.querySelector(".comment-list");

        // Alternar visibilidad de los comentarios
        commentToggleBtn.addEventListener("click", function (event) {
            // Para evitar que se propague y active el click del contenedor
            event.stopPropagation();
            commentsSection.style.display = (commentsSection.style.display === "none") ? "block" : "none";
        });

        // Agregar nuevo comentario dinámicamente
        addCommentBtn.addEventListener("click", function (event) {
            event.preventDefault();
            event.stopPropagation(); // Evitamos que el click se propague al contenedor
            let commentText = commentInput.value.trim();
            if (commentText) {
                let newComment = document.createElement("div");
                newComment.classList.add("mb-2");
                newComment.innerHTML = `<strong>Tú</strong> &middot; <small class="text-muted">Just now</small><p class="mb-0">${commentText}</p>`;
                commentList.appendChild(newComment);
                commentInput.value = "";
            }
        });

        // Listener para redirigir solo cuando se haga click directamente en el contenedor
        post.addEventListener("click", function (event) {
            // Comprobamos que el elemento clickeado sea el propio contenedor
            if (event.target === post) {
                let href = post.getAttribute("data-href");
                if (href) {
                    window.location.href = href;
                }
            }
        });
    });

    function getCookie(name) {
        return document.cookie.split('; ').find(row => row.startsWith(name + "="))?.split('=')[1];
    }
});
 */





