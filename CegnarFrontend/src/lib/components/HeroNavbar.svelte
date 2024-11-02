<script>
    import CloseToMenuIcon from '~icons/line-md/close-to-menu-alt-transition';
</script>


<div class="xl:ms-10 xl:mt-10 mt-8 xl:left-0 xl:translate-x-0 left-1/2 -translate-x-1/2 z-20 absolute">
    <div class="flex md:gap-10 md:justify-between justify-center items-center bg-background rounded-lg p-4 gap-4">
        <!-- Menu -->
        <div class="text-textPrimary font-2xl border-[0.5px] p-1 rounded md:hidden">
            <CloseToMenuIcon />
        </div>

        <!-- Logo -->
        <a class="text-white text-2xl" href="/">C</a>

        <!-- Links -->
        <ul class="md:inline-flex items-center gap-4 textPrimary hidden">
            <li class="hero-navbar-link">Galerija</li>
            <li class="hero-navbar-link">Zgodba</li>
            <li class="hero-navbar-link"><a href="/kontakt" class="border rounded p-2">Kontakt</a></li>
        </ul>
        <div class="hero-navbar-link md:hidden">
            <a href="/kontakt" class="border rounded p-2">Kontakt</a>
        </div>
    </div>
</div>