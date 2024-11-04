<script>
    // Icons
    import CloseToMenuIcon from '~icons/line-md/close-to-menu-alt-transition';

    export let logo;
</script>


<div class="xl:ms-10 xl:mt-10 mt-8 xl:left-0 xl:translate-x-0 left-1/2 -translate-x-1/2 z-20 absolute">
    <div class="flex md:gap-10 md:justify-between justify-center items-center bg-background rounded-lg px-2 gap-4">
        <!-- Menu -->
        <div class="text-textPrimary text-xl border-custom p-2 rounded md:hidden">
            <CloseToMenuIcon />
        </div>

        <!-- Logo -->
        <a href="/">
            <img src={logo} alt="Logo" class="w-16">
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
                <a href="/kontakt" class="link-outline">Kontakt</a>
            </li>
        </ul>
        <div class="hero-navbar-link md:hidden">
            <a href="/kontakt" class="link-outline">Kontakt</a>
        </div>
    </div>
</div>