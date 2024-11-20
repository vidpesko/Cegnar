<script>
    // Transition
    import { fade } from 'svelte/transition';
    // Icons
    import MenuToCloseIcon from '~icons/line-md/menu-to-close-alt-transition';

    export let closeNavigationMenu;
</script>

<div transition:fade={{ duration: 300 }} class="h-dvh left-0 bg-background text-textPrimary fixed top-0 z-50 w-full">
    <div class="absolute left-6 top-6">
        <button on:click={closeNavigationMenu} class="p-3 rounded-lg border-custom">
            <MenuToCloseIcon class="text-lg" />
        </button>
    </div>

    <!-- Links -->
    <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2">
        <ul class="navigation-menu-fullscreen">
            <li><a href="/">Domov</a></li>
            <li><a href="/zgodba">Zgodba</a></li>
            <li><a href="/galerija">Galerija</a></li>
            <li><a href="/kontakt">Kontakt</a></li>
        </ul>
    </div>
</div>