<template>
    <div class="offline-page">
      <h1>Oops! Sei offline.</h1>
      <p>Non riesco a raggiungere il server. Controlla la tua connessione e riprova.</p>
    </div>
  </template>
  
  <style scoped>
  .offline-page {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    height: 100vh;
    font-family: Arial, sans-serif;
    text-align: center;
  }
  
  h1 {
    font-size: 2em;
    margin-bottom: 20px;
  }
  
  p {
    font-size: 1.2em;
    color: #666;
  }
  </style>