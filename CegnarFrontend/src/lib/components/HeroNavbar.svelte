<script>
    // Icons
    import CloseToMenuIcon from '~icons/line-md/close-to-menu-alt-transition';

    export let logo;
    export let additionalClasses = "";
</script>


<div class="mt-8 left-1/2 -translate-x-1/2 z-20 absolute xl:left-0 xl:translate-x-0 xl:ms-10 xl:mt-10 {additionalClasses}">
    <div class="flex md:gap-10 md:justify-between justify-center items-center bg-background rounded-lg p-2 md:py-0">
        <!-- Menu -->
        <div class="text-textPrimary text-xl border-custom p-2 rounded md:hidden">
            <CloseToMenuIcon />
        </div>

        <!-- Logo -->
        <a href="/" class="h-full grow mx-1">
            <img src={logo} alt="Logo" class="w-16 my-auto scale-110 md:scale-100">
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
            <a href="/kontakt" class="link-outline">Kontakt</a>
        </div>
    </div>
</div>