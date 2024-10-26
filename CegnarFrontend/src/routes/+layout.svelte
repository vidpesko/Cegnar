<script>
    // Custom css
    import "../app.css";
    // Splide js css
    import '@splidejs/svelte-splide/css';
    // Icons
    import IGIcon from '~icons/mdi/instagram';
    import FacebookIcon from '~icons/mdi/facebook-box';
    import EmailIcon from '~icons/mdi/email';
</script>

<slot />

<!-- Footer -->
<footer class="bg-background text-white border-t-[0.5px] relative">
    
    <!-- Links & logo -->
    <div class="w-4/6 py-10">
        <h1>Cegu</h1>

    </div>

    <!-- Social & shoutout -->
    <div class="relative after:content-[''] after:absolute after:top-0 after:bg-textSecondary after:w-5/6 after:h-[0.5px] after:left-1/2 after:-translate-x-1/2">
        <!-- Social -->
        <div class="py-10">
            <ul class="footer-social flex justify-center gap-4">
                <li><a href="https://www.instagram.com/cegnarblacksmithing/"><IGIcon /></a></li>
                <li><a href="https://www.instagram.com/cegnarblacksmithing/"><FacebookIcon /></a></li>
                <li><a href="https://www.instagram.com/cegnarblacksmithing/"><EmailIcon /></a></li>
            </ul>
        </div>
        
        <!-- Designed by me -->
        <div class="w-full bg-red-400 text-center">
            <a>Izdelal Vid</a>
        </div>
    </div>
</footer>
