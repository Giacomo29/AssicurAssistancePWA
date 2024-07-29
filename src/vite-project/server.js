const express = require('express');
const path = require('path');
const app = express();

const hostname = '0.0.0.0'; 

// Definisci la directory di distribuzione dei tuoi file statici
app.use(express.static(path.join(__dirname, 'dist')));

// Aggiungi una rotta catch-all per servire l'index.html per il routing client-side
app.get('*', (req, res) => {
  res.sendFile(path.join(__dirname, 'dist', 'index.html'));
});

// Avvia il server sulla porta desiderata
const PORT = process.env.PORT || 3000;
app.listen(PORT, hostname, () => {
  console.log(`Server is running on port ${PORT} and hostname ${hostname}`);
});