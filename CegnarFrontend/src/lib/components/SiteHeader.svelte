<script>
    // Components
    import Navbar from "./Navbar.svelte";

    export let backgroundImg;
    export let site;
</script>

<Navbar current={site} />

<div class="h-[40vh] bg-no-repeat bg-cover bg-opacity-10 relative" style="background-image: url('https://picsum.photos/500/300');">
    <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-4 text-textSecondary text-center">
        <h1 class="text-textPrimary text-6xl uppercase font-heading">Galerija</h1>
        <p>Lorem ipsum, dolor sit amet consectetur adipisicing elit. nisi, beatae doloribus possimus optio illum vel. Aliquid, at.</p>
    </div>
</div>