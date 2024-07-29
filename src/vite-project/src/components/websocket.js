import { createApp } from 'vue';

const WebSocketInstance = new WebSocket('ws://localhost:8000/ws/notifications/');


WebSocketInstance.connect = function() {
  console.log('WebSocket connection created.');
};

WebSocketInstance.onopen = function() {
  console.log('WebSocket connection opened.');
};

WebSocketInstance.onclose = function() {
  console.log('WebSocket connection closed.');
};

WebSocketInstance.onmessage = function(event) {
  console.log('Message received:', event.data);
};


WebSocketInstance.listenForNotifications = function(callback) {
  this.onmessage = function(event) {
    console.log('Message received:', event.data);
    // Esegue la callback passando i dati ricevuti
    callback(event.data);
  };
};




const app = createApp();

// Aggiunge l'istanza WebSocket al prototipo di Vue per renderla accessibile globalmente
app.config.globalProperties.$webSocket = WebSocketInstance;

export default WebSocketInstance;
