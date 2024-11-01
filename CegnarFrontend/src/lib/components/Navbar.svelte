<script>
    import { fly } from "svelte/transition";
    import { onMount } from "svelte";
    // Logo
    // import logo from "../static/images/logo-white.png";
    // Icons
    import MenuIcon from '~icons/streamline/interface-setting-menu-2-button-parallel-horizontal-lines-menu-navigation-staggered-three-hamburger';
    import XIcon from '~icons/material-symbols/close-rounded'

    // Display menu
    export let showMenu = false;

    // Show navbar
    let showNavbar = true;

    onMount(() => {
        // Hide navbar when scrolled down, show it when scroll up
        let prevScrollPosition = window.scrollY;
        let scrollPosition = prevScrollPosition;
        let deltaScrollPosition = 0;

        window.addEventListener("scroll", () => {
            scrollPosition = window.scrollY;
            deltaScrollPosition = scrollPosition - prevScrollPosition;
            if ((deltaScrollPosition > 100) && (showNavbar == true)) {
                showNavbar = false;
                prevScrollPosition = scrollPosition;
                deltaScrollPosition = 0;
            } else if ((deltaScrollPosition < 0) && (deltaScrollPosition > -50)) {
                showNavbar = true;
                prevScrollPosition = scrollPosition;
            } else if (Math.abs(deltaScrollPosition) > 100) {
                deltaScrollPosition = 0;
                prevScrollPosition = scrollPosition;
            } 
        });
    });
</script>


{#if showNavbar}
<div transition:fly={{ y: -200, duration: 500 }} class="w-screen flex items-center p-2 px-10 h-16 z-30 text-black fixed bg-white bg-opacity-70 backdrop-blur-lg hover:backdrop-blur-0 hover:bg-opacity-100">
    <!-- Logo -->
    <div class="flex-1">
        <a href="/" class="text-xl"><img src="https://picsum.photos/500/300" alt="" width="60px"></a>
    </div>
    <div class="">
        <ul class="md:flex hidden items-center gap-x-4">
            <li>
                <a href="/galerija" class="">Zadnji izdelki</a>
            </li>
            <li>
                <a href="/zgodba" class="">Zgodba</a>
            </li>
            <!-- Contact -->
            <li>
                <a href="/kontakt" class="">Kontakt</a>
            </li>
        </ul>
        <!-- svelte-ignore a11y-click-events-have-key-events -->
        <div on:click={() => showMenu = !showMenu} tabindex="0" role="button" class="m-1 md:hidden">
            {#if !showMenu}
            <MenuIcon class="text-2xl text-white" />
            {:else}
            <XIcon class="text-4xl text-white" />
            {/if}
        </div>
    </div>
</div>
{/if}