<!-- Spinner.vue -->
<template>
    <div v-if="loading" class="text-center">
        <div class="spinner-border" :class="spinnerClass" role="status">
            <span class="visually-hidden">Loading...</span>
        </div>
    </div>
</template>

<script>
export default {
    props: {
        loading: {
            type: Boolean,
            required: true
        },
        color: {
            type: String,
            default: "primary" // Imposta il colore predefinito
        },
        size: {
            type: String,
            default: "" 
        }
    },
    computed: {
        spinnerClass() {
            return `text-${this.color} ${this.size && `spinner-${this.size}`}`;
        }
    }
};
</script>

<style scoped></style>