<script>
    export let type;
</script>

<div class:bg-green-400={type === "success"} class:bg-red-400={type === "error"} class="p-3 rounded-lg text-white flex justify-between items-center text-xl">
    <slot></slot>
</div>