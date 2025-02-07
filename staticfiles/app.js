document.addEventListener("DOMContentLoaded", function () {
    const clearBtn = document.querySelector("button[name='clear']");
    const searchInput = document.getElementById("id_ci_titular"); // Input de búsqueda
    const resultTable = document.querySelector("table"); // Tabla de resultados
    const noResultsText = document.getElementById("no-results"); // Texto "No se encontraron resultados"

    if (clearBtn) {
        clearBtn.addEventListener("click", function () {
            // Limpiar el campo de entrada
            if (searchInput) {
                searchInput.value = "";
            }

            // Ocultar la tabla de resultados
            if (resultTable) {
                resultTable.style.display = "none";
            }

            // Mostrar el mensaje de "No se encontraron resultados"
            if (noResultsText) {
                noResultsText.style.display = "block";
            }

            // Redirigir a la página sin parámetros GET
            window.history.replaceState({}, document.title, window.location.pathname);
            location.reload(); // Recarga la página con la URL limpia
        });
    }
});
