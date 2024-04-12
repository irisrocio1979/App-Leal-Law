function handleSearch() {
  const query = document.getElementById('queryInput').value;
  const result = procesarConsulta(query);
  
  // Mostrar el resultado en el contenedor
  const resultContainer = document.getElementById('resultContainer');
  const resultText = document.getElementById('resultText');
  
  resultText.innerText = result;
  resultContainer.style.display = 'block';
}

function procesarConsulta(query) {
  // Implementa la lógica para procesar la consulta y obtener la respuesta aquí
  return "Aquí iría la respuesta a la consulta. La interpretación jurídica es la forma en que el juez entiende el significado de la ley. Cuando ambas partes presentan su caso ante el tribunal, el juez se basa en sus interpretaciones de la ley para decidir qué parte debe ganar. \nLa interpretación jurídica ha desempeñado un enorme papel en la evolución de la legislación sobre derechos humanos. Las normas, los tratados y las constituciones de derechos humanos son, por su esencia, poco detallados, lo que deja mucho margen para la interpretación y la flexibilidad. Esto otorga a los jueces la posibilidad de interpretar la ley para incorporar los cambios en la sociedad y las costumbres sociales. Gracias a esta flexibilidad, la interpretación jurídica ha desempeñado un enorme papel en la ampliación de la legislación sobre derechos humanos. ,\nComo figuras imparciales, los jueces no deberían tomar decisiones basadas en sus creencias personales o políticas. Su trabajo es aplicar objetivamente la ley basándose en el caso que tienen en sus manos. Al decidir si una ley determinada corresponde al caso o cómo debe aplicarse, los jueces se apoyarán en un método de interpretación jurídica. \nLa forma en que un juez interpreta la ley puede tener un profundo impacto en la sociedad.";
}
