<script>
    // Components
    import Navbar from "./Navbar.svelte";

    export let backgroundImg;
    export let site;
</script>

<Navbar current={site} />

<div class="h-[30vh]" style="background-image: url('https://picsum.photos/500/300');">
    <h1>Hello</h1>
</div>