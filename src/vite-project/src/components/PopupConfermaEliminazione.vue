<template>
    <div class="popup-wrapper" v-if="showPopup">
        <div class="popup-overlay"></div>
        <div class="popup-content">
            <h2>Conferma Eliminazione</h2>
            <p>Sei sicuro di voler eliminare questo elemento?</p>
            <div class="popup-buttons">
                <button @click="cancelDelete">Annulla</button>
                <button @click="confirmDelete">Elimina</button>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    props: {
        showPopup: {
            type: Boolean,
            required: true
        }
    },
    methods: {
        cancelDelete() {
            // Emit event to cancel delete action
            this.$emit('cancel-delete');
        },
        confirmDelete() {
            // Emit event to confirm delete action
            this.$emit('confirm-delete');
        }
    }
}
</script>

<style scoped>
.popup-wrapper {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: 9999;
    display: flex;
    justify-content: center;
    align-items: center;
}

.popup-overlay {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    /* Sfondo sfocato */
}

.popup-content {
    background-color: #fff;
    padding: 20px;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.3);
    text-align: center;
}

.popup-buttons button {
    margin: 0 10px;
}
</style>