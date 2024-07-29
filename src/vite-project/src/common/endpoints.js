

const baseEndpoint = '/api/';

const endpoints = {
    //endpoint per le API di clienti
    clientiList: `${baseEndpoint}clienti/`,
    clientiDetail: `${baseEndpoint}clienti/`,
    clientiCognome: `${baseEndpoint}clienti/cerca-per-cognome/`,
    clientiTarga: `${baseEndpoint}clienti/cerca-per-targa/`,
    
    //endpoint per le API di veicoli
    veicoliList: `${baseEndpoint}veicoli/`,
    veicoliDetail: `${baseEndpoint}veicoli/`,
    veicoliCliente: `${baseEndpoint}veicoli/cliente/`,
    veicoliNonAssicurati: `${baseEndpoint}veicoli-non-assicurati/`,

    //endpoint per le API di polizze
    polizzeList: `${baseEndpoint}polizze/`,
    polizzeDetail: `${baseEndpoint}polizze/`,
    polizzeScadenza: `${baseEndpoint}polizze/scadenza-nel-mese/`,
    polizzeCognome: `${baseEndpoint}polizze/cerca-per-cognome/`,
    polizzeTarga: `${baseEndpoint}polizze/cerca-per-targa/`,
    polizzeCodiceFiscale: `${baseEndpoint}polizze/cerca-per-codice-fiscale/`,
    DownloadDocumenti: `${baseEndpoint}polizze/download_documenti/`,
    EliminaDocumento: `${baseEndpoint}polizze/`,
    AggiungiDocumento: `${baseEndpoint}polizze/aggiungi_documento/`,
    portafoglio: `${baseEndpoint}polizze/portafoglio/`,
    //endpoint per le API di compagnie

    compagnieList: `${baseEndpoint}compagnie/`,
    compagnieDetail: `${baseEndpoint}compagnie/`,
    compagniePolizze: `${baseEndpoint}compagnie-polizze/`,

    //endpoint per le API di broker

    brokerList: `${baseEndpoint}broker/`,
    brokerDetail: `${baseEndpoint}broker/`,

    //  endpoint per account
    account: `${baseEndpoint}user/`,
    modifyAccount: `${baseEndpoint}modifica-user/`,
    updateAvatar: `${baseEndpoint}user/avatar/`,
    resetPassword: `${baseEndpoint}request-reset-email/`,
    newPassword: `${baseEndpoint}password-reset-complete/`,
    resetPasswordToken: `${baseEndpoint}password-reset/`,





};

export {endpoints};