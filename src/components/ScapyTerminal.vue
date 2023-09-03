<template>
    <v-container class="pa-0 flex-grow-1 flex-shrink-1">
        <div class="btnbar">
            <div class="d-inline-block btn close"></div>
            <div class="d-inline-block btn minimize"></div>
            <div class="d-inline-block btn zoom"></div>
        </div>
        <div class="content">
            <pre style="white-space: pre-wrap;" v-html="props.content"></pre>
        </div>
    </v-container>
</template>

<script lang="ts" setup>
const props = defineProps(['content'])
</script>

<style scoped lang="scss">
.btn {
    height: 10px;
    width: 10px;
    border-radius: 50%;
    border: 1px solid #000;
    margin-top: 9px;
    margin-left: 4px;
    margin-right: 2px;
}

.close {
    background-color: #ff3b47;
    border-color: #9d252b;
}

.minimize {
    background-color: #ffc100;
    border-color: #9d802c;
}

.zoom {
    background-color: #00d742;
    border-color: #049931;
}

.btnbar {
    height: 25px;
    background-color: #bbb;
    margin: 0 auto;
    border-top-right-radius: 5px;
    border-top-left-radius: 5px;
}

.content {
    background-color: #151515;
    margin: 0 auto;
    padding: 10px 0px 10px 20px;
    border-bottom-left-radius: 5px;
    border-bottom-right-radius: 5px;
}
</style>