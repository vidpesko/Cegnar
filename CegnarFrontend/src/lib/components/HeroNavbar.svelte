<script>
    // Icons
    import CloseToMenuIcon from '~icons/line-md/close-to-menu-alt-transition';
    import MenuToCloseIcon from '~icons/line-md/menu-to-close-alt-transition';
    import HamburgerIcon from '~icons/pajamas/hamburger';

    export let logo;
    export let additionalClasses = "";

    export let openNavigationMenu;
</script>


<div class="mt-8 left-1/2 -translate-x-1/2 z-20 absolute xl:left-0 xl:translate-x-0 xl:ms-10 xl:mt-10 {additionalClasses}">
    <div class="flex md:gap-10 md:justify-between justify-around items-center bg-background rounded-lg md:px-2 px-9 py-1 md:py-0">
        <!-- Menu -->
        <button class="text-textPrimary text-xl border-custom p-2 rounded md:hidden" on:click={openNavigationMenu}>
            <HamburgerIcon />
        </button>
        <!-- Logo -->
        <a href="/" class="h-full grow shrink-0 mx-1">
            <img src={logo} alt="Logo" class="w-14 md:w-16 my-auto scale-110 md:scale-100">
        </a>

        <!-- Links -->
        <ul class="md:inline-flex items-center gap-2 textPrimary hidden">
            <li class="hero-navbar-link">
                <a href="/galerija" class="hover:link-outline">Galerija</a>
            </li>
            <li class="hero-navbar-link">
                <a href="/zgodba" class="hover:link-outline">Zgodba</a>
            </li>
            <li class="hero-navbar-link">
                <a href="/kontakt" data-sveltekit-reload class="link-outline">Kontakt</a>
            </li>
        </ul>
        <div class="hero-navbar-link md:hidden">
            <a href="/kontakt" data-sveltekit-reload class="link-outline">Kontakt</a>
        </div>
    </div>
</div>