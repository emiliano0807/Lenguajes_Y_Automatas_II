document.getElementById("rutaForm").addEventListener("submit", async function(event) {
    event.preventDefault();

    let inicio = document.getElementById("inicio").value.toUpperCase();
    let fin = document.getElementById("fin").value.toUpperCase();

    let response = await fetch("/buscar", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ inicio, fin })
    });

    let resultadoElement = document.getElementById("resultado");

    if (response.ok) {
        let data = await response.json();
        resultadoElement.textContent = "Ruta encontrada: " + data.ruta.join(" → ");
    } else {
        let errorData = await response.json();
        resultadoElement.textContent = "Error: " + errorData.error || errorData.mensaje;
    }
});
