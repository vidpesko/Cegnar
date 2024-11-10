<script>
    export let src;
    export let model;
    export let description;
    export let scrollPos
    export let closeModal;
</script>


<div class="fixed left-0 w-full top-0 h-screen z-30 p-10 bg-background bg-opacity-90">
    <!-- Close btn -->
    <button class="text-white text-xl absolute right-8 top-5" on:click={closeModal}>x</button>
    <!-- Content -->
    <div class="flex gap-8 items-center justify-center">
        <!-- Image -->
        <img {src} alt="" class="rounded-2xl">
        <!-- Text -->
        <div class="text-white text-start">
            <h2 class="text-textPrimary font-heading text-5xl">{model}</h2>
            <p class="text-lg mb-10">{@html description}</p>
            <a href="/kontakt?izdelek={model}" class="btn">Naroci tak noz</a>
        </div>
    </div>
</div>