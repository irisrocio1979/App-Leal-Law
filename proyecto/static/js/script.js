function handleSearch() {
  const query = document.getElementById('queryInput').value;

  fetch('/consulta', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ query: query })
  })
  .then(response => response.json())
  .then(data => {
    const result = data.response;

    // Mostrar el resultado en el contenedor
    const resultContainer = document.getElementById('resultContainer');
    const resultText = document.getElementById('resultText');
    
    resultText.innerText = result;
    resultContainer.style.display = 'block';
  })
  .catch(error => {
    console.error('Error:', error);
  });
}
