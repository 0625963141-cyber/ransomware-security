// script.js

document.addEventListener('DOMContentLoaded', function() {
    // Fonction pour afficher une alerte
    function showAlert() {
        alert('Votre appareil peut être infecté par un ransomware. Contactez-nous pour obtenir de l\'aide immédiate.');
    }

    // Fonction pour rediriger vers un numéro de téléphone
    function callSupport() {
        window.location.href = 'tel:+2120625963141';
    }

    // Événements pour les actions utilisateur
    document.getElementById('alertButton').addEventListener('click', showAlert);
    document.getElementById('callButton').addEventListener('click', callSupport);
});
