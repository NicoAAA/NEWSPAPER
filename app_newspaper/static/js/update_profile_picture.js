document.addEventListener("DOMContentLoaded", function () {
    const fileInput = document.querySelector("input[type='file']");
    const previewImg = document.getElementById("preview-img");
    const saveBtn = document.getElementById("save-btn");

    if (fileInput) {
        fileInput.addEventListener("change", function () {
            const file = this.files[0];
            if (file) {
                const reader = new FileReader();
                reader.onload = function (e) {
                    previewImg.src = e.target.result;
                    previewImg.classList.remove("d-none");
                };
                reader.readAsDataURL(file);
            }
        });
    }

    if (saveBtn) {
        saveBtn.addEventListener("click", function () {
            saveBtn.textContent = "Guardando...";
            saveBtn.disabled = true;
        });
    }
});
